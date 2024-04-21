import os
import shutil

from analyser import Analyser
from blob import Blob
from sonar import Sonar

id_jogo = '13º signo - 2º período - 2-2016'
pasta_jogo = './jogo'

#if os.path.exists(pasta_jogo):
#    shutil.rmtree(pasta_jogo)
#    os.makedirs(pasta_jogo)

blob: Blob = Blob()

#blob.download_folder(id_jogo, pasta_jogo)

#Analyser.processar(id_jogo)

#Sonar.executa_scanne(id_jogo)
Sonar.obter_métricas(id_jogo)

print('deletando pastas')
#shutil.rmtree(pasta_jogo)
#os.makedirs(pasta_jogo)