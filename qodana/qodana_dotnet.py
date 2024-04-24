import os
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET
import uuid
import pandas as pd
from io import StringIO
import pexpect
from sql_server import SQLServerConnector
import asyncio
import yaml


async def run_scan():
    # Comando a ser executado
    command = 'qodana scan'

    # Inicia o processo
    process = await asyncio.create_subprocess_shell(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Lê a saída do processo linha por linha
    while True:
        line = await process.stdout.readline()
        if line:
            # Imprime a linha (opcional)
            print(line.decode().strip())

            # Se a linha contém a pergunta, envia a resposta 'n'
            if "?  Do you want to open . [Y/n]" in line.decode():
                process.stdin.write(b'n\n')
                process.stdin.close()
                break  # Sai do loop quando a resposta é enviada
        else:
            break

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

def escrever_arquivo_yaml(caminho):

        caminho = os.path.join(caminho, 'qodana.yaml')

        dados_yaml = {
            'version': "1.0",
            'linter': "jetbrains/qodana-cdnet",
            'dotnet': {
                'project': "analise.csproj"
            }
        }

        # Abre o arquivo no modo de escrita
        with open(caminho, 'w') as arquivo:
            # Escreve os dados no arquivo YAML
            yaml.dump(dados_yaml, arquivo, default_flow_style=False)
        print(f"Arquivo YAML criado com sucesso em '{caminho}'")


def get_cloc(id_jogo):

    project_dir = os.path.join('E:\\jogos\\', id_jogo)

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

    # Copia o arquivo de configuracao do linter
    escrever_arquivo_yaml(project_dir)

    # Navegue até o diretório do projeto
    os.chdir(project_dir)

    # Inicia o processo
    asyncio.run(run_scan())

    # Execute o comando qodana cloc e capture a saída
    result = subprocess.run(['qodana', 'cloc', '-o=csv'], capture_output=True, text=True)

    # Verifique se o comando foi executado com sucesso
    if result.returncode == 0:
        csv_output = StringIO(result.stdout)

        # Leia os dados CSV usando o Pandas
        df = pd.read_csv(csv_output, header=0)
        # Exiba o DataFrame
        print(df)

        df = df[df['Language'] == 'C#']
        df['id_jogo'] = id_jogo

        db = SQLServerConnector()
        db.insert_data_from_dataframe(df, 'cloc')
    
    os.chdir('C:\\Users\\vm1\\Documents\\dev\\code-smell-game-analyser')
    

        

