# Codespaces

For this workshop, since we're not really doing any heavy lifting, we can work entirely within Github Codespaces.

First, fork this repository. You can open the repository in Codespaces by clicking the green "Code" button at the top of the repository and selecting "Open with Codespaces". The Codespaces environment will be set up for you, including all dependencies.

You will also need to run the following in the terminal in order to use `chromadb` (I'm not sure why this is necessary, but it is):

```bash
mkdir mkdir -p /home/codespace/.local/lib/python3.12/site-packages/google/colab
```

The `.gitignore` should already contain a line for the `.env` file, but if it doesn't then you should add the following to the `.gitignore` file:

```bash
.env
```

and save it.

You should then create a new file called `.env` and add your OpenAI API key to it.

```bash
OPENAI_API_KEY=<YOUR_API_KEY>
```

> [!WARNING]
> Please add `.env` to your `.gitignore` before adding the API key to the `.env` file and before pushing any changes to your repo! There are bots crawling GitHub for exposed API keys.