# Aula 3: Operadores

## 🎯 Objetivos da Aula

- Conhecer e dominar todos os operadores aritméticos do Python
- Aprender operadores de comparação e como usá-los em condições
- Entender operadores lógicos e sua importância na tomada de decisões
- Compreender precedência de operadores e como controlar a ordem das operações
- Praticar o uso de operadores em situações reais de programação

## 📚 Conteúdo Detalhado

### O que são Operadores?

Operadores são símbolos especiais que realizam operações em valores e variáveis. Eles são fundamentais para qualquer linguagem de programação, pois permitem manipular dados e tomar decisões.

#### Classificação dos Operadores:
1. **Aritméticos**: Realizam cálculos matemáticos
2. **De Comparação**: Comparam valores e retornam True/False
3. **Lógicos**: Combinam condições lógicas
4. **De Atribuição**: Atribuem valores às variáveis
5. **De Identidade**: Verificam se objetos são iguais
6. **De Associação**: Verificam se um valor está em uma sequência

### Operadores Aritméticos

Os operadores aritméticos realizam operações matemáticas básicas.

#### Operadores Básicos:

```python
a = 10
b = 3

# Adição
soma = a + b           # 13
print(f"Soma: {a} + {b} = {soma}")

# Subtração
subtracao = a - b      # 7
print(f"Subtração: {a} - {b} = {subtracao}")

# Multiplicação
multiplicacao = a * b  # 30
print(f"Multiplicação: {a} * {b} = {multiplicacao}")

# Divisão (sempre retorna float)
divisao = a / b        # 3.333...
print(f"Divisão: {a} / {b} = {divisao}")

# Divisão inteira (trunca o resultado)
divisao_inteira = a // b  # 3
print(f"Divisão inteira: {a} // {b} = {divisao_inteira}")

# Módulo (resto da divisão)
resto = a % b          # 1
print(f"Resto: {a} % {b} = {resto}")

# Exponenciação (potência)
potencia = a ** b      # 1000
print(f"Potência: {a} ** {b} = {potencia}")
```

#### Operações com Números Negativos:

```python
x = -5
y = 3

print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")      # -2
print(f"x - y = {x - y}")      # -8
print(f"x * y = {x * y}")      # -15
print(f"x / y = {x / y}")      # -1.666...
print(f"x // y = {x // y}")    # -2 (arredonda para baixo)
print(f"x % y = {x % y}")      # 1
print(f"x ** y = {x ** y}")    # -125
```

#### Operações com Float:

```python
# Precisão de ponto flutuante
a = 0.1
b = 0.2
c = a + b
print(f"{a} + {b} = {c}")  # 0.30000000000000004

# Para maior precisão, use round()
c_arredondado = round(c, 1)
print(f"Arredondado: {c_arredondado}")  # 0.3
```

### Operadores de Atribuição

Os operadores de atribuição combinam uma operação com atribuição.

#### Operadores Básicos:

```python
x = 5
print(f"Valor inicial: {x}")

# Adição e atribuição
x += 3    # x = x + 3
print(f"x += 3: {x}")  # 8

# Subtração e atribuição
x -= 2    # x = x - 2
print(f"x -= 2: {x}")  # 6

# Multiplicação e atribuição
x *= 4    # x = x * 4
print(f"x *= 4: {x}")  # 24

# Divisão e atribuição
x /= 3    # x = x / 3
print(f"x /= 3: {x}")  # 8.0

# Divisão inteira e atribuição
x //= 2   # x = x // 2
print(f"x //= 2: {x}")  # 4.0

# Módulo e atribuição
x %= 3    # x = x % 3
print(f"x %= 3: {x}")  # 1.0

# Exponenciação e atribuição
x **= 2   # x = x ** 2
print(f"x **= 2: {x}")  # 1.0
```

#### Exemplos Práticos:

```python
# Contador
contador = 0
contador += 1  # Incrementa
contador += 1  # Incrementa novamente
print(f"Contador: {contador}")  # 2

# Acumulador
soma = 0
soma += 10
soma += 20
soma += 30
print(f"Soma acumulada: {soma}")  # 60

# Multiplicador
preco = 100
preco *= 1.1  # Aumenta 10%
print(f"Preço com aumento: R$ {preco:.2f}")  # 110.00
```

### Operadores de Comparação

Os operadores de comparação comparam valores e retornam True ou False.

#### Operadores Básicos:

```python
a = 5
b = 3

# Igualdade
igual = a == b         # False
print(f"{a} == {b}: {igual}")

# Desigualdade
diferente = a != b     # True
print(f"{a} != {b}: {diferente}")

# Maior que
maior = a > b          # True
print(f"{a} > {b}: {maior}")

# Menor que
menor = a < b          # False
print(f"{a} < {b}: {menor}")

# Maior ou igual
maior_igual = a >= b   # True
print(f"{a} >= {b}: {maior_igual}")

# Menor ou igual
menor_igual = a <= b   # False
print(f"{a} <= {b}: {menor_igual}")
```

#### Comparações com Strings:

```python
# Comparação lexicográfica
nome1 = "Ana"
nome2 = "João"
nome3 = "ana"

print(f"'{nome1}' == '{nome2}': {nome1 == nome2}")  # False
print(f"'{nome1}' < '{nome2}': {nome1 < nome2}")    # True (A vem antes de J)
print(f"'{nome1}' == '{nome3}': {nome1 == nome3}")  # False (case sensitive)
print(f"'{nome1.lower()}' == '{nome3}': {nome1.lower() == nome3}")  # True
```

#### Comparações Múltiplas:

```python
idade = 18
tem_carteira = True

# Verificações múltiplas
pode_dirigir = idade >= 18 and tem_carteira
print(f"Pode dirigir: {pode_dirigir}")

# Verificações em cadeia
tempo_servico = 5
idade_aposentadoria = 65
idade_atual = 60

pode_aposentar = idade_atual >= idade_aposentadoria or tempo_servico >= 30
print(f"Pode aposentar: {pode_aposentar}")
```

### Operadores Lógicos

Os operadores lógicos combinam condições e retornam True ou False.

#### Operador AND:

```python
# AND: True apenas se AMBAS condições forem True
x = True
y = False
z = True

resultado1 = x and y  # False
resultado2 = x and z  # True
resultado3 = y and z  # False

print(f"True and False: {resultado1}")
print(f"True and True: {resultado2}")
print(f"False and True: {resultado3}")

# Exemplo prático
idade = 18
tem_carteira = True
tem_carro = False

pode_dirigir = idade >= 18 and tem_carteira
print(f"Pode dirigir: {pode_dirigir}")  # True

pode_sair_agora = idade >= 18 and tem_carteira and tem_carro
print(f"Pode sair agora: {pode_sair_agora}")  # False
```

#### Operador OR:

```python
# OR: True se PELO MENOS UMA condição for True
x = True
y = False
z = False

resultado1 = x or y   # True
resultado2 = y or z   # False
resultado3 = x or z   # True

print(f"True or False: {resultado1}")
print(f"False or False: {resultado2}")
print(f"True or False: {resultado3}")

# Exemplo prático
tem_dinheiro = False
tem_cartao = True
tem_cheque = False

pode_comprar = tem_dinheiro or tem_cartao or tem_cheque
print(f"Pode comprar: {pode_comprar}")  # True
```

#### Operador NOT:

```python
# NOT: Inverte o valor booleano
x = True
y = False

resultado1 = not x  # False
resultado2 = not y  # True

print(f"not True: {resultado1}")
print(f"not False: {resultado2}")

# Exemplo prático
tem_senha = False
pode_acessar = not tem_senha
print(f"Pode acessar sem senha: {pode_acessar}")  # True

# Combinação de operadores
idade = 16
tem_autorizacao = True

pode_entrar = (idade >= 18) or (idade >= 16 and tem_autorizacao)
print(f"Pode entrar: {pode_entrar}")  # True
```

#### Avaliação Preguiçosa (Short-circuit):

```python
# Python para de avaliar assim que encontra o resultado
x = True
y = False

# Com AND, se o primeiro for False, não avalia o segundo
resultado = x and y  # False (avalia ambos)
resultado2 = y and x  # False (para no primeiro)

# Com OR, se o primeiro for True, não avalia o segundo
resultado3 = x or y   # True (para no primeiro)
resultado4 = y or x   # True (avalia ambos)

print(f"x and y: {resultado}")
print(f"y and x: {resultado2}")
print(f"x or y: {resultado3}")
print(f"y or x: {resultado4}")
```

### Precedência de Operadores

A precedência determina a ordem em que as operações são executadas.

#### Ordem de Precedência (do maior para o menor):

1. **()** - Parênteses
2. **\*\*** - Exponenciação
3. **+x, -x** - Positivo/Negativo unário
4. **\*, /, //, %** - Multiplicação, Divisão, Divisão inteira, Módulo
5. **+, -** - Adição, Subtração
6. **==, !=, >, <, >=, <=** - Comparação
7. **not** - NOT lógico
8. **and** - AND lógico
9. **or** - OR lógico

#### Exemplos de Precedência:

```python
# Sem parênteses
resultado1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultado1}")  # 14 (não 20)

# Com parênteses
resultado2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {resultado2}")  # 20

# Operadores lógicos
a = True
b = False
c = True

resultado3 = a and b or c
print(f"a and b or c = {resultado3}")  # True

resultado4 = a and (b or c)
print(f"a and (b or c) = {resultado4}")  # True

# Expressão complexa
idade = 25
tem_carteira = True
tem_carro = False
tem_dinheiro = True

pode_sair = (idade >= 18 and tem_carteira) and (tem_carro or tem_dinheiro)
print(f"Pode sair: {pode_sair}")  # True
```

### Operadores de Identidade

Verificam se dois objetos são o mesmo objeto na memória.

```python
# is e is not
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a is b: {a is b}")      # False (objetos diferentes)
print(f"a is c: {a is c}")      # True (mesmo objeto)
print(f"a is not b: {a is not b}")  # True

# Com None
valor = None
print(f"valor is None: {valor is None}")  # True
```

### Operadores de Associação

Verificam se um valor está em uma sequência.

```python
# in e not in
frutas = ["maçã", "banana", "laranja"]
cor = "vermelho"

print(f"'maçã' in frutas: {'maçã' in frutas}")  # True
print(f"'uva' in frutas: {'uva' in frutas}")    # False
print(f"'vermelho' not in frutas: {cor not in frutas}")  # True

# Com strings
texto = "Python é incrível"
print(f"'Python' in texto: {'Python' in texto}")  # True
print(f"'Java' in texto: {'Java' in texto}")      # False
```

### Exemplos Práticos Avançados

#### Exemplo 1: Calculadora Avançada

```python
# Calculadora com validação
print("=== CALCULADORA AVANÇADA ===")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potência")
print("6. Módulo")

opcao = input("Escolha uma operação (1-6): ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == "1":
        resultado = num1 + num2
        operacao = "+"
    elif opcao == "2":
        resultado = num1 - num2
        operacao = "-"
    elif opcao == "3":
        resultado = num1 * num2
        operacao = "*"
    elif opcao == "4":
        if num2 == 0:
            print("❌ Erro: Divisão por zero!")
        else:
            resultado = num1 / num2
            operacao = "/"
    elif opcao == "5":
        resultado = num1 ** num2
        operacao = "**"
    elif opcao == "6":
        resultado = num1 % num2
        operacao = "%"
    else:
        print("❌ Opção inválida!")
        exit()
    
    print(f"\n{num1} {operacao} {num2} = {resultado}")
    
except ValueError:
    print("❌ Por favor, digite números válidos!")
```

#### Exemplo 2: Verificador de Elegibilidade

```python
# Verificador de elegibilidade para empréstimo
print("=== VERIFICADOR DE ELEGIBILIDADE ===")

# Coletando dados
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
tempo_emprego = int(input("Tempo de emprego (meses): "))
score_credito = int(input("Score de crédito (0-1000): "))
valor_emprestimo = float(input("Valor do empréstimo: "))

# Validações
idade_valida = idade >= 18 and idade <= 65
salario_suficiente = salario >= 2000
tempo_adequado = tempo_emprego >= 12
score_bom = score_credito >= 700
valor_adequado = valor_emprestimo <= salario * 10

# Verificação final
elegivel = (idade_valida and 
           salario_suficiente and 
           tempo_adequado and 
           score_bom and 
           valor_adequado)

print(f"\n=== RESULTADO ===")
print(f"Idade válida: {idade_valida}")
print(f"Salário suficiente: {salario_suficiente}")
print(f"Tempo de emprego adequado: {tempo_adequado}")
print(f"Score de crédito bom: {score_bom}")
print(f"Valor adequado: {valor_adequado}")
print(f"\nElegível para empréstimo: {'✅ SIM' if elegivel else '❌ NÃO'}")

if not elegivel:
    print("\nMotivos para não aprovação:")
    if not idade_valida:
        print("- Idade fora do intervalo permitido")
    if not salario_suficiente:
        print("- Salário insuficiente")
    if not tempo_adequado:
        print("- Tempo de emprego insuficiente")
    if not score_bom:
        print("- Score de crédito baixo")
    if not valor_adequado:
        print("- Valor do empréstimo muito alto")
```

#### Exemplo 3: Sistema de Desconto

```python
# Sistema de desconto baseado em múltiplas condições
print("=== SISTEMA DE DESCONTO ===")

# Dados do cliente
valor_compra = float(input("Valor da compra: R$ "))
cliente_vip = input("Cliente VIP? (s/n): ").lower() == 's'
pagamento_vista = input("Pagamento à vista? (s/n): ").lower() == 's'
primeira_compra = input("Primeira compra? (s/n): ").lower() == 's'

# Cálculo do desconto
desconto = 0

# Desconto por valor
if valor_compra >= 1000:
    desconto += 10
elif valor_compra >= 500:
    desconto += 5
elif valor_compra >= 100:
    desconto += 2

# Desconto VIP
if cliente_vip:
    desconto += 5

# Desconto à vista
if pagamento_vista:
    desconto += 3

# Desconto primeira compra
if primeira_compra:
    desconto += 2

# Limitar desconto máximo
desconto = min(desconto, 20)

# Cálculo do valor final
valor_desconto = valor_compra * (desconto / 100)
valor_final = valor_compra - valor_desconto

print(f"\n=== RESUMO ===")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

# Informações adicionais
if desconto > 0:
    print(f"\n🎉 Parabéns! Você economizou R$ {valor_desconto:.2f}!")
else:
    print(f"\n💡 Dica: Compre mais para ganhar descontos!")
```

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora Avançada**
   - Implemente todas as operações aritméticas
   - Use operadores de atribuição
   - Valide divisão por zero
   - Formate resultados com 2 casas decimais

2. **Verificador de Idade Completo**
   - Verifique se pode votar, dirigir, aposentar
   - Use operadores de comparação
   - Considere diferentes faixas etárias
   - Dê orientações específicas para cada idade

3. **Calculadora de Desconto Avançada**
   - Aplique desconto baseado em múltiplas condições
   - Use operadores lógicos
   - Considere valor da compra, tipo de cliente, forma de pagamento
   - Implemente desconto progressivo

4. **Verificador de Senha Robusto**
   - Valide senha com múltiplas condições
   - Combine operadores lógicos
   - Verifique comprimento, caracteres especiais, números
   - Dê feedback específico sobre cada validação

5. **Sistema de Notas Escolares**
   - Calcule média ponderada
   - Determine conceito (A, B, C, D, F)
   - Verifique aprovação/reprovação
   - Considere frequência e comportamento

## 📝 Dicas Importantes

### ✅ Boas Práticas:
- **Use parênteses**: Para deixar a precedência clara
- **Comente expressões complexas**: Explique a lógica
- **Teste operadores**: Sempre teste com diferentes valores
- **Use nomes descritivos**: Para variáveis booleanas
- **Valide entradas**: Antes de usar em operações

### ❌ Evite:
- **Expressões muito complexas**: Quebre em partes menores
- **Comparações desnecessárias**: `if x == True` → `if x`
- **Operadores confusos**: Use parênteses para clareza
- **Ignorar precedência**: Sempre considere a ordem das operações

### 🔧 Solução de Problemas Comuns:

#### Erro: "ZeroDivisionError"
- **Causa**: Divisão por zero
- **Solução**: Sempre valide o divisor antes da divisão

#### Erro: "TypeError: unsupported operand type"
- **Causa**: Operação entre tipos incompatíveis
- **Solução**: Converta para o tipo correto antes da operação

#### Erro: "NameError"
- **Causa**: Variável não definida
- **Solução**: Defina todas as variáveis antes de usar

#### Lógica incorreta:
- **Causa**: Precedência de operadores
- **Solução**: Use parênteses para controlar a ordem

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Estruturas de Controle** - como tomar decisões no código com if, elif e else.

### O que você vai aprender:
- 📚 Estruturas condicionais (if, elif, else)
- 📚 Operador ternário
- 📚 Estruturas aninhadas
- 📚 Blocos de código
- 📚 Indentação correta
- 📚 Tomada de decisões complexas

---

**Pratique os operadores! São fundamentais para qualquer linguagem! 🐍**

> 💡 **Dica**: Crie uma tabela com todos os operadores e teste cada um com diferentes valores. Isso vai ajudar a memorizar e entender como eles funcionam. 