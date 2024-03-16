

import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
import git
import pandas as pd

class Funcoes:

    @staticmethod
    def clona_repositorio(url):
        print('Clonando o repositório')
        git.Repo.clone_from(url, 'repositorio/')
        print('Finalizou a clonagem')

    @staticmethod
    def cria_pasta_temporaria():
        return tempfile.mkdtemp()
    
    def executar_analisador_csharp():
        try:
 
            project_dir_path = 'repositorio/'
            print('Iniciou a análise do CSharpAnalyzer')
            # Comando para executar o analisador C# de acordo com o sistema operacional
            if sys.platform.startswith('win'):
                comando = ["UnityCodeSmellAnalyzer/CSharpAnalyzer/CSharpAnalyzer.exe", "-p", project_dir_path]
            else:
                comando = ["mono", "UnityCodeSmellAnalyzer/CSharpAnalyzer/CSharpAnalyzer.exe", "-p", project_dir_path]

            # Executa o comando
            subprocess.run(comando, check=True)
            print("Analisador csharp executado com sucesso para o diretório do projeto:", project_dir_path)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o analisador C#:", e)

    def executar_analisador_code_smell(json_path):
        try:

            print('Iniciou a análise de code smells')
            # Comando para executar o analisador C# de acordo com o sistema operacional
            if sys.platform.startswith('win'):
                comando = ["UnityCodeSmellAnalyzer/CodeSmellAnalyzer/CodeSmellAnalyzer.exe", "-d", json_path]
            else:
                comando = ["mono", "UnityCodeSmellAnalyzer/CodeSmellAnalyzer/CodeSmellAnalyzer.exe", "-d", json_path]

            # Executa o comando
            subprocess.run(comando, check=True)
            print("Analisador smell executado com sucesso para o diretório do projeto:", json_path)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o analisador C#:", e)

    def json_para_csv(json_path):

        temp = tempfile.NamedTemporaryFile(suffix='.zip').name

        caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        with zipfile.ZipFile(temp, 'w') as zipf:
            
            for smell in pd.read_json(json_path)['SmellList']: 

                if smell['Occurrency'] != 0:
                    nome = smell['Name']
                    df = pd.DataFrame(smell['Smells'])
                    name = f'{nome}.csv'
                    df.to_csv(name)
                    zipf.write(name)

        shutil.move(temp, caminho_downloads)

        return True


