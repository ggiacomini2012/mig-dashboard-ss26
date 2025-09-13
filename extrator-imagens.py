# -*- coding: utf-8 -*-

# Este script utiliza a biblioteca PyMuPDF (fitz) para extrair
# todas as imagens de um arquivo PDF e salvá-las em uma pasta.

# 1. INSTALAÇÃO:
#    Antes de rodar, você precisa instalar a biblioteca. Abra seu terminal ou prompt de comando e execute:
#    pip install PyMuPDF

# 2. COMO USAR:
#    - Coloque este script na mesma pasta que o seu arquivo PDF.
#    - Altere o valor da variável 'nome_arquivo_pdf' para o nome do seu catálogo.
#    - Crie uma pasta para salvar as imagens ou altere o 'nome_pasta_saida'.
#    - Execute o script (ex: python extrator_de_imagens.py)

import fitz  # PyMuPDF
import os

# --- CONFIGURAÇÕES ---
# Nome do arquivo PDF do qual você quer extrair as imagens.
nome_arquivo_pdf = "Catálogo SS26_compressed.pdf"

# Nome da pasta onde as imagens extraídas serão salvas.
# O script criará esta pasta se ela não existir.
nome_pasta_saida = "imagens_do_catalogo"
# --------------------


def extrair_imagens_pdf(caminho_pdf, pasta_saida):
    """
    Extrai todas as imagens de um arquivo PDF e as salva em uma pasta de destino.
    """
    # Verifica se o arquivo PDF existe
    if not os.path.exists(caminho_pdf):
        print(f"Erro: O arquivo '{caminho_pdf}' não foi encontrado.")
        return

    # Cria a pasta de saída se ela não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
        print(f"Pasta '{pasta_saida}' criada com sucesso.")

    # Abre o arquivo PDF
    doc = fitz.open(caminho_pdf)
    contador_imagens = 0
    print(f"\nIniciando extração de imagens de '{caminho_pdf}'...")

    # Itera por todas as páginas do documento
    for i in range(len(doc)):
        pagina = doc[i]
        lista_imagens = pagina.get_images(full=True)

        if lista_imagens:
            print(f"Encontradas {len(lista_imagens)} imagens na página {i + 1}")

        # Itera por todas as imagens na página atual
        for img_index, img in enumerate(lista_imagens, start=1):
            # Obtém o XREF da imagem (identificador interno)
            xref = img[0]

            # Extrai os dados da imagem (bytes)
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Obtém a extensão da imagem (ex: png, jpeg)
            image_ext = base_image["ext"]

            # Define um nome de arquivo único para a imagem
            nome_imagem = f"pagina_{i+1:03d}_img_{img_index:02d}.{image_ext}"
            caminho_completo_imagem = os.path.join(pasta_saida, nome_imagem)

            # Salva a imagem no disco
            with open(caminho_completo_imagem, "wb") as f_imagem:
                f_imagem.write(image_bytes)
                contador_imagens += 1

    print("-" * 30)
    print(f"Extração concluída!")
    print(f"Total de {contador_imagens} imagens salvas na pasta '{pasta_saida}'.")
    print("-" * 30)


# Executa a função principal
if __name__ == "__main__":
    extrair_imagens_pdf(nome_arquivo_pdf, nome_pasta_saida)

