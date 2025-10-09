
## <img src="{{ site.baseurl }}/images/female.png" width="30"> Bem-vindos colegas ipeanos. Prazer imenso. 

### <img src="{{ site.baseurl }}/images/nerd.png" width="20"> Bernardo--COMIC/DISET/IPEA

## Aula 1. Aula 0

1. Objetivo da aula: `hello.py` com sucesso
- Instalação prévia? - [Instalação do Python, VS Code e ferramentas essenciais]({{ site.baseurl }}/configuracao/)
- interface: ambiente **VS Code**
- chamando o intérprete **python**
- hands-on inicial
2. Objetivo do curso: 
    - Autonomia, compreensão da lógica
    - Fundamentos
    - POO--programação orientada a objetos
    - Boas práticas
    - Compreensão mínima de: 
        - funções, 
        - classes, 
        - módulos e 
        - persistência
3. Muitos exercícios e exemplos depois da Aula3, para solidificar fundamentos.

## Disclaimer


---

3. **Referência básica:**

- [Pense Python 2ed.](https://penseallen.github.io/PensePython2e/)

---
## Ainda a instalação 
- [Instalação do Python, VS Code e ferramentas essenciais]({{ site.baseurl }}/configuracao/)

- 🗺️ O segredo "é o caminho!"

    - *Assim como na economia, na programação grande parte dos problemas de instalação são porque o sistema não sabe **onde** encontrar o Python e as bibliotecas, ou os arquivos ou as variáveis.*
    - Soluções: 
        - 1. Adicionar PATH na instalação
        - 2. Garantir ambiente do **python** é o mesmo das bibliotecas
        - 3. Ter certeza do caminho do script.py
        - 4. Localizar a variável no *namespace* correto (onde foi definida)

### 4. **Comofaz? I**
- **VS Code**
    -   **Python interativo (console)**
        - REPL: Read, Evaluate, Print, Loop back for more input
        - `python` no Terminal. **Enter**
        - Sair. `quit()`
    - **Teminal**. Qualquer texto *.py
        - `python script.py`
    
    - **Jupyter**
        - New File `hello.ipynb` (*usa servidor--online code*)
        - Escolha kernel (mesmo ambiente)
        - Alternativa (*browser*)
            - `jupyter notebook`
            - Sair: `CTRL + C`

## Exercício: hello.py 
Produzir output impresso na tela: *hello, world!*

- No Terminal do **VS Code**
    - 1. File/Open Folder (*crie um diretório para as aulas*)
    - 2. File/New File (*crie um arquivo chamado hello.py*)
    - 3. Dentro do arquivo digite: `print('Hello, world!!!')`
        - Sem espaços após **print**
        - Com aspas simples ou duplas, mas ou simples ou duplas
        *- Maiúsculas, vírgula e exclamação ao gosto do freguês ou freguesa.*
    - 3. Terminal/New Terminal (*verifique se está no ambiente criado na instalação*)
        - **Windows**: `venv-curso-ipea\Scripts\activate`
    - 4. Digite: `python hello.py`

- Console
    - Terminal. Digite `python` **Enter**
    ```python
    >>> print("hello world")  # Enter
    ```

---

### <img src="{{ site.baseurl }}/images/python.png" width="50">

1. Propósito geral, aplicações de larga escala 
2. Sintaxe limpa, uniforme, manutenção (computação) 
3. Bibliotecas consolidadas para dados, machine learning (comunidade)
4. Multi-paradigma: funcional (funnções), procedural (comandos), Orientada a objetos
5. Orientada a objetos básico: 
    - **métodos (funções) e dados (atributos)** em conjunto

### Vocabulário

1. script, programa
2. parâmetros
3. funções
4. output (print, transforma, persiste)

<img src="{{ site.baseurl }}/images/input_output.png">

---

<img src="{{ site.baseurl }}/images/inputoutput.png">

## Variables
### Hands-on II:

1. Tipos de dados `type()` + primeiras noções de classes, métodos e atributos
    ```python
    int
    str
    bool
    float
    ```
2. Variáveis
    - `input('Entre um número')`

3. Operadores

    ```python
    +
    -
    * 
    /
    **

    ==
    !=
    >=
    ```

4. `help()`

## Strings

1. Strings, como listas (que veremos) são uma sequência
2. Com isso, podem ser acessadas por meio de indexes
    - Lembre-se: em **python** indexing começa em 0.
    Logo: 
    ```python
    frase = 'python is cool'
    frase[1]  # ?
    ```
### Acessando itens (em strings e listas)

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
        - logo **[:]** é a lista/ toda
 
 `# simples é uma lista para ficar mais visual a posição (listas -> aula2)`
 `simples = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] `

 
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

### Strings--methods

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
```

## Reserved words

<img src="{{ site.baseurl }}/images/keywords.png">

## Built-in functions


<img src="{{ site.baseurl }}/images/builtin.png">


[Fonte imagens/Credit:](https://github.com/Asabeneh/30-Days-Of-Python/tree/master)

## Código pythonico

- **Cuidado com seu self futuro**
<img src="{{ site.baseurl }}/images/meme.png">
- ### [PEP 8 -- Jeito pythonista de ser](pep8-python-style-guide.md)

### Boas práticas--DRY: don't repeat yourself
www.greenteapress.com/thinkpython/html/thinkpython005.html
1. **Encapsulation**

    *Wrapping a piece of code up in a function is called encapsulation. One of the benefits of encapsulation is that it attaches a name to the code, which serves as a kind of documentation. Another advantage is that if you re-use the code, it is more concise to call a function twice than to copy and paste the body!*
            
2. **Generalization**

    *Adding a **parameter** to a function is called generalization because it makes the function more general*

### For Fun

1. `import antigravity`
2. `import this`
3. [**Gamification I**](https://py.checkio.org)
4. [**Gamification II**](http://www.pythonchallenge.com/pc/def/0.html)
5. [Automatizando uma fazenda com **Python**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/)

### [Links Úteis]({{ site.baseurl }}/referencias/)

### Exercícios

1. Quanto é '5' * 5?
2. `print(5 + 5)` é igual a `print('5' + '5')`? Why?
3. Quanto é :  `(25 ∗ (2 + 23)/54)2`
4. Quantas horas inteiras tem em 200 minutos? Use `//` floor division
5. Quantos minutos sobram? Use `%` remainder