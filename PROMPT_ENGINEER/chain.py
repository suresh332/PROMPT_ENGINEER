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
def generate_answer(refined_prompt, max_tokens=200):
    # Tokenize input
    inputs = tokenizer(refined_prompt, return_tensors="pt").to(device)

    # Generate output
    output = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    # Decode and return
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer.strip()