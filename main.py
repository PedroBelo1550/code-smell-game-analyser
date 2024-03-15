import tempfile
import os
import git

def clona_repositorio(url, destino):
    git.Repo.clone_from(url, destino)

def cria_pasta_temporaria():
    return tempfile.mkdtemp()

projeto_path = cria_pasta_temporaria()

repositorio_git = 'https://github.com/Hyperparticle/nodulus.git'

#Clona o repositório: 
clona_repositorio(repositorio_git,projeto_path)

#Roda o CSharpAnalyzer, necesária para obter os bad smells. 





