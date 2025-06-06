from .config import SYSTEM_PROMPT

def build_prompt(user_input, history):
    prompt = "<|begin_of_text|>\n"
    prompt += "<|start_header_id|>system<|end_header_id|>\n" + SYSTEM_PROMPT + "\n<|eot_id|>\n"

    for turn in history:
        prompt += "<|start_header_id|>user<|end_header_id|>\n" + turn["user"] + "\n<|eot_id|>\n"
        prompt += "<|start_header_id|>assistant<|end_header_id|>\n" + turn["assistant"] + "\n<|eot_id|>\n"

    prompt += "<|start_header_id|>user<|end_header_id|>\n" + user_input + "\n<|eot_id|>\n"
    prompt += "<|start_header_id|>assistant<|end_header_id|>\n"
    return prompt
