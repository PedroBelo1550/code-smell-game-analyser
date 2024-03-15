

import csv
import json
import subprocess
import sys
import tempfile
import git
import pandas as pd

class Funcoes:

    @staticmethod
    def clona_repositorio(url, destino):
        git.Repo.clone_from(url, destino)

    @staticmethod
    def cria_pasta_temporaria():
        return tempfile.mkdtemp()
    
    def executar_analisador_csharp(project_dir_path):
        try:
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
        arquivo_temporario = tempfile.NamedTemporaryFile(delete=False, suffix='.csv').name
        # Abre o arquivo CSV para escrita
        with open(arquivo_temporario, 'w', newline='') as csvfile:
            # Define os campos do CSV
            fieldnames = ['name', 'script', 'metodo', 'line']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Escreve o cabeçalho
            writer.writeheader()

            # Itera sobre os dados do JSON
            for smell in pd.read_json(json_path)['SmellList']: 
                    
                name = smell['Name']

                for s in smell['Smells']:
                    script = s['Script']
                    line = s['Line']

                    # Escreve os dados no arquivo CSV
                    writer.writerow({'name': name, 'script': script, 'line': line})

        return arquivo_temporario


