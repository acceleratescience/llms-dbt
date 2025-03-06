markdown
| Model                                | BLEU EN-DE | BLEU EN-FR | Training Cost EN-DE (FLOPs) | Training Cost EN-FR (FLOPs) |
|--------------------------------------|------------|------------|-----------------------------|-----------------------------|
| ByteNet [18]                         | 23.75      |            |                             |                             |
| Deep-Att + PosUnk [39]               |            | 39.2       |                             | 1.0 · 10²⁰                  |
| GNMT + RL [38]                       | 24.6       | 39.92      | 2.3 · 10¹⁹                  | 1.4 · 10²⁰                  |
| ConvS2S [9]                          | 25.16      | 40.46      | 9.6 · 10¹⁸                  | 1.5 · 10²⁰                  |
| MoE [32]                             | 26.03      | 40.56      | 2.0 · 10¹⁹                  | 1.2 · 10²⁰                  |
| Deep-Att + PosUnk Ensemble [39]      |            | 40.4       |                             | 8.0 · 10²⁰                  |
| GNMT + RL Ensemble [38]              | 26.30      | 41.16      | 1.8 · 10²⁰                  | 1.1 · 10²¹                  |
| ConvS2S Ensemble [9]                 | 26.36      | 41.29      | 7.7 · 10¹⁹                  | 1.2 · 10²¹                  |
| Transformer (base model)             | 27.3       | 38.1       | 3.3 · 10¹⁸                  |                             |
| Transformer (big)                    | 28.4       | 41.8       | 2.3 · 10¹⁹                  |                             |
