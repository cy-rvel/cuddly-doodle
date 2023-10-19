import openai

# 设置你的API密钥
openai.api_key = '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'

def ask_gpt4(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']

# 测试函数
if __name__ == "__main__":
    question = input("请告诉我大语言模型是什么 ")
    try:
        answer = ask_gpt4(question)
        print("GPT-4的回答:", answer)
    except openai.error.RateLimitError:
        print("已超过API使用限额，请稍后再试或检查你的OpenAI账户。")