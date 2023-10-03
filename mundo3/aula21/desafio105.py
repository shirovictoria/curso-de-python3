"""
Faça um programa tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidades de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também os docsStrings da função.
"""
def notas(*notas, situacao=False):
    """
    Calcula informações sobre notas de alunos.

    :param notas: Uma ou mais notas dos alunos.
    :param situacao: Define se a situação do aluno será calculada (opcional).
    :return: Um dicionário com informações sobre as notas.
    """
    resultado = {
        'Quantidade de Notas': len(notas),
        'Maior Nota': max(notas),
        'Menor Nota': min(notas),
        'Média da Turma': sum(notas) / len(notas)
    }
    if situacao:
        if resultado['Média da Turma'] >= 7:
            resultado['Situação'] = 'Aprovado'
        else:
            resultado['Situação'] = 'Reprovado'

    return resultado
notas_alunos = (8.5, 9.0, 7.5, 6.0, 9.5)
informacoes = notas(*notas_alunos, situacao=True)

for chave, valor in informacoes.items():
    print(f'{chave}: {valor}')
