# Warmup - Primeira Iteração

Repositório de aquecimento para explorar integração com a API da OpenAI usando Python.

## Descrição

Este projeto contém um exemplo básico de integração com a API GPT-3.5 da OpenAI, demonstrando como fazer chamadas simples para geração de conteúdo textual.

## Estrutura do Projeto

```
000.warmup/
├── .env                # Template de variáveis de ambiente (versionado)
├── .env.local          # Variáveis de ambiente locais (NÃO versionado)
├── .gitignore          # Arquivos ignorados pelo Git
├── lession-1.py        # Script principal de exemplo
├── pyproject.toml      # Configuração do projeto Python
├── poetry.lock         # Lock de dependências do Poetry
└── README.md           # Documentação do projeto
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

### Pré-requisitos

- Python 3.13 ou superior
- Poetry instalado (`curl -sSL https://install.python-poetry.org | python3 -`)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd 000.warmup
   ```

2. **Instale as dependências com Poetry**
   ```bash
   poetry install
   ```

3. **Configure as variáveis de ambiente**

   ⚠️ **OBRIGATÓRIO**: Copie o arquivo `.env` para `.env.local` e configure sua chave da API:

   ```bash
   cp .env .env.local
   ```

   Edite o arquivo `.env.local` e substitua o placeholder pela sua chave real da OpenAI:
   ```
   OPENAI_API_KEY=sk-seu-token-real-aqui
   ```

   > **Nota**: O arquivo `.env` contém apenas placeholders e serve como template. O arquivo `.env.local` contém suas credenciais reais e **NÃO deve ser commitado** (já está no .gitignore).

## Exemplo de Uso

O script `lession-1.py` demonstra uma chamada básica à API da OpenAI para gerar nomes de produtos fictícios.

### Executando o script

⚠️ **OBRIGATÓRIO**: Ative o ambiente virtual antes de executar o script:

**Opção 1: Usando Poetry (recomendado)**
```bash
poetry run python lession-1.py
```

**Opção 2: Ativando o ambiente virtual manualmente**
```bash
source .venv/bin/activate
python3 lession-1.py
```

**Opção 3: Usando o shell do Poetry**
```bash
poetry shell
python3 lession-1.py
```

### O que o script faz

1. Carrega as variáveis de ambiente do arquivo `.env` (base)
2. Sobrescreve com valores do arquivo `.env.local` (credenciais reais)
3. Inicializa o cliente OpenAI com a chave da API
4. Faz uma requisição ao modelo GPT-3.5 Turbo (16k)
5. Solicita a geração de 5 nomes de produtos fictícios
6. Exibe o resultado no console

### Padrão 12 Factor App

Este projeto segue o padrão [12 Factor App](https://12factor.net/) para gestão de configurações:

- **`.env`** → Template versionado com placeholders (commitado no git)
- **`.env.local`** → Valores reais e sensíveis (ignorado pelo git)

O código carrega primeiro o `.env` como base e depois o `.env.local` para sobrescrever valores específicos do ambiente local.

## Modelo Utilizado

- **gpt-3.5-turbo-16k** - Versão do GPT-3.5 com contexto expandido de 16k tokens

## Autor

William Correa (wilcorrea@gmail.com)

## Versão

0.1.0
