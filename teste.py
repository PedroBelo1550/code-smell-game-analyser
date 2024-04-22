import os
import re

def remove_special_chars(folder_path):
    # Percorre todas as pastas dentro da pasta especificada
    for root, dirs, files in os.walk(folder_path):
        for name in dirs:
            # Cria um novo nome removendo caracteres especiais
            new_name = re.sub(r'[^\w\s-]|º', '', name)
            new_name = re.sub(r'\s+', ' ', new_name)
            new_name = re.sub('_', ' ', new_name)# Substitui espaços por underscores
            # Caminho completo da pasta original
            old_path = os.path.join(root, name)
            # Caminho completo da nova pasta
            new_path = os.path.join(root, new_name)
            # Renomeia a pasta original para o novo nome
            os.rename(old_path, new_path)

# Substitua 'caminho_da_pasta' pelo caminho da pasta que você deseja modificar
remove_special_chars('E:\\jogos')
