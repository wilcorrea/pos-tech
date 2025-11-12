from openai_utils import gerar_resposta


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

    gerar_resposta(
        prompt_sistema=prompt_sistema,
        prompt_usuario=produto,
        model="gpt-3.5-turbo",
        temperature=1.0,
        max_tokens=256
    )


print("Digite as categorias validas:")
categorias_validas = input()
while True:
    print("Digite o nome do produto:")
    nome_do_produto = input()
    categorizar_produto(nome_do_produto, categorias_validas)
