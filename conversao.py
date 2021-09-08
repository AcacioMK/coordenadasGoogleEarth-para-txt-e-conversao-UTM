#  ===================================
#  Parte do projeto "GPC Topo", software para gerenciar clientes, projetos e conversão de arquivos e coordenadas.
#  Este código é apenas um demonstrativo e uma parte pequena do módulo de conversão e extração de dados.

from pyproj import Proj, transform
import xml.etree.ElementTree as ET
import requests

arquivo = "xml/2.kml"
tree = ET.parse(arquivo)

root = tree.getroot()

filtro = "*"

def converterDados(dados):
    arquivoTxt = 'txt/1.txt'
    arquivo = open(arquivoTxt, 'w')
    indice = 0
    for i in dados:
        d = dados[indice].split(',')
        x1 = d[0]
        y1 = d[1]

        inProj = Proj(init='epsg:4326')
        outProj = Proj(init='epsg:31983')

        rs = transform(inProj, outProj, x1, y1)
        arquivo.write(f'{rs} \n')
        indice += 1

    arquivo.close()


for child in root.iter(filtro):

    rs = str(child.tag)
    pontos = []
    if rs.endswith('coordinates'):
        pontos = str(child.text)
        pontos = pontos.strip()
        pontos = pontos.strip(',0')
        pontos = pontos.split(",0 ")

converterDados(pontos)

#  Verificando Tipo de Objeto (Linha ou Área)
for child in root.iter(filtro):
    rs = str(child.tag)
    if rs.endswith('outerBoundaryIs'):  # verificando se é perímetro
        pass
    elif rs.endswith('LineString'):  # verificando se é linha
        pass
