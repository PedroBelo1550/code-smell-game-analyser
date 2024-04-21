import subprocess
import sys
import requests
import json


class Sonar:
    URL = 'http://localhost:9000'
    TOKEN = 'sqp_9478adbcce8083bd469fabe344918cc00d2f2e05'
    PROJECT = 'game-smells'

    @staticmethod
    def executa_scanne(jogo):
        try:

            comando = None

            print(f'Iniciou a análise do Sonar para o jogo {jogo}')
            # Comando para executar o analisador C# de acordo com o sistema operacional
            if sys.platform.startswith('win'):
                comando = ["C:\\Program Files\\sonar-scanner-5.0.1.3006-windows\\bin\\sonar-scanner.bat",
                           "-D", f"sonar.projectKey={Sonar.PROJECT}", "-D",
                           'sonar.sources=C:\\Users\\vm1\\Documents\\dev\\code-smell-game-analyser\\jogo.',
                           "-D", f"sonar.host.url={Sonar.URL}", "-D",
                           f"sonar.token={Sonar.TOKEN}", "-D",
                           "sonar.projectBaseDir=C:\\Users\\vm1\\Documents\\dev\\code-smell-game-analyser\\jogo"]

            # Executa o comando
            subprocess.run(comando, check=True)
            print("Análise do sonar concluída:")
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o sonar", e)

    @staticmethod
    def obter_métricas():

        métricas = ['cognitive_complexity', 'duplicated_lines', 'sqale_debt_ratio', 'ncloc', 'bugs']

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

            # Salvando as métricas em um arquivo JSON
            with open('metrics.json', 'w') as f:
                json.dump(metrics_dict, f, indent=4)

            print("Métricas salvas com sucesso em metrics.json")
        else:
            print(f"Erro ao obter métricas: {response.status_code} - {response.text}")

