from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
    print("Elemento CRIAR CONTA clicado com sucesso.")
except Exception as e:
    print("Erro ao encontrar ou clicar no elemento: ", e)

# Espera até que o elemento input NOME esteja presente na página e preenche ele com o texto BOT
try:
    elemento_nome = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]'))
    )
    elemento_nome.send_keys("BOT")
    print("Elemento input NOME nomeado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento de nome: ", e)

# Espera até que o elemento botão AVANÇAR esteja presente na página e clica nele
try:
    elemento_avançar = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="collectNameNext"]/div/button'))
    )
    elemento_avançar.click()
    print("Elemento botão AVANÇAR clicado com sucesso.")
except Exception as e:
    print("Erro ao encontrar ou clicar no elemento: ", e)

# Espera até que o elemento input DIA esteja presente na página e preenche ele com os números 01
try:
    elemento_dia = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="day"]'))
    )
    elemento_dia.send_keys("01")
    print("Elemento input DIA enumerado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento input DIA: ", e)

# Espera 1 segundo para que não bug a entrada nos inputs
sleep(1)

# Espera até que o elemento select MÊS esteja presente na página e preenche ele com a opção janeiro
try:
    elemento_mês = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="month"]'))
    )
    # Crie um objeto Select com o elemento
    elemento_mês = Select(elemento_mês)
    # Selecione a primeira opção (índice 1)
    elemento_mês.select_by_index(1)
    print("Elemento select MÊS selecionado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento select MÊS: ", e)

# Espera 1 segundo para que não bug a entrada nos inputs
sleep(1)

# Espera até que o elemento input ANO esteja presente na página e preenche ele com os números 2000
try:
    elemento_ano = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="year"]'))
    )
    elemento_ano.send_keys("2000")
    print("Elemento input ANO enumerado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento input ANO: ", e)

# Espera 1 segundo para que não bug a entrada nos inputs
sleep(1)

# Espera até que o elemento select GÊNERO esteja presente na página e preenche ele com a opção MULHER
try:
    elemento_gênero = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gender"]'))
    )
    # Crie um objeto Select com o elemento
    elemento_gênero = Select(elemento_gênero)
    # Selecione a primeira opção (índice 1)
    elemento_gênero.select_by_index(1)
    print("Elemento select GÊNERO selecionado com sucesso.")
except Exception as e:
    print("Erro ao encontrar o elemento select GÊNERO: ", e)

# Feche o navegador após a execução do script
sleep(5)
driver.quit()


