import os
import shutil

from analyser import Analyser
from sonar import Sonar

id_jogo = '13º signo - 2º período - 2-2016'
pasta_projeto = 'C:\\Users\\vm1\\Documents\\dev\\analise_sonar'
origem = 'E:\\jogos'

if os.path.exists(pasta_projeto):
    shutil.rmtree(pasta_projeto)
    os.makedirs(pasta_projeto)
else:
    os.makedirs(pasta_projeto)

print('copiando os dados')
origem = os.path.join(origem, id_jogo)
destino = os.path.join(pasta_projeto, id_jogo)
#Copia os dados
shutil.copytree(origem, destino)

#Analyser.processar(id_jogo, destino)
Sonar.executa_scanne(id_jogo)
Sonar.obter_métricas(id_jogo)

print('deletando pastas')
shutil.rmtree(destino)
shutil.rmtree(pasta_projeto)
shutil.rmtree('./jogo')
os.makedirs(destino)