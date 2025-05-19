import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="🧠 Fine-Tuned GPT-2 Text Generator", layout="centered")

# Title
st.title("📝 Fine-Tuned GPT-2 Text Generator")
st.markdown("Enter a prompt and generate creative text using your **fine-tuned GPT-2 model** (trained on WikiText-2).")

# Sidebar controls
st.sidebar.title("⚙️ Settings")
max_length = st.sidebar.slider("Max length", 50, 300, 100, step=10)
temperature = st.sidebar.slider("Temperature", 0.5, 1.5, 1.0, step=0.1)

# Load model
@st.cache_resource
def load_generator():
    device = 0 if torch.cuda.is_available() else -1
    generator = pipeline(
        "text-generation",
        model="./gpt2-finetuned-wikitext2",
        tokenizer="./gpt2-finetuned-wikitext2",
        device=device
    )
    return generator

generator = load_generator()

# Prompt input
prompt = st.text_area("✍️ Enter your prompt", value="In the beginning", height=150)

# Generate button
if st.button("🚀 Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Generating text..."):
            output = generator(prompt, max_length=max_length, temperature=temperature, num_return_sequences=1)
            generated_text = output[0]['generated_text']
        st.success("✅ Generation complete!")
        st.text_area("📄 Output", generated_text, height=300)

# Footer
st.markdown("---")
st.caption("Model: Fine-tuned GPT-2 on WikiText-2 | Built with ❤️ using Streamlit and HuggingFace Transformers")
