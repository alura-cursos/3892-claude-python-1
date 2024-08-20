import anthropic
import dotenv
import os
from helpers import *

dotenv.load_dotenv()
cliente = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"

def analisador_de_sentimentos(restaurante):
    prompt_do_sistema = f"""
    Você é um analisador de sentimentos de avaliações de restaurantes.
    Escreva um parágrafo com até 50 palavras resumindo as avaliações e
    depois atribua qual o sentimento geral para o produto.
    Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

    # Formato de Saída

    Nome do Restaurante: {restaurante}
    Resumo das Avaliações:
    Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
    Ponto fortes: lista com três bullets
    Pontos fracos: lista com três bullets

    """
    prompt_do_usuario = carrega(f'./dados/avaliacoes/avaliacoes-{restaurante}.txt')
    print(f'Iniciou a análise do {restaurante}')
    try:
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
        salva(f'./dados/avaliacoes/analise-{restaurante}.txt',resposta)
        print(f'Finalizou a análise do {restaurante}')
    except anthropic.APIConnectionError as e:
        print("O servidor não pode ser acessado! Erro:", e.__cause__)
    except anthropic.RateLimitError as e:
        print("Um status code 429 foi recebido! Limite de acesso foi atingido.")
    except anthropic.APIStatusError as e:
        print(f"Um erro {e.status_code} foi recebido. Mais informações: {e.response}")
    except Exception as e:
        print(f"Um erro insperado ocorreu: {e}")

lista_de_restaurantes = ['Restaurante de Comida Vegana', 'Restaurante de Comida Chinesa','Restaurante de Bolos e Doces']

for restaurante in lista_de_restaurantes:
    analisador_de_sentimentos(restaurante)