from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam
import dotenv

dotenv.load_dotenv('.env')
dotenv.load_dotenv('.env.local', override=True)

client = OpenAI()

mensagem_sistema: ChatCompletionSystemMessageParam = {
    "role": "system",
    "content": "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
}

mensagem_usuario: ChatCompletionUserMessageParam = {
    "role": "user",
    "content": "Gere 5 produtos"
}

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[mensagem_sistema, mensagem_usuario]
)

print(resposta.choices[0].message.content)
