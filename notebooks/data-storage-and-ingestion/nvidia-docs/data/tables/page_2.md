markdown
| Layer Type                  | Complexity per Layer | Sequential Operations | Maximum Path Length |
|-----------------------------|----------------------|-----------------------|---------------------|
| Self-Attention              | O(n² · d)            | O(1)                  | O(1)                |
| Recurrent                   | O(n · d²)            | O(n)                  | O(n)                |
| Convolutional               | O(k · n · d²)        | O(1)                  | O(logₖ(n))          |
| Self-Attention (restricted) | O(r · n · d)         | O(1)                  | O(n/r)              |
