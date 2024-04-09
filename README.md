# code-smell-game-analyser
Melhoria no sistema de verificação de code smells de aplicações unity, o UnityCodeSmellAnalyzer

Comando para construir a aplicação
````
pyinstaller --onefile  --add-data="UnityCodeSmellAnalyzer;UnityCodeSmellAnalyzer" --hidden-import=git   main.py
``

````cmd
sonar-scanner.bat -D"sonar.projectKey=game-smells" -D"sonar.sources=C:\Users\vm1\Documents\dev\analise_sonar." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_07d2a8556245a1c2bace2833d126f862de2e7a73"
``