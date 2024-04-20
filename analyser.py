from funcoes import Funcoes

class Analyser:

    def processar(self, url, id_jogo):
        repositorio_git = url
        json_output = 'CodeAnalysis.json'
        json_smell = 'codeSmells.json'
        repositorio_path = 'repositorio'
        log= 'CSharpAnalyzer.log'
        linter= 'Linter.log'

        Funcoes.remove_folder(repositorio_path)
        Funcoes.remove_arq(json_output)
        Funcoes.remove_arq(json_smell)
        Funcoes.remove_arq(log)
        Funcoes.remove_arq(linter)

        #Clona o repositório: 
        Funcoes.clona_repositorio(repositorio_git)

        #Roda o CSharpAnalyzer, necesária para obter os bad smells. 
        Funcoes.executar_analisador_csharp()
        Funcoes.executar_analisador_code_smell(json_output)
        Funcoes.json_para_csv(json_smell, id_jogo)

        Funcoes.remove_arq(json_output, False)
        Funcoes.remove_arq(json_smell, False)
        Funcoes.remove_arq(log, False)
        Funcoes.remove_arq(linter, False)
        print('Finalizou')






