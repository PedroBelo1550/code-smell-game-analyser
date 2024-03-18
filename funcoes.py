import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from git import Repo
import pandas as pd

class Funcoes:

    @staticmethod
    def clona_repositorio(url):

        destino = Funcoes.get_data_path('repositorio')

        if os.path.exists(url):
           print('Copiando pasta')
           shutil.copytree(url,destino)
        else:
            os.makedirs(destino)
            print('Clonando o repositório')
            Repo.clone_from(url, destino)
            print('Finalizou a clonagem')

    @staticmethod
    def remove_arq(path):
        path = Funcoes.get_data_path(path)
        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def remove_folder(path):
        path = Funcoes.get_data_path(path)
        if os.path.exists(path):
            shutil.rmtree(path)
        

    @staticmethod
    def cria_pasta_temporaria():
        return tempfile.mkdtemp()
    
    @staticmethod
    def executar_analisador_csharp():
        try:
 
            project_dir_path = Funcoes.get_data_path('repositorio')

            print(f'Iniciou a análise do CSharpAnalyzer {project_dir_path}')
            # Comando para executar o analisador C# de acordo com o sistema operacional
            if sys.platform.startswith('win'):
                comando = [Funcoes.get_data_path("UnityCodeSmellAnalyzer/CSharpAnalyzer/CSharpAnalyzer.exe"), "-p", project_dir_path]
            else:
                comando = ["mono", Funcoes.get_data_path("UnityCodeSmellAnalyzer/CSharpAnalyzer/CSharpAnalyzer.exe"), "-p", project_dir_path]

            # Executa o comando
            subprocess.run(comando, check=True)
            print("Analisador csharp executado com sucesso para o diretório do projeto:", project_dir_path)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o analisador C#:", e)

    @staticmethod
    def executar_analisador_code_smell(json_path):
        try:

            print('Iniciou a análise de code smells')
            # Comando para executar o analisador C# de acordo com o sistema operacional
            if sys.platform.startswith('win'):
                comando = [Funcoes.get_data_path("UnityCodeSmellAnalyzer/CodeSmellAnalyzer/CodeSmellAnalyzer.exe"), "-d", json_path]
            else:
                comando = ["mono", Funcoes.get_data_path("UnityCodeSmellAnalyzer/CodeSmellAnalyzer/CodeSmellAnalyzer.exe"), "-d", json_path]

            # Executa o comando
            subprocess.run(comando, check=True)
            print("Analisador smell executado com sucesso para o diretório do projeto:", json_path)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar o analisador C#:", e)

    @staticmethod
    def json_para_csv(json_path, name_repo):

        name_repo = 'Resultados code smells - ' + name_repo + '.zip'

        pasta_temporaria = Funcoes.get_data_path('temporaria')
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
                    zipf.write(name, f'{nome}.csv')

        shutil.move(name_repo, caminho_downloads)

        return True
    
    @staticmethod
    def get_data_path(relative_path):
        """Retorna o caminho para um arquivo ou diretório incluído no pacote."""
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_repo_name(repo_url: str):
        c = '/'
        if sys.platform.startswith('win'):
            c = '\\'

        name_repo = repo_url.split(c)
        name_repo = name_repo[len(name_repo)-1].replace('.git', '').replace(c, '')
        return name_repo



