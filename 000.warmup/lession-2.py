from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
import dotenv

dotenv.load_dotenv('.env')
dotenv.load_dotenv('.env.local', override=True)

client = OpenAI()


def categorizar_produto(produto: str, categorias: str) -> None:
    prompt_sistema = f"""
    Você é um categorizador de produtos.
    Você deve escolher uma categoria da lista abaixo:
    Se as categorias informadas não forem categorias validas, responda com "Não posso ajudá-lo com isso"
    ##### Lista de categorias válidas
    {categorias}
    ##### Exemplo
    bola de tênis
    Esportes
    """

    mensagem_sistema: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": prompt_sistema
    }

    mensagem_usuario: ChatCompletionUserMessageParam = {
        "role": "user",
        "content": produto
    }

    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[mensagem_sistema, mensagem_usuario],
        temperature=1.0,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(resposta.choices[0].message.content)


print("Digite as categorias validas:")
categorias_validas = input()
while True:
    print("Digite o nome do produto:")
    nome_do_produto = input()
    categorizar_produto(nome_do_produto, categorias_validas)
