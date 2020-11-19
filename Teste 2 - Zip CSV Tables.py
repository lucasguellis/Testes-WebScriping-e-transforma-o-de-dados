"""
    Extrair do pdf os dados dos quadros 30, 31, 32
    salvar dados dessas tableas em csvs
    zipar todos os csvs num arquivo
    Teste_Intuitive_Care_Lucas.zip
"""

import tabula
import pandas as pd
import os, zipfile

dir = os.path.dirname(os.path.realpath(__file__))
print(dir)

PDFname = r"Padrao_TISS_Componente_Organizacional Outubro.pdf"

#tabela 30
tab30 = tabula.read_pdf(r"{}\{}".format(dir, PDFname), pages=79, area=(4, 5, 26, 90), relative_area=True)
tab30[0].to_csv(r"{}\Tabela_30.csv".format(dir))

#tabela 31
tab311 = tabula.read_pdf(r"{}\{}".format(dir, PDFname), pages=79, area=(60, 5, 100, 90), relative_area=True)
tab312 = tabula.read_pdf(r"{}\{}".format(dir, PDFname), multiple_tables=True, pages=(80,81,82,83,84))

tab311[0].to_csv(r"{}\Tabela_311.csv".format(dir))
for c in range (5):
    tab312[c].to_csv(r"{}\Tabela_31{}.csv".format(dir, c+2))

tab311 = pd.read_csv("Tabela_311.csv")
tab312 = pd.read_csv("Tabela_312.csv")
tab313 = pd.read_csv("Tabela_313.csv")
tab314 = pd.read_csv("Tabela_314.csv")
tab315 = pd.read_csv("Tabela_315.csv")
tab316 = pd.read_csv("Tabela_316.csv")
tab31 = pd.concat([tab311, tab312, tab313, tab314, tab315, tab316], axis=1).to_csv(r"{}\Tabela_31.csv".format(dir))

for c in range (6):
    os.remove("{}\Tabela_31{}.csv".format(dir, c+1))

#tabela 32
tab32 = tabula.read_pdf(r"{}\{}".format(dir, PDFname), pages=84)
tab32[0].to_csv(r"{}\Tabela_32.csv".format(dir))


os.chdir("{}".format(dir))
novoArquivoZIP = zipfile.ZipFile ("Teste_Intuitive_Care_Lucas.zip", "w")
novoArquivoZIP.write ("Tabela_30.csv", compress_type=zipfile.ZIP_DEFLATED)
novoArquivoZIP.write ("Tabela_31.csv", compress_type=zipfile.ZIP_DEFLATED)
novoArquivoZIP.write ("Tabela_32.csv", compress_type=zipfile.ZIP_DEFLATED)
novoArquivoZIP.close()

for c in range (3):
    os.remove("{}\Tabela_3{}.csv".format(dir, c))
