import requests as req
import json

#enviar arquivos por uma API

def enviar_arquivo():
    # Definição do caminho do arquivo
    caminho = r"C:\Users\dudag\Downloads\3_historias_de_usuario.docx" # CORRIJA SEU LINK AQUI

    # URL do serviço de upload
    url = "https://file.io"

    # Abrir o arquivo e enviá-lo
    with open(caminho, "rb") as arquivo:
       response = req.post(url, files={"file": arquivo})

    # Processar a resposta
    for line in response.text.splitlines():
        if "https://file.io/" in line:
            try:
                data = json.loads(line)
                print("JSON data:", data)

                # Exibir informações do arquivo enviado
                print("Link para o arquivo enviado", data.get("link", "Não disponível"))
                print("Key:", data.get("key", "Não disponível"))

            except json.JSONDecodeError as e:
               print("Erro ao decodificar JSON:", e)
               print("Linha bruta:", line)
            break

def enviar_arquivo_chave():
    #caminho para arquivo e a chave de upload:
    caminho = "C:/Users/dudag/Downloads/3_historias_de_usuario.docx"
    chave_acesso = 

    #enviar arquivo
    requisicao = req.post(
        url="https://file.io",
        files={"file":open(caminho, "rb")},
        headers = {"Authorization": chave_acesso}
    )
    saida_requisicao = requisicao.json()

def receber_arquivo(file_url):
    requisicao = req.get(file_url)

    #Para SALVAR o arquivo
    if requisicao.ok:
        with open ("arquivo_baixado.pdf", "wb") as file:
            file.write(requisicao.content)
        print("Arquivo baixado com Sucesso!")
    else:
        print("Erro ao bauixar arquivo:\n", requisicao.json())


enviar_arquivo()
