from openai_utils import gerar_resposta
import tiktoken

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo")


def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./dados/lista_de_compras_10_clientes.csv")

lista_de_tokens = codificador.encode(prompt_sistema + prompt_usuario)
numero_de_tokens = len(lista_de_tokens)
print(f"Número de tokens na entrada: {numero_de_tokens}")
modelo = "gpt-3.5-turbo"
tamanho_esperado_saida = 2048
if numero_de_tokens >= 4096 - tamanho_esperado_saida:
    modelo = "gpt-3.5-turbo-16k"
print(f"Modelo escolhido: {modelo}")

gerar_resposta(
    prompt_sistema=prompt_sistema,
    prompt_usuario=prompt_usuario,
    model=modelo,
    temperature=1.0,
    max_tokens=tamanho_esperado_saida
)
