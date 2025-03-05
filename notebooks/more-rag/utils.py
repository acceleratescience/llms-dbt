from jinja2 import Template, Environment, FileSystemLoader
import os
from pathlib import Path
from typing import List, Union
import bm25s
from llama_index.core import SimpleDirectoryReader

from abc import ABC, abstractmethod
from typing import List, Tuple, Union
from pathlib import Path

class TemplateManager:
    def __init__(self, template_dir: str = "prompts"):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self._templates = {}
    
    def get_template(self, template_name: str, force_reload=False) -> Template:
        if template_name not in self._templates or force_reload:
            self._templates[template_name] = self.env.get_template(template_name)
        return self._templates[template_name]
    
    def render(self, template_name: str, force_reload=False, **kwargs) -> str:
        template = self.get_template(template_name, force_reload=force_reload)
        return template.render(**kwargs)
    

class BaseSearcher(ABC):
    """Abstract base class defining the interface for search implementations."""
    
    def __init__(self):
        self.doc_paths = []
        self.documents = []
    
    @abstractmethod
    def fit_from_directory(self, directory: Union[str, Path], **kwargs):
        """Load and index documents from a directory."""
        pass
    
    @abstractmethod
    def search(self, query: str, n: int = 5) -> List[Tuple[float, str, str]]:
        """Search for documents matching the query."""
        pass

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def load_documents(self, directory: Union[str, Path]) -> List[str]:
        files = SimpleDirectoryReader(directory, recursive=True).load_data()
        cwd = os.getcwd()
        
        unique_files = {}
        for doc in files:
            path = "."+doc.metadata['file_path'][len(cwd):]
            if path not in unique_files:
                unique_files[path] = doc.text
        
        self.doc_paths = list(unique_files.keys())
        return list(unique_files.values())
    
    def format_context(self, results: List[Tuple[float, str, str]]) -> str:
        """Format search results into a structured context string."""
        formatted_text = ""
        for score, file_path, content in results:
            # Extract title from file path (remove extension and path)
            title = os.path.splitext(os.path.basename(file_path))[0]
            
            formatted_text += f"title: {title}\n"
            formatted_text += f"similarity score: {score:.4f}\n"
            formatted_text += f"content: {content}\n\n"
        
        return formatted_text.strip()
    
    def search_and_format(self, query: str, n: int = 5) -> str:
        """Search and format results in one call."""
        results = self.search(query, n)
        return self.format_context(results)
    

class BM25Search(BaseSearcher):
    def __init__(self):
        super().__init__()
        self.retriever = None
    
    def fit_from_directory(self, directory: Union[str, Path], **kwargs):
        self.documents = self.load_documents(directory)
        
        corpus_tokens = bm25s.tokenize(self.documents, stopwords="en")
        self.retriever = bm25s.BM25(**kwargs)
        self.retriever.index(corpus_tokens)
        
        print(f"Processed {len(self.documents)} documents")

    def search(self, query: str, n: int = 5) -> List[Tuple[float, str, str]]:
        query_tokens = bm25s.tokenize(query, stopwords="en")
        docs, scores = self.retriever.retrieve(query_tokens, corpus=self.documents, k=n)
        
        results = []
        for doc, score in zip(docs[0], scores[0]):
            if score > 0:
                doc_idx = self.documents.index(doc)
                text = self.read_file(self.doc_paths[doc_idx])
                results.append((score, self.doc_paths[doc_idx], text))
        
        return sorted(results, key=lambda x: x[0], reverse=True)

    def save_index(self, path: str):
        self.retriever.save(path)
    
    def load_index(self, path: str):
        self.retriever = bm25s.BM25.load(path, load_corpus=True)