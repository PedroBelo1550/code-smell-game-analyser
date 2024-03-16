import os
import shutil
from funcoes import Funcoes

projeto_path = Funcoes.cria_pasta_temporaria()
repositorio_git = 'https://github.com/coconauts/startcraft-unity3d.git'
json_output = 'CodeAnalysis.json'
json_smell = 'codeSmells.json'
repositorio_path = 'repositorio'

if os.path.exists(repositorio_path):
    # Deletar o repositório existente
    shutil.rmtree(repositorio_path)

os.makedirs(repositorio_path)


#Clona o repositório: 
Funcoes.clona_repositorio(repositorio_git)

#Roda o CSharpAnalyzer, necesária para obter os bad smells. 
Funcoes.executar_analisador_csharp()
Funcoes.executar_analisador_code_smell(json_output)
print(Funcoes.json_para_csv(json_smell))






