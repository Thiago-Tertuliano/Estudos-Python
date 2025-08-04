# Aula 4: Estruturas de Controle

## 🎯 Objetivos da Aula

- Entender como tomar decisões no código usando estruturas condicionais
- Dominar o uso de if, elif e else em diferentes cenários
- Aprender a usar o operador ternário para decisões simples
- Compreender estruturas aninhadas e como organizá-las
- Praticar a criação de fluxos de decisão complexos e eficientes

## 📚 Conteúdo Detalhado

### O que são Estruturas de Controle?

Estruturas de controle permitem que o programa tome decisões e execute diferentes blocos de código baseado em condições. Elas são fundamentais para criar programas inteligentes que respondem a diferentes situações.

#### Por que usar estruturas de controle?
- **Tomar decisões**: Executar código diferente baseado em condições
- **Validar dados**: Verificar se entradas são válidas
- **Criar fluxos**: Organizar a lógica do programa
- **Evitar erros**: Tratar situações excepcionais
- **Melhorar UX**: Dar feedback apropriado ao usuário

### Estrutura Condicional Básica (if)

A estrutura `if` executa um bloco de código apenas se uma condição for verdadeira.

#### Sintaxe Básica:
```python
if condicao:
    # código a ser executado se a condição for True
    print("Condição é verdadeira!")
```

#### Exemplo Simples:
```python
idade = 18

if idade >= 18:
    print("Você é maior de idade!")
    print("Pode dirigir e votar.")
```

#### Características Importantes:
- A condição deve retornar True ou False
- O bloco de código deve estar indentado (4 espaços)
- Pode conter qualquer quantidade de código
- A indentação define o que pertence ao bloco

### Estrutura if-else

A estrutura `if-else` permite executar um bloco quando a condição é verdadeira e outro quando é falsa.

#### Sintaxe:
```python
if condicao:
    # código se condição for True
    print("Condição verdadeira!")
else:
    # código se condição for False
    print("Condição falsa!")
```

#### Exemplo Prático:
```python
idade = 16

if idade >= 18:
    print("Você é maior de idade!")
    print("Pode dirigir e votar.")
else:
    print("Você é menor de idade!")
    print("Ainda não pode dirigir.")
    anos_restantes = 18 - idade
    print(f"Faltam {anos_restantes} anos para ser maior de idade.")
```

### Estrutura if-elif-else

A estrutura `if-elif-else` permite testar múltiplas condições em sequência.

#### Sintaxe:
```python
if condicao1:
    # código se condicao1 for True
    print("Condição 1 é verdadeira!")
elif condicao2:
    # código se condicao2 for True (e condicao1 for False)
    print("Condição 2 é verdadeira!")
elif condicao3:
    # código se condicao3 for True (e anteriores forem False)
    print("Condição 3 é verdadeira!")
else:
    # código se nenhuma condição for True
    print("Nenhuma condição é verdadeira!")
```

#### Exemplo com Notas:
```python
nota = 8.5

if nota >= 9.0:
    print("Excelente! Conceito A")
elif nota >= 7.0:
    print("Bom! Conceito B")
elif nota >= 5.0:
    print("Regular! Conceito C")
elif nota >= 3.0:
    print("Insuficiente! Conceito D")
else:
    print("Muito insuficiente! Conceito F")
```

#### Exemplo com Idade:
```python
idade = 25

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 30:
    print("Jovem adulto")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```

### Operador Ternário

O operador ternário permite escrever estruturas condicionais simples em uma linha.

#### Sintaxe:
```python
resultado = valor_se_verdadeiro if condicao else valor_se_falso
```

#### Exemplos:
```python
# Exemplo básico
idade = 18
status = "maior de idade" if idade >= 18 else "menor de idade"
print(f"Status: {status}")

# Exemplo com números
numero = 10
resultado = "par" if numero % 2 == 0 else "ímpar"
print(f"O número {numero} é {resultado}")

# Exemplo com strings
nome = "João"
saudacao = f"Olá, {nome}!" if nome else "Olá, visitante!"
print(saudacao)

# Exemplo com cálculos
preco = 100
desconto = preco * 0.1 if preco >= 50 else 0
preco_final = preco - desconto
print(f"Preço final: R$ {preco_final:.2f}")
```

### Estruturas Aninhadas

Estruturas aninhadas são estruturas condicionais dentro de outras estruturas condicionais.

#### Sintaxe:
```python
if condicao1:
    if condicao2:
        # código se ambas condições forem True
        print("Ambas condições são verdadeiras!")
    else:
        # código se condicao1 for True mas condicao2 for False
        print("Apenas condição 1 é verdadeira!")
else:
    if condicao3:
        # código se condicao1 for False mas condicao3 for True
        print("Apenas condição 3 é verdadeira!")
    else:
        # código se nenhuma condição for True
        print("Nenhuma condição é verdadeira!")
```

#### Exemplo Prático - Sistema de Login:
```python
usuario = "admin"
senha = "123456"
tentativas = 2

if usuario == "admin":
    if senha == "123456":
        print("Login realizado com sucesso!")
        print("Bem-vindo ao sistema!")
    else:
        print("Senha incorreta!")
        if tentativas > 0:
            print(f"Você ainda tem {tentativas} tentativas.")
        else:
            print("Conta bloqueada!")
else:
    print("Usuário não encontrado!")
```

#### Exemplo - Verificação de Elegibilidade:
```python
idade = 25
tem_carteira = True
tem_carro = False
tem_dinheiro = True

if idade >= 18:
    if tem_carteira:
        if tem_carro:
            print("Pode sair dirigindo!")
        elif tem_dinheiro:
            print("Pode sair de táxi ou ônibus!")
        else:
            print("Pode sair, mas não tem transporte!")
    else:
        print("Precisa de carteira para dirigir!")
else:
    print("Precisa ser maior de idade!")
```

### Operadores de Comparação em Condições

#### Operadores Básicos:
```python
# Igualdade
if x == y:
    print("x é igual a y")

# Desigualdade
if x != y:
    print("x é diferente de y")

# Maior que
if x > y:
    print("x é maior que y")

# Menor que
if x < y:
    print("x é menor que y")

# Maior ou igual
if x >= y:
    print("x é maior ou igual a y")

# Menor ou igual
if x <= y:
    print("x é menor ou igual a y")
```

#### Operadores Lógicos:
```python
# AND - ambas condições devem ser True
if idade >= 18 and tem_carteira:
    print("Pode dirigir!")

# OR - pelo menos uma condição deve ser True
if tem_dinheiro or tem_cartao:
    print("Pode comprar!")

# NOT - inverte a condição
if not tem_senha:
    print("Acesso livre!")

# Combinações
if (idade >= 18 and tem_carteira) or (idade >= 16 and tem_autorizacao):
    print("Pode entrar!")
```

### Validação de Dados

#### Validação Básica:
```python
# Verificar se número é positivo
numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo!")
elif numero < 0:
    print("Número negativo!")
else:
    print("Número zero!")
```

#### Validação de String:
```python
nome = input("Digite seu nome: ")

if nome.strip():  # Verifica se não está vazio após remover espaços
    print(f"Olá, {nome}!")
else:
    print("Nome não pode estar vazio!")
```

#### Validação de Faixas:
```python
nota = float(input("Digite sua nota (0-10): "))

if 0 <= nota <= 10:
    if nota >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")
else:
    print("Nota deve estar entre 0 e 10!")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Calculadora de IMC com Classificação

```python
# Calculadora de IMC
print("=== CALCULADORA DE IMC ===")

try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        
        print(f"\nSeu IMC: {imc:.2f}")
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            recomendacao = "Considere ganhar peso de forma saudável."
        elif imc < 25:
            classificacao = "Peso normal"
            recomendacao = "Mantenha seus hábitos saudáveis!"
        elif imc < 30:
            classificacao = "Sobrepeso"
            recomendacao = "Considere uma dieta equilibrada e exercícios."
        elif imc < 35:
            classificacao = "Obesidade grau I"
            recomendacao = "Procure orientação médica para perder peso."
        elif imc < 40:
            classificacao = "Obesidade grau II"
            recomendacao = "É importante buscar ajuda médica."
        else:
            classificacao = "Obesidade grau III"
            recomendacao = "Procure atendimento médico urgente."
        
        print(f"Classificação: {classificacao}")
        print(f"Recomendação: {recomendacao}")
        
    else:
        print("❌ Peso e altura devem ser valores positivos!")
        
except ValueError:
    print("❌ Por favor, digite números válidos!")
```

#### Exemplo 2: Sistema de Desconto por Categoria

```python
# Sistema de desconto
print("=== SISTEMA DE DESCONTO ===")

valor_compra = float(input("Valor da compra: R$ "))
categoria = input("Categoria (A/B/C): ").upper()
pagamento_vista = input("Pagamento à vista? (s/n): ").lower() == 's'

# Validação da categoria
if categoria not in ['A', 'B', 'C']:
    print("❌ Categoria inválida!")
    exit()

# Cálculo do desconto baseado na categoria
if categoria == 'A':
    desconto_categoria = 10
elif categoria == 'B':
    desconto_categoria = 5
else:  # categoria == 'C'
    desconto_categoria = 2

# Desconto adicional para pagamento à vista
desconto_vista = 3 if pagamento_vista else 0

# Desconto por valor da compra
if valor_compra >= 1000:
    desconto_valor = 5
elif valor_compra >= 500:
    desconto_valor = 3
elif valor_compra >= 100:
    desconto_valor = 1
else:
    desconto_valor = 0

# Cálculo do desconto total
desconto_total = desconto_categoria + desconto_vista + desconto_valor
desconto_total = min(desconto_total, 20)  # Máximo 20%

# Cálculo do valor final
valor_desconto = valor_compra * (desconto_total / 100)
valor_final = valor_compra - valor_desconto

print(f"\n=== RESUMO ===")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto categoria {categoria}: {desconto_categoria}%")
print(f"Desconto à vista: {desconto_vista}%")
print(f"Desconto por valor: {desconto_valor}%")
print(f"Desconto total: {desconto_total}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
```

#### Exemplo 3: Verificador de Elegibilidade para Empréstimo

```python
# Verificador de elegibilidade
print("=== VERIFICADOR DE ELEGIBILIDADE ===")

# Coletando dados
idade = int(input("Idade: "))
salario = float(input("Salário: R$ "))
tempo_emprego = int(input("Tempo de emprego (meses): "))
score_credito = int(input("Score de crédito (0-1000): "))
valor_emprestimo = float(input("Valor do empréstimo: R$ "))

# Validações individuais
erros = []

if idade < 18 or idade > 65:
    erros.append("Idade deve estar entre 18 e 65 anos")

if salario < 1500:
    erros.append("Salário mínimo de R$ 1.500,00")

if tempo_emprego < 6:
    erros.append("Mínimo 6 meses de emprego")

if score_credito < 600:
    erros.append("Score de crédito mínimo de 600")

if valor_emprestimo > salario * 12:
    erros.append("Valor do empréstimo muito alto")

# Verificação final
if not erros:
    print("\n✅ APROVADO!")
    print("Seu empréstimo foi aprovado com sucesso!")
    
    # Cálculo da taxa de juros baseada no score
    if score_credito >= 800:
        taxa_juros = 0.8
        print("Taxa de juros: 0.8% ao mês (score excelente)")
    elif score_credito >= 700:
        taxa_juros = 1.2
        print("Taxa de juros: 1.2% ao mês (score bom)")
    else:
        taxa_juros = 1.8
        print("Taxa de juros: 1.8% ao mês (score regular)")
    
    # Cálculo do valor total
    valor_total = valor_emprestimo * (1 + taxa_juros/100) ** 12
    juros_total = valor_total - valor_emprestimo
    
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
    print(f"Juros totais: R$ {juros_total:.2f}")
    
else:
    print("\n❌ REPROVADO!")
    print("Motivos para reprovação:")
    for erro in erros:
        print(f"- {erro}")
```

### Boas Práticas

#### ✅ Faça:
- **Use nomes descritivos** para variáveis booleanas
- **Mantenha condições simples** - quebre condições complexas
- **Use parênteses** para clareza em condições complexas
- **Comente decisões importantes** - explique a lógica
- **Teste todos os caminhos** - verifique todos os casos

#### ❌ Evite:
- **Condições muito complexas** - quebre em partes menores
- **Aninhamento excessivo** - use elif quando possível
- **Código duplicado** - reutilize lógica comum
- **Condições desnecessárias** - simplifique quando possível

#### 🔧 Solução de Problemas Comuns:

#### Erro: "IndentationError"
- **Causa**: Problemas com indentação
- **Solução**: Use 4 espaços consistentemente

#### Erro: "SyntaxError"
- **Causa**: Dois pontos faltando após if/elif/else
- **Solução**: Sempre use `:` após condições

#### Lógica incorreta:
- **Causa**: Ordem das condições
- **Solução**: Teste condições mais específicas primeiro

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora de Média com Conceito**
   - Calcule média de 3 notas
   - Determine conceito (A, B, C, D, F)
   - Verifique aprovação/reprovação
   - Dê feedback específico

2. **Sistema de Login Robusto**
   - Valide usuário e senha
   - Implemente sistema de tentativas
   - Diferentes níveis de acesso
   - Mensagens de erro específicas

3. **Calculadora de Frete**
   - Calcule frete baseado em peso e distância
   - Aplique descontos por região
   - Diferentes modalidades de entrega
   - Validação de dados de entrada

4. **Verificador de Senha Forte**
   - Valide comprimento mínimo
   - Verifique presença de maiúsculas, minúsculas, números
   - Verifique caracteres especiais
   - Dê pontuação de força da senha

5. **Sistema de Notas Escolares**
   - Calcule média ponderada
   - Considere frequência e comportamento
   - Determine aprovação/reprovação
   - Gere relatório detalhado

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Loops** - como repetir código de forma eficiente.

### O que você vai aprender:
- 📚 Loop while - repetição com condição
- 📚 Loop for - iteração sobre sequências
- 📚 Break e continue - controle de fluxo
- 📚 Loops aninhados - estruturas complexas
- 📚 List comprehension - loops compactos
- 📚 Padrões de iteração comuns

---

**Pratique as estruturas de controle! São fundamentais para criar programas inteligentes! 🐍**

> 💡 **Dica**: Crie um fluxograma das suas decisões antes de programar. Isso ajuda a visualizar a lógica e identificar possíveis problemas.
