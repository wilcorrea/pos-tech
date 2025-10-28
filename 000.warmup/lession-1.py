from openai import OpenAI
import dotenv

# Carrega .env como base
dotenv.load_dotenv('.env')
# Carrega .env.local para sobrescrever valores locais (override=True é o padrão)
dotenv.load_dotenv('.env.local', override=True)

client = OpenAI()

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages = [
      {
       "role" : "system",
       "content" : "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
      },
      {
       "role" : "user",
       "content" : "Gere 5 produtos"
      }
    ]
)

print(resposta.choices[0].message.content)
