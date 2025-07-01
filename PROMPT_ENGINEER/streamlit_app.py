import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return tokenizer, model, device

tokenizer, model, device = load_model()

# Refining function (simplified)
def refine_prompt_simple(user_prompt):
    instruction = f"""
Rewrite this prompt to be more clear, specific, and professional for an AI to understand and answer better.

Original: {user_prompt}
Rewritten:
"""
    inputs = tokenizer(instruction, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=80)
    refined = tokenizer.decode(output[0], skip_special_tokens=True)
    return refined.split("Rewritten:")[-1].strip()

# Answer generation
def generate_answer(refined_prompt):
    inputs = tokenizer(refined_prompt, return_tensors="pt").to(device)
    output = model.generate(
        **inputs,
        max_new_tokens=250,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Streamlit UI
st.title("🧠 Prompt Refining Agent")
st.markdown("Refines your vague prompt using prompt engineering rules and gives a better LLM answer!")

user_prompt = st.text_area("✍️ Enter your raw prompt:", placeholder="e.g. tell me about ai")

if st.button("🔁 Refine & Generate"):
    with st.spinner("Refining prompt..."):
        refined = refine_prompt_simple(user_prompt)
        st.success("✅ Prompt refined!")
        st.markdown(f"**📝 Refined Prompt:** `{refined}`")

    with st.spinner("Generating answer..."):
        answer = generate_answer(refined)
        st.success("✅ Answer generated!")
        st.markdown(f"**🤖 Answer:**\n\n{answer}")
