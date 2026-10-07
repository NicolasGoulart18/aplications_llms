import os #pacote do SO
from dotenv import load_dotenv #pacote para ler as variáveis de ambiente do arquivo .env (variavel da chave de api)
from openai import OpenAI #pacote para acessar a API da OpenAI

load_dotenv() # lendo as variaveis de ambiente do arquivo .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # OpenAI-> metodo que vai contruir o cliente, e informo que a api key é aquel que esta no sistema operacionala, carregado no arquivo .env
MODELO = "gpt-5.5-pro"

def testar_conexao():
    resposta = client.responses.create(
        model=MODELO,
        input= "Responda com 'Conexão bem sucedida!' para testar a conexão com a API da OpenAI."
    )
    return resposta.output_text

def main():
    print("Testando a conexão com a API da OpenAI...")
    print(testar_conexao())

if __name__ == "__main__":
    main()