import streamlit as st
from transformers import pipeline, set_seed
from langchain.llms import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from gtts import gTTS
import tempfile
import os

# --- SETUP ---
st.set_page_config(page_title="DialogueForge", page_icon="🗣️")
st.title("🧠 DialogueForge: AI NPC Dialogue Generator with Memory & Voice")

# Character templates
character_templates = {
    "Mysterious Mage": "You are a wise and ancient mage. Speak in riddles and old tongue.",
    "Angry Knight": "You are a furious knight betrayed by your king. Speak with rage and pride.",
    "Sneaky Thief": "You are a sarcastic thief always up to mischief. Speak casually and with humor.",
    "Innocent Villager": "You are a naive villager witnessing something strange. Speak simply, with fear."
}

# Emotion tone modifiers
emotion_tones = {
    "Neutral": "",
    "Angry": "Speak with a harsh and furious tone.",
    "Happy": "Speak with joy and excitement.",
    "Sad": "Speak in a quiet, melancholic tone.",
    "Sarcastic": "Respond with witty, ironic humor."
}

# --- LLM Setup ---
@st.cache_resource
def load_llm():
    generator_pipeline = pipeline("text-generation", model="gpt2", max_new_tokens=100)
    return HuggingFacePipeline(pipeline=generator_pipeline)

llm = load_llm()
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# --- UI INPUTS ---
character = st.selectbox("🎭 Choose NPC Character", list(character_templates.keys()))
emotion = st.selectbox("🎨 Select Emotion", list(emotion_tones.keys()))
user_input = st.text_input("📝 What does the player say or do?", placeholder="e.g., The hero enters the tavern...")

# --- GENERATE RESPONSE ---
if st.button("Generate NPC Response"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        # Build prompt
        full_prompt = f"{character_templates[character]} {emotion_tones[emotion]} Situation: {user_input}"
        
        # Generate dialogue
        response = conversation.run(full_prompt)

        # Display output
        st.markdown("### 🎙️ NPC Says:")
        st.success(response)

        # Text-to-Speech
        try:
            tts = gTTS(response)
            with tempfile.NamedTemporaryFile(delete=True) as fp:
                tts_path = f"{fp.name}.mp3"
                tts.save(tts_path)
                audio_file = open(tts_path, 'rb')
                st.audio(audio_file.read(), format='audio/mp3')
        except Exception as e:
            st.error(f"Voice generation failed: {e}")

# --- Show Chat History ---
with st.expander("🧾 Chat Memory"):
    st.text(memory.buffer if memory.buffer else "No conversation history yet.")

