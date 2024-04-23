import os
import subprocess
import xml.etree.ElementTree as ET
import uuid
import pandas as pd
from io import StringIO

def generate_csproj(project_dir, project_name, files):
    # Cria o elemento raiz do arquivo .csproj
    csproj = ET.Element('Project', xmlns="http://schemas.microsoft.com/developer/msbuild/2003")

    # Adiciona uma seção PropertyGroup com algumas propriedades básicas
    property_group = ET.SubElement(csproj, 'PropertyGroup')
    ET.SubElement(property_group, 'OutputType').text = 'Exe'
    ET.SubElement(property_group, 'TargetFramework').text = 'netcoreapp4.8.1'
    # Adiciona um ProjectGuid
    ET.SubElement(property_group, 'ProjectGuid').text = "{" + str(uuid.uuid4()) + '}'

    # Adiciona os arquivos .cs ao elemento ItemGroup
    item_group = ET.SubElement(csproj, 'ItemGroup')
    for file in files:
        ET.SubElement(item_group, 'Compile', Include=file)

    # Adiciona uma seção Target para a compilação
    build_target = ET.SubElement(csproj, 'Target', Name='Build')
    ET.SubElement(build_target, 'Message', Text='Building...')

    # Cria a árvore XML
    tree = ET.ElementTree(csproj)

    # Escreve o arquivo .csproj
    csproj_path = os.path.join(project_dir, f'analise.csproj')
    tree.write(csproj_path, encoding="utf-8", xml_declaration=True)


# Lista de diretórios dos projetos C#
project_directories = [
    'C:\\Users\\vm1\\Documents\\dev\\analise_sonar\\',
    # Adicione mais diretórios conforme necessário
]

# Caminho para o SonarScanner para MSBuild
sonar_scanner_path = 'sonarscanner'

# Configurações do SonarQube
sonar_project_key = 'teste'
sonar_token = 'sqp_f4c7a707397b72587b3a89aba29dd00384254dc0'

for project_dir in project_directories:
    # Obter todos os arquivos .cs no diretório do projeto
    cs_files = []

    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.cs'):
                # Concatena o caminho do arquivo com o diretório raiz
                cs_files.append(os.path.join(root, file))

    # Gerar o arquivo .csproj
    project_name = os.path.basename(project_dir)
    generate_csproj(project_dir, project_name, cs_files)

    # Navegue até o diretório do projeto
    os.chdir(project_dir)

    # Inicie a análise do SonarQube
    subprocess.run([
        'qodana', 'scan'
    ])

    # Execute o comando qodana cloc e capture a saída
    result = subprocess.run(['qodana', 'cloc', '-o=csv'], capture_output=True, text=True)

    # Verifique se o comando foi executado com sucesso
    if result.returncode == 0:
        csv_output = StringIO(result.stdout)

        # Leia os dados CSV usando o Pandas
        df = pd.read_csv(csv_output)
        # Exiba o DataFrame
        print(df)

    result = subprocess.run(['qodana', 'view', '-f="./qodana.sarif.json"'], capture_output=True, text=True)
