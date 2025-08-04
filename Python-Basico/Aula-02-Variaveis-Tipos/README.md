# Aula 2: Variáveis e Tipos de Dados

## 🎯 Objetivos da Aula

- Entender o que são variáveis e como criá-las
- Conhecer os tipos de dados básicos do Python
- Aprender a converter entre diferentes tipos
- Praticar o uso de variáveis em programas

## 📚 Conteúdo

### O que são Variáveis?

Variáveis são "caixas" que armazenam dados na memória do computador. Em Python, você não precisa declarar o tipo da variável - o Python faz isso automaticamente.

```python
nome = "João"        # String
idade = 25           # Inteiro
altura = 1.75        # Float
ativo = True         # Boolean
```

### Tipos de Dados Básicos

#### 1. Números Inteiros (int)
```python
idade = 25
ano = 2024
quantidade = -10
```

#### 2. Números Decimais (float)
```python
preco = 29.99
altura = 1.75
pi = 3.14159
```

#### 3. Strings (str)
```python
nome = "Maria"
frase = 'Python é incrível!'
texto = """Texto com
múltiplas linhas"""
```

#### 4. Booleanos (bool)
```python
ativo = True
inativo = False
```

#### 5. None (NoneType)
```python
valor = None  # Representa "nada" ou "vazio"
```

### Verificando o Tipo de uma Variável

```python
nome = "João"
idade = 25
altura = 1.75

print(type(nome))    # <class 'str'>
print(type(idade))   # <class 'int'>
print(type(altura))  # <class 'float'>
```

### Nomes de Variáveis

#### ✅ Nomes Válidos:
```python
nome = "João"
idade_aluno = 20
preco_produto = 29.99
PI = 3.14159  # Constantes em maiúsculo
```

#### ❌ Nomes Inválidos:
```python
# 1nome = "João"     # Não pode começar com número
# nome-aluno = "João" # Não pode usar hífen
# class = "Python"    # Palavra reservada
```

### Conversão de Tipos (Type Casting)

#### Convertendo para Inteiro
```python
numero_string = "25"
numero_inteiro = int(numero_string)
print(numero_inteiro)  # 25

# Também funciona com float
numero_float = 25.7
numero_inteiro = int(numero_float)
print(numero_inteiro)  # 25 (trunca a parte decimal)
```

#### Convertendo para Float
```python
numero_string = "25.5"
numero_float = float(numero_string)
print(numero_float)  # 25.5

# De inteiro para float
numero_inteiro = 25
numero_float = float(numero_inteiro)
print(numero_float)  # 25.0
```

#### Convertendo para String
```python
idade = 25
idade_string = str(idade)
print(idade_string)  # "25"

preco = 29.99
preco_string = str(preco)
print(preco_string)  # "29.99"
```

#### Convertendo para Boolean
```python
# Valores que se tornam True
print(bool(1))      # True
print(bool("texto")) # True
print(bool(25))     # True

# Valores que se tornam False
print(bool(0))      # False
print(bool(""))     # False
print(bool(None))   # False
```

### Operações com Diferentes Tipos

#### Strings
```python
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # "João Silva"

# Repetindo strings
separador = "-" * 20
print(separador)  # "--------------------"
```

#### Números
```python
a = 10
b = 3

soma = a + b        # 13
subtracao = a - b   # 7
multiplicacao = a * b  # 30
divisao = a / b     # 3.333...
divisao_inteira = a // b  # 3
resto = a % b       # 1
potencia = a ** b   # 1000
```

### Input do Usuário

```python
# Input sempre retorna uma string
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Convertendo para número
idade = int(idade)

print(f"Olá {nome}, você tem {idade} anos!")
```

### Formatação de Strings

```python
nome = "Maria"
idade = 25
altura = 1.65

# F-strings (recomendado)
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}m")

# Método format()
print("Nome: {}, Idade: {}, Altura: {}m".format(nome, idade, altura))

# % (estilo antigo)
print("Nome: %s, Idade: %d, Altura: %.2fm" % (nome, idade, altura))
```

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora de Média**
   - Crie variáveis para 3 notas
   - Calcule e exiba a média

2. **Conversor de Temperatura**
   - Converta Celsius para Fahrenheit
   - Fórmula: F = C * 9/5 + 32

3. **Calculadora de Área**
   - Calcule área de um retângulo
   - Calcule área de um círculo

4. **Manipulação de Strings**
   - Concatene strings
   - Use métodos de string

## 📝 Dicas Importantes

- **Nomes descritivos**: Use nomes que expliquem o que a variável contém
- **Snake_case**: Use underscore para separar palavras (padrão Python)
- **Case sensitive**: `nome` e `Nome` são diferentes
- **Sempre converta input**: `input()` sempre retorna string

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Operadores** - como fazer comparações e operações lógicas em Python.

---

**Pratique muito! A repetição é a mãe do aprendizado! 🐍** 