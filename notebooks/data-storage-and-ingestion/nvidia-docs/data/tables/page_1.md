markdown
| Layer Type                | Input Dimensions | Output Dimensions |
|---------------------------|------------------|-------------------|
| Scaled Dot-Product        | Q: (batch, seq, dk) | V: (batch, seq, dv) |
| Attention                 | K: (batch, seq, dk) |                   |
|                           | V: (batch, seq, dv) |                   |
| Multi-Head Attention      | Q: (batch, seq, dmodel) | V: (batch, seq, dmodel) |
|                           | K: (batch, seq, dmodel) |                   |
|                           | V: (batch, seq, dmodel) |                   |
