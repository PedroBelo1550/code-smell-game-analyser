from radon.complexity import cc_visit
from radon.metrics import h_visit
from radon.visitors import ComplexityVisitor

def calculate_complexity(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
    content = content.replace(b'\xef\xbb\xbf', b'').decode('utf-8')
    complexity_visitor = ComplexityVisitor.from_code(content)
    cc_visit(complexity_visitor)
    return complexity_visitor.complexity

file_path = './jogo/a perdição de marajó - 2º período - 2-2017/Assets/Scripts/Game/CameraMovement.cs'
complexity = calculate_complexity(file_path)
print(f'Complexidade Ciclomática: {complexity}')
