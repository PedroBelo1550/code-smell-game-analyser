import os
import shutil

from analyser import Analyser
from blob import Blob

id_jogo = 'a perdição de marajó - 2º período - 2-2017'
pasta_jogo = './jogo'

#if os.path.exists(pasta_jogo):
#    shutil.rmtree(pasta_jogo)
#    os.makedirs(pasta_jogo)

blob: Blob = Blob()

#blob.download_folder(id_jogo, pasta_jogo)

Analyser.processar(id_jogo)

print('deletando pastas')
#shutil.rmtree(pasta_jogo)
#os.makedirs(pasta_jogo)