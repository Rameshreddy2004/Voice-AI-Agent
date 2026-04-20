def build_messages(user_text, memory, lang):
    return [
        {"role": "system", "content": f"You are a multilingual medical assistant. Respond in {lang}."},
        {"role": "system", "content": f"Memory: {memory}"},
        {"role": "user", "content": user_text}
    ]
