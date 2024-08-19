import anthropic
import os
import dotenv

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="Listar apenas os nomes dos alimentos, sem adicionar descrição.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "3 alimentos com brócolis"
                }
            ]
        }
    ]
)
resposta = message.content[0].text
print(resposta)