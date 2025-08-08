from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do navegador
options = Options()
options.add_argument("--headless")  # Sem interface gráfica
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Acessa o Power BI
driver.get("https://app.powerbi.com/view?r=XXXX")  # link real do painel

# Aguarda carregar o painel
time.sleep(10)

# Tira print
screenshot_path = "/caminho/para/powerbi_print.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot salva em: {screenshot_path}")

driver.quit()
