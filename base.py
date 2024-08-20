import anthropic
import dotenv
import os

dotenv.load_dotenv()
cliente = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"

prompt_do_sistema = f"""

"""
prompt_do_usuario = ""

mensagem = cliente.messages.create(
    model=modelo,
    max_tokens=2000,
    temperature=0,
    system=prompt_do_sistema,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt_do_usuario
                }
            ]
        }
    ]
)
resposta = mensagem.content[0].text