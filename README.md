# code-smell-game-analyser
Melhoria no sistema de verificação de code smells de aplicações unity, o UnityCodeSmellAnalyzer

Comando para construir a aplicação
````
pyinstaller --onefile  --add-data="UnityCodeSmellAnalyzer;UnityCodeSmellAnalyzer" --hidden-import=git   main.py
``