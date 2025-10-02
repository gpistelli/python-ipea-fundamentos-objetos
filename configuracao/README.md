## 🔧 Configuração do Ambiente de Desenvolvimento

## Recomendações para o Curso

### ⚡ VS Code + Python 
**Mais leve e direto para análise de dados**

1. **Instalar Python**
   - [Python.org](https://www.python.org/downloads/) - baixe a versão 3.12.10
   - **NÃO** baixar Python da Microsoft Store
   ## ⚠️ **Marque a opção "Add Python to PATH" durante a instalação**


2. **Instalar VS Code**
   - [VS Code Download](https://code.visualstudio.com/download)
   - Depois de instalado VS Code e Python, instale algumas extensões
   - Extensões essenciais (no VS Code busque botão extensions CTRL+Shift+X na barra lateral à esquerda):
   - Verifique o autor e aperte `install`

     - **Python** (Microsoft)
     - **Pylance** (melhor autocompletar)
     - **GitLens** (para versionamento)

3. **Próximos Passos: Instalar Git**
- [Git Download](https://git-scm.com/downloads)
- Configuração básica (após instalação, abra o terminal):
`git config --global user.name "Seu Nome"`
`git config --global user.email "seu.email@ipea.gov.br"`

4. **Instalar environment**
- Abra o Terminal
- Verifique se a versão de python está correta. O caminho para a versão python deverá ser: `/venv-curso-ipea/bin/python
   - Windows
      - `where python`
   - Linux/Mac
      - `which python`
- `python -m venv venv-curso-ipea ` 
   Você está chamando o interpreter `python` e pedindo a ele para rodar um módulo `-m` que se chama `venv` de virtual environment. Em seguida, dá o nome ao seu novo ambiente `venv-curso-ipea`
- Em seguida precisa ativar o ambiente e avisar ao VS Code para utilizá-lo. Faça isso com
   - Windows
      - `venv-curso-ipea\Scripts\activate`
   - Mac/Linux
      - `source venv-curso-ipea/bin/activate`

5. **Verificar Instalação**
```python
# executar no terminal (na barra de cima Terminal/New terminal):
python --version
pip --version
```
- Se a versão que aparecer for diferente, pode ser que você tenha que indicar ao VS Code qual o caminho correto (usando CTRL+Shift+P)

6. **Instalar bibliotecas dentro do environment do curso**
bibliotecas principais**
- Abra o terminal. Você deve ver algo como `(venv-curso-ipea)` antes do prompt e digite
- `pip install pandas numpy scikit-learn jupyter matplotlib seaborn plotly openpyxl`

7. **Tenha um arquivo .gitignore**
Evite que arquivos de configuração sejam carregados para o repositório na nuvem. 

Copie as seguintes configurações em um arquivo na raiz do seu projeto nomeado `.gitignore` (File/New File)

```
# Environments
venv-curso-ipea/
env/
.venv/

# VS Code
.vscode/
*.code-workspace

# Python
__pycache__/
*.pyc
*.pyo
.python-version

# Dados grandes
dados/raw/
*.csv
*.xlsx
!dados/exemplos/sample_data.csv
```

### Caveats--detalhes--troubleshooting

1. Caso tenha mais de um **python** instalado no seu computador, pode ser necessário `CTRL+Shift+P` (abre a paletta de comando do VS Code) e digite `Python: Select interpreter` (para avisar ao VS Code qual versão de Python seu projeto irá utilizar)
2. Logo que abrir o VS Code, use a opção `File/Open Folder` para indicar o caminho da pasta que vai utilizar para o curso. 
3. Em um momento seguinte do curso, vamos `clonar` o repositório diretamente do GitHub.
4. Se houver um arquivo de bibliotecas necessárias, utilize `pip install -r configuracao/requirements.txt` para instalar direto do arquivo. Tenha certeza de que está no ambiente certo--aparecerá (venv-curso-ipea) no prompt do Terminal
5. Se tiver problemas de permissão no Windows, utilize sempre bibliotecas no seu usuário com: `pip install --user pandas numpy scikit-learn jupyter matplotlib seaborn`
6. Sempre confira em algum diretório o seu prompt está, em qual pasta está o script a ser rodado. Confira ainda se o ambiente está ativo (aparece o nome entre parenteses, antes do prompt)
7. Se o python não estiver sendo reconhecido pelo sistema, tente adicionar o caminho (descubra o caminho com `where python`) ao PATH: 
   - System Properties → Environment Variables → PATH
   - Adicione: C:\caminho\para\python312\
8. - Atenção: [Boas práticas Windows](boaspraticas.md)