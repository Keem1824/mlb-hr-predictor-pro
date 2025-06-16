
# ask_gpt.py — plug-and-play GPT insight mode
import os

# UNCOMMENT WHEN ONLINE
# import openai
# from dotenv import load_dotenv
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question, context=""):
    # UNCOMMENT WHEN ONLINE
    # prompt = f"""You are an MLB analytics expert. Based on this HR prediction data:
{context}

Answer: {question}"""
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return response['choices'][0]['message']['content']
    return "🧠 [Mocked GPT Response] This would be a smart, insightful answer using HR probabilities and context."
