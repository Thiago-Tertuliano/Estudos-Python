# Aula 6: Listas

## 🎯 Objetivos da Aula

- Entender o que são listas e como criá-las em Python
- Dominar a manipulação de listas (adicionar, remover, modificar elementos)
- Aprender a usar métodos de lista (append, remove, insert, etc.)
- Compreender slicing e indexação avançada
- Praticar list comprehension para criar listas de forma eficiente
- Trabalhar com listas aninhadas e matrizes

## 📚 Conteúdo Detalhado

### O que são Listas?

Listas são estruturas de dados que armazenam coleções ordenadas de elementos. Em Python, as listas são mutáveis, ou seja, podem ser modificadas após a criação.

#### Características das Listas:
- **Mutáveis**: Podem ser alteradas após a criação
- **Ordenadas**: Os elementos mantêm a ordem de inserção
- **Heterogêneas**: Podem conter diferentes tipos de dados
- **Indexadas**: Acessadas por posição (índice)
- **Dinâmicas**: Podem crescer ou diminuir conforme necessário

#### Por que usar listas?
- **Organizar dados**: Agrupar informações relacionadas
- **Processar coleções**: Aplicar operações em múltiplos itens
- **Implementar algoritmos**: Ordenação, busca, filtros
- **Armazenar resultados**: Coletar dados de cálculos ou operações
- **Criar estruturas complexas**: Matrizes, listas de listas

### Criando Listas

#### Lista Vazia:
```python
# Criação de lista vazia
lista_vazia = []
lista_vazia2 = list()

print(f"Lista vazia: {lista_vazia}")
print(f"Tipo: {type(lista_vazia)}")
```

#### Lista com Elementos:
```python
# Lista com números
numeros = [1, 2, 3, 4, 5]
print(f"Números: {numeros}")

# Lista com strings
frutas = ["maçã", "banana", "laranja"]
print(f"Frutas: {frutas}")

# Lista mista
mista = [1, "texto", 3.14, True]
print(f"Lista mista: {mista}")

# Lista com repetições
repetida = [1, 2, 2, 3, 3, 3]
print(f"Com repetições: {repetida}")
```

#### Lista usando range():
```python
# Lista de 0 a 4
lista1 = list(range(5))
print(f"Range(5): {lista1}")

# Lista de 1 a 10
lista2 = list(range(1, 11))
print(f"Range(1, 11): {lista2}")

# Lista com passo
lista3 = list(range(0, 20, 2))
print(f"Range(0, 20, 2): {lista3}")
```

### Acessando Elementos

#### Indexação Básica:
```python
frutas = ["maçã", "banana", "laranja", "uva", "morango"]

# Primeiro elemento (índice 0)
primeira = frutas[0]
print(f"Primeira fruta: {primeira}")

# Último elemento
ultima = frutas[-1]
print(f"Última fruta: {ultima}")

# Elemento do meio
meio = frutas[2]
print(f"Fruta do meio: {meio}")

# Verificando se índice existe
try:
    elemento = frutas[10]
    print(f"Elemento: {elemento}")
except IndexError:
    print("❌ Índice fora do range!")
```

#### Slicing (Fatiamento):
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Primeiros 3 elementos
primeiros = numeros[:3]
print(f"Primeiros 3: {primeiros}")

# Últimos 3 elementos
ultimos = numeros[-3:]
print(f"Últimos 3: {ultimos}")

# Do índice 2 ao 6
meio = numeros[2:7]
print(f"Do índice 2 ao 6: {meio}")

# Com passo (de 2 em 2)
pares = numeros[::2]
print(f"Com passo 2: {pares}")

# Invertendo a lista
invertida = numeros[::-1]
print(f"Invertida: {invertida}")
```

### Modificando Listas

#### Alterando Elementos:
```python
cores = ["vermelho", "verde", "azul", "amarelo"]

# Alterando um elemento
cores[1] = "roxo"
print(f"Após alteração: {cores}")

# Alterando múltiplos elementos
cores[0:2] = ["preto", "branco"]
print(f"Após alteração múltipla: {cores}")
```

#### Adicionando Elementos:
```python
frutas = ["maçã", "banana"]

# Adicionando no final
frutas.append("laranja")
print(f"Após append: {frutas}")

# Adicionando em posição específica
frutas.insert(1, "uva")
print(f"Após insert: {frutas}")

# Adicionando múltiplos elementos
frutas.extend(["morango", "abacaxi"])
print(f"Após extend: {frutas}")

# Concatenando listas
outras_frutas = ["kiwi", "manga"]
todas_frutas = frutas + outras_frutas
print(f"Concatenadas: {todas_frutas}")
```

#### Removendo Elementos:
```python
numeros = [1, 2, 3, 4, 5, 3, 6, 3]

# Removendo por valor (primeira ocorrência)
numeros.remove(3)
print(f"Após remove(3): {numeros}")

# Removendo por índice
removido = numeros.pop(2)
print(f"Elemento removido: {removido}")
print(f"Após pop(2): {numeros}")

# Removendo o último elemento
ultimo = numeros.pop()
print(f"Último elemento: {ultimo}")
print(f"Após pop(): {numeros}")

# Removendo todos os elementos
numeros.clear()
print(f"Após clear: {numeros}")
```

### Métodos de Lista

#### Métodos de Busca:
```python
letras = ["a", "b", "c", "a", "d", "a"]

# Contando ocorrências
contagem = letras.count("a")
print(f"Quantidade de 'a': {contagem}")

# Encontrando índice
indice = letras.index("c")
print(f"Índice de 'c': {indice}")

# Verificando se elemento existe
existe = "b" in letras
print(f"'b' existe na lista: {existe}")

# Verificando se elemento não existe
nao_existe = "z" not in letras
print(f"'z' não existe na lista: {nao_existe}")
```

#### Métodos de Ordenação:
```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Ordenando em ordem crescente
numeros.sort()
print(f"Ordenada crescente: {numeros}")

# Ordenando em ordem decrescente
numeros.sort(reverse=True)
print(f"Ordenada decrescente: {numeros}")

# Criando nova lista ordenada
numeros_originais = [3, 1, 4, 1, 5, 9, 2, 6]
ordenada = sorted(numeros_originais)
print(f"Original: {numeros_originais}")
print(f"Ordenada: {ordenada}")

# Invertendo a ordem
numeros.reverse()
print(f"Invertida: {numeros}")
```

#### Métodos de Cópia:
```python
original = [1, 2, 3, 4, 5]

# Cópia superficial
copia1 = original.copy()
copia2 = original[:]
copia3 = list(original)

print(f"Original: {original}")
print(f"Cópia 1: {copia1}")
print(f"Cópia 2: {copia2}")
print(f"Cópia 3: {copia3}")

# Verificando se são objetos diferentes
print(f"Original é copia1: {original is copia1}")
print(f"Original é copia2: {original is copia2}")
```

### List Comprehension

List comprehension é uma forma concisa de criar listas baseadas em outras sequências.

#### Sintaxe Básica:
```python
# Forma tradicional
quadrados = []
for i in range(10):
    quadrados.append(i ** 2)

# List comprehension
quadrados_comp = [i ** 2 for i in range(10)]

print(f"Forma tradicional: {quadrados}")
print(f"List comprehension: {quadrados_comp}")
```

#### Exemplos Práticos:
```python
# Números pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]
print(f"Números pares: {pares}")

# Quadrados dos números pares
quadrados_pares = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"Quadrados dos pares: {quadrados_pares}")

# Comprimento das palavras
palavras = ["python", "programação", "lista", "comprehension"]
tamanhos = [len(palavra) for palavra in palavras]
print(f"Tamanhos: {tamanhos}")

# Palavras com mais de 5 letras
longas = [palavra for palavra in palavras if len(palavra) > 5]
print(f"Palavras longas: {longas}")

# Múltiplas condições
numeros = [x for x in range(50) if x % 2 == 0 and x % 3 == 0]
print(f"Números divisíveis por 2 e 3: {numeros}")
```

### Listas Aninhadas

#### Lista de Listas:
```python
# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for linha in matriz:
    print(linha)

# Acessando elementos
elemento = matriz[1][2]  # Linha 1, coluna 2
print(f"Elemento [1][2]: {elemento}")

# Modificando elemento
matriz[0][0] = 10
print(f"Após modificação: {matriz}")
```

#### Criando Matrizes:
```python
# Matriz vazia 3x3
matriz_vazia = [[0 for _ in range(3)] for _ in range(3)]
print("Matriz vazia:")
for linha in matriz_vazia:
    print(linha)

# Matriz com valores crescentes
matriz_crescente = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print("Matriz crescente:")
for linha in matriz_crescente:
    print(linha)
```

### Operações com Listas

#### Operações Matemáticas:
```python
# Soma de listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
soma = lista1 + lista2
print(f"Soma: {soma}")

# Repetição
repetida = [1, 2] * 3
print(f"Repetida: {repetida}")

# Verificando igualdade
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = [3, 2, 1]

print(f"A == B: {lista_a == lista_b}")
print(f"A == C: {lista_a == lista_c}")
```

#### Funções Built-in:
```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Funções básicas
print(f"Lista: {numeros}")
print(f"Tamanho: {len(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")
print(f"Soma: {sum(numeros)}")

# Verificando se lista está vazia
vazia = []
print(f"Lista vazia: {not vazia}")
print(f"Lista não vazia: {bool(numeros)}")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Sistema de Gerenciamento de Alunos

```python
# Sistema de gerenciamento de alunos
print("=== SISTEMA DE GERENCIAMENTO DE ALUNOS ===")

alunos = []
notas_alunos = []

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar aluno")
    print("2. Adicionar notas")
    print("3. Calcular médias")
    print("4. Listar alunos")
    print("5. Buscar aluno")
    print("6. Sair")
    
    opcao = input("\nDigite sua opção (1-6): ")
    
    if opcao == "1":
        nome = input("Digite o nome do aluno: ").strip()
        if nome and nome not in alunos:
            alunos.append(nome)
            notas_alunos.append([])
            print(f"✅ Aluno '{nome}' adicionado!")
        else:
            print("❌ Nome inválido ou aluno já existe!")
            
    elif opcao == "2":
        if alunos:
            print("\nAlunos disponíveis:")
            for i, aluno in enumerate(alunos):
                print(f"{i+1}. {aluno}")
            
            try:
                indice = int(input("Digite o número do aluno: ")) - 1
                if 0 <= indice < len(alunos):
                    nota = float(input("Digite a nota: "))
                    if 0 <= nota <= 10:
                        notas_alunos[indice].append(nota)
                        print(f"✅ Nota {nota} adicionada para {alunos[indice]}!")
                    else:
                        print("❌ Nota deve estar entre 0 e 10!")
                else:
                    print("❌ Índice inválido!")
            except ValueError:
                print("❌ Digite um número válido!")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "3":
        if alunos:
            print("\n=== MÉDIAS DOS ALUNOS ===")
            for i, aluno in enumerate(alunos):
                notas = notas_alunos[i]
                if notas:
                    media = sum(notas) / len(notas)
                    status = "Aprovado" if media >= 7 else "Reprovado"
                    print(f"{aluno}: {media:.2f} ({status})")
                else:
                    print(f"{aluno}: Sem notas")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "4":
        if alunos:
            print("\n=== LISTA DE ALUNOS ===")
            for i, aluno in enumerate(alunos):
                notas = notas_alunos[i]
                print(f"{i+1}. {aluno} - {len(notas)} notas")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "5":
        if alunos:
            nome_busca = input("Digite o nome do aluno: ").strip()
            if nome_busca in alunos:
                indice = alunos.index(nome_busca)
                notas = notas_alunos[indice]
                print(f"\nAluno: {nome_busca}")
                print(f"Notas: {notas}")
                if notas:
                    media = sum(notas) / len(notas)
                    print(f"Média: {media:.2f}")
            else:
                print("❌ Aluno não encontrado!")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "6":
        print("👋 Obrigado por usar o sistema!")
        break
        
    else:
        print("❌ Opção inválida!")
```

#### Exemplo 2: Calculadora de Estatísticas

```python
# Calculadora de estatísticas
print("=== CALCULADORA DE ESTATÍSTICAS ===")

numeros = []

while True:
    try:
        entrada = input("Digite um número (ou 'sair' para terminar): ")
        
        if entrada.lower() == 'sair':
            break
            
        numero = float(entrada)
        numeros.append(numero)
        print(f"✅ Número {numero} adicionado!")
        
    except ValueError:
        print("❌ Digite um número válido!")

if numeros:
    print(f"\n=== RESULTADOS ===")
    print(f"Números: {numeros}")
    print(f"Quantidade: {len(numeros)}")
    print(f"Soma: {sum(numeros)}")
    print(f"Média: {sum(numeros) / len(numeros):.2f}")
    print(f"Máximo: {max(numeros)}")
    print(f"Mínimo: {min(numeros)}")
    
    # Mediana
    ordenados = sorted(numeros)
    n = len(ordenados)
    if n % 2 == 0:
        mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    else:
        mediana = ordenados[n//2]
    print(f"Mediana: {mediana:.2f}")
    
    # Moda (valor mais frequente)
    from collections import Counter
    contador = Counter(numeros)
    moda = contador.most_common(1)[0][0]
    print(f"Moda: {moda}")
    
else:
    print("❌ Nenhum número foi inserido!")
```

#### Exemplo 3: Jogo da Velha

```python
# Jogo da Velha
print("=== JOGO DA VELHA ===")

# Inicializando tabuleiro
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador_atual = "X"

def imprimir_tabuleiro():
    print("\n  0 1 2")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} {'|'.join(linha)}")
        if i < 2:
            print("  -----")

def verificar_vitoria():
    # Linhas
    for linha in tabuleiro:
        if linha.count(linha[0]) == 3 and linha[0] != " ":
            return True
    
    # Colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != " ":
            return True
    
    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True
    
    return False

def tabuleiro_cheio():
    return all(cell != " " for linha in tabuleiro for cell in linha)

# Loop principal do jogo
while True:
    imprimir_tabuleiro()
    print(f"\nVez do jogador {jogador_atual}")
    
    try:
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))
        
        if 0 <= linha <= 2 and 0 <= coluna <= 2:
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual
                
                if verificar_vitoria():
                    imprimir_tabuleiro()
                    print(f"\n🎉 Jogador {jogador_atual} venceu!")
                    break
                elif tabuleiro_cheio():
                    imprimir_tabuleiro()
                    print("\n😐 Empate!")
                    break
                else:
                    jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("❌ Posição já ocupada!")
        else:
            print("❌ Posição inválida!")
            
    except ValueError:
        print("❌ Digite números válidos!")
```

### Boas Práticas

#### ✅ Faça:
- **Use nomes descritivos** para listas
- **Inicialize listas vazias** quando necessário
- **Use list comprehension** para operações simples
- **Verifique se lista está vazia** antes de acessar
- **Use métodos apropriados** para cada operação

#### ❌ Evite:
- **Modificar lista durante iteração** - pode causar erros
- **Usar listas para dados heterogêneos** - use dicionários
- **Criar listas muito grandes** - considere geradores
- **Ignorar índices negativos** - podem ser úteis

#### 🔧 Solução de Problemas Comuns:

#### Erro: "IndexError"
- **Causa**: Acessando índice fora do range
- **Solução**: Use len() para verificar tamanho

#### Erro: "ValueError"
- **Causa**: Tentando remover elemento inexistente
- **Solução**: Verifique se elemento existe antes de remover

#### Performance ruim:
- **Causa**: Operações repetitivas em listas grandes
- **Solução**: Use métodos built-in e list comprehension

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Sistema de Agenda de Contatos**
   - Adicione, remova e liste contatos
   - Busque contatos por nome
   - Armazene nome, telefone e email
   - Valide dados de entrada

2. **Calculadora de Notas Escolares**
   - Calcule média de múltiplas disciplinas
   - Determine conceito e aprovação
   - Armazene histórico de notas
   - Gere relatório detalhado

3. **Jogo de Adivinhação com Histórico**
   - Implemente jogo com múltiplas rodadas
   - Armazene tentativas e resultados
   - Calcule estatísticas de jogo
   - Mostre ranking de jogadores

4. **Sistema de Estoque**
   - Gerencie produtos e quantidades
   - Adicione e remova itens
   - Calcule valor total do estoque
   - Alerte sobre produtos em baixa

5. **Gerador de Matrizes**
   - Crie matrizes de diferentes tamanhos
   - Implemente operações básicas
   - Calcule determinante e transposta
   - Visualize matrizes formatadas

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Tuplas e Dicionários** - estruturas de dados mais avançadas.

### O que você vai aprender:
- 📚 Tuplas - listas imutáveis
- 📚 Dicionários - estruturas chave-valor
- 📚 Métodos de dicionário
- 📚 Operações com tuplas e dicionários
- 📚 Aplicações práticas
- 📚 Estruturas de dados complexas

---

**Pratique as listas! São fundamentais para organizar dados! 🐍**

> 💡 **Dica**: Experimente criar listas com diferentes tipos de dados e veja como o Python lida com cada um. Isso vai ajudar a entender melhor as capacidades das listas.
