# 🧠 DialogueForge: AI-Powered NPC Dialogue Generator

DialogueForge is a generative AI application that creates dynamic NPC (Non-Playable Character) dialogue for games based on player input, character personality, and emotion.

Built using:
- 🤖 GPT-2 (Hugging Face Transformers)
- 🧠 LangChain (Chat memory)
- 🎭 Streamlit (UI)
- 🎙️ gTTS (Text-to-Speech voice output)

Live Demo: [Launch on Hugging Face Spaces](https://huggingface.co/spaces/your-username/dialogueforge) 🚀  
(Replace with your actual Space link)

---

## 🎮 Features

- Select from unique game NPCs (e.g., Angry Knight, Mysterious Mage)
- Choose emotional tone: Happy, Sad, Angry, etc.
- Generate dynamic, in-character dialogue
- Hear the NPC speak the generated line using TTS
- Chat memory so NPCs remember previous prompts

---

## 📸 Demo Screenshot

![DialogueForge Screenshot](assets/sample_ui.png)

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/your-username/dialogueforge.git
cd dialogueforge
pip install -r requirements.txt
streamlit run app.py
