# generator.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

torch.set_num_threads(2)

def load_llm():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    # gpt2 has no pad token by default — set it to eos
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    return tokenizer, model

def generate_answer(tokenizer, model, prompt, max_new_tokens=120):
    # Ensure prompt is tokenized with truncation to model max length
    max_model_input = model.config.n_positions if hasattr(model.config, "n_positions") else 1024
    # Reserve space for new tokens
    max_input_length = max(1, max_model_input - max_new_tokens)

    inputs = tokenizer(prompt,
                       return_tensors="pt",
                       truncation=True,
                       max_length=max_input_length,
                       padding=False)

    # Move to model device if needed
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Use max_new_tokens to control how many tokens are generated (safer)
    outputs = model.generate(**inputs,
                             max_new_tokens=max_new_tokens,
                             do_sample=True,
                             top_k=50,
                             top_p=0.95,
                             pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
