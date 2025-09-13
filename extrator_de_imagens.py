import fitz  # PyMuPDF
import io
import os
import re
from PIL import Image

# Mude para True para gerar um PDF com as caixas desenhadas
MODO_DEBUG = False 

def extrair_e_renomear_imagens_pdf(caminho_pdf: str, pasta_saida: str, pagina_inicial: int = 1):
    """
    Navega por um arquivo PDF, extrai imagens e as renomeia com base em um
    texto de referência próximo que corresponda a um padrão específico.
    """
    if not os.path.exists(caminho_pdf):
        print(f"Erro: Arquivo PDF não encontrado em '{caminho_pdf}'")
        return

    try:
        os.makedirs(pasta_saida, exist_ok=True)
        print(f"Salvando imagens na pasta: '{pasta_saida}'")
    except OSError as e:
        print(f"Erro ao criar a pasta de saída: {e}")
        return

    padrao_referencia = re.compile(r"\b\d{3}SS\d{5}\b")
    doc = fitz.open(caminho_pdf)
    imagens_processadas = 0
    indice_inicial = pagina_inicial - 1

    for num_pagina, pagina in enumerate(doc):
        if num_pagina < indice_inicial:
            continue

        print(f"\n--- Processando Página {num_pagina + 1} ---")

        # MODO_DEBUG: Desenha retângulos para análise visual
        if MODO_DEBUG:
            # Desenha caixas azuis em todos os blocos de texto
            blocos_texto = pagina.get_text("blocks")
            for x0, y0, x1, y1, texto, _, _ in blocos_texto:
                pagina.draw_rect(fitz.Rect(x0, y0, x1, y1), color=(0, 0, 1), width=1) # Azul

            # Desenha caixas vermelhas em todas as imagens
            for img_info in pagina.get_images(full=True):
                try:
                    caixas_imagem = pagina.get_image_bbox(img_info)
                    pagina.draw_rect(caixas_imagem, color=(1, 0, 0), width=1) # Vermelho
                except ValueError:
                    print("  [!] Aviso: Não foi possível obter a caixa de uma imagem.")
            
            continue # Pula para a próxima página após desenhar

        # LÓGICA DE EXTRAÇÃO NORMAL (só roda se MODO_DEBUG for False)
        lista_imagens = pagina.get_images(full=True)
        if not lista_imagens:
            print("Nenhuma imagem encontrada nesta página.")
            continue
        
        blocos_texto = pagina.get_text("blocks")

        for img_index, img_info in enumerate(lista_imagens):
            try:
                caixas_imagem = pagina.get_image_bbox(img_info)
            except ValueError:
                print(f"  [!] Aviso: Pulando imagem {img_index+1} (não foi possível obter a caixa).")
                continue
            
            nome_arquivo_encontrado = None

            for x0, y0, x1, y1, texto, _, _ in blocos_texto:
                # --- LÓGICA DE PROXIMIDADE MELHORADA ---
                distancia_vertical_ok = (y0 > caixas_imagem.y1) and (y0 - caixas_imagem.y1 < 100)
                sobreposicao_horizontal_ok = (caixas_imagem.x0 < x1 and caixas_imagem.x1 > x0)

                if distancia_vertical_ok and sobreposicao_horizontal_ok:
                    match = padrao_referencia.search(texto)
                    if match:
                        extensao_base = doc.extract_image(img_info[0])["ext"]
                        nome_arquivo_encontrado = f"{match.group(0)}.{extensao_base}"
                        print(f"  [+] Sucesso! Imagem {img_index+1} associada à referência: '{nome_arquivo_encontrado}'")
                        break
            
            if nome_arquivo_encontrado:
                xref = img_info[0]
                imagem_base = doc.extract_image(xref)
                dados_imagem = imagem_base["image"]
                caminho_final = os.path.join(pasta_saida, nome_arquivo_encontrado)
            else:
                xref = img_info[0]
                imagem_base = doc.extract_image(xref)
                dados_imagem = imagem_base["image"]
                extensao = imagem_base["ext"]
                nome_padrao = f"pagina_{num_pagina+1:03}_img_{img_index+1:02}.{extensao}"
                caminho_final = os.path.join(pasta_saida, nome_padrao)
                print(f"  [!] Aviso: Nenhuma referência encontrada para imagem {img_index+1}. Salvando como '{nome_padrao}'")

            try:
                img = Image.open(io.BytesIO(dados_imagem))
                img.save(caminho_final)
                imagens_processadas += 1
            except Exception as e:
                print(f"  [X] Erro ao salvar a imagem '{caminho_final}': {e}")

    if MODO_DEBUG:
        caminho_debug_pdf = "debug_visual_layout.pdf"
        doc.save(caminho_debug_pdf, garbage=4, deflate=True, clean=True)
        print(f"\n--- MODO DEBUG CONCLUÍDO ---")
        print(f"PDF de depuração salvo como: '{caminho_debug_pdf}'")
        print("Abra este arquivo para ver as caixas de imagens (vermelho) e texto (azul).")
    else:
        print(f"\n--- Concluído! ---")
        print(f"Total de imagens salvas: {imagens_processadas}")
        
    doc.close()

# --- COMO USAR ---
if __name__ == "__main__":
    # caminho_do_meu_pdf = "./Catálogo SS26_compressed.pdf" 
    caminho_do_meu_pdf = "./debug_visual_layout.pdf" 
    pasta_de_imagens = "imagens_extraidas"
    extrair_e_renomear_imagens_pdf(caminho_do_meu_pdf, pasta_de_imagens, pagina_inicial=32)