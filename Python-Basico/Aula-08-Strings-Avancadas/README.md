# Aula 8: Strings Avançadas

## 🎯 Objetivos da Aula

- Dominar métodos avançados de manipulação de strings
- Aprender diferentes técnicas de formatação de strings
- Compreender expressões regulares básicas
- Praticar validação e processamento de texto
- Trabalhar com strings de forma eficiente
- Implementar funcionalidades de processamento de dados textuais

## 📚 Conteúdo Detalhado

### O que são Strings Avançadas?

Strings avançadas envolvem técnicas sofisticadas de manipulação, formatação e processamento de texto. Python oferece ferramentas poderosas para trabalhar com strings de forma eficiente e elegante.

#### Por que aprender strings avançadas?
- **Processamento de dados**: Limpar e formatar dados textuais
- **Validação de entrada**: Verificar formatos de email, telefone, etc.
- **Análise de texto**: Extrair informações de documentos
- **Formatação de saída**: Criar relatórios e documentos
- **Automação**: Processar arquivos de texto automaticamente

### Métodos de String Avançados

#### Métodos de Busca e Substituição:
```python
texto = "Python é uma linguagem de programação incrível!"

# Encontrar posição de substring
posicao = texto.find("linguagem")
print(f"Posição de 'linguagem': {posicao}")

# Encontrar última ocorrência
ultima_pos = texto.rfind("a")
print(f"Última posição de 'a': {ultima_pos}")

# Substituir substring
novo_texto = texto.replace("incrível", "poderosa")
print(f"Após replace: {novo_texto}")

# Substituir múltiplas ocorrências
texto_multiplo = "a a a a a"
texto_substituido = texto_multiplo.replace("a", "b", 3)  # Substitui apenas 3 primeiras
print(f"Substituição limitada: {texto_substituido}")
```

#### Métodos de Verificação:
```python
# Verificações básicas
palavra = "Python123"

print(f"É alfanumérico: {palavra.isalnum()}")
print(f"É alfabético: {palavra.isalpha()}")
print(f"É numérico: {palavra.isdigit()}")
print(f"É minúsculo: {palavra.islower()}")
print(f"É maiúsculo: {palavra.isupper()}")
print(f"É título: {palavra.istitle()}")
print(f"É espaço: {'   '.isspace()}")

# Verificações específicas
email = "usuario@email.com"
print(f"Contém '@': {'@' in email}")
print(f"Termina com '.com': {email.endswith('.com')}")
print(f"Começa com 'usuario': {email.startswith('usuario')}")
```

#### Métodos de Transformação:
```python
texto = "  Python é INCRÍVEL!  "

# Removendo espaços
sem_espacos = texto.strip()
print(f"Sem espaços: '{sem_espacos}'")

# Removendo apenas da esquerda
sem_esquerda = texto.lstrip()
print(f"Sem espaços à esquerda: '{sem_esquerda}'")

# Removendo apenas da direita
sem_direita = texto.rstrip()
print(f"Sem espaços à direita: '{sem_direita}'")

# Transformando case
maiusculo = texto.upper()
minusculo = texto.lower()
titulo = texto.title()
capitalize = texto.capitalize()

print(f"Maiúsculo: {maiusculo}")
print(f"Minúsculo: {minusculo}")
print(f"Título: {titulo}")
print(f"Capitalize: {capitalize}")
```

### Formatação Avançada de Strings

#### F-strings Avançadas:
```python
nome = "João"
idade = 25
salario = 2500.50

# Formatação básica
print(f"Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}")

# Alinhamento
print(f"Nome: {nome:>10}")
print(f"Idade: {idade:>10}")
print(f"Salário: R$ {salario:>10.2f}")

# Preenchimento com caracteres
print(f"Nome: {nome:*<10}")
print(f"Idade: {idade:*>10}")
print(f"Salário: R$ {salario:*^15.2f}")

# Expressões complexas
print(f"Ano de nascimento: {2024 - idade}")
print(f"Salário anual: R$ {salario * 12:,.2f}")

# Formatação condicional
status = "ativo" if idade >= 18 else "inativo"
print(f"Status: {status}")
```

#### Método format() Avançado:
```python
# Formatação com índices
texto = "Nome: {0}, Idade: {1}, Salário: R$ {2:.2f}"
resultado = texto.format("João", 25, 2500.50)
print(resultado)

# Formatação com nomes
texto = "Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}"
resultado = texto.format(nome="João", idade=25, salario=2500.50)
print(resultado)

# Formatação com dicionário
dados = {"nome": "João", "idade": 25, "salario": 2500.50}
texto = "Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}"
resultado = texto.format(**dados)
print(resultado)
```

#### Formatação com % (Estilo Antigo):
```python
nome = "João"
idade = 25
salario = 2500.50

# Formatação básica
texto = "Nome: %s, Idade: %d, Salário: R$ %.2f" % (nome, idade, salario)
print(texto)

# Formatação com dicionário
dados = {"nome": "João", "idade": 25, "salario": 2500.50}
texto = "Nome: %(nome)s, Idade: %(idade)d, Salário: R$ %(salario).2f" % dados
print(texto)
```

### Expressões Regulares Básicas

#### Introdução às Regex:
```python
import re

texto = "Meu email é usuario@email.com e meu telefone é (11) 99999-9999"

# Buscando padrões
emails = re.findall(r'\w+@\w+\.\w+', texto)
print(f"Emails encontrados: {emails}")

telefones = re.findall(r'\(\d{2}\) \d{5}-\d{4}', texto)
print(f"Telefones encontrados: {telefones}")

# Verificando se string corresponde a padrão
email_valido = "usuario@email.com"
padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(padrao_email, email_valido):
    print("Email válido!")
else:
    print("Email inválido!")
```

#### Padrões Comuns:
```python
import re

# Padrões básicos
texto = "CPF: 123.456.789-00, CNPJ: 12.345.678/0001-90"

# CPF
cpfs = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto)
print(f"CPFs: {cpfs}")

# CNPJ
cnpjs = re.findall(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', texto)
print(f"CNPJs: {cnpjs}")

# Validação de senha forte
senha = "Senha123!"
padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
if re.match(padrao_senha, senha):
    print("Senha forte!")
else:
    print("Senha fraca!")
```

### Manipulação Avançada de Strings

#### Divisão e Junção:
```python
# Divisão de strings
texto = "maçã,banana,laranja,uva,morango"
frutas = texto.split(",")
print(f"Frutas: {frutas}")

# Divisão com limite
texto2 = "a-b-c-d-e"
partes = texto2.split("-", 2)  # Divide apenas 2 vezes
print(f"Partes: {partes}")

# Junção de strings
palavras = ["Python", "é", "incrível"]
frase = " ".join(palavras)
print(f"Frase: {frase}")

# Junção com separador personalizado
numeros = ["1", "2", "3", "4", "5"]
sequencia = " -> ".join(numeros)
print(f"Sequência: {sequencia}")
```

#### Substituição Avançada:
```python
import re

texto = "O preço é R$ 100,00 e o desconto é 10%"

# Substituindo números por X
texto_anonimo = re.sub(r'\d+', 'X', texto)
print(f"Texto anônimo: {texto_anonimo}")

# Substituindo com função
def dobrar_numero(match):
    numero = int(match.group())
    return str(numero * 2)

texto_dobrado = re.sub(r'\d+', dobrar_numero, texto)
print(f"Texto com números dobrados: {texto_dobrado}")

# Removendo caracteres especiais
texto_limpo = re.sub(r'[^\w\s]', '', texto)
print(f"Texto limpo: {texto_limpo}")
```

### Validação de Strings

#### Validação de Email:
```python
import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))

# Testando emails
emails_teste = [
    "usuario@email.com",
    "usuario.email@dominio.com",
    "usuario@email",
    "@email.com",
    "usuario@.com"
]

for email in emails_teste:
    if validar_email(email):
        print(f"✅ {email} é válido")
    else:
        print(f"❌ {email} é inválido")
```

#### Validação de CPF:
```python
import re

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf_limpo = re.sub(r'\D', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf_limpo) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if len(set(cpf_limpo)) == 1:
        return False
    
    # Validação dos dígitos verificadores (simplificada)
    return True

# Testando CPFs
cpfs_teste = [
    "123.456.789-00",
    "111.111.111-11",
    "123.456.789",
    "abc.def.ghi-jk"
]

for cpf in cpfs_teste:
    if validar_cpf(cpf):
        print(f"✅ {cpf} é válido")
    else:
        print(f"❌ {cpf} é inválido")
```

#### Validação de Senha:
```python
def validar_senha(senha):
    erros = []
    
    if len(senha) < 8:
        erros.append("Senha deve ter pelo menos 8 caracteres")
    
    if not re.search(r'[a-z]', senha):
        erros.append("Senha deve conter pelo menos uma letra minúscula")
    
    if not re.search(r'[A-Z]', senha):
        erros.append("Senha deve conter pelo menos uma letra maiúscula")
    
    if not re.search(r'\d', senha):
        erros.append("Senha deve conter pelo menos um número")
    
    if not re.search(r'[@$!%*?&]', senha):
        erros.append("Senha deve conter pelo menos um caractere especial")
    
    return len(erros) == 0, erros

# Testando senhas
senhas_teste = [
    "Senha123!",
    "senha123",
    "SENHA123",
    "Senha!",
    "12345678"
]

for senha in senhas_teste:
    valida, erros = validar_senha(senha)
    if valida:
        print(f"✅ '{senha}' é válida")
    else:
        print(f"❌ '{senha}' é inválida: {', '.join(erros)}")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Processador de Texto

```python
# Processador de texto
print("=== PROCESSADOR DE TEXTO ===")

def processar_texto(texto):
    # Estatísticas básicas
    palavras = texto.split()
    caracteres = len(texto)
    caracteres_sem_espaco = len(texto.replace(" ", ""))
    
    # Contagem de palavras
    contador_palavras = {}
    for palavra in palavras:
        palavra_limpa = palavra.lower().strip(".,!?;:")
        if palavra_limpa:
            contador_palavras[palavra_limpa] = contador_palavras.get(palavra_limpa, 0) + 1
    
    # Palavras mais frequentes
    palavras_frequentes = sorted(contador_palavras.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Frases (divididas por pontuação)
    import re
    frases = re.split(r'[.!?]+', texto)
    frases = [f.strip() for f in frases if f.strip()]
    
    return {
        "palavras": len(palavras),
        "caracteres": caracteres,
        "caracteres_sem_espaco": caracteres_sem_espaco,
        "frases": len(frases),
        "palavras_frequentes": palavras_frequentes,
        "palavra_mais_longa": max(palavras, key=len) if palavras else "",
        "palavra_mais_curta": min(palavras, key=len) if palavras else ""
    }

# Testando o processador
texto_teste = """
Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos. 
Foi criada por Guido van Rossum em 1991. Python é conhecida por sua simplicidade e 
legibilidade. É amplamente usada em web development, data science, machine learning e 
automação. Python tem uma sintaxe clara e uma grande biblioteca padrão.
"""

resultado = processar_texto(texto_teste)

print("=== ANÁLISE DO TEXTO ===")
print(f"Palavras: {resultado['palavras']}")
print(f"Caracteres (com espaços): {resultado['caracteres']}")
print(f"Caracteres (sem espaços): {resultado['caracteres_sem_espaco']}")
print(f"Frases: {resultado['frases']}")
print(f"Palavra mais longa: '{resultado['palavra_mais_longa']}'")
print(f"Palavra mais curta: '{resultado['palavra_mais_curta']}'")

print("\nPalavras mais frequentes:")
for palavra, frequencia in resultado['palavras_frequentes']:
    print(f"  '{palavra}': {frequencia} vezes")
```

#### Exemplo 2: Validador de Formulário

```python
# Validador de formulário
print("=== VALIDADOR DE FORMULÁRIO ===")

import re

def validar_formulario(dados):
    erros = {}
    
    # Validação de nome
    nome = dados.get("nome", "").strip()
    if not nome:
        erros["nome"] = "Nome é obrigatório"
    elif len(nome) < 2:
        erros["nome"] = "Nome deve ter pelo menos 2 caracteres"
    elif not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome):
        erros["nome"] = "Nome deve conter apenas letras"
    
    # Validação de email
    email = dados.get("email", "").strip()
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not email:
        erros["email"] = "Email é obrigatório"
    elif not re.match(padrao_email, email):
        erros["email"] = "Email inválido"
    
    # Validação de telefone
    telefone = dados.get("telefone", "").strip()
    padrao_telefone = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    if not telefone:
        erros["telefone"] = "Telefone é obrigatório"
    elif not re.match(padrao_telefone, telefone):
        erros["telefone"] = "Telefone deve estar no formato (11) 99999-9999"
    
    # Validação de CPF
    cpf = dados.get("cpf", "").strip()
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if not cpf:
        erros["cpf"] = "CPF é obrigatório"
    elif not re.match(padrao_cpf, cpf):
        erros["cpf"] = "CPF deve estar no formato 123.456.789-00"
    
    # Validação de senha
    senha = dados.get("senha", "")
    if not senha:
        erros["senha"] = "Senha é obrigatória"
    elif len(senha) < 8:
        erros["senha"] = "Senha deve ter pelo menos 8 caracteres"
    elif not re.search(r'[a-z]', senha):
        erros["senha"] = "Senha deve conter pelo menos uma letra minúscula"
    elif not re.search(r'[A-Z]', senha):
        erros["senha"] = "Senha deve conter pelo menos uma letra maiúscula"
    elif not re.search(r'\d', senha):
        erros["senha"] = "Senha deve conter pelo menos um número"
    
    return len(erros) == 0, erros

# Simulando dados do formulário
dados_formulario = {
    "nome": "João Silva",
    "email": "joao@email.com",
    "telefone": "(11) 99999-9999",
    "cpf": "123.456.789-00",
    "senha": "Senha123"
}

valido, erros = validar_formulario(dados_formulario)

if valido:
    print("✅ Formulário válido!")
    print("Dados aceitos:")
    for campo, valor in dados_formulario.items():
        if campo == "senha":
            print(f"  {campo}: {'*' * len(valor)}")
        else:
            print(f"  {campo}: {valor}")
else:
    print("❌ Formulário inválido!")
    print("Erros encontrados:")
    for campo, erro in erros.items():
        print(f"  {campo}: {erro}")
```

#### Exemplo 3: Gerador de Senhas

```python
# Gerador de senhas
print("=== GERADOR DE SENHAS ===")

import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, 
                incluir_numeros=True, incluir_especiais=True):
    caracteres = ""
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not caracteres:
        return "Erro: Nenhum tipo de caractere selecionado"
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def avaliar_forca_senha(senha):
    pontos = 0
    feedback = []
    
    # Comprimento
    if len(senha) >= 8:
        pontos += 1
    else:
        feedback.append("Senha muito curta")
    
    # Letras maiúsculas
    if re.search(r'[A-Z]', senha):
        pontos += 1
    else:
        feedback.append("Sem letras maiúsculas")
    
    # Letras minúsculas
    if re.search(r'[a-z]', senha):
        pontos += 1
    else:
        feedback.append("Sem letras minúsculas")
    
    # Números
    if re.search(r'\d', senha):
        pontos += 1
    else:
        feedback.append("Sem números")
    
    # Caracteres especiais
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', senha):
        pontos += 1
    else:
        feedback.append("Sem caracteres especiais")
    
    # Avaliação
    if pontos <= 2:
        classificacao = "Fraca"
    elif pontos <= 3:
        classificacao = "Média"
    elif pontos <= 4:
        classificacao = "Forte"
    else:
        classificacao = "Muito Forte"
    
    return pontos, classificacao, feedback

# Gerando senhas
print("Senhas geradas:")
for i in range(5):
    senha = gerar_senha(comprimento=12)
    pontos, classificacao, feedback = avaliar_forca_senha(senha)
    print(f"  {i+1}. {senha} - {classificacao} ({pontos}/5 pontos)")

# Senha personalizada
print("\nSenha personalizada (apenas números e letras):")
senha_personalizada = gerar_senha(comprimento=10, incluir_especiais=False)
print(f"  {senha_personalizada}")

# Avaliando senha do usuário
senha_usuario = input("\nDigite uma senha para avaliar: ")
if senha_usuario:
    pontos, classificacao, feedback = avaliar_forca_senha(senha_usuario)
    print(f"\nAvaliação da senha: {classificacao} ({pontos}/5 pontos)")
    if feedback:
        print("Sugestões de melhoria:")
        for sugestao in feedback:
            print(f"  - {sugestao}")
```

### Boas Práticas

#### ✅ Faça:
- **Use f-strings** para formatação simples e legível
- **Valide entrada** antes de processar strings
- **Use expressões regulares** para padrões complexos
- **Comente regex** - elas podem ser difíceis de entender
- **Teste casos extremos** - strings vazias, caracteres especiais

#### ❌ Evite:
- **Concatenar strings em loops** - use join()
- **Regex muito complexas** - quebre em partes menores
- **Ignorar encoding** - especifique encoding quando necessário
- **Processar strings grandes** - use geradores para arquivos grandes

#### 🔧 Solução de Problemas Comuns:

#### Erro: "UnicodeDecodeError"
- **Causa**: Problemas com encoding de caracteres
- **Solução**: Especifique encoding ao abrir arquivos

#### Regex não funciona:
- **Causa**: Caracteres especiais não escapados
- **Solução**: Use raw strings (r"") ou escape caracteres

#### Performance ruim:
- **Causa**: Operações repetitivas em strings grandes
- **Solução**: Use métodos built-in e list comprehension

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Processador de Arquivos de Texto**
   - Leia e processe arquivos de texto
   - Conte palavras, linhas, caracteres
   - Encontre palavras mais frequentes
   - Gere relatórios de análise

2. **Validador de Dados Pessoais**
   - Valide CPF, CNPJ, telefone, email
   - Implemente validação de endereço
   - Crie sistema de feedback detalhado
   - Teste com dados reais

3. **Formatador de Documentos**
   - Formate textos automaticamente
   - Aplique regras de capitalização
   - Corrija espaçamento e pontuação
   - Gere documentos padronizados

4. **Sistema de Busca de Texto**
   - Implemente busca por palavras-chave
   - Destaque resultados encontrados
   - Calcule relevância de resultados
   - Suporte a busca case-insensitive

5. **Gerador de Relatórios**
   - Crie relatórios formatados
   - Use templates de texto
   - Substitua placeholders dinamicamente
   - Gere relatórios em diferentes formatos

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Funções** - como organizar e reutilizar código.

### O que você vai aprender:
- 📚 Definição e criação de funções
- 📚 Parâmetros e argumentos
- 📚 Retorno de valores
- 📚 Escopo de variáveis
- 📚 Funções anônimas (lambda)
- 📚 Decoradores básicos

---

**Pratique strings avançadas! São fundamentais para processamento de dados! 🐍**

> 💡 **Dica**: Crie um arquivo de texto com dados reais e pratique as técnicas aprendidas. Isso vai ajudar a entender como aplicar as ferramentas em situações práticas.
