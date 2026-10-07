# Aplicação com LLMs

Projeto de estudo para integrar um modelo de linguagem a uma aplicação Python. Usa a biblioteca `openai` com o endpoint compatível do Gemini.

## Preparação

1. Instale as dependências: `python -m pip install -r requirements.txt`.
2. Crie um arquivo `.env` na pasta do projeto e coloque `GEMINI_API_KEY=sua_chave_aqui` (chave criada no Google AI Studio).
3. Execute `python main.py`.

O arquivo `.env` contém sua chave e é ignorado pelo Git. O `.env.example` é apenas um modelo, sem chave real. O exemplo usa `gemini-3.8-flash`; a disponibilidade e os limites gratuitos dependem do projeto no Google AI Studio.

No código, `base_url` direciona o cliente ao Gemini. A requisição usa `chat.completions.create`, e o texto retornado fica em `resposta.choices[0].message.content`.
