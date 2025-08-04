# Aula 2: Variáveis e Tipos de Dados

## 🎯 Objetivos da Aula

- Entender o que são variáveis e como criá-las corretamente
- Conhecer todos os tipos de dados básicos do Python
- Aprender a converter entre diferentes tipos de forma segura
- Praticar o uso de variáveis em programas reais
- Compreender a importância dos tipos de dados na programação

## 📚 Conteúdo Detalhado

### O que são Variáveis?

Variáveis são "caixas" ou "containers" que armazenam dados na memória do computador. Em Python, você não precisa declarar o tipo da variável - o Python faz isso automaticamente baseado no valor que você atribui.

#### Conceito Fundamental:
```python
# Uma variável é como uma etiqueta em uma caixa
nome = "João"        # A caixa "nome" contém "João"
idade = 25           # A caixa "idade" contém 25
altura = 1.75        # A caixa "altura" contém 1.75
ativo = True         # A caixa "ativo" contém True
```

#### Por que usar variáveis?
- **Reutilização**: Use o mesmo valor em vários lugares
- **Legibilidade**: Nomes descritivos tornam o código mais claro
- **Manutenção**: Mude o valor em um lugar, afeta todo o código
- **Organização**: Estrutura melhor os dados do programa

### Tipos de Dados Básicos

Python tem vários tipos de dados nativos. Vamos conhecer os principais:

#### 1. Números Inteiros (int)

Números inteiros, positivos ou negativos, sem parte decimal.

```python
idade = 25
ano = 2024
quantidade = -10
temperatura = 0
populacao = 2147483647  # Número grande
```

**Características:**
- Não têm limite de tamanho (Python 3)
- Podem ser positivos ou negativos
- Usados para contagem, idade, anos, etc.

#### 2. Números Decimais (float)

Números com parte decimal (ponto flutuante).

```python
preco = 29.99
altura = 1.75
pi = 3.14159
temperatura = -5.5
peso = 70.0
```

**Características:**
- Precisão limitada (aproximadamente 15-17 dígitos)
- Podem ter notação científica: `1.23e-4`
- Usados para medidas, preços, cálculos científicos

#### 3. Strings (str)

Sequências de caracteres (texto).

```python
nome = "Maria"
frase = 'Python é incrível!'
texto = """Texto com
múltiplas linhas"""
palavra = "a"
vazio = ""
```

**Características:**
- Imutáveis (não podem ser alteradas diretamente)
- Podem usar aspas simples ou duplas
- Suportam caracteres especiais e Unicode
- Podem ser vazias

#### 4. Booleanos (bool)

Valores lógicos: True ou False.

```python
ativo = True
inativo = False
tem_carteira = True
e_maior_idade = False
```

**Características:**
- Apenas dois valores possíveis
- Usados em condições e lógica
- Resultado de comparações
- Base para tomada de decisões

#### 5. None (NoneType)

Representa "nada" ou "vazio".

```python
valor = None
resultado = None
configuracao = None
```

**Características:**
- Valor único do tipo NoneType
- Usado para indicar ausência de valor
- Padrão para funções que não retornam nada
- Útil em estruturas de dados opcionais

### Verificando o Tipo de uma Variável

A função `type()` retorna o tipo de uma variável:

```python
nome = "João"
idade = 25
altura = 1.75
ativo = True
valor = None

print(type(nome))    # <class 'str'>
print(type(idade))   # <class 'int'>
print(type(altura))  # <class 'float'>
print(type(ativo))   # <class 'bool'>
print(type(valor))   # <class 'NoneType'>
```

#### Verificação em tempo de execução:
```python
# Verificando tipos dinamicamente
dados = [nome, idade, altura, ativo, valor]

for item in dados:
    print(f"Valor: {item}, Tipo: {type(item)}")
```

### Nomes de Variáveis

#### ✅ Nomes Válidos:
```python
nome = "João"
idade_aluno = 20
preco_produto = 29.99
PI = 3.14159  # Constantes em maiúsculo
_privado = "valor"  # Começa com underscore
variavel123 = "ok"  # Números no final
```

#### ❌ Nomes Inválidos:
```python
# 1nome = "João"     # Não pode começar com número
# nome-aluno = "João" # Não pode usar hífen
# class = "Python"    # Palavra reservada
# if = "condicao"     # Palavra reservada
# for = "loop"        # Palavra reservada
```

#### Palavras Reservadas do Python:
```python
# Estas palavras não podem ser usadas como nomes de variáveis:
# and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, None,
# nonlocal, not, or, pass, raise, return, True, try, while, with, yield
```

#### Convenções de Nomenclatura:

1. **snake_case** (recomendado para variáveis):
   ```python
   nome_completo = "João Silva"
   data_nascimento = "1990-01-01"
   salario_mensal = 2500.00
   ```

2. **UPPER_CASE** (para constantes):
   ```python
   PI = 3.14159
   GRAVIDADE = 9.81
   MAX_TENTATIVAS = 3
   ```

3. **camelCase** (menos comum em Python):
   ```python
   nomeCompleto = "João Silva"
   dataNascimento = "1990-01-01"
   ```

### Conversão de Tipos (Type Casting)

Python permite converter entre tipos de dados usando funções específicas.

#### Convertendo para Inteiro (int)

```python
# String para inteiro
numero_string = "25"
numero_inteiro = int(numero_string)
print(numero_inteiro)  # 25

# Float para inteiro (trunca a parte decimal)
numero_float = 25.7
numero_inteiro = int(numero_float)
print(numero_inteiro)  # 25

# Boolean para inteiro
valor_bool = True
numero_inteiro = int(valor_bool)
print(numero_inteiro)  # 1

# Erro comum - string inválida
# int("abc")  # ValueError: invalid literal for int()
```

#### Convertendo para Float (float)

```python
# String para float
numero_string = "25.5"
numero_float = float(numero_string)
print(numero_float)  # 25.5

# Inteiro para float
numero_inteiro = 25
numero_float = float(numero_inteiro)
print(numero_float)  # 25.0

# String com notação científica
cientifico = "1.23e-4"
numero_float = float(cientifico)
print(numero_float)  # 0.000123
```

#### Convertendo para String (str)

```python
# Inteiro para string
idade = 25
idade_string = str(idade)
print(idade_string)  # "25"

# Float para string
preco = 29.99
preco_string = str(preco)
print(preco_string)  # "29.99"

# Boolean para string
ativo = True
ativo_string = str(ativo)
print(ativo_string)  # "True"

# None para string
valor = None
valor_string = str(valor)
print(valor_string)  # "None"
```

#### Convertendo para Boolean (bool)

```python
# Valores que se tornam True
print(bool(1))      # True
print(bool("texto")) # True
print(bool(25))     # True
print(bool([1, 2, 3])) # True (lista não vazia)

# Valores que se tornam False
print(bool(0))      # False
print(bool(""))     # False
print(bool(None))   # False
print(bool([]))     # False (lista vazia)
print(bool(()))     # False (tupla vazia)
print(bool({}))     # False (dicionário vazio)
```

### Operações com Diferentes Tipos

#### Operações com Strings

```python
# Concatenação
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)  # "João Silva"

# Repetição
separador = "-" * 20
print(separador)  # "--------------------"

# Comprimento
texto = "Python"
print(len(texto))  # 6

# Acesso a caracteres
primeira_letra = texto[0]  # "P"
ultima_letra = texto[-1]   # "n"
```

#### Operações com Números

```python
a = 10
b = 3

# Operações básicas
soma = a + b        # 13
subtracao = a - b   # 7
multiplicacao = a * b  # 30
divisao = a / b     # 3.333...
divisao_inteira = a // b  # 3
resto = a % b       # 1
potencia = a ** b   # 1000

# Operações com float
c = 10.5
d = 2.3
resultado = c + d   # 12.8
```

#### Operações Mistas

```python
# String + número (erro)
# nome = "João" + 25  # TypeError

# Conversão necessária
nome = "João"
idade = 25
frase = nome + " tem " + str(idade) + " anos"
print(frase)  # "João tem 25 anos"

# F-strings (recomendado)
frase = f"{nome} tem {idade} anos"
print(frase)  # "João tem 25 anos"
```

### Input do Usuário

A função `input()` sempre retorna uma string, mesmo se o usuário digitar um número.

#### Input Básico:
```python
# Coletando dados do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Convertendo para número
idade = int(idade)

print(f"Olá {nome}, você tem {idade} anos!")
```

#### Input com Validação:
```python
# Input com tratamento de erro
try:
    idade = input("Digite sua idade: ")
    idade = int(idade)
    print(f"Você tem {idade} anos!")
except ValueError:
    print("Por favor, digite um número válido!")
```

#### Input de Diferentes Tipos:
```python
# String
nome = input("Nome: ")

# Inteiro
idade = int(input("Idade: "))

# Float
altura = float(input("Altura (metros): "))

# Boolean (convertendo string)
ativo = input("Ativo? (s/n): ").lower() == 's'
```

### Formatação de Strings

#### F-strings (Recomendado - Python 3.6+)

```python
nome = "Maria"
idade = 25
altura = 1.65
salario = 2500.50

# Formatação básica
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}m")

# Formatação de números
print(f"Salário: R$ {salario:.2f}")

# Formatação com alinhamento
print(f"Nome: {nome:>10}")
print(f"Idade: {idade:>10}")

# Expressões dentro de f-strings
print(f"Ano de nascimento: {2024 - idade}")
```

#### Método format()

```python
nome = "João"
idade = 30
salario = 3000.00

# Formatação básica
print("Nome: {}, Idade: {}, Salário: R$ {:.2f}".format(nome, idade, salario))

# Formatação com índices
print("Nome: {0}, Idade: {1}, Salário: R$ {2:.2f}".format(nome, idade, salario))

# Formatação com nomes
print("Nome: {n}, Idade: {i}, Salário: R$ {s:.2f}".format(n=nome, i=idade, s=salario))
```

#### % (Estilo Antigo)

```python
nome = "Ana"
idade = 28
altura = 1.70

# Formatação com %
print("Nome: %s, Idade: %d, Altura: %.2fm" % (nome, idade, altura))
```

### Exemplos Práticos Avançados

#### Exemplo 1: Calculadora de Média com Validação

```python
# Calculadora de média com validação de entrada
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # Validação das notas
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
        media = (nota1 + nota2 + nota3) / 3
        print(f"Média: {media:.2f}")
        
        if media >= 7:
            print("Status: Aprovado")
        elif media >= 5:
            print("Status: Recuperação")
        else:
            print("Status: Reprovado")
    else:
        print("Notas devem estar entre 0 e 10!")
        
except ValueError:
    print("Por favor, digite apenas números!")
```

#### Exemplo 2: Conversor de Unidades

```python
# Conversor de unidades
print("=== CONVERSOR DE UNIDADES ===")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
print("3. Quilômetros para Milhas")
print("4. Quilos para Libras")

opcao = input("Escolha uma opção (1-4): ")

try:
    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.1f}°C")
        
    elif opcao == "3":
        km = float(input("Digite a distância em quilômetros: "))
        milhas = km * 0.621371
        print(f"{km} km = {milhas:.2f} milhas")
        
    elif opcao == "4":
        kg = float(input("Digite o peso em quilogramas: "))
        libras = kg * 2.20462
        print(f"{kg} kg = {libras:.2f} libras")
        
    else:
        print("Opção inválida!")
        
except ValueError:
    print("Por favor, digite um número válido!")
```

#### Exemplo 3: Validador de Dados

```python
# Validador de dados pessoais
print("=== VALIDADOR DE DADOS ===")

# Coletando dados
nome = input("Nome completo: ").strip()
cpf = input("CPF (apenas números): ").replace(".", "").replace("-", "")
idade = input("Idade: ")
email = input("E-mail: ").lower()

# Validações
erros = []

# Validar nome
if len(nome) < 3:
    erros.append("Nome deve ter pelo menos 3 caracteres")

# Validar CPF
if not cpf.isdigit() or len(cpf) != 11:
    erros.append("CPF deve ter 11 dígitos numéricos")

# Validar idade
try:
    idade_int = int(idade)
    if idade_int < 0 or idade_int > 120:
        erros.append("Idade deve estar entre 0 e 120")
except ValueError:
    erros.append("Idade deve ser um número")

# Validar email
if "@" not in email or "." not in email:
    erros.append("E-mail inválido")

# Resultado
if erros:
    print("\n❌ Dados inválidos:")
    for erro in erros:
        print(f"  - {erro}")
else:
    print("\n✅ Dados válidos!")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    print(f"Idade: {idade} anos")
    print(f"E-mail: {email}")
```

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora de Média Avançada**
   - Crie variáveis para 4 notas
   - Calcule a média ponderada (pesos diferentes)
   - Valide se as notas estão entre 0 e 10
   - Exiba o conceito (A, B, C, D, F)

2. **Conversor de Temperatura Completo**
   - Converta entre Celsius, Fahrenheit e Kelvin
   - Implemente todas as conversões possíveis
   - Valide as temperaturas de entrada
   - Formate a saída com unidades

3. **Calculadora de Área e Perímetro**
   - Calcule área e perímetro de retângulo
   - Calcule área e circunferência de círculo
   - Calcule área de triângulo
   - Use constantes para π

4. **Manipulação de Strings Avançada**
   - Concatene strings de diferentes formas
   - Use métodos de string (upper, lower, strip, etc.)
   - Crie um gerador de senhas simples
   - Valide formato de e-mail

5. **Sistema de Cadastro Simples**
   - Coleta dados pessoais
   - Valida formato de CPF, telefone, e-mail
   - Calcula idade a partir da data de nascimento
   - Gera um relatório formatado

## 📝 Dicas Importantes

### ✅ Boas Práticas:
- **Nomes descritivos**: Use nomes que expliquem o que a variável contém
- **Snake_case**: Use underscore para separar palavras (padrão Python)
- **Sempre converta input**: `input()` sempre retorna string
- **Valide dados**: Sempre verifique se os dados são válidos
- **Use f-strings**: São mais legíveis e eficientes
- **Documente conversões**: Comente quando fizer conversões complexas

### ❌ Evite:
- **Nomes genéricos**: `a`, `b`, `x`, `y` (exceto em loops simples)
- **Conversões desnecessárias**: Só converta quando realmente precisar
- **Ignorar erros**: Sempre trate possíveis erros de conversão
- **Misturar estilos**: Escolha um padrão e mantenha consistência

### 🔧 Solução de Problemas Comuns:

#### Erro: "ValueError: invalid literal for int()"
- **Causa**: Tentando converter string não numérica para int
- **Solução**: Valide a entrada antes de converter

#### Erro: "TypeError: can only concatenate str (not 'int')"
- **Causa**: Tentando concatenar string com número
- **Solução**: Converta o número para string ou use f-strings

#### Erro: "NameError: name 'variavel' is not defined"
- **Causa**: Usando variável antes de defini-la
- **Solução**: Sempre defina variáveis antes de usá-las

#### Erro: "IndentationError"
- **Causa**: Problemas com indentação
- **Solução**: Use 4 espaços consistentemente

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Operadores** - como fazer comparações e operações lógicas em Python.

### O que você vai aprender:
- 📚 Operadores aritméticos (+, -, *, /, //, %, **)
- 📚 Operadores de comparação (==, !=, >, <, >=, <=)
- 📚 Operadores lógicos (and, or, not)
- 📚 Operadores de atribuição (+=, -=, *=, etc.)
- 📚 Precedência de operadores
- 📚 Avaliação de expressões complexas

---

**Pratique muito! A repetição é a mãe do aprendizado! 🐍**

> 💡 **Dica**: Experimente criar seus próprios exemplos. Tente converter dados do seu dia a dia para variáveis Python e veja como os tipos se comportam. 