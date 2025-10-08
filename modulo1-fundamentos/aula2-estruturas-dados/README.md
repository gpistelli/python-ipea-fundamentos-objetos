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

- 1. `append(item)`  # appends to the end of the list
- 2. `pop()`  # returns last item
- 3. `sort()`  # accepts parameter `reverse` 
- 4. outras?

### Acessando itens

- 1. Use index, mas começe pelo **0**   `# como maioria das "linguagens" de programação`
- 2. *MUTABLE*: Quando você "assign" um valor novo, ele substitui o anterior

```python
>>> supermercado[2] = 'rúcula'
>>> supermercado

# What happens for supermercado[-1] ?
```

1. **Sobre iterables e indexes**
    - dois pontos (colon) são importantes dentro de colchetes para indexes
        - [início:fim(não incluído)]
        - **[4:7]** do então 4 até o antes do 7
            - note que o 7o. termo está incluído porque começou em 0
        - início omitido é 0
        - fim omitido é o último -1
        - logo **[:]** é a lista toda

 `simples = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
 
 Teste no console
 ```python
 simples[0]
 simples[-1]
 simples[4]
 simples[:4]
 simples[:]
 simples[-2:]
 simples[:-2]
 simples[-2:-2]
 # be careful
 simples[10]
 # note que só acessamos os itens. não modificamos as listas
 # métodos, todavia, alteram a lista inplace
 ```

2. Apply **python** general functions to lists

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
motivator = 'python is cool'
type(motivator)
motivator.capitalize()
help(str)
# endswith, isnum, isalpha, islower, isupper, join, 
# lower, split,s trip, title, zfill
motivator[6]
motivator.split(' ')

subject, verb, adjective = motivator.split(' ')
sintaxe_tuple = motivator.split(' ')

CNPJ_BB = 191
# be carefult
CNPJ_BB.zfill(14)
# what is the error?
# ...

str(CNPJ_BB).zfill(14)

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

## Dicionários key:value--muitíssimo útil--fast-indexado
```python
# Cria-se com CHAVES
# Par chave, valor com dois pontos
# Assign como listas, com colchetes--chave = valor

armario1 = {}
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
