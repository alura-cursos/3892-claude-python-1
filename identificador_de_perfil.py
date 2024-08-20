import anthropic
import dotenv
import os

dotenv.load_dotenv()
cliente = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"

def identificador_de_perfil():
    prompt_do_sistema = f"""
    Identifique o perfil de consumo de comida para cada cliente a seguir.

    # Formato da Saída

    cliente - perfil do cliente em 3 palavras.
    """
    prompt_do_usuario = """
    cliente00:"caldo verde, bacalhau à brás, pastel de nata"
    cliente01:"sushi, tempura, sorvete mochi"
    cliente02:"hambúrguer, batata frita, milkshake de baunilha"
    cliente03:"pizza margherita, bruschetta, tiramisù"
    cliente04:"tacos, guacamole, churros"
    cliente05:"falafel, homus, baklava"
    cliente06:"curry de frango, naan, lassi de manga"
    cliente07:"salada caesar, sopa de tomate, cheesecake"
    cliente08:"sushi vegetariano, edamame, bolo de chá verde"
    cliente09:"bife grelhado, purê de batatas, pudim de leite"
    cliente10:"paella, tapas, crema catalana"
    """

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
    resposta = mensagem
    return resposta

resposta_assistente = identificador_de_perfil()
resposta_texto = resposta_assistente.content[0].text
resposta_tokens = resposta_assistente.usage
print(resposta_texto)
print(f'Tokens de entrada: {resposta_tokens.input_tokens}')
print(f'Tokens de saida: {resposta_tokens.output_tokens}')