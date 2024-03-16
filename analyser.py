import os
import shutil
from funcoes import Funcoes

class Analyser:


    def processar(url):
        projeto_path = Funcoes.cria_pasta_temporaria()
        repositorio_git = url
        json_output = 'CodeAnalysis.json'
        json_smell = 'codeSmells.json'
        repositorio_path = 'repositorio'
        log= 'CSharpAnalyzer.log'

        #Limpa a pasta antes de começar.
        if os.path.exists(repositorio_path):
            # Deletar o repositório existente
            shutil.rmtree(repositorio_path)

        #Deleta arquivos temporarios
        if os.path.exists(json_output):
            os.remove(json_output)

        if os.path.exists(json_smell):
            os.remove(json_smell)
        
        if os.path.exists(json_smell):
            os.remove(log)

        os.makedirs(repositorio_path)

        name_repo = Funcoes.get_repo_name(repositorio_git)

        #Clona o repositório: 
        Funcoes.clona_repositorio(repositorio_git)

        #Roda o CSharpAnalyzer, necesária para obter os bad smells. 
        Funcoes.executar_analisador_csharp()
        Funcoes.executar_analisador_code_smell(json_output)
        Funcoes.json_para_csv(json_smell, name_repo)
        print('Finalizou')






