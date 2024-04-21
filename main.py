import pandas as pd
import os
import shutil
from sonar import Sonar

nome_arq = 'Catalogação.csv'
df = pd.read_csv(nome_arq, delimiter=';')

for index, row in df.iterrows():
    print(row['pasta'])
    try:

        id_jogo = row['pasta']
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
        # Copia os dados
        shutil.copytree(origem, destino)

        # Analyser.processar(id_jogo, destino)
        Sonar.executa_scanne(id_jogo)
        Sonar.obter_métricas(id_jogo)

        print('deletando pastas')
        shutil.rmtree(destino)
        shutil.rmtree(pasta_projeto)
        shutil.rmtree('./jogo')
        os.makedirs(destino)

        df.at[index, 'processado'] = True
        df.to_csv(nome_arq, index=False)

    except Exception as e:
        shutil.rmtree(destino)
        shutil.rmtree(pasta_projeto)
        shutil.rmtree('./jogo')
        os.makedirs(destino)
        # Se ocorrer um erro, imprimir mensagem de erro e pular para a próxima iteração
        print(f"Erro ao processar a linha {index}: {e}")
        continue





