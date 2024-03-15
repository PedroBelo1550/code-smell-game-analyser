from funcoes import Funcoes

projeto_path = Funcoes.cria_pasta_temporaria()
repositorio_git = 'https://github.com/Hyperparticle/nodulus.git'
json_output = 'CodeAnalysis.json'
json_smell = 'codeSmells.json'


#Clona o repositório: 
Funcoes.clona_repositorio(repositorio_git,projeto_path)

#Roda o CSharpAnalyzer, necesária para obter os bad smells. 
Funcoes.executar_analisador_csharp(projeto_path)
Funcoes.executar_analisador_code_smell(json_output)
print(Funcoes.json_para_csv(json_smell))






