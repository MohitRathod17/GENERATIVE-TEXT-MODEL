# 🧠 Fine-Tuned GPT-2 Text Generator

A Streamlit web app for generating creative text using a **fine-tuned GPT-2 model** trained on WikiText-2. Built with 🤗 HuggingFace Transformers and 🐍 PyTorch.

---

## 🚀 Features

- 📝 Generate coherent and creative text using your custom fine-tuned GPT-2 model.
- 🎛️ Adjustable generation parameters:
  - `max_length`
  - `temperature`
- ⚡ GPU support (if available)
- 🖥️ Clean and user-friendly interface using Streamlit

---

## 📁 Project Structure

```text
.
├── app.py                    # Streamlit application
├── text_generator.ipynb      # Jupyter Notebook (model training or testing)
├── gpt2-finetuned-wikitext2/ # Directory with fine-tuned GPT-2 model and tokenizer
