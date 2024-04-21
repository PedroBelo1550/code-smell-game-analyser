import pandas as pd
import os
import shutil

from analyser import Analyser
from funcoes import Funcoes
from sonar import Sonar

nome_arq = 'Catalogação.csv'
df = pd.read_csv(nome_arq)

for index, row in df.iterrows():
    print(row['pasta'])

    try:
        if not row['processado']:
            id_jogo = str(row['pasta'])
            pasta_projeto = 'C:\\Users\\vm1\\Documents\\dev\\analise_sonar'
            origem = 'E:\\jogos'

            Funcoes.remove_folder(pasta_projeto)
            Funcoes.remove_folder('./jogo')
            os.makedirs('./jogo')
            os.makedirs(pasta_projeto)

            print('copiando os dados')
            origem = os.path.join(origem, id_jogo)
            destino = os.path.join(pasta_projeto, id_jogo)
            # Copia os dados
            shutil.copytree(origem, destino)

            Analyser.processar(id_jogo, destino)
            Sonar.executa_scanne(id_jogo)
            Sonar.obter_métricas(id_jogo)

    except Exception as e:
        # Se ocorrer um erro, imprimir mensagem de erro e pular para a próxima iteração
        print(f"Erro ao processar a linha {index}: {e}")
        continue

    df.at[index, 'processado'] = True
    df.to_csv(nome_arq, index=False)
