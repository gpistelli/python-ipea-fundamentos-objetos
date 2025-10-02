#!/usr/bin/env python3
"""
Script de Verificação de Instalação - Python para Análise de Dados IPEA
Autor: Bernardo Alves Furtado
"""

import sys
import subprocess
import importlib.util

def print_color(text, color="green"):
    """Função para imprimir texto colorido"""
    colors = {
        "green": "\033[92m",
        "yellow": "\033[93m", 
        "red": "\033[91m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['reset']}")

def verificar_python():
    """Verifica a versão do Python"""
    print_color("🐍 Verificando Python...", "blue")
    try:
        version = sys.version_info
        print_color(f"✅ Python {version.major}.{version.minor}.{version.micro} instalado", "green")
        
        if version.major == 3 and version.minor >= 8:
            print_color("✅ Versão compatível (3.8+)", "green")
        else:
            print_color("⚠️  Versão muito antiga, recomendo Python 3.8+", "yellow")
            
        return True
    except Exception as e:
        print_color(f"❌ Erro ao verificar Python: {e}", "red")
        return False

def verificar_pip():
    """Verifica se pip está disponível"""
    print_color("\n📦 Verificando pip...", "blue")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True, check=True)
        print_color(f"✅ {result.stdout.strip()}", "green")
        return True
    except subprocess.CalledProcessError:
        print_color("❌ pip não encontrado", "red")
        return False

def verificar_biblioteca(nome, nome_import=None):
    """Verifica se uma biblioteca específica está instalada"""
    nome_import = nome_import or nome
    try:
        spec = importlib.util.find_spec(nome_import)
        if spec is not None:
            # Tenta obter a versão
            try:
                mod = importlib.import_module(nome_import)
                version = getattr(mod, '__version__', 'versão não disponível')
                print_color(f"✅ {nome}: {version}", "green")
            except:
                print_color(f"✅ {nome} instalado", "green")
            return True
        else:
            print_color(f"❌ {nome} não instalado", "red")
            return False
    except ImportError:
        print_color(f"❌ {nome} não instalado", "red")
        return False

def verificar_bibliotecas_essenciais():
    """Verifica todas as bibliotecas essenciais do curso"""
    print_color("\n📚 Verificando bibliotecas essenciais...", "blue")
    
    bibliotecas = [
        ("pandas", "pandas"),           # Manipulação de dados
        ("numpy", "numpy"),             # Computação numérica
        ("scikit-learn", "sklearn"),    # Machine Learning
        ("jupyter", "jupyter"),         # Jupyter notebooks
        ("matplotlib", "matplotlib"),   # Visualização
        ("seaborn", "seaborn"),         # Visualização estatística
    ]
    
    resultados = []
    for nome, import_name in bibliotecas:
        resultados.append(verificar_biblioteca(nome, import_name))
    
    return all(resultados)

def verificar_editor():
    """Verifica se VS Code está instalado (aproximação)"""
    print_color("\n⚡ Verificando editores...", "blue")
    
    # Verifica se o comando 'code' está disponível
    try:
        subprocess.run(["code", "--version"], capture_output=True, check=True)
        print_color("✅ VS Code detectado (comando 'code' disponível)", "green")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_color("⚠️  VS Code não detectado (opcional)", "yellow")
        return False

def verificar_git():
    """Verifica se Git está instalado"""
    print_color("\n🔧 Verificando Git...", "blue")
    try:
        result = subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
        print_color(f"✅ {result.stdout.strip()}", "green")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_color("❌ Git não encontrado", "red")
        return False

def mostrar_comandos_instalacao():
    """Mostra comandos para instalar o que falta"""
    print_color("\n🔧 COMANDOS DE INSTALAÇÃO:", "yellow")
    print_color("=" * 50, "yellow")
    
    print_color("\n📦 Instalar bibliotecas essenciais:", "blue")
    print("pip install pandas numpy scikit-learn jupyter matplotlib seaborn")
    
    print_color("\n🐍 Instalar com conda (se preferir):", "blue")
    print("conda install pandas numpy scikit-learn jupyter matplotlib seaborn")
    
    print_color("\n⚡ Instalar VS Code:", "blue")
    print("https://code.visualstudio.com/download")
    
    print_color("\n🔧 Instalar Git:", "blue")
    print("https://git-scm.com/downloads")
    
    print_color("=" * 50, "yellow")

def main():
    """Função principal"""
    print_color("🔍 VERIFICAÇÃO DO AMBIENTE PYTHON - CURSO IPEA", "blue")
    print_color("=" * 60, "blue")
    
    resultados = []
    
    # Executa todas as verificações
    resultados.append(verificar_python())
    resultados.append(verificar_pip())
    resultados.append(verificar_bibliotecas_essenciais())
    resultados.append(verificar_editor())
    resultados.append(verificar_git())
    
    print_color("\n" + "=" * 60, "blue")
    
    # Resumo final
    sucessos = sum(resultados)
    total = len(resultados)
    
    if sucessos == total:
        print_color(f"🎉 PERFEITO! {sucessos}/{total} verificações passaram!", "green")
        print_color("Seu ambiente está pronto para o curso!", "green")
    elif sucessos >= total - 1:
        print_color(f"✅ QUASE LÁ! {sucessos}/{total} verificações passaram.", "green")
        print_color("Alguns itens opcionais em falta, mas pode prosseguir.", "yellow")
        mostrar_comandos_instalacao()
    else:
        print_color(f"⚠️  ATENÇÃO! Apenas {sucessos}/{total} verificações passaram.", "red")
        print_color("É necessário instalar alguns componentes:", "red")
        mostrar_comandos_instalacao()
    
    print_color("\n💡 DICA: Execute este script periodicamente para verificar seu ambiente!", "blue")

if __name__ == "__main__":
    main()