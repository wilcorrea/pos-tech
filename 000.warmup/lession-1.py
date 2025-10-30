from openai_utils import gerar_resposta

gerar_resposta(
    prompt_sistema="Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário.",
    prompt_usuario="Gere 5 produtos",
    model="gpt-3.5-turbo-16k"
)
