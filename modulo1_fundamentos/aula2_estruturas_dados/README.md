# Aula 2

Goal: Listas, tuplas, dicionários, conjuntos e suas operações principais. Exercícios

## Listas--mutable--iterable 

 - sequência (strings também)

```python
notas_curso = [0, 0, 1, 0, 3, 0, 2, 0, 9, 8]  # ;)
supermercado = ['banana', 'ovos', 'alface', 'leite']
total_mess = ['aulas', 43, ['October', 16]]
empty_list = list()
empty_list2 = []
```

### Métodos

1. `append(item)`  # appends to the end of the list
2. `pop()`  # returns last item
3. `sort()`  # accepts parameter `reverse` 
4. outras?

5. Apply **python** general functions to lists

```python
len(simples)
sum(simples)
# outras?
```
### Gotcha!

```python

a = [1, 2, 3]
b = a
a.append(4)
# What is the value of b?
# is serve para testar se o objeto é o mesmo
a is b
# id() é uma função que identifica o número individual do objeto na memória
id(a)
id(b)
```

### Fun thing (relacionada)
```python
a, b = 1, 2
# quais valores de a e de b?
a, b = b, a
# e agora?

# revisite total_mess
# o que total_mess[2][1] retorna?
```

## Tuplas (tuples)--immutable

```python
luck_numbers = (43, 16, 88)
type(luck_numbers)
help(luck_numbers)
16 in luck_numbers
69 in luck_numbers
luck_numbers.count(16)
luck_numbers[1]
```
1. Indexes igual à listas. 
2. Porém, imutável -> não recebe assignment  # Wrong: `t[0] = 9`

### Cool example: tuple + str method
```python
# introducing string formatting on the fly and join :)
print(f'join is {'super'.upper()} cool string method')
# systematics. print + f + single or double quotes + variable between brackets: 
print(f"this f-string works and is {adjective}")  
# as long as adjective exists in the namespace

# very common example tupla para assignment
hora = 60  # padrão
minutos = 200  # para transformar em horas e minutos

horas, minutos = minutos // hora, minutos % hora
```

## Dicionários key: value--muitíssimo útil--fast-indexado--mapping
```python
# Cria-se com CHAVES
# Par chave, valor com dois pontos
# Assign como listas, com colchetes--chave = valor

armario1 = {}
armario1 = dict()  # também funciona. Acho mais explícito
key = 'gavetao'
value = 'lençóis especiais'

# É necessário ter criado o dicionário antes. 
# Mesma coisa com append para lista.
armario1[key] = value
armario1
armario2 = {key: value}
armario2
armario3 = {'gavetao': 'lençóis especiais'}
armario3

armario1 == armario2 == armario3
armario1 is armario2
```

### Métodos

1. `armario1.keys()`  # chaves
2. `armario1.values()`  # valores
3. `armario1.items()`  # lista de tuples de chaves e valores 

    ```python
    armario1['gaveta_alta`] = 'pijamas
    [(key1, value1), (key2, value2)]
    armario1['gaveta_alta`] = 'pijamas
    ```

## Fun thing: salto ao futuro (das aulas)
### 🤔 good idea?

```python


def histogram(string): 
    """ Exemplo de dicionário como uma função para contagem: histogram. 
    Inclui parâmetro de input, retorna dicionário criado, faz loop e testa condicional. 
    Muita calma nessa hora!
    """
    # Cria o dicionário
    meu_dict = dict()
    # Começa o loop pelas letras da palavra
    for letter in string:
        # Testa se a letra já está no dicionário
        if letter not in meu_dict:
            # Inicia contagem
            meu_dict[letter] = 1
        # Se ela já estava, aumenta a contagem em 1
        else:
            meu_dict[letter] += 1
    # Depois do loop retorna o dicionário pronto
    return meu_dict

# Para chamar a função
palavra_teste = 'abracadabra'
resposta = histogram(palavra_teste)

```

## Sets--Conjuntos--elementos únicos!

```python
conjunto = set()
outro_conjunto = {87, 91, 88}  # Chaves, mas não para chave-valor. 
""" unordered, unchangeable, no duplicate values"""
# Method
conjunto.add(88)  # Não é append, como lista, é ADD
print(len(conjunto))
conjunto.add(88)
print(len(conjunto))
conjunto.add(81)
```

### Methods
 - `in` `88 in conjunto`
 - `conjunto.update(outro_conjunto)`  # também pode update com uma lista
 - `uniao = conjunto.union(outro_conjunto)`  # retorna um set
 - `conjunto.intersection(outro_conjunto)`  # mantém só os elementos, presentes em ambos, retorna um set
 - `diferenca = conjunto.difference(outro_conjunto)`  # retorna a diferença

### Vida prática--eliminar duplicates

`lista_elementos_unicos = list(set(lista_com_duplicados))`




