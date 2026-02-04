import openai
from config import Config

# SambaNova API configuration
client = openai.OpenAI(
    api_key=Config.SAMBA_NOVA_API_KEY,
    base_url="https://api.sambanova.ai/v1",
)

def get_ai_response(prompt):
    response = client.chat.completions.create(
        model="llama3-70b", # Ya jo bhi model SambaNova provide kare
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content
