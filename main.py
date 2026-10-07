import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Carrega as variáveis do arquivo .env

chave_api = os.getenv("GEMINI_API_KEY")
if not chave_api:
    raise RuntimeError("Defina GEMINI_API_KEY no arquivo .env.")

# A biblioteca OpenAI envia as requisições para a API compatível do Gemini.
client = OpenAI(
    api_key=chave_api,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
MODELO = "gemini-3.8-flash"


def testar_conexao():
    resposta = client.chat.completions.create(
        model=MODELO,
        messages=[
            {
                "role": "user",
                "content": "Responda com 'Conexão bem sucedida!' para testar a conexão com a API do Gemini.",
            }
        ],
    )
    return resposta.choices[0].message.content


def main():
    print("Testando a conexão com a API do Gemini...")
    print(testar_conexao())


if __name__ == "__main__":
    main()
