from pathlib import Path
import sys

# Add parent directory to the front of Python path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

""" Exemplo de sorted histogramas usando dicionários.
    Adaptado de Think Python. Chapter 11

"""

from aula3_controle_fluxo import lists_generator


def histogram(data):
    # Calcula a frequência de ocorrência de cada key
    d = dict()
    for each in data:
        d[each] = d.get(each, 0) + 1
    return d


def print_sorted(d):
    # Ordena o dicionário em ordem alfabética das keys
    for key in sorted(d):
        print(f'{key}: {d[key]}')


if __name__ == '__main__':
    string1 = 'paralelepipedo'
    d1 = histogram(string1)
    print(string1)
    print_sorted(d1)
    print('')
    d2 = histogram(lists_generator.generate())
    print('lista aleatória')
    print_sorted(d2)
