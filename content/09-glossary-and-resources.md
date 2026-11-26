# Glossary {#glossary}

| Term | Meaning | Chapter |
|---|---|---|
| Action | A choice an RL agent makes, such as move, turn or mine. | 8 |
| Agent | The learner and decision-maker in reinforcement learning. | 8 |
| Artificial intelligence (AI) | Computer systems doing tasks that normally need human intelligence, such as recognising images, understanding language or making decisions. | 1 |
| Artificial general intelligence (AGI) | Theoretical AI that could learn and perform any intellectual task a human can, in new situations, without retraining. Also called Strong AI. | 3 |
| Backpropagation | The method that works out how each weight in a network should change to reduce the loss. | 7 |
| Bias (algorithmic) | Unfair patterns an AI learns from flawed data and then repeats or amplifies. | 1 |
| Black box | A model whose inputs and outputs are known but whose reasoning is unclear. | 5 |
| Computer vision | Narrow AI that interprets images and video: classification, detection, tracking, recognition. | 4 |
| Connectionism | Building intelligence from networks of simple connected units (neural networks). | 7 |
| Convolutional neural network (CNN) | A network that slides small filters over images; used for computer vision. | 7 |
| Deep learning | Machine learning with neural networks that have many hidden layers. | 1, 7 |
| Environment | Everything an RL agent interacts with. | 8 |
| Expert system | A rule-based program that gives advice in a specialist area. | 4, 6 |
| Exploration vs exploitation | The choice between trying new actions (explore) and repeating the best known action (exploit). | 8 |
| Feedforward network | A network where information flows one way, from input to output. | 7 |
| Inference engine | The part of a symbolic system that applies rules to facts to reach conclusions. | 6 |
| Knowledge base | The collection of facts and rules a symbolic system reasons with. | 6 |
| Learning rate | How big a step each weight update takes. Too big is unstable; too small is slow. | 7 |
| Limited memory AI | AI that uses recent data and past training to decide, such as self-driving cars and chatbots. | 3 |
| Loss | A number measuring how wrong a model's predictions are. | 7 |
| Machine learning | AI that learns patterns from data instead of following hand-written rules. | 1, 2 |
| Narrow AI | AI trained for one task or a narrow set of tasks; the only type that exists today. Also called Weak AI. | 3 |
| Natural language processing (NLP) | AI that works with human language: translation, chatbots, spam filters. | 4 |
| Overfitting | When a model memorises its training data (including noise) and performs badly on new data. | 2 |
| Policy | An RL agent's learned strategy for choosing actions. | 8 |
| Prolog | A logic programming language for writing facts and rules and asking questions. | 6 |
| Q-learning | An RL method that learns a value (Q) for every state–action pair from rewards. | 8 |
| Reactive machine | AI with no memory that reacts only to the current input, such as Deep Blue. | 3 |
| Recurrent neural network (RNN) | A network with loops that lets it use earlier items in a sequence. | 7 |
| Reinforcement learning (RL) | Learning to act by trial and error using rewards and penalties. | 2, 8 |
| Reward | The feedback number an agent receives after an action. | 8 |
| Sparse (delayed) reward | A reward that comes only after a long chain of actions. | 8 |
| State | The current situation of an agent and its environment. | 8 |
| Structured / unstructured data | Data in rows and columns / data with no fixed format (images, text, audio, video). | 2 |
| Subsumption architecture | A hierarchy of simple behaviours in which higher layers override (subsume) lower ones. | 8 |
| Super AI | Theoretical AI whose abilities would surpass humans in every area. | 3 |
| Supervised learning | Learning from examples that have the correct answers (labels). | 2 |
| Symbolic AI | AI that reasons over symbols using human-written rules. | 6 |
| Test data | Data hidden during training and used to check how well a model works on new examples. | 2 |
| Transformer | A network built on self-attention; the basis of large language models. | 7 |
| Unsupervised learning | Learning patterns or groups from data with no labels. | 2 |
| Weight | A number setting how strongly one unit influences another in a neural network. | 7 |

# Supplementary Resources {#supplementary}

| Resource | What it is and why to use it | How to access |
|---|---|---|
| **CSMAXXXING AI Lab** | Our own offline web page: one interactive mission per chapter with instant feedback, a real Prolog engine, a neuron simulator, a bandit game and a Q-learning grid. Missions award badges (saved in your browser only). | `activities/ai-lab/index.html`. Double-click to open in Chrome, Edge, Firefox or Safari. No internet needed. |
| **Python activity files** | `canteen_neuron.py`, `three_doors_bandit.py` and `diamond_hunt_qlearning.py`: the same ideas as Labs 7A, 8B and 8C as short, commented programs to run and modify. | `activities/code/`. Needs Python 3 (no extra packages). Run with `python filename.py`. |
| **Prolog file** | `family.pl`, the knowledge base for Lab 6. | `activities/prolog/`. Paste into SWISH or the AI Lab. |
| **CSMAXXXING Video Tutorials** | Our team's video explanations for each chapter, including the Minecraft speedrun / reinforcement-learning lecture. Submitted separately as the *Video Tutorials* assignment. | Team Google Drive folder: <https://drive.google.com/drive/folders/1lsnS5zVKpcZWO3ieUxUFK0_NMUHiegBL> |
| **Kahoot practice challenge** (optional) | A timed multiple-choice quiz made by our team for quick recall practice. Kahoot challenges can expire; if the link no longer works, use the Test Bank instead, which covers the same content. | <https://kahoot.it/challenge/03772119?challenge-id=57467697-25a7-424c-9f82-3967c1284b04_1794033556332> |
| **Test Bank** | 40 true/false, 40 multiple-choice and 10 open-ended questions with explained answers. | Separate Word file in the Study Guide package. |

# References {#references}

- Baker, B. et al. (2022). Video PreTraining (VPT): Learning to act by watching unlabeled online videos. *NeurIPS 2022*. arXiv:2206.11795.
- China, C. R. (2024). *Artificial intelligence advantages and disadvantages.* IBM. <https://www.ibm.com/think/insights/artificial-intelligence-advantages-disadvantages>
- Coursera Staff (2026). *How Does AI Work?* <https://www.coursera.org/articles/how-does-ai-work>
- Coursera Staff (n.d.). *4 Types of AI.* <https://www.coursera.org/articles/types-of-ai>
- DataCamp (2023). *What is Symbolic AI?* <https://www.datacamp.com/blog/what-is-symbolic-ai>
- Hafner, D., Pasukonis, J., Ba, J. and Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature.* <https://www.nature.com/articles/s41586-025-08744-2>
- IBM Data and AI Team (2024). *Understanding the different types of artificial intelligence.* <https://www.ibm.com/think/topics/artificial-intelligence-types>
- IBM (n.d.). *What is a neural network?*; *What is a recurrent neural network?*; *What is a transformer model?* <https://www.ibm.com/think>
- Moore, R. K. (2016). PCT and beyond. arXiv:1611.05379.
- National Institute of Standards and Technology (2023). *AI Risk Management Framework.* <https://www.nist.gov/itl/ai-risk-management-framework>
- OpenAI (2022). *Learning to play Minecraft with Video PreTraining.* <https://openai.com/index/vpt/>
- OVHcloud (n.d.). *What is reinforcement learning?* <https://www.ovhcloud.com/en-in/learn/what-is-reinforcement-learning/>
- Smilkov, D. and Carter, S. *TensorFlow Playground.* Apache 2.0. <https://github.com/tensorflow/playground>
- Stanford Emerging Technology Review (2026). *Artificial Intelligence.* <https://setr.stanford.edu/technology/artificial-intelligence/2026>
- Stanford Encyclopedia of Philosophy (n.d.). *Connectionism.* <https://plato.stanford.edu/entries/connectionism/>
- Tau Prolog (v0.3.4). BSD-3-Clause. <http://tau-prolog.org>
- Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433–460.
- University of York (n.d.). *Rodney A. Brooks.* <https://www-users.cs.york.ac.uk/susan/books/pages/b/RodneyABrooks.htm>
- van der Walt, S. et al. (2014). scikit-image: image processing in Python. *PeerJ*, 2, e453.
- Verpex (2025). *Reinforcement learning: How machines learn through rewards.* <https://verpex.com/blog/website-tips/what-is-reinforcement-learning>
- Wang, Z. J. et al. (2020). CNN Explainer. arXiv:2004.15004.
- Wooldridge, M., Parsons, S. and Payne, T. R. (2018). *COMP310 Chapter 5.* University of Liverpool.

**Media credits.** All figures and diagrams, the AI Lab and the mascot "Max" were created for this module by the CSMAXXXING team with AI assistance (recorded in the project log); every figure is generated from code kept in the repository. Photographs in Figures 2.1, 2.2, 4.1 and 7.4 are sample images distributed with the open-source scikit-image library (the astronaut image is a public-domain NASA photograph). Figures 7.6–7.8 are screenshots of TensorFlow Playground (Apache 2.0). The Minecraft-style diagram in Figure 8.5 is an original drawing, not game artwork.
