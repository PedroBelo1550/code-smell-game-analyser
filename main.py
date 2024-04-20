import os
import shutil

from blob import Blob

pasta_jogo = './jogo'

os.makedirs(pasta_jogo)
blob: Blob = Blob()

blob.download_folder('13º signo - 2º período - 2-2016', pasta_jogo)

print('deletenado pastas')
shutil.rmtree(pasta_jogo)
os.makedirs(pasta_jogo)