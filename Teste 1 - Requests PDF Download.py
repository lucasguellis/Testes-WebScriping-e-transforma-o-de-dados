from urllib.parse import urlparse

import requests

site = "http://ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
drive = requests.get(site)
parsed_url = urlparse(site)
base_url = parsed_url[0] +"://"+ parsed_url[1]
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

for mes in meses:
    loc = drive.text.find("Padrão TISS – Versão {}/20".format(mes))
    if loc != -1:
        complemento = str(drive.text[loc:].split('href=')[1].split(" ")[0]) #Pega o link do próximo site
        site = base_url + complemento[1:-1] #Monta a URL dos PDFs mais recentes
        drive = requests.get(site)

        loc = drive.text.find("table-responsive") #Encontra a tabela dos PDF's
        loc2 = drive.text[loc:].find("Componente Organizacional") #Encontra o comp org
        complemento = str(drive.text[loc:][loc2:].split("href=")[1].split(" ")[0]) #Pega o link do PDF
        site = base_url + complemento[1:-1] #Monta a url do PDF desejado
        drive = requests.get(site)

        with open('Padrao_TISS_Componente_Organizacional {}.pdf'.format(mes), 'wb') as f: #Baixa o Pdf
            f.write(drive.content)
