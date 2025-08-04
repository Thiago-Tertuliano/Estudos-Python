# Aula 3: Operadores

## 🎯 Objetivos da Aula

- Conhecer os operadores aritméticos
- Aprender operadores de comparação
- Entender operadores lógicos
- Compreender precedência de operadores

## 📚 Conteúdo

### Operadores Aritméticos

```python
a = 10
b = 3

soma = a + b           # 13
subtracao = a - b      # 7
multiplicacao = a * b  # 30
divisao = a / b        # 3.333...
divisao_inteira = a // b  # 3
resto = a % b          # 1
potencia = a ** b      # 1000
```

### Operadores de Atribuição

```python
x = 5
x += 3    # x = x + 3 (8)
x -= 2    # x = x - 2 (6)
x *= 4    # x = x * 4 (24)
x /= 3    # x = x / 3 (8.0)
x //= 2   # x = x // 2 (4)
x %= 3    # x = x % 3 (1)
x **= 2   # x = x ** 2 (1)
```

### Operadores de Comparação

```python
a = 5
b = 3

igual = a == b         # False
diferente = a != b     # True
maior = a > b          # True
menor = a < b          # False
maior_igual = a >= b   # True
menor_igual = a <= b   # False
```

### Operadores Lógicos

```python
# AND (e)
x = True
y = False
resultado_and = x and y  # False

# OR (ou)
resultado_or = x or y    # True

# NOT (não)
resultado_not = not x    # False
```

### Precedência de Operadores

1. **()** - Parênteses
2. **\*\*** - Exponenciação
3. **+x, -x** - Positivo/Negativo
4. **\*, /, //, %** - Multiplicação, Divisão
5. **+, -** - Adição, Subtração
6. **==, !=, >, <, >=, <=** - Comparação
7. **not** - NOT lógico
8. **and** - AND lógico
9. **or** - OR lógico

### Exemplos Práticos

```python
# Calculadora simples
num1 = 10
num2 = 5

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")
print(f"Divisão inteira: {num1 // num2}")
print(f"Resto: {num1 % num2}")
print(f"Potência: {num1 ** num2}")

# Comparações
idade = 18
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira
print(f"Pode dirigir: {pode_dirigir}")

# Operadores de atribuição
salario = 1000
salario += 200  # Aumento de 200
salario *= 1.1  # Aumento de 10%
print(f"Salário final: R$ {salario}")
```

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora Avançada**
   - Implemente todas as operações aritméticas
   - Use operadores de atribuição

2. **Verificador de Idade**
   - Verifique se pode votar, dirigir, etc.
   - Use operadores de comparação

3. **Calculadora de Desconto**
   - Aplique desconto baseado em condições
   - Use operadores lógicos

4. **Verificador de Senha**
   - Valide senha com múltiplas condições
   - Combine operadores lógicos

## 📝 Dicas Importantes

- **Parênteses**: Use para controlar a ordem das operações
- **Comparações**: Sempre retornam True ou False
- **Operadores lógicos**: Avaliam de forma "preguiçosa"
- **Atribuição**: `+=` é mais eficiente que `x = x + 1`

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Estruturas de Controle** - como tomar decisões no código com if, elif e else.

---

**Pratique os operadores! São fundamentais para qualquer linguagem! 🐍** 