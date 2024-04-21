import os
import subprocess
import sys
import requests
import json

from funcoes import Funcoes


class Sonar:
    URL = 'http://localhost'
    TOKEN = 'squ_19ec4b96c27ef99cc60c72f990c40b4bd53fb194'
    PROJECT = 'game-smells'
    DIR = 'C:\\Users\\vm1\\Documents\\dev\\code-smell-game-analyser\\jogo'

    @staticmethod
    def executa_scanne(jogo):
        try:

            comando = None

            print(f'Iniciou a análise do Sonar para o jogo {jogo}')
            # Comando para executar o analisador C# de acordo com o sistema operacional
            if sys.platform.startswith('win'):
                os.chdir(r'C:\\Program Files\\sonar-scanner-5.0.1.3006-windows\\bin\\')
                #comando = f'sonar-scanner.bat -D"sonar.projectKey={Sonar.PROJECT}" -D"sonar.sources={Sonar.DIR}." -D"sonar.host.url={Sonar.URL}" -D"sonar.token={Sonar.TOKEN}" -D"sonar.projectBaseDir={Sonar.DIR}"'
                comando = 'sonar-scanner.bat -D"sonar.projectKey=game-smells" -D"sonar.sources=C:\\Users\\vm1\\Documents\\dev\\analise_sonar." -D"sonar.host.url=http://localhost" -D"sonar.token=squ_19ec4b96c27ef99cc60c72f990c40b4bd53fb194" -D"sonar.projectBaseDir=C:\\Users\\vm1\\Documents\\dev\\analise_sonar"'

            # Executa o comando
            subprocess.run(comando, shell=True)
            print("Análise do sonar concluída:")
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o sonar", e)

    @staticmethod
    def obter_métricas(id_jogo):
        os.chdir(r'C:\Users\vm1\Documents\dev\code-smell-game-analyser')

        métricas = ['files', 'duplicated_lines', 'sqale_debt_ratio', 'lines', 'bugs']

        headers = {'Authorization': f'Bearer {Sonar.TOKEN}'}
        endpoint = f'{Sonar.URL}/api/measures/component'
        params = {
            'component': Sonar.PROJECT,
            'metricKeys': ','.join(métricas)
        }
        response = requests.get(endpoint, headers=headers, params=params)
        if response.status_code == 200:
            # Convertendo a resposta JSON em um dicionário Python
            data = response.json()

            # Extraindo as métricas desejadas
            metrics = data['component']['measures']

            # Criando um dicionário com as métricas
            metrics_dict = {metric['metric']: metric['value'] for metric in metrics}

            metrics_dict['id_jogo'] = Funcoes.normalize(id_jogo)

            print("Métricas salvas com sucesso em metrics.json")
        else:
            print(f"Erro ao obter métricas: {response.status_code} - {response.text}")

