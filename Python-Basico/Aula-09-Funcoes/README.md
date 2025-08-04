# Aula 9: Funções

## 🎯 Objetivos da Aula

- Entender o que são funções e por que usá-las
- Dominar a criação e definição de funções em Python
- Aprender sobre parâmetros e argumentos (posicionais, nomeados, padrão)
- Compreender o retorno de valores e múltiplos retornos
- Praticar o escopo de variáveis (local, global, nonlocal)
- Trabalhar com funções lambda e funções anônimas
- Implementar funções em cenários práticos e reais

## 📚 Conteúdo Detalhado

### O que são Funções?

Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas permitem organizar o código, evitar repetição e criar programas mais modulares e legíveis.

#### Por que usar funções?
- **Reutilização de código**: Evitar repetir o mesmo código
- **Organização**: Dividir problemas complexos em partes menores
- **Manutenção**: Facilita a correção e atualização de código
- **Testabilidade**: Funções isoladas são mais fáceis de testar
- **Legibilidade**: Código mais limpo e compreensível
- **Modularidade**: Criar componentes independentes

### Criando Funções

#### Sintaxe Básica:
```python
def nome_da_funcao():
    # código da função
    print("Executando a função!")
```

#### Exemplo Simples:
```python
def saudacao():
    print("Olá! Bem-vindo ao Python!")
    print("Esta é uma função simples.")

# Chamando a função
saudacao()
```

#### Função com Parâmetros:
```python
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo ao Python!")

# Chamando com argumento
saudacao_personalizada("João")
saudacao_personalizada("Maria")
```

### Parâmetros e Argumentos

#### Parâmetros Posicionais:
```python
def calcular_area(base, altura):
    area = base * altura
    return area

# Chamando com argumentos posicionais
area_retangulo = calcular_area(10, 5)
print(f"Área do retângulo: {area_retangulo}")
```

#### Parâmetros Nomeados:
```python
def calcular_area(base, altura):
    area = base * altura
    return area

# Chamando com argumentos nomeados
area = calcular_area(base=10, altura=5)
print(f"Área: {area}")

# Ordem pode ser diferente com argumentos nomeados
area2 = calcular_area(altura=5, base=10)
print(f"Área 2: {area2}")
```

#### Parâmetros com Valores Padrão:
```python
def saudacao(nome="Visitante", hora="dia"):
    if hora == "manhã":
        cumprimento = "Bom dia"
    elif hora == "tarde":
        cumprimento = "Boa tarde"
    elif hora == "noite":
        cumprimento = "Boa noite"
    else:
        cumprimento = "Olá"
    
    print(f"{cumprimento}, {nome}!")

# Chamando com valores padrão
saudacao()  # "Olá, Visitante!"

# Chamando com alguns argumentos
saudacao("João")  # "Olá, João!"
saudacao("Maria", "tarde")  # "Boa tarde, Maria!"
```

#### Múltiplos Parâmetros:
```python
def calcular_media(nota1, nota2, nota3, nota4=0):
    total = nota1 + nota2 + nota3 + nota4
    quantidade = 4 if nota4 > 0 else 3
    media = total / quantidade
    return media

# Chamando com 3 notas
media1 = calcular_media(8.5, 7.8, 9.2)
print(f"Média com 3 notas: {media1:.2f}")

# Chamando com 4 notas
media2 = calcular_media(8.5, 7.8, 9.2, 8.0)
print(f"Média com 4 notas: {media2:.2f}")
```

### Retorno de Valores

#### Retorno Simples:
```python
def quadrado(numero):
    resultado = numero ** 2
    return resultado

# Usando o valor retornado
valor = quadrado(5)
print(f"Quadrado de 5: {valor}")

# Usando diretamente em expressões
soma_quadrados = quadrado(3) + quadrado(4)
print(f"Soma dos quadrados: {soma_quadrados}")
```

#### Múltiplos Retornos:
```python
def calcular_estatisticas(numeros):
    if not numeros:
        return 0, 0, 0
    
    soma = sum(numeros)
    media = soma / len(numeros)
    maximo = max(numeros)
    
    return soma, media, maximo

# Usando múltiplos retornos
valores = [10, 20, 30, 40, 50]
soma, media, maximo = calcular_estatisticas(valores)

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Máximo: {maximo}")
```

#### Retorno Condicional:
```python
def verificar_idade(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

# Testando a função
idades = [5, 15, 25, 70, -5]
for idade in idades:
    categoria = verificar_idade(idade)
    print(f"Idade {idade}: {categoria}")
```

### Tipos de Parâmetros

#### Parâmetros Arbitrários (*args):
```python
def somar_todos(*numeros):
    return sum(numeros)

# Chamando com diferentes quantidades de argumentos
resultado1 = somar_todos(1, 2, 3)
print(f"Soma de 3 números: {resultado1}")

resultado2 = somar_todos(1, 2, 3, 4, 5)
print(f"Soma de 5 números: {resultado2}")

resultado3 = somar_todos()
print(f"Soma de 0 números: {resultado3}")
```

#### Parâmetros de Palavras-chave (**kwargs):
```python
def criar_perfil(**dados):
    perfil = {}
    for chave, valor in dados.items():
        perfil[chave] = valor
    return perfil

# Criando perfis com diferentes dados
perfil1 = criar_perfil(nome="João", idade=25, cidade="São Paulo")
print(f"Perfil 1: {perfil1}")

perfil2 = criar_perfil(nome="Maria", profissao="Engenheira", salario=5000)
print(f"Perfil 2: {perfil2}")
```

#### Combinação de Tipos de Parâmetros:
```python
def processar_dados(nome, idade, *hobbies, **informacoes_adicionais):
    resultado = {
        "nome": nome,
        "idade": idade,
        "hobbies": list(hobbies),
        "informacoes_adicionais": informacoes_adicionais
    }
    return resultado

# Usando a função
dados = processar_dados(
    "João", 
    25, 
    "futebol", 
    "música", 
    "leitura",
    cidade="São Paulo",
    profissao="Desenvolvedor"
)

print("Dados processados:")
for chave, valor in dados.items():
    print(f"  {chave}: {valor}")
```

### Escopo de Variáveis

#### Variáveis Locais:
```python
def calcular_area(base, altura):
    area = base * altura  # Variável local
    print(f"Área calculada: {area}")
    return area

# A variável 'area' só existe dentro da função
resultado = calcular_area(10, 5)
# print(area)  # Erro! 'area' não existe aqui
```

#### Variáveis Globais:
```python
contador = 0  # Variável global

def incrementar():
    global contador  # Declarando que vamos usar a variável global
    contador += 1
    print(f"Contador: {contador}")

def zerar():
    global contador
    contador = 0
    print("Contador zerado!")

# Testando
incrementar()  # Contador: 1
incrementar()  # Contador: 2
zerar()        # Contador zerado!
incrementar()  # Contador: 1
```

#### Variáveis Nonlocal:
```python
def funcao_externa():
    x = 10  # Variável da função externa
    
    def funcao_interna():
        nonlocal x  # Usando variável da função externa
        x = 20
        print(f"Valor de x na função interna: {x}")
    
    print(f"Valor de x antes: {x}")
    funcao_interna()
    print(f"Valor de x depois: {x}")

funcao_externa()
```

### Funções Lambda (Anônimas)

#### Sintaxe Básica:
```python
# Função normal
def quadrado(x):
    return x ** 2

# Função lambda equivalente
quadrado_lambda = lambda x: x ** 2

# Testando
print(f"Quadrado normal: {quadrado(5)}")
print(f"Quadrado lambda: {quadrado_lambda(5)}")
```

#### Usando Lambda com Funções Built-in:
```python
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Elevar ao quadrado
quadrados = list(map(lambda x: x ** 2, numeros))
print(f"Quadrados: {quadrados}")

# Ordenar por critério personalizado
pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 20}
]

# Ordenar por idade
ordenadas_idade = sorted(pessoas, key=lambda p: p["idade"])
print("Ordenadas por idade:")
for pessoa in ordenadas_idade:
    print(f"  {pessoa['nome']}: {pessoa['idade']} anos")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Calculadora Avançada

```python
# Calculadora com funções
print("=== CALCULADORA AVANÇADA ===")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero < 0:
        return "Erro: Número negativo!"
    return numero ** 0.5

def calcular_media(*numeros):
    if not numeros:
        return "Erro: Nenhum número fornecido!"
    return sum(numeros) / len(numeros)

# Menu de operações
operacoes = {
    "1": ("Soma", somar),
    "2": ("Subtração", subtrair),
    "3": ("Multiplicação", multiplicar),
    "4": ("Divisão", dividir),
    "5": ("Potência", potencia),
    "6": ("Raiz Quadrada", raiz_quadrada),
    "7": ("Média", calcular_media)
}

while True:
    print("\nEscolha uma operação:")
    for opcao, (nome, _) in operacoes.items():
        print(f"{opcao}. {nome}")
    print("0. Sair")
    
    escolha = input("\nDigite sua opção: ")
    
    if escolha == "0":
        print("👋 Obrigado por usar a calculadora!")
        break
    
    if escolha in operacoes:
        nome, funcao = operacoes[escolha]
        print(f"\n=== {nome.upper()} ===")
        
        if escolha == "6":  # Raiz quadrada
            try:
                numero = float(input("Digite o número: "))
                resultado = funcao(numero)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("❌ Digite um número válido!")
                
        elif escolha == "7":  # Média
            try:
                entrada = input("Digite os números separados por vírgula: ")
                numeros = [float(x.strip()) for x in entrada.split(",")]
                resultado = funcao(*numeros)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("❌ Digite números válidos!")
                
        else:  # Operações com dois números
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = funcao(num1, num2)
                print(f"Resultado: {resultado}")
            except ValueError:
                print("❌ Digite números válidos!")
    else:
        print("❌ Opção inválida!")
```

#### Exemplo 2: Sistema de Validação

```python
# Sistema de validação com funções
print("=== SISTEMA DE VALIDAÇÃO ===")

def validar_email(email):
    import re
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(padrao, email))

def validar_senha(senha):
    if len(senha) < 8:
        return False, "Senha deve ter pelo menos 8 caracteres"
    
    if not any(c.isupper() for c in senha):
        return False, "Senha deve conter pelo menos uma letra maiúscula"
    
    if not any(c.islower() for c in senha):
        return False, "Senha deve conter pelo menos uma letra minúscula"
    
    if not any(c.isdigit() for c in senha):
        return False, "Senha deve conter pelo menos um número"
    
    return True, "Senha válida"

def validar_idade(idade):
    try:
        idade_int = int(idade)
        if 0 <= idade_int <= 120:
            return True, "Idade válida"
        else:
            return False, "Idade deve estar entre 0 e 120"
    except ValueError:
        return False, "Idade deve ser um número"

def validar_telefone(telefone):
    import re
    padrao = r'^\(\d{2}\) \d{4,5}-\d{4}$'
    return bool(re.match(padrao, telefone))

def validar_formulario(dados):
    erros = {}
    
    # Validar nome
    nome = dados.get("nome", "").strip()
    if not nome:
        erros["nome"] = "Nome é obrigatório"
    elif len(nome) < 2:
        erros["nome"] = "Nome deve ter pelo menos 2 caracteres"
    
    # Validar email
    email = dados.get("email", "").strip()
    if not validar_email(email):
        erros["email"] = "Email inválido"
    
    # Validar senha
    senha = dados.get("senha", "")
    senha_valida, msg_senha = validar_senha(senha)
    if not senha_valida:
        erros["senha"] = msg_senha
    
    # Validar idade
    idade = dados.get("idade", "")
    idade_valida, msg_idade = validar_idade(idade)
    if not idade_valida:
        erros["idade"] = msg_idade
    
    # Validar telefone
    telefone = dados.get("telefone", "").strip()
    if telefone and not validar_telefone(telefone):
        erros["telefone"] = "Telefone deve estar no formato (11) 99999-9999"
    
    return len(erros) == 0, erros

# Testando o sistema
dados_teste = {
    "nome": "João Silva",
    "email": "joao@email.com",
    "senha": "Senha123",
    "idade": "25",
    "telefone": "(11) 99999-9999"
}

valido, erros = validar_formulario(dados_teste)

if valido:
    print("✅ Formulário válido!")
    print("Dados aceitos:")
    for campo, valor in dados_teste.items():
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

#### Exemplo 3: Processador de Dados

```python
# Processador de dados com funções
print("=== PROCESSADOR DE DADOS ===")

def processar_numeros(numeros):
    """Processa uma lista de números e retorna estatísticas"""
    if not numeros:
        return None
    
    return {
        "quantidade": len(numeros),
        "soma": sum(numeros),
        "media": sum(numeros) / len(numeros),
        "maximo": max(numeros),
        "minimo": min(numeros),
        "pares": len([x for x in numeros if x % 2 == 0]),
        "impares": len([x for x in numeros if x % 2 != 0])
    }

def processar_texto(texto):
    """Processa um texto e retorna estatísticas"""
    palavras = texto.split()
    caracteres = len(texto)
    caracteres_sem_espaco = len(texto.replace(" ", ""))
    
    # Contagem de palavras
    contador = {}
    for palavra in palavras:
        palavra_limpa = palavra.lower().strip(".,!?;:")
        if palavra_limpa:
            contador[palavra_limpa] = contador.get(palavra_limpa, 0) + 1
    
    # Palavras mais frequentes
    palavras_frequentes = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:5]
    
    return {
        "palavras": len(palavras),
        "caracteres": caracteres,
        "caracteres_sem_espaco": caracteres_sem_espaco,
        "palavra_mais_longa": max(palavras, key=len) if palavras else "",
        "palavra_mais_curta": min(palavras, key=len) if palavras else "",
        "palavras_frequentes": palavras_frequentes
    }

def processar_lista_pessoas(pessoas):
    """Processa uma lista de pessoas e retorna estatísticas"""
    if not pessoas:
        return None
    
    idades = [p["idade"] for p in pessoas]
    cidades = [p["cidade"] for p in pessoas]
    
    # Estatísticas por cidade
    contador_cidades = {}
    for cidade in cidades:
        contador_cidades[cidade] = contador_cidades.get(cidade, 0) + 1
    
    return {
        "total_pessoas": len(pessoas),
        "idade_media": sum(idades) / len(idades),
        "idade_maxima": max(idades),
        "idade_minima": min(idades),
        "cidades_unicas": len(set(cidades)),
        "pessoas_por_cidade": contador_cidades
    }

# Testando o processador
print("=== TESTE COM NÚMEROS ===")
numeros_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats_numeros = processar_numeros(numeros_teste)
if stats_numeros:
    print("Estatísticas dos números:")
    for chave, valor in stats_numeros.items():
        print(f"  {chave}: {valor}")

print("\n=== TESTE COM TEXTO ===")
texto_teste = "Python é uma linguagem de programação incrível. Python é muito popular!"
stats_texto = processar_texto(texto_teste)
print("Estatísticas do texto:")
for chave, valor in stats_texto.items():
    if chave == "palavras_frequentes":
        print(f"  {chave}:")
        for palavra, freq in valor:
            print(f"    '{palavra}': {freq} vezes")
    else:
        print(f"  {chave}: {valor}")

print("\n=== TESTE COM PESSOAS ===")
pessoas_teste = [
    {"nome": "João", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", "idade": 22, "cidade": "São Paulo"},
    {"nome": "Ana", "idade": 28, "cidade": "Belo Horizonte"}
]
stats_pessoas = processar_lista_pessoas(pessoas_teste)
if stats_pessoas:
    print("Estatísticas das pessoas:")
    for chave, valor in stats_pessoas.items():
        if chave == "pessoas_por_cidade":
            print(f"  {chave}:")
            for cidade, quantidade in valor.items():
                print(f"    {cidade}: {quantidade} pessoas")
        else:
            print(f"  {chave}: {valor}")
```

### Boas Práticas

#### ✅ Faça:
- **Use nomes descritivos** para funções e parâmetros
- **Documente funções** com docstrings
- **Mantenha funções pequenas** - uma função, uma responsabilidade
- **Use valores padrão** para parâmetros opcionais
- **Teste funções** com diferentes entradas

#### ❌ Evite:
- **Funções muito longas** - quebre em funções menores
- **Efeitos colaterais** - funções devem ser previsíveis
- **Parâmetros globais** - passe dados como parâmetros
- **Nomes genéricos** - use nomes que expliquem a função

#### 🔧 Solução de Problemas Comuns:

#### Erro: "NameError: name 'x' is not defined"
- **Causa**: Tentando usar variável fora do escopo
- **Solução**: Passe dados como parâmetros ou use global/nonlocal

#### Erro: "TypeError: missing required positional argument"
- **Causa**: Chamando função sem argumentos obrigatórios
- **Solução**: Forneça todos os argumentos necessários

#### Função não retorna valor esperado:
- **Causa**: Lógica incorreta ou falta de return
- **Solução**: Verifique a lógica e adicione return quando necessário

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora Científica**
   - Implemente funções para operações matemáticas
   - Use funções lambda para operações simples
   - Crie menu interativo
   - Valide entradas de dados

2. **Sistema de Gerenciamento de Biblioteca**
   - Funções para adicionar, remover, buscar livros
   - Funções para gerenciar usuários
   - Funções para controle de empréstimos
   - Relatórios com funções de agregação

3. **Processador de Arquivos**
   - Funções para ler e escrever arquivos
   - Funções para processar diferentes formatos
   - Funções para validação de dados
   - Funções para geração de relatórios

4. **Sistema de Autenticação**
   - Funções para validação de credenciais
   - Funções para criptografia básica
   - Funções para gerenciamento de sessões
   - Funções para controle de permissões

5. **Gerador de Relatórios**
   - Funções para formatar dados
   - Funções para cálculos estatísticos
   - Funções para geração de gráficos
   - Funções para exportação de dados

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Módulos e Bibliotecas** - como organizar e reutilizar código em arquivos separados.

### O que você vai aprender:
- 📚 Criação e uso de módulos
- 📚 Importação de módulos
- 📚 Biblioteca padrão do Python
- 📚 Instalação de bibliotecas externas
- 📚 Organização de projetos
- 📚 Boas práticas de modularização

---

**Pratique funções! São fundamentais para organizar código! 🐍**

> 💡 **Dica**: Comece criando funções simples e vá aumentando a complexidade gradualmente. Isso vai ajudar a entender como as funções se relacionam e como organizar melhor seu código.
