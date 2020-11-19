"""Acessar o site, buscar a versão mais recente do padrao tiss e baixar
"""

from selenium import webdriver
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
DOWNLOAD_DIR = "C:\\Users\\Lucas\\Downloads"

#Configura o Chrome para baixar PDF's ao invés de abrir
options = webdriver.ChromeOptions()
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
               "download.default_directory": DOWNLOAD_DIR , "download.extensions_to_open": "applications/pdf",
           "plugins.always_open_pdf_externally": True}
options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(PATH, options=options)

#Caminho até o PDF
driver.get("http://ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar")

driver.find_element_by_class_name("alert-link").click()
driver.find_element_by_xpath("/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a").click()


sleep(3)
driver.close()
