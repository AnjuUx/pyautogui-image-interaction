import time
import cv2
import pyautogui as py
import numpy as np
import pygetwindow as gw
import os
import glob
from datetime import datetime


largura, altura = py.size()
print(f"🖥️ Resolução detectada: {largura}x{altura}")

# Defina a resolução mínima esperada
if largura < 1280 or altura < 720:
    print("⚠️ Resolução muito baixa. O script pode não funcionar corretamente.")
py.PAUSE = 1




# def clicar_em_imagem(imagem, precisao=0.8, intervalo=3, timeout=None):

#     print(f"🔍 Procurando '{imagem}' para clicar...")
#     inicio = time.time()

#     while True:
#         time.sleep(intervalo)

#         # Carrega a imagem de referência
#         template = cv2.imread(imagem)
#         if template is None:
#             print(f"❌ Erro ao carregar a imagem: {imagem}")
#             return False

#         # Captura a tela e converte para BGR
#         screenshot = py.screenshot()
#         tela = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

#         # Aplica template matching (comparação de imagem)
#         resultado = cv2.matchTemplate(tela, template, cv2.TM_CCOEFF_NORMED)
#         _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

#         # Verifica se a correspondência é suficiente
#         if max_val >= precisao:
#             altura, largura = template.shape[:2]
#             centro_x = max_loc[0] + largura // 2
#             centro_y = max_loc[1] + altura // 2

#             print(f"✅ Imagem encontrada!{imagem} Clicando em ({centro_x}, {centro_y})")
#             py.moveTo(centro_x, centro_y, duration=0.5)
#             py.click()
#             return True
#         else:
#             print("⏳ Imagem ainda não encontrada... tentando novamente.")

#         # Verifica se há tempo limite e se foi atingido
#         if timeout and (time.time() - inicio > timeout):
#             print(f"⏱️ Timeout atingido para '{imagem}'. Encerrando busca.")
#             return False


def clicar_em_imagem(imagem, precisao=0.8, intervalo=3, timeout=None, acao="clicar"):
    print(f"🔍 Procurando '{imagem}' na tela...")
    inicio = time.time()

    while True:
        time.sleep(intervalo)

        template = cv2.imread(imagem)
        if template is None:
            print(f"❌ Erro ao carregar a imagem: {imagem}")
            return False

        screenshot = py.screenshot()
        tela = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        resultado = cv2.matchTemplate(tela, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= precisao:
            altura, largura = template.shape[:2]
            centro_x = max_loc[0] + largura // 2
            centro_y = max_loc[1] + altura // 2

            print(f"✅ Imagem encontrada: {imagem} em ({centro_x}, {centro_y})")

            if acao == "clicar":
                py.moveTo(centro_x, centro_y, duration=0.5)
                py.click()
                print("🖱️ Clique executado.")
            elif acao == "enter":
                py.press("enter")
                print("⏎ ENTER pressionado.")
            elif acao =="detectar":
                 print("🔎 Imagem detectada, sem interação.")
            else:
                print("⚠️ Ação desconhecida. Nenhuma interação realizada.")

            return True
        else:
            print("⏳ Ainda procurando...")

        if timeout and (time.time() - inicio > timeout):
            print(f"⏱️ Timeout atingido para '{imagem}'")
            return False


def fechar_chrome(mover_para_monitor_principal=True):

    nome_janela = "Google Chrome"
    
    # Busca janelas com o nome (mesmo que estejam minimizadas)
    janelas = gw.getWindowsWithTitle(nome_janela)

    if not janelas:
        print("❌ Nenhuma janela do Chrome foi encontrada.")
        return

    chrome = janelas[0]
    print(f"✅ Janela encontrada: {chrome.title}")

    # Se estiver minimizada, restaura
    if chrome.isMinimized:
        chrome.restore()
        print("🔄 Janela restaurada (estava minimizada).")
        time.sleep(1)

    chrome.activate()
    time.sleep(1)

    if mover_para_monitor_principal:
        chrome.moveTo(0, 0)
        print("↪️ Chrome movido para o monitor principal.")

    time.sleep(0.5)
    py.hotkey("alt", "f4")
    print("❌ Chrome foi fechado com sucesso.")


fechar_chrome()
time.sleep(2)

py.press("win")
py.write("chrome")
clicar_em_imagem("img/chrom.png")
clicar_em_imagem ("img/perfil.png")
clicar_em_imagem ("img/over.png")
clicar_em_imagem ("img/camp.png")
clicar_em_imagem ("img/ins.png")
clicar_em_imagem ("img/sea.png")
clicar_em_imagem ("img/data.png")
clicar_em_imagem ("img/this.png")
clicar_em_imagem ("img/dow.png")
clicar_em_imagem ("img/csv.png")
def renomear_arquivo_ads(pasta_download):
    data_atual = datetime.now().strftime("%Y%m")  # Ex: 202507
    novo_nome = f"base_google_Search_{data_atual}.csv"
    caminho_novo = os.path.join(pasta_download, novo_nome)

    arquivos = glob.glob(os.path.join(pasta_download, "Search terms report*.csv"))
    arquivos.sort(key=os.path.getmtime)

    if not arquivos:
        print("❌ Nenhum arquivo 'Search terms report*.csv' encontrado.")
        return None

    if os.path.exists(caminho_novo):
        os.remove(caminho_novo)
        print(f"🗑️ Arquivo anterior '{novo_nome}' removido.")

    ultimo = arquivos[-1]
    os.rename(ultimo, caminho_novo)
    print(f"✅ Renomeado: {ultimo} → {caminho_novo}")
    return novo_nome

py.hotkey("ctrl","t")
clicar_em_imagem("img/share.png")
clicar_em_imagem("img/pesquisa.png")
clicar_em_imagem("img/carregar.png")
clicar_em_imagem("img/arquivo.png")



# Obtém o nome do arquivo renomeado
pasta_download = os.path.expanduser("~/Downloads")
nome_arquivo = renomear_arquivo_ads(pasta_download)
caminho_completo = os.path.join(nome_arquivo)
# Digita o caminho e confirma
time.sleep(1)
py.write(caminho_completo)
py.press("enter")
print(f"📤 Arquivo carregado: {caminho_completo}")



clicar_em_imagem("img/ok.png", timeout=3,  acao="detectar")
  
clicar_em_imagem("img/substituir.png", timeout=3, acao="enter")

fechar_chrome ()