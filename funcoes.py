

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

    def json_para_csv(json_path, name_repo):

        name_repo = 'Resultados code smells: ' + name_repo + '.zip'

        pasta_temporaria = 'temporaria'
        if os.path.exists(pasta_temporaria):
            # Deletar o repositório existente
            shutil.rmtree(pasta_temporaria)

        os.makedirs(pasta_temporaria)

        caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        with zipfile.ZipFile(name_repo, 'w') as zipf:
            
            for smell in pd.read_json(json_path)['SmellList']: 

                if smell['Occurrency'] != 0:
                    nome = smell['Name']
                    df = pd.DataFrame(smell['Smells'])
                    name = f'{pasta_temporaria}/{nome}.csv'
                    df.to_csv(name)
                    zipf.write(name)

        shutil.move(name_repo, caminho_downloads)

        return True
    
    def get_repo_name(repo_url):
        name_repo = repo_url.split('/')
        name_repo = name_repo[len(name_repo)-1].replace('.git', '')



