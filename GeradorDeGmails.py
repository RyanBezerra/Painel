from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


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

# Espera até que o elemento CRIAR CONTA esteja presente na página e clica nele
try:
    elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/header/div[1]/div[5]/ul/li[1]/a'))
    )
    elemento.click()
    print("Elemento clicado com sucesso.")
except Exception as e:
    print("Erro ao encontrar ou clicar no elemento: ", e)

# Espera até que o elemento input NOME esteja presente na página e preenche ele com o texto BOT
try:
    elemento_nome = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]'))
    )
    elemento_nome.send_keys("BOT")
    print("Elemento nome nomeado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento de nome: ", e)

# Espera até que o elemento botão AVANÇAR esteja presente na página e clica nele
try:
    elemento_avançar = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="collectNameNext"]/div/button'))
    )
    elemento_avançar.click()
    print("Elemento clicado com sucesso.")
except Exception as e:
    print("Erro ao encontrar ou clicar no elemento: ", e)

# Espera até que o elemento input DIA esteja presente na página e preenche ele com os números 01
try:
    elemento_dia = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="day"]'))
    )
    elemento_dia.send_keys("01")
    print("Elemento nome nomeado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento de nome: ", e)

# Espera até que o elemento select MÊS esteja presente na página e clica nele
try:
    elemento_mês = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="month"]'))
    )
    elemento_mês.click()
        # Espera até que o elemento as opções dos MÊSES estejam presente na página e clica na opção janeiro
    try:
        elemento_mês_janeiro = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="month"]/option[2]'))
        )
        elemento_mês_janeiro.click()
        
        print("Elemento nome nomeado com sucesso.")
    except Exception as e:
        print("Erro ao encontrar o elemento de nome: ", e)
    print("Elemento nome nomeado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento de nome: ", e)

# Feche o navegador após a execução do script
sleep(5)
driver.quit()


