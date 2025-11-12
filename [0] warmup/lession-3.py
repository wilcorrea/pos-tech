from openai_utils import gerar_resposta


def carrega(nome_do_arquivo: str) -> str:
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")
        return ""


prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./dados/lista_de_compras_10_clientes.csv")

gerar_resposta(
    prompt_sistema=prompt_sistema,
    prompt_usuario=prompt_usuario,
    model="gpt-3.5-turbo",
    temperature=1.0,
    max_tokens=256
)
