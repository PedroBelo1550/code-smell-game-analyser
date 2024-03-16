import os
import shutil
from funcoes import Funcoes

class Analyser:


    def processar(url):
        repositorio_git = url
        json_output = 'CodeAnalysis.json'
        json_smell = 'codeSmells.json'
        repositorio_path = 'repositorio'
        log= 'CSharpAnalyzer.log'

        Funcoes.remove_folder(repositorio_path)
        Funcoes.remove_arq(json_output)
        Funcoes.remove_arq(json_smell)
        Funcoes.remove_arq(log)
        
        name_repo = Funcoes.get_repo_name(repositorio_git)

        #Clona o repositório: 
        Funcoes.clona_repositorio(repositorio_git)

        #Roda o CSharpAnalyzer, necesária para obter os bad smells. 
        Funcoes.executar_analisador_csharp()
        Funcoes.executar_analisador_code_smell(json_output)
        Funcoes.json_para_csv(json_smell, name_repo)
        print('Finalizou')






