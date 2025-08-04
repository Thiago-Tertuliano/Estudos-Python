# Aula 5: Loops

## 🎯 Objetivos da Aula

- Entender como repetir código de forma eficiente usando loops
- Dominar o uso do loop while para repetições baseadas em condições
- Aprender a usar o loop for para iterar sobre sequências
- Compreender break e continue para controle de fluxo
- Praticar loops aninhados e padrões de iteração comuns

## 📚 Conteúdo Detalhado

### O que são Loops?

Loops (laços) são estruturas que permitem repetir um bloco de código múltiplas vezes. Eles são essenciais para processar dados, automatizar tarefas e criar programas eficientes.

#### Por que usar loops?
- **Automatizar tarefas repetitivas**: Evitar código duplicado
- **Processar coleções de dados**: Listas, strings, arquivos
- **Implementar algoritmos**: Busca, ordenação, cálculos
- **Criar interfaces interativas**: Menus, jogos, aplicações
- **Otimizar performance**: Executar operações em lote

### Loop While

O loop `while` repete um bloco de código enquanto uma condição for verdadeira.

#### Sintaxe Básica:
```python
while condicao:
    # código a ser repetido
    print("Executando...")
```

#### Exemplo Simples:
```python
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

print("Loop finalizado!")
```

#### Características Importantes:
- A condição é verificada antes de cada iteração
- O loop para quando a condição se torna False
- É responsabilidade do programador garantir que o loop termine
- Pode executar zero ou mais vezes

### Controle de Loop While

#### Incremento/Decremento:
```python
# Contador crescente
i = 1
while i <= 10:
    print(f"Número: {i}")
    i += 1

# Contador decrescente
j = 10
while j >= 1:
    print(f"Número: {j}")
    j -= 1

# Contador com passo
k = 0
while k <= 20:
    print(f"Número: {k}")
    k += 2  # Incrementa de 2 em 2
```

#### Condições Complexas:
```python
# Múltiplas condições
senha = ""
tentativas = 0

while senha != "123456" and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1
    
    if senha != "123456":
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")

if senha == "123456":
    print("Acesso permitido!")
else:
    print("Conta bloqueada!")
```

### Loop For

O loop `for` itera sobre uma sequência (lista, tupla, string, etc.) ou um range de números.

#### Sintaxe Básica:
```python
for item in sequencia:
    # código a ser executado para cada item
    print(item)
```

#### Iterando sobre Listas:
```python
frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(f"Fruta: {fruta}")

# Com índice
for i, fruta in enumerate(frutas):
    print(f"Fruta {i+1}: {fruta}")
```

#### Iterando sobre Strings:
```python
palavra = "Python"

for letra in palavra:
    print(f"Letra: {letra}")

# Contando vogais
vogais = 0
for letra in palavra.lower():
    if letra in 'aeiou':
        vogais += 1

print(f"Vogais na palavra '{palavra}': {vogais}")
```

#### Usando range():
```python
# Range com um parâmetro (0 até n-1)
for i in range(5):
    print(f"Número: {i}")

# Range com dois parâmetros (início, fim)
for i in range(1, 6):
    print(f"Número: {i}")

# Range com três parâmetros (início, fim, passo)
for i in range(0, 10, 2):
    print(f"Número par: {i}")

# Range decrescente
for i in range(10, 0, -1):
    print(f"Contagem regressiva: {i}")
```

### Break e Continue

#### Break:
O `break` interrompe completamente o loop e sai dele.

```python
# Exemplo: Encontrar o primeiro número divisível por 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Primeiro número divisível por 7: {i}")
        break

# Exemplo: Sistema de login
senha_correta = "123456"
tentativas = 0

while True:
    senha = input("Digite a senha: ")
    tentativas += 1
    
    if senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    elif tentativas >= 3:
        print("Conta bloqueada!")
        break
    else:
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")
```

#### Continue:
O `continue` pula para a próxima iteração do loop.

```python
# Exemplo: Imprimir apenas números pares
for i in range(1, 11):
    if i % 2 != 0:  # Se for ímpar
        continue
    print(f"Número par: {i}")

# Exemplo: Processar apenas itens válidos
produtos = ["maçã", "", "banana", None, "laranja"]

for produto in produtos:
    if not produto:  # Se estiver vazio ou None
        continue
    print(f"Processando: {produto}")
```

### Loops Aninhados

Loops aninhados são loops dentro de outros loops.

#### Exemplo Básico:
```python
# Tabuada
for i in range(1, 6):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
```

#### Exemplo Prático - Matriz:
```python
# Criar uma matriz 3x3
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = i * 3 + j + 1
        linha.append(valor)
    matriz.append(linha)

# Imprimir a matriz
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:2}", end=" ")
    print()  # Nova linha
```

#### Exemplo - Padrões:
```python
# Triângulo de asteriscos
altura = 5

for i in range(altura):
    for j in range(i + 1):
        print("*", end="")
    print()  # Nova linha

# Triângulo invertido
for i in range(altura, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

### Padrões de Iteração Comuns

#### Iteração com Índice:
```python
frutas = ["maçã", "banana", "laranja"]

# Usando enumerate
for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice + 1}: {fruta}")

# Usando range
for i in range(len(frutas)):
    print(f"Fruta {i + 1}: {frutas[i]}")
```

#### Iteração Reversa:
```python
# Usando reversed()
for i in reversed(range(5)):
    print(f"Número: {i}")

# Usando range com passo negativo
for i in range(4, -1, -1):
    print(f"Número: {i}")
```

#### Iteração com Condições:
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(f"Números pares: {pares}")

# Encontrar o maior número
maior = numeros[0]
for num in numeros:
    if num > maior:
        maior = num

print(f"Maior número: {maior}")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Calculadora de Média com Validação

```python
# Calculadora de média com validação
print("=== CALCULADORA DE MÉDIA ===")

notas = []
contador = 1

while True:
    try:
        nota = float(input(f"Digite a nota {contador} (ou -1 para sair): "))
        
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            notas.append(nota)
            contador += 1
        else:
            print("❌ Nota deve estar entre 0 e 10!")
            continue
            
    except ValueError:
        print("❌ Por favor, digite um número válido!")
        continue

if notas:
    media = sum(notas) / len(notas)
    print(f"\n=== RESULTADO ===")
    print(f"Quantidade de notas: {len(notas)}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Status: Aprovado!")
    else:
        print("Status: Reprovado!")
else:
    print("Nenhuma nota foi inserida!")
```

#### Exemplo 2: Jogo de Adivinhação

```python
import random

# Jogo de adivinhação
print("=== JOGO DE ADIVINHAÇÃO ===")
print("Pensei em um número entre 1 e 100!")

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10

while tentativas < max_tentativas:
    try:
        palpite = int(input(f"\nTentativa {tentativas + 1}/{max_tentativas}: "))
        tentativas += 1
        
        if palpite < 1 or palpite > 100:
            print("❌ Digite um número entre 1 e 100!")
            continue
            
        if palpite == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("📈 Dica: O número é maior!")
        else:
            print("📉 Dica: O número é menor!")
            
    except ValueError:
        print("❌ Por favor, digite um número válido!")
        continue

if tentativas >= max_tentativas and palpite != numero_secreto:
    print(f"\n😔 Game Over! O número era {numero_secreto}.")
```

#### Exemplo 3: Sistema de Menu Interativo

```python
# Sistema de menu
print("=== SISTEMA DE MENU ===")

while True:
    print("\nEscolha uma opção:")
    print("1. Calcular área do círculo")
    print("2. Calcular área do retângulo")
    print("3. Calcular área do triângulo")
    print("4. Sair")
    
    opcao = input("\nDigite sua opção (1-4): ")
    
    if opcao == "1":
        try:
            raio = float(input("Digite o raio do círculo: "))
            if raio > 0:
                area = 3.14159 * raio ** 2
                print(f"Área do círculo: {area:.2f}")
            else:
                print("❌ Raio deve ser positivo!")
        except ValueError:
            print("❌ Digite um número válido!")
            
    elif opcao == "2":
        try:
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            if base > 0 and altura > 0:
                area = base * altura
                print(f"Área do retângulo: {area:.2f}")
            else:
                print("❌ Base e altura devem ser positivas!")
        except ValueError:
            print("❌ Digite números válidos!")
            
    elif opcao == "3":
        try:
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            if base > 0 and altura > 0:
                area = (base * altura) / 2
                print(f"Área do triângulo: {area:.2f}")
            else:
                print("❌ Base e altura devem ser positivas!")
        except ValueError:
            print("❌ Digite números válidos!")
            
    elif opcao == "4":
        print("👋 Obrigado por usar o sistema!")
        break
        
    else:
        print("❌ Opção inválida! Digite 1, 2, 3 ou 4.")
```

#### Exemplo 4: Processamento de Lista de Compras

```python
# Sistema de lista de compras
print("=== LISTA DE COMPRAS ===")

compras = []
precos = []

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Calcular total")
    print("5. Sair")
    
    opcao = input("\nDigite sua opção (1-5): ")
    
    if opcao == "1":
        item = input("Digite o nome do item: ").strip()
        if item:
            try:
                preco = float(input("Digite o preço do item: R$ "))
                if preco >= 0:
                    compras.append(item)
                    precos.append(preco)
                    print(f"✅ Item '{item}' adicionado!")
                else:
                    print("❌ Preço deve ser positivo!")
            except ValueError:
                print("❌ Digite um preço válido!")
        else:
            print("❌ Nome do item não pode estar vazio!")
            
    elif opcao == "2":
        if compras:
            print("\nItens na lista:")
            for i, item in enumerate(compras):
                print(f"{i+1}. {item} - R$ {precos[i]:.2f}")
            
            try:
                indice = int(input("Digite o número do item a remover: ")) - 1
                if 0 <= indice < len(compras):
                    item_removido = compras.pop(indice)
                    preco_removido = precos.pop(indice)
                    print(f"✅ Item '{item_removido}' removido!")
                else:
                    print("❌ Índice inválido!")
            except ValueError:
                print("❌ Digite um número válido!")
        else:
            print("❌ Lista vazia!")
            
    elif opcao == "3":
        if compras:
            print("\n=== LISTA DE COMPRAS ===")
            total = 0
            for i, (item, preco) in enumerate(zip(compras, precos)):
                print(f"{i+1}. {item} - R$ {preco:.2f}")
                total += preco
            print(f"\nTotal: R$ {total:.2f}")
        else:
            print("❌ Lista vazia!")
            
    elif opcao == "4":
        if compras:
            total = sum(precos)
            print(f"\n💰 Total da compra: R$ {total:.2f}")
        else:
            print("❌ Lista vazia!")
            
    elif opcao == "5":
        print("👋 Obrigado por usar a lista de compras!")
        break
        
    else:
        print("❌ Opção inválida! Digite 1, 2, 3, 4 ou 5.")
```

### Boas Práticas

#### ✅ Faça:
- **Use nomes descritivos** para variáveis de controle
- **Garanta que loops terminem** - evite loops infinitos
- **Use break e continue** para simplificar lógica
- **Comente loops complexos** - explique a lógica
- **Teste casos extremos** - lista vazia, um item, etc.

#### ❌ Evite:
- **Loops infinitos acidentais** - sempre verifique a condição
- **Modificar a sequência** durante iteração
- **Loops muito aninhados** - quebre em funções
- **Código duplicado** - reutilize lógica comum

#### 🔧 Solução de Problemas Comuns:

#### Loop Infinito:
- **Causa**: Condição nunca se torna False
- **Solução**: Verifique se a variável de controle está sendo modificada

#### Erro: "IndexError"
- **Causa**: Acessando índice fora do range
- **Solução**: Use len() para verificar o tamanho da lista

#### Performance ruim:
- **Causa**: Loops desnecessários ou ineficientes
- **Solução**: Use list comprehension ou funções built-in quando possível

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Calculadora de Estatísticas**
   - Calcule média, mediana, máximo, mínimo
   - Use loops para processar lista de números
   - Valide entrada de dados
   - Exiba resultados formatados

2. **Jogo da Velha**
   - Implemente tabuleiro 3x3
   - Use loops aninhados para verificar vitória
   - Alternância entre jogadores
   - Interface de usuário simples

3. **Sistema de Notas Escolares**
   - Calcule média de múltiplos alunos
   - Use loops para processar turma
   - Determine aprovação/reprovação
   - Gere relatório da turma

4. **Calculadora de Juros Compostos**
   - Calcule evolução do investimento
   - Use loops para simular anos
   - Mostre progressão mês a mês
   - Compare diferentes taxas

5. **Gerador de Padrões**
   - Crie diferentes padrões com asteriscos
   - Use loops aninhados
   - Implemente triângulos, quadrados, diamantes
   - Permita configuração do tamanho

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Listas** - como trabalhar com coleções de dados.

### O que você vai aprender:
- 📚 Criação e manipulação de listas
- 📚 Métodos de lista (append, remove, insert, etc.)
- 📚 Slicing e indexação avançada
- 📚 List comprehension
- 📚 Listas aninhadas e matrizes
- 📚 Operações com listas

---

**Pratique os loops! São fundamentais para automatizar tarefas! 🐍**

> 💡 **Dica**: Desenhe o fluxo do seu loop antes de programar. Isso ajuda a visualizar como os dados serão processados e identificar possíveis problemas.
