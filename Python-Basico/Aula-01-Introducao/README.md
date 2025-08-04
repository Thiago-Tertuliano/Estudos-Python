# Aula 1: Introdução ao Python

## 🎯 Objetivos da Aula

- Entender o que é Python e suas características fundamentais
- Aprender como instalar e configurar o Python no seu computador
- Criar seu primeiro programa e entender a estrutura básica
- Familiarizar-se com o ambiente de desenvolvimento
- Compreender a importância da indentação e sintaxe do Python

## 📚 Conteúdo Detalhado

### O que é Python?

Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos. Foi criada por Guido van Rossum em 1991 e é conhecida por sua simplicidade e versatilidade.

#### Características Principais:

- **Simplicidade**: Sintaxe clara e legível, similar ao inglês
- **Versatilidade**: Usada em web, IA, ciência de dados, automação, jogos
- **Comunidade**: Uma das maiores comunidades de desenvolvedores do mundo
- **Bibliotecas**: Milhares de bibliotecas disponíveis para diferentes propósitos
- **Multiplataforma**: Funciona em Windows, Mac, Linux sem modificações

#### Onde Python é Usado:

- **Desenvolvimento Web**: Django, Flask, FastAPI
- **Ciência de Dados**: Pandas, NumPy, Matplotlib
- **Inteligência Artificial**: TensorFlow, PyTorch, scikit-learn
- **Automação**: Selenium, requests, beautifulsoup
- **Aplicações Desktop**: Tkinter, PyQt, Kivy
- **Jogos**: Pygame, Arcade

### Características Técnicas do Python

✅ **Fácil de aprender** - Sintaxe intuitiva e legível  
✅ **Multiplataforma** - Funciona em Windows, Mac, Linux  
✅ **Open Source** - Gratuito e com código aberto  
✅ **Interpretado** - Não precisa compilar, executa diretamente  
✅ **Dinâmico** - Tipos definidos em tempo de execução  
✅ **Orientado a Objetos** - Suporte completo a POO  
✅ **Garbage Collection** - Gerenciamento automático de memória  

### Instalação do Python

#### Windows:
1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente (3.11+ recomendado)
3. Execute o instalador
4. **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação
5. Clique em "Install Now"

#### Verificar instalação:
```bash
python --version
# Deve mostrar algo como: Python 3.11.0

python -c "print('Python está funcionando!')"
```

#### Alternativa: Anaconda
Para ciência de dados, considere instalar o Anaconda:
- Inclui Python + bibliotecas científicas
- Gerenciador de pacotes integrado
- Ambiente isolado

### Primeiro Programa: Hello World

O primeiro programa que todo programador escreve:

```python
print("Hello, World!")
```

#### Explicação:
- `print()` é uma função que exibe texto na tela
- O texto entre aspas é uma **string** (texto)
- O programa termina com uma nova linha

#### Variações:
```python
# Com aspas simples
print('Hello, World!')

# Com múltiplas linhas
print("Hello,")
print("World!")

# Com formatação
print("Hello, World!")  # Comentário na mesma linha
```

### Comentários em Python

Comentários são textos que explicam o código mas não são executados.

#### Comentário de Uma Linha:
```python
# Este é um comentário de uma linha
nome = "João"  # Comentário no final da linha
```

#### Comentário de Múltiplas Linhas:
```python
"""
Este é um comentário
de múltiplas linhas.
Muito útil para documentar
funções e classes.
"""

'''
Também podemos usar
aspas simples para
comentários longos.
'''
```

#### Boas Práticas para Comentários:
- Use comentários para explicar **por que**, não **o que**
- Mantenha comentários atualizados
- Use comentários para documentar decisões importantes
- Evite comentários óbvios

### Estrutura Básica de um Programa Python

Um programa Python típico segue esta estrutura:

```python
# 1. Imports (se necessário)
import math
import random

# 2. Variáveis e dados
nome = "João"
idade = 25
altura = 1.75

# 3. Lógica do programa
print(f"Olá, {nome}! Você tem {idade} anos.")
area_circulo = math.pi * 5 ** 2
print(f"Área do círculo: {area_circulo:.2f}")

# 4. Funções (veremos mais tarde)
def saudacao():
    return "Bem-vindo ao Python!"

# 5. Execução principal
if __name__ == "__main__":
    print(saudacao())
```

### Conceitos Fundamentais

#### 1. Indentação
Python usa indentação para definir blocos de código:

```python
if True:
    print("Este código está indentado")
    print("Este também")
print("Este não está")
```

#### 2. Case Sensitive
Python diferencia maiúsculas de minúsculas:

```python
nome = "João"
Nome = "Maria"
NOME = "Pedro"

print(nome)  # "João"
print(Nome)  # "Maria"
print(NOME)  # "Pedro"
```

#### 3. Nomes de Variáveis
- Podem conter letras, números e underscore (_)
- Não podem começar com número
- São case sensitive
- Não podem usar palavras reservadas

```python
# ✅ Válidos
nome = "João"
idade_aluno = 20
preco_produto = 29.99
PI = 3.14159

# ❌ Inválidos
# 1nome = "João"     # Começa com número
# nome-aluno = "João" # Usa hífen
# class = "Python"    # Palavra reservada
```

### Ambiente de Desenvolvimento

#### Editores Recomendados:

1. **VS Code** (Recomendado para iniciantes)
   - Gratuito e poderoso
   - Extensões Python disponíveis
   - Integração com terminal

2. **PyCharm**
   - IDE completa para Python
   - Versão Community gratuita
   - Debugger integrado

3. **IDLE** (Vem com Python)
   - Simples e básico
   - Bom para aprender
   - Interface gráfica simples

#### Configurando VS Code:
1. Instale o VS Code
2. Instale a extensão "Python" da Microsoft
3. Abra uma pasta com seus arquivos Python
4. Configure o interpretador Python (Ctrl+Shift+P → "Python: Select Interpreter")

### Executando Programas Python

#### Método 1: Terminal/Prompt
```bash
python meu_programa.py
```

#### Método 2: VS Code
- Abra o arquivo .py
- Pressione F5 ou clique em "Run"

#### Método 3: IDLE
- Abra o IDLE
- File → Open → selecione o arquivo
- F5 para executar

### Exemplos Práticos

#### Exemplo 1: Calculadora Simples
```python
# Calculadora básica
numero1 = 10
numero2 = 5

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
```

#### Exemplo 2: Informações Pessoais
```python
# Coletando informações
nome = "Maria"
idade = 25
cidade = "São Paulo"
profissao = "Desenvolvedora"

# Exibindo informações
print("=== Informações Pessoais ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")

# Criando uma apresentação
apresentacao = f"Olá! Sou {nome}, tenho {idade} anos, moro em {cidade} e trabalho como {profissao}."
print(f"\nApresentação: {apresentacao}")
```

#### Exemplo 3: Formatação de Strings
```python
# Diferentes formas de formatar strings
nome = "João"
idade = 30
salario = 2500.50

# F-strings (recomendado)
print(f"Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}")

# Método format()
print("Nome: {}, Idade: {}, Salário: R$ {:.2f}".format(nome, idade, salario))

# % (estilo antigo)
print("Nome: %s, Idade: %d, Salário: R$ %.2f" % (nome, idade, salario))
```

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Hello World Personalizado**
   - Crie um programa que imprima "Olá, [seu nome]!"
   - Use f-strings para formatação

2. **Informações Pessoais**
   - Crie variáveis com seu nome, idade, cidade e profissão
   - Imprima uma frase completa usando essas informações
   - Experimente diferentes formas de formatação

3. **Calculadora Simples**
   - Crie variáveis com dois números
   - Imprima a soma, subtração, multiplicação e divisão
   - Formate os resultados com 2 casas decimais

4. **Calculadora de Área**
   - Calcule a área de um retângulo (base × altura)
   - Calcule a área de um círculo (π × raio²)
   - Use comentários para explicar as fórmulas

5. **Conversor de Temperatura**
   - Converta Celsius para Fahrenheit (F = C × 9/5 + 32)
   - Converta Fahrenheit para Celsius (C = (F - 32) × 5/9)
   - Teste com diferentes temperaturas

## 📝 Dicas Importantes

### ✅ Faça:
- **Pratique diariamente** - A consistência é mais importante que a quantidade
- **Experimente** - Modifique os exemplos para entender melhor
- **Use comentários** - Documente seu código desde o início
- **Teste diferentes valores** - Não se limite aos exemplos
- **Leia o código** - Entenda cada linha antes de executar

### ❌ Evite:
- **Pular conceitos** - Cada detalhe é importante
- **Copiar sem entender** - Sempre analise o que está fazendo
- **Ignorar erros** - Erros são oportunidades de aprendizado
- **Desistir** - Programação tem curva de aprendizado

### 🔧 Solução de Problemas Comuns:

#### Erro: "python não é reconhecido"
- **Solução**: Reinstale o Python marcando "Add to PATH"

#### Erro: "IndentationError"
- **Solução**: Use espaços consistentes (4 espaços por nível)

#### Erro: "SyntaxError"
- **Solução**: Verifique parênteses, aspas e dois pontos

#### Erro: "NameError"
- **Solução**: Verifique se a variável foi definida antes de usar

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Variáveis e Tipos de Dados** - a base para armazenar e manipular informações em Python.

### O que você vai aprender:
- 📚 Números inteiros e decimais
- 📚 Strings e booleanos
- 📚 Conversão de tipos
- 📚 Input do usuário
- 📚 Formatação avançada de strings

---

**Lembre-se**: A prática leva à perfeição! 🐍

> 💡 **Dica**: Programe todos os dias, mesmo que seja por apenas 30 minutos. A consistência é mais importante que a intensidade. 