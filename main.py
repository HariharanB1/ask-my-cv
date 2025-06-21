from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Load the CV text
def load_cv():
    with open("cv.txt", "r", encoding="utf-8") as file:
        return file.read()

def ask_cv(question, cv_text):
    prompt = f"""
You are a helpful assistant answering questions about Hariharan's resume. Only refer to the content inside the CV below.

CV:
{cv_text}

Based on the above CV, answer the following question truthfully. If the answer is not in the CV, say: "This information is not available in the CV."

Question: {question}
Answer:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


# Run it
if __name__ == "__main__":
    cv_data = load_cv()
    while True:
        q = input("Ask about the CV (or type 'quit'): ")
        if q.lower() in ['quit', 'exit']:
            break
        answer = ask_cv(q, cv_data)
        print("\n👉", answer, "\n")
