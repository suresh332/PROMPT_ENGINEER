# PROMPT_ENGINEER
# 🧠 Prompt Engineering Agent

A lightweight, open-source prompt refining agent inspired by Google's prompt engineering research. Designed to improve the quality of user prompts and generate accurate answers using free and local models (no expensive APIs required).

## 🔍 Overview

This project is a two-step agent system:

1. **Prompt Refinement Agent** – Takes a raw user input (e.g., "tell me about AI") and rewrites it into a clearer, goal-driven prompt using a research-backed prompt template.
2. **Answer Generation Agent** – Takes the refined prompt and generates a final answer using a lightweight language model.

The system is currently built using:
- `google/flan-t5-small` from Hugging Face (lightweight and free)
- Streamlit for the frontend UI
- Python backend

This setup ensures it can run even on low-resource devices or Colab environments, without needing expensive OpenAI or commercial APIs.

---

## 🧪 Example

**Raw Prompt:**
tell me about ai
**Refined Prompt:**
Explain the concept of Artificial Intelligence in simple terms with examples.
**Final Answer:**
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. These machines are programmed to think and learn. For example, AI powers virtual assistants like Siri or recommendation systems on Netflix.

📁 prompt-engineer-agent/
├── streamlit_app.py # Main Streamlit interface
├── chain.py # Prompt refinement and generation logic
├── model_setup.py # Loads and manages Hugging Face models
├── example.txt # Sample prompts for testing
├── requirements.py # Python dependencies (note: use .txt in production)
└── README.md # Project documentation (this file)

📌 Future Plans
🔁 Replace flan-t5-small with chatgpt, gemma-2b-it, or mistral when API/GPU access allows

🧠 Train a domain-specific refinement model

✨ Add advanced instruction templates (e.g., CoT, Self-Ask, SMART prompting)

🔍 Integrate retrieval for context-aware answering (RAG)

📚 Based On
📄 Google Prompt Engineering Whitepaper (2024)

🤗 Hugging Face Transformers

🧪 Streamlit for UI

🙌 Acknowledgements
Thanks to the open-source community and research pioneers in prompting, including Google, Hugging Face, and OpenAI for inspiration and tools.

📬 Contact
Made with ❤️ by purbia suresh
📧 Email: suresh7665purbiya@gmail.com
🔗 www.linkedin.com/in/suresh7665purbiya
