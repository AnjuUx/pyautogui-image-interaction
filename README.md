# 🧠 Automação de Relatórios Google Ads

Automação completa para extração, renomeação e upload de relatórios do Google Ads (Campanha, Termos de Pesquisa e Locais Correspondentes) utilizando reconhecimento de imagem com PyAutoGUI e OpenCV.

## 📂 Estrutura do Projeto
img/
├── chrom.png
├── perfil.png
├── over.png
├── camp.png
├── ...
google_ads.py
google_matched.py
google_sear.py

## 📜 Scripts

### ✅ `google_ads.py`
- Abre o Google Chrome e acessa o perfil.
- Navega até os relatórios de campanhas no Google Ads.
- Faz o download do relatório CSV.
- Renomeia o arquivo com o padrão `base_google_ads_YYYYMM.csv`.
- Faz upload do relatório renomeado para o sistema da empresa.

### 🌍 `google_matched.py`
- Acessa a aba de "Locais correspondentes".
- Faz download do relatório `Matched locations`.
- Renomeia com o padrão `base_google_Matched_YYYYMM.csv`.
- Realiza upload do relatório no sistema.

### 🔍 `google_sear.py`
- Navega até os "Termos de pesquisa".
- Baixa o relatório `Search terms`.
- Renomeia com `base_google_Search_YYYYMM.csv`.
- Envia o arquivo para a plataforma destino.

## 🛠 Tecnologias e Bibliotecas

- `pyautogui` – automação de cliques e digitação.
- `opencv-python` – comparação de imagens na tela.
- `pygetwindow` – manipulação de janelas do Windows.
- `glob`, `os`, `datetime` – manipulação de arquivos e nomes.
- Arquivos `.png` da pasta `img/` são usados como referência visual.

## 🚀 Como Usar

1. Certifique-se de que o Chrome está instalado.
2. Coloque as imagens de referência em `img/`.
3. Execute um dos scripts:
   ```bash
   python google_ads.py
   python google_matched.py
   python google_sear.py


⚠️ Requisitos
Resolução mínima recomendada: 1280x720.

Tela principal deve exibir o Chrome.

Interface do Google Ads deve estar em português com as imagens correspondentes ao layout da pasta img.

🔒 Observações de Segurança
O script simula interações humanas com o sistema.

Certifique-se de não mover janelas ou interagir com o computador durante a execução.

Evite mudanças no layout do Google Ads que possam invalidar as imagens usadas.

📦 Exemplo de Saída
Após a execução de um script, o terminal exibirá:

less
Copiar
Editar
✅ Imagem encontrada: img/dow.png em (980, 540)
🖱️ Clique executado.
📤 Arquivo carregado: base_google_ads_202507.csv
❌ Chrome foi fechado com sucesso.
📁 Nomeação Automática dos Arquivos
Os arquivos baixados são renomeados automaticamente no formato:

base_google_ads_202507.csv

base_google_Matched_202507.csv

base_google_Search_202507.csv

👨‍💻 Autor
Automação criada por Juan Mathias, com foco em eficiência e confiabilidade em ambientes reais.




