# ========================================
# AULA 1: INTRODUÇÃO AO PYTHON
# EXERCÍCIOS PRÁTICOS
# ========================================

print("=" * 50)
print("AULA 1: INTRODUÇÃO AO PYTHON")
print("=" * 50)

# ========================================
# EXERCÍCIO 1: HELLO WORLD PERSONALIZADO
# ========================================

print("\n--- EXERCÍCIO 1: HELLO WORLD PERSONALIZADO ---")

# TODO: Substitua "Seu Nome" pelo seu nome real
nome = "Seu Nome"
print(f"Olá, {nome}! Bem-vindo ao Python!")

# ========================================
# EXERCÍCIO 2: INFORMAÇÕES PESSOAIS
# ========================================

print("\n--- EXERCÍCIO 2: INFORMAÇÕES PESSOAIS ---")

# TODO: Preencha suas informações pessoais
nome = "Seu Nome"
idade = 25  # Substitua pela sua idade
cidade = "Sua Cidade"  # Substitua pela sua cidade
profissao = "Sua Profissão"  # Substitua pela sua profissão

# Imprimindo as informações
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")
print(f"Profissão: {profissao}")

# Criando uma frase completa
print(f"\nOlá! Sou {nome}, tenho {idade} anos, moro em {cidade} e trabalho como {profissao}.")

# ========================================
# EXERCÍCIO 3: CALCULADORA SIMPLES
# ========================================

print("\n--- EXERCÍCIO 3: CALCULADORA SIMPLES ---")

# Definindo dois números
numero1 = 10
numero2 = 5

# Realizando as operações
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Exibindo os resultados
print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"Soma: {numero1} + {numero2} = {soma}")
print(f"Subtração: {numero1} - {numero2} = {subtracao}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"Divisão: {numero1} / {numero2} = {divisao}")

# ========================================
# EXERCÍCIO 4: COMENTÁRIOS E DOCUMENTAÇÃO
# ========================================

print("\n--- EXERCÍCIO 4: COMENTÁRIOS E DOCUMENTAÇÃO ---")

# Este é um comentário de uma linha

"""
Este é um comentário de múltiplas linhas.
Podemos escrever várias linhas de documentação.
Muito útil para explicar código complexo.
"""

# Variáveis com comentários explicativos
preco = 29.99  # Preço do produto em reais
quantidade = 3  # Quantidade de itens
desconto = 0.1  # 10% de desconto

# Calculando o total com desconto
total_sem_desconto = preco * quantidade
valor_desconto = total_sem_desconto * desconto
total_com_desconto = total_sem_desconto - valor_desconto

print(f"Preço unitário: R$ {preco}")
print(f"Quantidade: {quantidade}")
print(f"Total sem desconto: R$ {total_sem_desconto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Total com desconto: R$ {total_com_desconto:.2f}")

# ========================================
# DESAFIO EXTRA: CALCULADORA DE IMC
# ========================================

print("\n--- DESAFIO EXTRA: CALCULADORA DE IMC ---")

# TODO: Substitua pelos seus dados reais
peso = 70.5  # Peso em kg
altura = 1.75  # Altura em metros

# Calculando o IMC
imc = peso / (altura ** 2)

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
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
# CONCLUSÃO DA AULA
# ========================================

print("\n" + "=" * 50)
print("PARABÉNS! Você completou a Aula 1!")
print("=" * 50)
print("\nO que você aprendeu:")
print("✅ Como criar seu primeiro programa Python")
print("✅ Como usar a função print()")
print("✅ Como criar variáveis")
print("✅ Como fazer comentários")
print("✅ Como fazer operações matemáticas básicas")
print("✅ Como usar f-strings para formatação")

print("\nNa próxima aula, vamos aprender sobre:")
print("📚 Variáveis e Tipos de Dados")
print("📚 Números inteiros e decimais")
print("📚 Strings e booleanos")
print("📚 Conversão de tipos")

print("\nContinue praticando e bons estudos! 🐍") 