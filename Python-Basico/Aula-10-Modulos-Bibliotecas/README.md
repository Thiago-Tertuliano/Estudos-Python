# Aula 10: Módulos e Bibliotecas

## 🎯 Objetivos da Aula

- Entender o que são módulos e como organizar código em arquivos separados
- Dominar diferentes formas de importação de módulos
- Conhecer a biblioteca padrão do Python e seus módulos principais
- Aprender a instalar e usar bibliotecas externas
- Praticar a criação de módulos próprios
- Compreender boas práticas de organização de projetos

## 📚 Conteúdo Detalhado

### O que são Módulos?

Módulos são arquivos Python que contêm funções, classes e variáveis que podem ser importados e usados em outros programas. Eles permitem organizar código em arquivos separados e reutilizar funcionalidades.

#### Por que usar módulos?
- **Organização**: Dividir código em arquivos lógicos
- **Reutilização**: Usar código em múltiplos programas
- **Manutenção**: Facilitar a correção e atualização
- **Colaboração**: Trabalhar em equipe de forma organizada
- **Namespace**: Evitar conflitos de nomes
- **Modularidade**: Criar componentes independentes

### Criando Módulos Próprios

#### Módulo Simples:
```python
# arquivo: matematica.py

# Constantes
PI = 3.14159
GRAVIDADE = 9.81

# Funções
def somar(a, b):
    """Soma dois números"""
    return a + b

def subtrair(a, b):
    """Subtrai dois números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b

def dividir(a, b):
    """Divide dois números"""
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def area_circulo(raio):
    """Calcula a área de um círculo"""
    return PI * raio ** 2

def area_retangulo(base, altura):
    """Calcula a área de um retângulo"""
    return base * altura
```

#### Usando o Módulo:
```python
# arquivo: main.py

# Importação completa
import matematica

# Usando funções do módulo
resultado = matematica.somar(10, 5)
print(f"Soma: {resultado}")

area = matematica.area_circulo(5)
print(f"Área do círculo: {area:.2f}")

# Usando constantes
print(f"Valor de PI: {matematica.PI}")
```

### Formas de Importação

#### Importação Completa:
```python
import matematica

# Usando com prefixo do módulo
soma = matematica.somar(10, 5)
print(soma)
```

#### Importação de Funções Específicas:
```python
from matematica import somar, subtrair

# Usando diretamente
soma = somar(10, 5)
subtracao = subtrair(10, 5)
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
```

#### Importação com Alias:
```python
import matematica as math

# Usando com alias
resultado = math.somar(10, 5)
print(resultado)
```

#### Importação de Tudo (Não Recomendado):
```python
from matematica import *

# Usando diretamente (pode causar conflitos)
soma = somar(10, 5)
print(soma)
```

#### Importação com Alias para Funções:
```python
from matematica import somar as soma_func

# Usando com alias
resultado = soma_func(10, 5)
print(resultado)
```

### Módulos da Biblioteca Padrão

#### Módulo math:
```python
import math

# Constantes
print(f"PI: {math.pi}")
print(f"e: {math.e}")

# Funções trigonométricas
angulo = math.pi / 4  # 45 graus
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"Seno de 45°: {seno:.4f}")
print(f"Cosseno de 45°: {cosseno:.4f}")
print(f"Tangente de 45°: {tangente:.4f}")

# Funções logarítmicas
log_natural = math.log(10)
log_base_10 = math.log10(100)
print(f"ln(10): {log_natural:.4f}")
print(f"log10(100): {log_base_10:.4f}")

# Funções de arredondamento
print(f"Arredondamento: {math.ceil(3.2)}")  # Para cima
print(f"Arredondamento: {math.floor(3.8)}")  # Para baixo
print(f"Valor absoluto: {math.fabs(-5)}")
```

#### Módulo random:
```python
import random

# Números aleatórios
numero_float = random.random()  # Entre 0 e 1
print(f"Número aleatório: {numero_float}")

numero_int = random.randint(1, 10)  # Entre 1 e 10
print(f"Número inteiro: {numero_int}")

# Escolha aleatória
frutas = ["maçã", "banana", "laranja", "uva"]
fruta_aleatoria = random.choice(frutas)
print(f"Fruta escolhida: {fruta_aleatoria}")

# Embaralhar lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Lista embaralhada: {numeros}")

# Amostra aleatória
amostra = random.sample(range(1, 51), 6)  # 6 números de 1 a 50
print(f"Números da sorte: {amostra}")
```

#### Módulo datetime:
```python
from datetime import datetime, date, timedelta

# Data e hora atual
agora = datetime.now()
print(f"Data e hora atual: {agora}")

# Data atual
hoje = date.today()
print(f"Data atual: {hoje}")

# Criando datas específicas
data_especifica = datetime(2024, 1, 15, 14, 30, 0)
print(f"Data específica: {data_especifica}")

# Formatação de data
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data formatada: {data_formatada}")

# Operações com datas
amanha = hoje + timedelta(days=1)
ontem = hoje - timedelta(days=1)
print(f"Amanhã: {amanha}")
print(f"Ontem: {ontem}")

# Diferença entre datas
diferenca = data_especifica - agora
print(f"Dias de diferença: {diferenca.days}")
```

#### Módulo os:
```python
import os

# Informações do sistema
print(f"Sistema operacional: {os.name}")
print(f"Diretório atual: {os.getcwd()}")

# Listar arquivos
arquivos = os.listdir(".")
print(f"Arquivos no diretório: {arquivos}")

# Criar diretório
if not os.path.exists("teste"):
    os.mkdir("teste")
    print("Diretório 'teste' criado!")

# Verificar se arquivo existe
arquivo_teste = "teste.txt"
if os.path.exists(arquivo_teste):
    print(f"Arquivo '{arquivo_teste}' existe!")
else:
    print(f"Arquivo '{arquivo_teste}' não existe!")

# Informações de arquivo
if os.path.exists(arquivo_teste):
    tamanho = os.path.getsize(arquivo_teste)
    modificacao = os.path.getmtime(arquivo_teste)
    print(f"Tamanho: {tamanho} bytes")
    print(f"Última modificação: {datetime.fromtimestamp(modificacao)}")
```

#### Módulo json:
```python
import json

# Dados Python
dados_python = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo",
    "hobbies": ["futebol", "música", "leitura"],
    "ativo": True
}

# Convertendo para JSON
json_string = json.dumps(dados_python, indent=2, ensure_ascii=False)
print("JSON formatado:")
print(json_string)

# Convertendo de JSON para Python
dados_recuperados = json.loads(json_string)
print(f"\nDados recuperados: {dados_recuperados}")

# Salvando em arquivo
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_python, arquivo, indent=2, ensure_ascii=False)

# Lendo de arquivo
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)
    print(f"\nDados lidos do arquivo: {dados_lidos}")
```

### Instalando Bibliotecas Externas

#### Usando pip:
```bash
# Instalar uma biblioteca
pip install requests

# Instalar versão específica
pip install requests==2.28.1

# Instalar múltiplas bibliotecas
pip install requests pandas numpy matplotlib

# Listar bibliotecas instaladas
pip list

# Ver informações de uma biblioteca
pip show requests
```

#### Usando requirements.txt:
```txt
# arquivo: requirements.txt
requests==2.28.1
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
```

```bash
# Instalar todas as bibliotecas do arquivo
pip install -r requirements.txt
```

### Exemplos Práticos Avançados

#### Exemplo 1: Sistema de Gerenciamento de Arquivos

```python
# Sistema de gerenciamento de arquivos
print("=== SISTEMA DE GERENCIAMENTO DE ARQUIVOS ===")

import os
import shutil
from datetime import datetime

def listar_arquivos(diretorio="."):
    """Lista todos os arquivos em um diretório"""
    arquivos = []
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isfile(caminho_completo):
            tamanho = os.path.getsize(caminho_completo)
            modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_completo))
            arquivos.append({
                "nome": item,
                "tamanho": tamanho,
                "modificacao": modificacao
            })
    return arquivos

def criar_backup(arquivo_origem, diretorio_backup="backup"):
    """Cria um backup de um arquivo"""
    if not os.path.exists(arquivo_origem):
        return False, "Arquivo não encontrado"
    
    # Criar diretório de backup se não existir
    if not os.path.exists(diretorio_backup):
        os.makedirs(diretorio_backup)
    
    # Nome do arquivo de backup com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = os.path.basename(arquivo_origem)
    nome_backup = f"{nome_arquivo}_{timestamp}"
    caminho_backup = os.path.join(diretorio_backup, nome_backup)
    
    try:
        shutil.copy2(arquivo_origem, caminho_backup)
        return True, f"Backup criado: {caminho_backup}"
    except Exception as e:
        return False, f"Erro ao criar backup: {e}"

def organizar_por_tipo(diretorio="."):
    """Organiza arquivos por extensão"""
    extensoes = {}
    
    for arquivo in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            nome, extensao = os.path.splitext(arquivo)
            if extensao:
                if extensao not in extensoes:
                    extensoes[extensao] = []
                extensoes[extensao].append(arquivo)
    
    return extensoes

# Testando o sistema
print("Arquivos no diretório atual:")
arquivos = listar_arquivos()
for arquivo in arquivos:
    print(f"  {arquivo['nome']} - {arquivo['tamanho']} bytes - {arquivo['modificacao']}")

print("\nOrganização por tipo:")
organizacao = organizar_por_tipo()
for extensao, lista_arquivos in organizacao.items():
    print(f"  {extensao}: {len(lista_arquivos)} arquivos")

# Criar backup de um arquivo (se existir)
arquivo_teste = "teste.txt"
if os.path.exists(arquivo_teste):
    sucesso, mensagem = criar_backup(arquivo_teste)
    print(f"\n{mensagem}")
else:
    print(f"\nArquivo '{arquivo_teste}' não encontrado para backup")
```

#### Exemplo 2: Sistema de Logs

```python
# Sistema de logs
print("=== SISTEMA DE LOGS ===")

import logging
from datetime import datetime

def configurar_logger(nome_arquivo="app.log", nivel=logging.INFO):
    """Configura o sistema de logs"""
    # Configurar formato
    formato = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Configurar handler para arquivo
    file_handler = logging.FileHandler(nome_arquivo, encoding='utf-8')
    file_handler.setFormatter(formato)
    
    # Configurar handler para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formato)
    
    # Configurar logger
    logger = logging.getLogger('MeuApp')
    logger.setLevel(nivel)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def registrar_acao(logger, acao, usuario="sistema", detalhes=""):
    """Registra uma ação no log"""
    mensagem = f"Ação: {acao} | Usuário: {usuario}"
    if detalhes:
        mensagem += f" | Detalhes: {detalhes}"
    
    logger.info(mensagem)

def registrar_erro(logger, erro, contexto=""):
    """Registra um erro no log"""
    mensagem = f"Erro: {erro}"
    if contexto:
        mensagem += f" | Contexto: {contexto}"
    
    logger.error(mensagem)

# Testando o sistema de logs
logger = configurar_logger("teste.log")

# Registrando ações
registrar_acao(logger, "Login", "joao", "Login bem-sucedido")
registrar_acao(logger, "Criar arquivo", "maria", "Arquivo 'relatorio.txt' criado")
registrar_acao(logger, "Logout", "joao")

# Registrando erros
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    registrar_erro(logger, str(e), "Divisão por zero")

try:
    arquivo = open("arquivo_inexistente.txt", "r")
except FileNotFoundError as e:
    registrar_erro(logger, str(e), "Tentativa de abrir arquivo inexistente")

print("\nLogs registrados! Verifique o arquivo 'teste.log'")
```

#### Exemplo 3: Processador de Dados com Pandas

```python
# Processador de dados com pandas
print("=== PROCESSADOR DE DADOS ===")

# Nota: Este exemplo requer pandas instalado
# pip install pandas

try:
    import pandas as pd
    import numpy as np
    from datetime import datetime
    
    def criar_dados_exemplo():
        """Cria dados de exemplo"""
        dados = {
            'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
            'idade': [25, 30, 22, 28, 35],
            'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília'],
            'salario': [5000, 6000, 4500, 5500, 7000],
            'departamento': ['TI', 'RH', 'TI', 'Vendas', 'TI']
        }
        return pd.DataFrame(dados)
    
    def analisar_dados(df):
        """Analisa os dados do DataFrame"""
        print("=== ANÁLISE DOS DADOS ===")
        
        # Informações básicas
        print(f"Total de registros: {len(df)}")
        print(f"Colunas: {list(df.columns)}")
        
        # Estatísticas numéricas
        print("\nEstatísticas numéricas:")
        print(df.describe())
        
        # Análise por departamento
        print("\nAnálise por departamento:")
        dept_stats = df.groupby('departamento').agg({
            'idade': ['mean', 'count'],
            'salario': ['mean', 'sum']
        }).round(2)
        print(dept_stats)
        
        # Pessoas com salário acima da média
        salario_medio = df['salario'].mean()
        acima_media = df[df['salario'] > salario_medio]
        print(f"\nPessoas com salário acima da média ({salario_medio:.2f}):")
        print(acima_media[['nome', 'salario']])
        
        return {
            'total_registros': len(df),
            'salario_medio': salario_medio,
            'idade_media': df['idade'].mean(),
            'departamentos': df['departamento'].nunique()
        }
    
    def exportar_relatorio(df, nome_arquivo):
        """Exporta relatório em diferentes formatos"""
        # CSV
        df.to_csv(f"{nome_arquivo}.csv", index=False, encoding='utf-8')
        print(f"Relatório CSV salvo: {nome_arquivo}.csv")
        
        # Excel (requer openpyxl)
        try:
            df.to_excel(f"{nome_arquivo}.xlsx", index=False)
            print(f"Relatório Excel salvo: {nome_arquivo}.xlsx")
        except ImportError:
            print("openpyxl não instalado - pulando Excel")
        
        # JSON
        df.to_json(f"{nome_arquivo}.json", orient='records', indent=2, force_ascii=False)
        print(f"Relatório JSON salvo: {nome_arquivo}.json")
    
    # Testando o processador
    print("Criando dados de exemplo...")
    df = criar_dados_exemplo()
    
    print("Dados criados:")
    print(df)
    
    # Analisando dados
    estatisticas = analisar_dados(df)
    
    # Exportando relatório
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"relatorio_{timestamp}"
    exportar_relatorio(df, nome_arquivo)
    
    print(f"\nEstatísticas resumidas:")
    for chave, valor in estatisticas.items():
        print(f"  {chave}: {valor}")

except ImportError:
    print("Pandas não está instalado. Para usar este exemplo:")
    print("pip install pandas")
    print("pip install openpyxl  # para suporte a Excel")
```

### Organização de Projetos

#### Estrutura Básica de Projeto:
```
meu_projeto/
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── models.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   └── test_models.py
├── data/
│   ├── input/
│   └── output/
└── logs/
```

#### Exemplo de Módulo Utilitário:
```python
# arquivo: src/utils.py

import os
import json
from datetime import datetime

def carregar_configuracao(arquivo="config.json"):
    """Carrega configurações de um arquivo JSON"""
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_configuracao(config, arquivo="config.json"):
    """Salva configurações em um arquivo JSON"""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def criar_log(nome_arquivo):
    """Cria um arquivo de log com timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"log_{nome_arquivo}_{timestamp}.txt"

def validar_arquivo(arquivo):
    """Valida se um arquivo existe e é legível"""
    return os.path.exists(arquivo) and os.access(arquivo, os.R_OK)
```

### Boas Práticas

#### ✅ Faça:
- **Use nomes descritivos** para módulos e funções
- **Documente módulos** com docstrings
- **Organize imports** (padrão, terceiros, locais)
- **Use __init__.py** para pacotes
- **Teste módulos** independentemente

#### ❌ Evite:
- **Importar tudo** com `from modulo import *`
- **Ciclos de importação** - módulos importando-se mutuamente
- **Nomes conflitantes** - use aliases quando necessário
- **Dependências desnecessárias** - importe apenas o que usar

#### 🔧 Solução de Problemas Comuns:

#### Erro: "ModuleNotFoundError"
- **Causa**: Módulo não encontrado no PYTHONPATH
- **Solução**: Verifique o caminho e use sys.path se necessário

#### Erro: "ImportError"
- **Causa**: Problema na importação ou dependência faltando
- **Solução**: Verifique se a biblioteca está instalada

#### Ciclo de importação:
- **Causa**: Módulos importando-se mutuamente
- **Solução**: Reorganize a estrutura ou use importação local

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Sistema de Gerenciamento de Biblioteca**
   - Crie módulos para livros, usuários, empréstimos
   - Use JSON para persistência de dados
   - Implemente sistema de logs
   - Crie relatórios em diferentes formatos

2. **Processador de Arquivos Avançado**
   - Módulo para processar diferentes tipos de arquivo
   - Sistema de backup automático
   - Validação de integridade de arquivos
   - Geração de relatórios de processamento

3. **Sistema de Configuração**
   - Módulo para gerenciar configurações
   - Suporte a diferentes formatos (JSON, YAML, INI)
   - Validação de configurações
   - Sistema de backup de configurações

4. **API de Dados**
   - Módulo para consumir APIs externas
   - Cache de dados
   - Tratamento de erros
   - Exportação de dados

5. **Sistema de Logs Avançado**
   - Módulo de logging configurável
   - Diferentes níveis de log
   - Rotação de arquivos de log
   - Análise de logs

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Tratamento de Exceções** - como lidar com erros de forma elegante.

### O que você vai aprender:
- 📚 Try/except básico e avançado
- 📚 Tipos de exceções
- 📚 Finally e else
- 📚 Raise e exceções customizadas
- 📚 Boas práticas de tratamento de erros
- 📚 Debugging e logging de erros

---

**Pratique módulos e bibliotecas! São fundamentais para projetos reais! 🐍**

> 💡 **Dica**: Comece criando módulos simples e vá aumentando a complexidade. Isso vai ajudar a entender como organizar melhor seu código e reutilizar funcionalidades.
