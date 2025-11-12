from openai import OpenAI
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletion
)
import dotenv

dotenv.load_dotenv('.env')
dotenv.load_dotenv('.env.local', override=True)

client = OpenAI()


def gerar_resposta(
    prompt_sistema: str,
    prompt_usuario: str,
    model: str = "gpt-3.5-turbo",
    temperature: float = 1.0,
    max_tokens: int = 256,
    top_p: float = 1.0,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0,
    imprimir: bool = True
) -> str:
    """
    Gera uma resposta usando a API da OpenAI.

    Args:
        prompt_sistema: Instruções do sistema para o modelo
        prompt_usuario: Prompt do usuário
        model: Modelo a ser usado (padrão: gpt-3.5-turbo)
        temperature: Controla aleatoriedade (0.0-2.0)
        max_tokens: Máximo de tokens na resposta
        top_p: Nucleus sampling
        frequency_penalty: Penalidade por frequência
        presence_penalty: Penalidade por presença
        imprimir: Se True, imprime a resposta no console

    Returns:
        O conteúdo da resposta gerada
    """
    mensagem_sistema: ChatCompletionSystemMessageParam = {
        "role": "system",
        "content": prompt_sistema
    }

    mensagem_usuario: ChatCompletionUserMessageParam = {
        "role": "user",
        "content": prompt_usuario
    }

    resposta: ChatCompletion = client.chat.completions.create(
        model=model,
        messages=[mensagem_sistema, mensagem_usuario],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    conteudo = resposta.choices[0].message.content or ""

    if imprimir:
        print(conteudo)

    return conteudo
