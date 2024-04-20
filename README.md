# code-smell-game-analyser
Melhoria no sistema de verificação de code smells de aplicações unity, o UnityCodeSmellAnalyzer

Comando para construir a aplicação
````
pyinstaller --onefile  --add-data="UnityCodeSmellAnalyzer;UnityCodeSmellAnalyzer" --hidden-import=git   main.py
``

Comando para executar o scanner
````cmd
cd C:\Program Files\sonar-scanner-5.0.1.3006-windows\bin

C:\Program Files\sonar-scanner-5.0.1.3006-windows\bin\sonar-scanner.bat -D"sonar.projectKey=game-smells" -D"sonar.sources=C:\Users\vm1\Documents\dev\analise_sonar." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_07d2a8556245a1c2bace2833d126f862de2e7a73" -D"sonar.projectBaseDir=C:\Users\vm1\Documents\dev\analise_sonar"
``

Comando para extracao de dados em json.
````
curl -u "token:sqp_07d2a8556245a1c2bace2833d126f862de2e7a73" "http://localhost:9000/api/project_analyses/search?project=game-smells" > C:\Users\vm1\Documents\dev\resultado_analise.json
``