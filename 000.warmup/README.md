# Warmup - Primeira Iteração

Repositório de aquecimento para explorar integração com a API da OpenAI usando Python.

## Descrição

Este projeto contém um exemplo básico de integração com a API GPT-3.5 da OpenAI, demonstrando como fazer chamadas simples para geração de conteúdo textual.

## Estrutura do Projeto

```
000.warmup/
├── .env.local          # Configuração de variáveis de ambiente
├── .gitignore          # Arquivos ignorados pelo Git
├── lession-1.py        # Script principal de exemplo
├── pyproject.toml      # Configuração do projeto Python
└── poetry.lock         # Lock de dependências do Poetry
```

## Tecnologias Utilizadas

- **Python 3.13+**
- **OpenAI API** - Cliente oficial da OpenAI para Python
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **Poetry** - Gerenciador de dependências e ambientes virtuais

## Dependências

- `openai (>=2.6.1,<3.0.0)` - Cliente da API OpenAI
- `python-dotenv (>=1.2.1,<2.0.0)` - Carregamento de variáveis de ambiente
- `requests (>=2.32.5,<3.0.0)` - Requisições HTTP

## Configuração

1. Clone o repositório
2. Crie um arquivo `.env.local` com sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_aqui
   ```
3. Instale as dependências usando Poetry:
   ```bash
   poetry install
   ```

## Exemplo de Uso

O script `lession-1.py` demonstra uma chamada básica à API da OpenAI para gerar nomes de produtos fictícios:

```python
python lession-1.py
```

### O que o script faz

- Carrega as variáveis de ambiente do arquivo `.env.local`
- Inicializa o cliente OpenAI
- Faz uma requisição ao modelo GPT-3.5 Turbo
- Solicita a geração de 5 nomes de produtos fictícios
- Exibe o resultado no console

## Modelo Utilizado

- **gpt-3.5-turbo-16k** - Versão do GPT-3.5 com contexto expandido de 16k tokens

## Autor

William Correa (wilcorrea@gmail.com)

## Versão

0.1.0
