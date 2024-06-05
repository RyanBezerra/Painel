from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configurações do EdgeDriver
options = webdriver.EdgeOptions()
options.add_argument('--disable-logging')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument('--disable-blink-features=AutomationControlled')

# Inicializa o WebDriver
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

driver.maximize_window()

driver.get('https://www.google.com/intl/pt-BR/account/about/')

# Espera até que o elemento esteja presente na página e clica nele
try:
    elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[1]/a'))
    )
    elemento.click()
    print("Elemento clicado com sucesso.")
except Exception as e:
    print("Erro ao encontrar ou clicar no elemento: ", e)

# Feche o navegador após a execução do script
driver.quit()


