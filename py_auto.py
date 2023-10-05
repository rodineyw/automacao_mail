from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

# Passo 1 = Iniciando o navegador
print("Iniciando o navegador")
navegador.get("https://outlook.com/login")
sleep(10)

# Passo 2 = Preenchendo o e-mail e Senha
print("Digitando e-mail")
navegador.find_element(
    "xpath",
    "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]",
).send_keys("rodineywan@outlook.com")
sleep(0.5)
navegador.find_element(
    "xpath",
    "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input",
).click()
sleep(5)

print("Digitando senha")
navegador.find_element(
    "xpath",
    "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input",
).send_keys("Roy371928@$")
sleep(0.5)
navegador.find_element(
    "xpath",
    "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input",
).click()
sleep(1)

# Passo 3 = Confirmação para continuar conectado
print("Confirmando para continuar conectado")
navegador.find_element(
    "xpath",
    "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[1]/div/label/input",
).click()
sleep(0.5)

navegador.find_element(
    "xpath",
    "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input",
).click()
