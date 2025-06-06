from llama_chat.llm_engine import llm
from llama_chat.prompt_builder import build_prompt

def chat_loop():
    print("🦙 LLaMA 3.2 3B CLI Chat. Type '/exit' to quit.\n")
    history = []

    while True:
        user_input = input("👤 You: ").strip()
        if user_input.lower() == "/exit":
            break

        prompt = build_prompt(user_input, history)

        response = ""
        for chunk in llm(prompt, max_tokens=512, stop=["<|eot_id|>"], stream=True):
            delta = chunk["choices"][0]["text"]
            print(delta, end="", flush=True)
            response += delta

        print()
        history.append({"user": user_input, "assistant": response.strip()})

if __name__ == "__main__":
    chat_loop()
