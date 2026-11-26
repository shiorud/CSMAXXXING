# Resource mapping (v3.0, Stage 3 final)

Where each major Markdown topic is used across the learning system. **Guide** = Study Guide v3.0 (same section numbers as the Markdown). **Test Bank** = `CSMAXXXING_TestBank_v3.0.docx` (A = true/false, B = multiple choice, C = open-ended). **Slides** = `CSMAXXXING_Stage3_FinalPPT_v3.0.pptx` (slide numbers). **Video** = CSMAXXXING Video Tutorials (separate assignment; team Drive folder). **Lab** = CSMAXXXING AI Lab tab. "—" = deliberately not used in that medium (reason given).

| Markdown topic (file → section) | Guide | Lab / activity | Test Bank | Slides | Video |
|---|---|---|---|---|---|
| Start here: outcomes, prerequisites, route (`00`) | Start Here | — | — | 3 (goals and roadmap) | Intro |
| What is AI; AI ⊃ ML ⊃ DL (`01` 1.1) | 1.1 | Lab 1 AI Spotter | A1, A2, A5, B1, B3 | 5, 6 | Ch 1 |
| History of AI (`01` 1.2) | 1.2 | — (reading + timeline is enough) | A3, B2, B5 | 7 | Ch 1 |
| Impact, bias, jobs (`01` 1.3) | 1.3 | Lab 1 reflection | A4, B4, C1 | 8 | Ch 1 |
| Data as numbers; structured vs unstructured (`02` 2.1) | 2.1 | — | A6, A7, B10 | 9 | Ch 2 |
| Five-step process (`02` 2.2) | 2.2 | Lab 2 Pass-or-Fail; optional Teachable Machine | A8, B6, B7, C2 | 10, 11, 12 | Ch 2 |
| Supervised / unsupervised / reinforcement (`02` 2.3) | 2.3 | — | A9, B8 | 13 | Ch 2 |
| Training, testing, overfitting (`02` 2.4) | 2.4 | Lab 2 "Test on new fruit" | A10, B9, C2 | 12, 14 | Ch 2 |
| Capability types: Narrow / AGI / Super (`03` 3.1) | 3.1 | Lab 3 Name That AI | A11, A12, B11, B12, B14, C3 | 16, 17, 38 | Ch 3 |
| Functional types (`03` 3.2) | 3.2 | Lab 3 reflection | A13–A15, B13, B15, C3 | 18 | Ch 3 |
| Computer vision (`04` 4.1) | 4.1 | Lab 4 Warehouse | A16, B16, B20 | 19, 20 | Ch 4 |
| Robotics, expert systems (`04` 4.2–4.3) | 4.2–4.3 | Lab 4 | A17, A18, A20, B17, B18, C4 | 20 | Ch 4 |
| Language AI / generative AI (`04` 4.4) | 4.4 | — | A19, B19 | 20 | Ch 4 |
| Traditional programming vs ML (`05` 5.1) | 5.1 | Lab 5 | A21, B23 | 21 | Ch 5 |
| Six trade-offs, black box, workforce (`05` 5.2–5.4) | 5.2–5.4 | Lab 5 Choose Your Tool | A22–A25, B21, B22, B24, B25, C5 | 22, 23 | Ch 5 |
| Symbolic AI, knowledge base, inference (`06` 6.1) | 6.1 | — | A26, B26, B30 | 25 | Ch 6 |
| Prolog (`06` 6.2) | 6.2 | Lab 6 Family Detective (AI Lab Prolog tab; SWISH; `family.pl`) | A29, A30, B27, B28, C6 | 26, 27 | Ch 6 |
| Strengths and limits of symbolic AI (`06` 6.3) | 6.3 | Lab 6 step 4 | A27, A28, B29, C6, C10 | 27 | Ch 6 |
| Artificial neuron (`07` 7.1–7.2) | 7.1–7.2 | Lab 7A Canteen Neuron; `canteen_neuron.py` | A31–A33, B31, B32, C7 | 28, 29 | Ch 7 |
| Layers, learning, loss, learning rate (`07` 7.3–7.4) | 7.3–7.4 | Lab 7B TensorFlow Playground (screenshots as fallback) | A34, B33, B34, C7 | 29, 30 | Ch 7 |
| Symbolic vs connectionist (`07` 7.5) | 7.5 | — | C10 | 27, 31 | Ch 7 |
| Network families: FF, CNN, RNN, Transformer (`07` 7.6) | 7.6 | — (CNN Explainer optional) | A35, B35 | 31 | Ch 7 |
| Behaviour-based AI, subsumption (`08` 8.1) | 8.1 | Lab 8A Layer the Vacuum | A36, B36 | 32 | Ch 8 |
| RL vocabulary (`08` 8.2) | 8.2 | Lab 8C | A37, A38, B38, C8 | 33 | Ch 8 |
| Exploration vs exploitation (`08` 8.3) | 8.3 | Lab 8B Three Doors; `three_doors_bandit.py` | A39, B37, B38, C8 | 34, 35 | Ch 8 |
| Q-learning (`08` 8.4) | 8.4 | Lab 8C Diamond Hunt; `diamond_hunt_qlearning.py` | B40, C8 | 36 | Ch 8 |
| Minecraft case study: VPT, DreamerV3 (`08` 8.5) | 8.5 | — | A40, B39, C9 | 2, 37, 38 | Ch 8 (Minecraft speedrun RL video) |
| Module wrap-up: three bets combined (`08`) | Wrap-up | — | C10 | 24, 39 | Ch 8 |
| Glossary, resources, references (`09`) | Glossary, Resources, References | — | — | 40, 41 | — |

## Consistency decisions applied to every resource

| Item | Agreed wording / value |
|---|---|
| Five steps | Input → Processing → Outcomes → Adjustments → Assessments |
| Capability types | Narrow AI (Weak AI), General AI (AGI / Strong AI), Super AI. Only Narrow exists. |
| ChatGPT | Narrow AI (limited to text-based tasks) |
| Prolog rule name | `aunt_or_uncle` (was `auntOrUncle` in v2) |
| Canteen neuron | weights friend +2, rain −3, hungry +2; GO if total ≥ 2; case E = 1 (stay), after rain = −1 case E = 3 (GO) |
| Fruit example | "red AND round" = 4/6; "red or green, and round" = 6/6 training, 4/6 on new fruit |
| Three doors | A = 1, B ≈ 0.83, C = 1.5 per turn |
| Diamond Hunt | lava −10, diamond +10, step −1; shortest path 8 steps |
| TensorFlow Playground | circle data, 0 hidden layers ≈ 0.53 test loss; 1 hidden layer × 4 neurons ≈ 0.008; learning rate 10 ≈ 0.74 |

## Known gaps

- The **Video Tutorials** column names chapters, not file names. The team must check each row against the final video files in the *Video Tutorials* submission and correct any chapter whose video covers a different topic. Recorded in the Submission Report as a limitation until confirmed.
- Topics marked "—" for Lab are covered by figures, worked examples and Quick Checks instead; adding a lab would repeat a neighbouring activity.
