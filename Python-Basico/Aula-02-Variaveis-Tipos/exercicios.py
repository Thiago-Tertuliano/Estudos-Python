# ========================================
# AULA 2: VARIÁVEIS E TIPOS DE DADOS
# EXERCÍCIOS PRÁTICOS
# ========================================

print("=" * 50)
print("AULA 2: VARIÁVEIS E TIPOS DE DADOS")
print("=" * 50)

# ========================================
# EXERCÍCIO 1: VERIFICANDO TIPOS DE DADOS
# ========================================

print("\n--- EXERCÍCIO 1: VERIFICANDO TIPOS DE DADOS ---")

# Criando variáveis de diferentes tipos
nome = "Maria"
idade = 25
altura = 1.65
ativo = True
salario = 2500.50
valor = None

# Verificando os tipos
print(f"nome: {nome} - Tipo: {type(nome)}")
print(f"idade: {idade} - Tipo: {type(idade)}")
print(f"altura: {altura} - Tipo: {type(altura)}")
print(f"ativo: {ativo} - Tipo: {type(ativo)}")
print(f"salario: {salario} - Tipo: {type(salario)}")
print(f"valor: {valor} - Tipo: {type(valor)}")

# ========================================
# EXERCÍCIO 2: CONVERSÃO DE TIPOS
# ========================================

print("\n--- EXERCÍCIO 2: CONVERSÃO DE TIPOS ---")

# String para número
numero_string = "42"
numero_inteiro = int(numero_string)
numero_float = float(numero_string)

print(f"String original: '{numero_string}'")
print(f"Convertido para int: {numero_inteiro}")
print(f"Convertido para float: {numero_float}")

# Float para int (trunca a parte decimal)
preco = 29.99
preco_inteiro = int(preco)
print(f"Preço original: {preco}")
print(f"Preço como inteiro: {preco_inteiro}")

# Número para string
idade = 25
idade_string = str(idade)
print(f"Idade como número: {idade}")
print(f"Idade como string: '{idade_string}'")

# Conversão para boolean
print(f"\nConversões para boolean:")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('texto'): {bool('texto')}")
print(f"bool(''): {bool('')}")
print(f"bool(None): {bool(None)}")

# ========================================
# EXERCÍCIO 3: CALCULADORA DE MÉDIA
# ========================================

print("\n--- EXERCÍCIO 3: CALCULADORA DE MÉDIA ---")

# Definindo as notas
nota1 = 8.5
nota2 = 7.8
nota3 = 9.2

# Calculando a média
soma_notas = nota1 + nota2 + nota3
media = soma_notas / 3

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Soma das notas: {soma_notas}")
print(f"Média: {media:.2f}")

# Verificando se foi aprovado (média >= 7.0)
aprovado = media >= 7.0
print(f"Aprovado: {aprovado}")

# ========================================
# EXERCÍCIO 4: CONVERSOR DE TEMPERATURA
# ========================================

print("\n--- EXERCÍCIO 4: CONVERSOR DE TEMPERATURA ---")

# Temperatura em Celsius
celsius = 25.0

# Convertendo para Fahrenheit
fahrenheit = celsius * 9/5 + 32

print(f"Temperatura em Celsius: {celsius}°C")
print(f"Temperatura em Fahrenheit: {fahrenheit}°F")

# Convertendo de volta para Celsius
celsius_calculado = (fahrenheit - 32) * 5/9
print(f"Verificação - Celsius calculado: {celsius_calculado}°C")

# ========================================
# EXERCÍCIO 5: CALCULADORA DE ÁREA
# ========================================

print("\n--- EXERCÍCIO 5: CALCULADORA DE ÁREA ---")

# Área do retângulo
base = 10
altura_retangulo = 5
area_retangulo = base * altura_retangulo

print(f"Retângulo:")
print(f"Base: {base}")
print(f"Altura: {altura_retangulo}")
print(f"Área: {area_retangulo}")

# Área do círculo
raio = 5
pi = 3.14159
area_circulo = pi * raio ** 2

print(f"\nCírculo:")
print(f"Raio: {raio}")
print(f"Área: {area_circulo:.2f}")

# ========================================
# EXERCÍCIO 6: MANIPULAÇÃO DE STRINGS
# ========================================

print("\n--- EXERCÍCIO 6: MANIPULAÇÃO DE STRINGS ---")

# Strings básicas
nome = "João"
sobrenome = "Silva"
idade = 25

# Concatenação
nome_completo = nome + " " + sobrenome
print(f"Nome completo: {nome_completo}")

# F-string
apresentacao = f"Olá, sou {nome_completo} e tenho {idade} anos."
print(f"Apresentação: {apresentacao}")

# Repetindo strings
separador = "=" * 30
print(f"Separador: {separador}")

# Métodos de string
texto = "  Python é incrível!  "
print(f"Texto original: '{texto}'")
print(f"Texto em maiúsculo: '{texto.upper()}'")
print(f"Texto em minúsculo: '{texto.lower()}'")
print(f"Texto sem espaços: '{texto.strip()}'")
print(f"Quantidade de caracteres: {len(texto)}")

# ========================================
# EXERCÍCIO 7: INPUT DO USUÁRIO
# ========================================

print("\n--- EXERCÍCIO 7: INPUT DO USUÁRIO ---")

# Simulando input do usuário (comentado para não interromper o programa)
# nome_usuario = input("Digite seu nome: ")
# idade_usuario = input("Digite sua idade: ")
# altura_usuario = input("Digite sua altura (em metros): ")

# Simulando com valores fixos
nome_usuario = "Ana"
idade_usuario = "28"
altura_usuario = "1.70"

# Convertendo tipos
idade_usuario_int = int(idade_usuario)
altura_usuario_float = float(altura_usuario)

print(f"Nome: {nome_usuario}")
print(f"Idade: {idade_usuario_int} anos")
print(f"Altura: {altura_usuario_float}m")

# Criando uma frase completa
frase_completa = f"Olá {nome_usuario}! Você tem {idade_usuario_int} anos e {altura_usuario_float}m de altura."
print(f"Frase completa: {frase_completa}")

# ========================================
# EXERCÍCIO 8: CALCULADORA DE IMC
# ========================================

print("\n--- EXERCÍCIO 8: CALCULADORA DE IMC ---")

# Dados da pessoa
peso = 70.5  # kg
altura_imc = 1.75  # metros

# Calculando IMC
imc = peso / (altura_imc ** 2)

print(f"Peso: {peso} kg")
print(f"Altura: {altura_imc} m")
print(f"IMC: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Classificação: {classificacao}")

# ========================================
# DESAFIO EXTRA: CALCULADORA FINANCEIRA
# ========================================

print("\n--- DESAFIO EXTRA: CALCULADORA FINANCEIRA ---")

# Dados do investimento
capital_inicial = 1000.0
taxa_juros = 0.05  # 5% ao mês
tempo_meses = 12

# Calculando juros compostos
montante = capital_inicial * (1 + taxa_juros) ** tempo_meses
juros_ganhos = montante - capital_inicial

print(f"Capital inicial: R$ {capital_inicial:.2f}")
print(f"Taxa de juros: {taxa_juros * 100}% ao mês")
print(f"Tempo: {tempo_meses} meses")
print(f"Montante final: R$ {montante:.2f}")
print(f"Juros ganhos: R$ {juros_ganhos:.2f}")

# ========================================
# CONCLUSÃO DA AULA
# ========================================

print("\n" + "=" * 50)
print("PARABÉNS! Você completou a Aula 2!")
print("=" * 50)
print("\nO que você aprendeu:")
print("✅ Como criar e usar variáveis")
print("✅ Os tipos de dados básicos do Python")
print("✅ Como converter entre diferentes tipos")
print("✅ Como fazer operações com strings")
print("✅ Como usar input() e converter tipos")
print("✅ Como formatar strings com f-strings")

print("\nNa próxima aula, vamos aprender sobre:")
print("📚 Operadores aritméticos")
print("📚 Operadores de comparação")
print("📚 Operadores lógicos")
print("📚 Precedência de operadores")

print("\nContinue praticando e bons estudos! 🐍") 