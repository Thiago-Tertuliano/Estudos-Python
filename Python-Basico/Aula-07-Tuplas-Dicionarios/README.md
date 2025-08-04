# Aula 7: Tuplas e Dicionários

## 🎯 Objetivos da Aula

- Entender o que são tuplas e suas características de imutabilidade
- Dominar o uso de dicionários para estruturas chave-valor
- Aprender métodos específicos de tuplas e dicionários
- Compreender quando usar cada estrutura de dados
- Praticar operações com tuplas e dicionários em cenários reais
- Trabalhar com estruturas de dados complexas e aninhadas

## 📚 Conteúdo Detalhado

### O que são Tuplas?

Tuplas são estruturas de dados similares às listas, mas com uma diferença fundamental: são **imutáveis**. Uma vez criada, uma tupla não pode ser modificada.

#### Características das Tuplas:
- **Imutáveis**: Não podem ser alteradas após a criação
- **Ordenadas**: Os elementos mantêm a ordem de inserção
- **Heterogêneas**: Podem conter diferentes tipos de dados
- **Indexadas**: Acessadas por posição (índice)
- **Eficientes**: Mais rápidas que listas para operações simples
- **Hasháveis**: Podem ser usadas como chaves em dicionários

#### Por que usar tuplas?
- **Dados que não devem mudar**: Coordenadas, configurações
- **Chaves de dicionários**: Tuplas podem ser chaves
- **Retorno de funções**: Múltiplos valores de retorno
- **Performance**: Mais rápidas que listas para leitura
- **Integridade de dados**: Garantir que dados não sejam alterados

### Criando Tuplas

#### Tupla Vazia:
```python
# Criação de tupla vazia
tupla_vazia = ()
tupla_vazia2 = tuple()

print(f"Tupla vazia: {tupla_vazia}")
print(f"Tipo: {type(tupla_vazia)}")
```

#### Tupla com Elementos:
```python
# Tupla com números
coordenadas = (10, 20)
print(f"Coordenadas: {coordenadas}")

# Tupla com strings
cores = ("vermelho", "verde", "azul")
print(f"Cores: {cores}")

# Tupla mista
pessoa = ("João", 25, 1.75, True)
print(f"Pessoa: {pessoa}")

# Tupla com um elemento (vírgula necessária)
singleton = (42,)
print(f"Singleton: {singleton}")
```

#### Tupla usando range():
```python
# Tupla de 0 a 4
tupla1 = tuple(range(5))
print(f"Range(5): {tupla1}")

# Tupla de 1 a 10
tupla2 = tuple(range(1, 11))
print(f"Range(1, 11): {tupla2}")

# Tupla com passo
tupla3 = tuple(range(0, 20, 2))
print(f"Range(0, 20, 2): {tupla3}")
```

### Acessando Elementos de Tuplas

#### Indexação e Slicing:
```python
coordenadas = (10, 20, 30, 40, 50)

# Primeiro elemento
primeiro = coordenadas[0]
print(f"Primeiro: {primeiro}")

# Último elemento
ultimo = coordenadas[-1]
print(f"Último: {ultimo}")

# Slicing
meio = coordenadas[1:4]
print(f"Meio: {meio}")

# Com passo
pares = coordenadas[::2]
print(f"Pares: {pares}")
```

#### Desempacotamento:
```python
# Desempacotamento básico
coordenadas = (10, 20)
x, y = coordenadas
print(f"x = {x}, y = {y}")

# Desempacotamento com resto
valores = (1, 2, 3, 4, 5)
primeiro, segundo, *resto = valores
print(f"Primeiro: {primeiro}")
print(f"Segundo: {segundo}")
print(f"Resto: {resto}")

# Desempacotamento ignorando valores
pessoa = ("João", 25, "São Paulo", "Brasil")
nome, idade, *_ = pessoa
print(f"Nome: {nome}, Idade: {idade}")
```

### Operações com Tuplas

#### Operações Básicas:
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenação
concatenada = tupla1 + tupla2
print(f"Concatenada: {concatenada}")

# Repetição
repetida = tupla1 * 3
print(f"Repetida: {repetida}")

# Verificando se elemento existe
existe = 2 in tupla1
print(f"2 existe na tupla: {existe}")

# Contando ocorrências
contagem = tupla1.count(2)
print(f"Ocorrências de 2: {contagem}")

# Encontrando índice
indice = tupla1.index(2)
print(f"Índice de 2: {indice}")
```

#### Funções Built-in:
```python
numeros = (3, 1, 4, 1, 5, 9, 2, 6)

print(f"Tupla: {numeros}")
print(f"Tamanho: {len(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")
print(f"Soma: {sum(numeros)}")
```

### O que são Dicionários?

Dicionários são estruturas de dados que armazenam pares chave-valor. Cada elemento é uma associação entre uma chave única e um valor.

#### Características dos Dicionários:
- **Mutáveis**: Podem ser alterados após a criação
- **Não ordenados** (até Python 3.7): A ordem não é garantida
- **Chaves únicas**: Cada chave aparece apenas uma vez
- **Chaves imutáveis**: Strings, números, tuplas podem ser chaves
- **Valores heterogêneos**: Podem ser de qualquer tipo
- **Acesso rápido**: Busca eficiente por chave

#### Por que usar dicionários?
- **Dados estruturados**: Informações com identificadores
- **Configurações**: Parâmetros nomeados
- **Cache/Memoização**: Armazenar resultados de cálculos
- **Contadores**: Contar ocorrências de elementos
- **Mapeamentos**: Relacionar dados

### Criando Dicionários

#### Dicionário Vazio:
```python
# Criação de dicionário vazio
dicionario_vazio = {}
dicionario_vazio2 = dict()

print(f"Dicionário vazio: {dicionario_vazio}")
print(f"Tipo: {type(dicionario_vazio)}")
```

#### Dicionário com Elementos:
```python
# Dicionário básico
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
print(f"Pessoa: {pessoa}")

# Dicionário com diferentes tipos
config = {
    "porta": 8080,
    "host": "localhost",
    "ativo": True,
    "cores": ["vermelho", "verde", "azul"]
}
print(f"Config: {config}")

# Dicionário aninhado
empresa = {
    "nome": "TechCorp",
    "funcionarios": {
        "João": {"cargo": "Desenvolvedor", "salario": 5000},
        "Maria": {"cargo": "Designer", "salario": 4500}
    }
}
print(f"Empresa: {empresa}")
```

#### Usando dict():
```python
# A partir de lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
dicionario = dict(pares)
print(f"De lista de tuplas: {dicionario}")

# A partir de argumentos nomeados
dicionario2 = dict(nome="João", idade=25, cidade="SP")
print(f"De argumentos: {dicionario2}")

# A partir de zip
chaves = ["a", "b", "c"]
valores = [1, 2, 3]
dicionario3 = dict(zip(chaves, valores))
print(f"De zip: {dicionario3}")
```

### Acessando Elementos de Dicionários

#### Acesso Básico:
```python
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo",
    "profissao": "Desenvolvedor"
}

# Acesso por chave
nome = pessoa["nome"]
print(f"Nome: {nome}")

# Acesso seguro (não gera erro se chave não existir)
idade = pessoa.get("idade", 0)
print(f"Idade: {idade}")

# Verificando se chave existe
if "email" in pessoa:
    print(f"Email: {pessoa['email']}")
else:
    print("Email não encontrado")
```

#### Acesso a Dicionários Aninhados:
```python
empresa = {
    "nome": "TechCorp",
    "funcionarios": {
        "João": {"cargo": "Desenvolvedor", "salario": 5000},
        "Maria": {"cargo": "Designer", "salario": 4500}
    }
}

# Acesso aninhado
cargo_joao = empresa["funcionarios"]["João"]["cargo"]
print(f"Cargo do João: {cargo_joao}")

# Acesso seguro aninhado
salario_maria = empresa.get("funcionarios", {}).get("Maria", {}).get("salario", 0)
print(f"Salário da Maria: {salario_maria}")
```

### Modificando Dicionários

#### Adicionando e Modificando:
```python
pessoa = {"nome": "João", "idade": 25}

# Adicionando nova chave
pessoa["cidade"] = "São Paulo"
print(f"Após adicionar cidade: {pessoa}")

# Modificando valor existente
pessoa["idade"] = 26
print(f"Após modificar idade: {pessoa}")

# Adicionando múltiplos elementos
pessoa.update({
    "profissao": "Desenvolvedor",
    "email": "joao@email.com"
})
print(f"Após update: {pessoa}")
```

#### Removendo Elementos:
```python
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo",
    "profissao": "Desenvolvedor"
}

# Removendo por chave
idade_removida = pessoa.pop("idade")
print(f"Idade removida: {idade_removida}")
print(f"Após remover idade: {pessoa}")

# Removendo último item (Python 3.7+)
ultimo_item = pessoa.popitem()
print(f"Último item removido: {ultimo_item}")
print(f"Após popitem: {pessoa}")

# Removendo chave específica
del pessoa["cidade"]
print(f"Após del: {pessoa}")

# Limpando dicionário
pessoa.clear()
print(f"Após clear: {pessoa}")
```

### Métodos de Dicionário

#### Métodos de Busca:
```python
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Obtendo chaves
chaves = pessoa.keys()
print(f"Chaves: {list(chaves)}")

# Obtendo valores
valores = pessoa.values()
print(f"Valores: {list(valores)}")

# Obtendo itens
itens = pessoa.items()
print(f"Itens: {list(itens)}")

# Verificando se chave existe
existe_nome = "nome" in pessoa
print(f"'nome' existe: {existe_nome}")

# Obtendo valor com padrão
idade = pessoa.get("idade", 0)
email = pessoa.get("email", "Não informado")
print(f"Idade: {idade}")
print(f"Email: {email}")
```

#### Métodos de Cópia:
```python
original = {"a": 1, "b": 2, "c": 3}

# Cópia superficial
copia1 = original.copy()
copia2 = dict(original)

print(f"Original: {original}")
print(f"Cópia 1: {copia1}")
print(f"Cópia 2: {copia2}")

# Verificando se são objetos diferentes
print(f"Original é copia1: {original is copia1}")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Sistema de Cadastro de Produtos

```python
# Sistema de cadastro de produtos
print("=== SISTEMA DE CADASTRO DE PRODUTOS ===")

produtos = {}

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Buscar produto")
    print("3. Listar produtos")
    print("4. Atualizar produto")
    print("5. Remover produto")
    print("6. Calcular valor total")
    print("7. Sair")
    
    opcao = input("\nDigite sua opção (1-7): ")
    
    if opcao == "1":
        codigo = input("Digite o código do produto: ").strip()
        if codigo and codigo not in produtos:
            nome = input("Digite o nome do produto: ").strip()
            try:
                preco = float(input("Digite o preço: R$ "))
                quantidade = int(input("Digite a quantidade: "))
                
                if preco >= 0 and quantidade >= 0:
                    produtos[codigo] = {
                        "nome": nome,
                        "preco": preco,
                        "quantidade": quantidade
                    }
                    print(f"✅ Produto '{nome}' adicionado!")
                else:
                    print("❌ Preço e quantidade devem ser positivos!")
            except ValueError:
                print("❌ Digite valores numéricos válidos!")
        else:
            print("❌ Código inválido ou produto já existe!")
            
    elif opcao == "2":
        codigo = input("Digite o código do produto: ").strip()
        if codigo in produtos:
            produto = produtos[codigo]
            print(f"\nProduto encontrado:")
            print(f"Código: {codigo}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Valor total: R$ {produto['preco'] * produto['quantidade']:.2f}")
        else:
            print("❌ Produto não encontrado!")
            
    elif opcao == "3":
        if produtos:
            print("\n=== LISTA DE PRODUTOS ===")
            for codigo, produto in produtos.items():
                valor_total = produto['preco'] * produto['quantidade']
                print(f"{codigo}: {produto['nome']} - R$ {produto['preco']:.2f} x {produto['quantidade']} = R$ {valor_total:.2f}")
        else:
            print("❌ Nenhum produto cadastrado!")
            
    elif opcao == "4":
        codigo = input("Digite o código do produto: ").strip()
        if codigo in produtos:
            print(f"Produto atual: {produtos[codigo]}")
            
            campo = input("Campo a atualizar (nome/preco/quantidade): ").strip()
            if campo in ["nome", "preco", "quantidade"]:
                novo_valor = input(f"Novo valor para {campo}: ").strip()
                
                if campo == "nome":
                    produtos[codigo][campo] = novo_valor
                    print("✅ Nome atualizado!")
                else:
                    try:
                        valor_numerico = float(novo_valor) if campo == "preco" else int(novo_valor)
                        if valor_numerico >= 0:
                            produtos[codigo][campo] = valor_numerico
                            print(f"✅ {campo} atualizado!")
                        else:
                            print("❌ Valor deve ser positivo!")
                    except ValueError:
                        print("❌ Digite um valor numérico válido!")
            else:
                print("❌ Campo inválido!")
        else:
            print("❌ Produto não encontrado!")
            
    elif opcao == "5":
        codigo = input("Digite o código do produto: ").strip()
        if codigo in produtos:
            produto_removido = produtos.pop(codigo)
            print(f"✅ Produto '{produto_removido['nome']}' removido!")
        else:
            print("❌ Produto não encontrado!")
            
    elif opcao == "6":
        if produtos:
            valor_total = sum(produto['preco'] * produto['quantidade'] for produto in produtos.values())
            quantidade_total = sum(produto['quantidade'] for produto in produtos.values())
            print(f"\n=== RESUMO ===")
            print(f"Quantidade de produtos: {len(produtos)}")
            print(f"Quantidade total de itens: {quantidade_total}")
            print(f"Valor total do estoque: R$ {valor_total:.2f}")
        else:
            print("❌ Nenhum produto cadastrado!")
            
    elif opcao == "7":
        print("👋 Obrigado por usar o sistema!")
        break
        
    else:
        print("❌ Opção inválida!")
```

#### Exemplo 2: Sistema de Notas Escolares

```python
# Sistema de notas escolares
print("=== SISTEMA DE NOTAS ESCOLARES ===")

alunos = {}

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar aluno")
    print("2. Adicionar nota")
    print("3. Calcular médias")
    print("4. Listar alunos")
    print("5. Buscar aluno")
    print("6. Relatório da turma")
    print("7. Sair")
    
    opcao = input("\nDigite sua opção (1-7): ")
    
    if opcao == "1":
        matricula = input("Digite a matrícula: ").strip()
        if matricula and matricula not in alunos:
            nome = input("Digite o nome do aluno: ").strip()
            if nome:
                alunos[matricula] = {
                    "nome": nome,
                    "notas": [],
                    "frequencia": 0
                }
                print(f"✅ Aluno '{nome}' adicionado!")
            else:
                print("❌ Nome não pode estar vazio!")
        else:
            print("❌ Matrícula inválida ou aluno já existe!")
            
    elif opcao == "2":
        if alunos:
            print("\nAlunos disponíveis:")
            for matricula, dados in alunos.items():
                print(f"{matricula}: {dados['nome']}")
            
            matricula = input("Digite a matrícula: ").strip()
            if matricula in alunos:
                try:
                    nota = float(input("Digite a nota: "))
                    if 0 <= nota <= 10:
                        alunos[matricula]["notas"].append(nota)
                        print(f"✅ Nota {nota} adicionada para {alunos[matricula]['nome']}!")
                    else:
                        print("❌ Nota deve estar entre 0 e 10!")
                except ValueError:
                    print("❌ Digite um número válido!")
            else:
                print("❌ Aluno não encontrado!")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "3":
        if alunos:
            print("\n=== MÉDIAS DOS ALUNOS ===")
            for matricula, dados in alunos.items():
                notas = dados["notas"]
                if notas:
                    media = sum(notas) / len(notas)
                    status = "Aprovado" if media >= 7 else "Reprovado"
                    print(f"{dados['nome']}: {media:.2f} ({status})")
                else:
                    print(f"{dados['nome']}: Sem notas")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "4":
        if alunos:
            print("\n=== LISTA DE ALUNOS ===")
            for matricula, dados in alunos.items():
                notas = dados["notas"]
                print(f"{matricula}: {dados['nome']} - {len(notas)} notas")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "5":
        if alunos:
            matricula = input("Digite a matrícula: ").strip()
            if matricula in alunos:
                dados = alunos[matricula]
                notas = dados["notas"]
                print(f"\nAluno: {dados['nome']}")
                print(f"Matrícula: {matricula}")
                print(f"Notas: {notas}")
                if notas:
                    media = sum(notas) / len(notas)
                    print(f"Média: {media:.2f}")
                    print(f"Status: {'Aprovado' if media >= 7 else 'Reprovado'}")
            else:
                print("❌ Aluno não encontrado!")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "6":
        if alunos:
            print("\n=== RELATÓRIO DA TURMA ===")
            
            total_alunos = len(alunos)
            alunos_com_notas = sum(1 for dados in alunos.values() if dados["notas"])
            
            if alunos_com_notas > 0:
                todas_notas = []
                for dados in alunos.values():
                    todas_notas.extend(dados["notas"])
                
                media_geral = sum(todas_notas) / len(todas_notas)
                aprovados = sum(1 for dados in alunos.values() 
                              if dados["notas"] and sum(dados["notas"]) / len(dados["notas"]) >= 7)
                
                print(f"Total de alunos: {total_alunos}")
                print(f"Alunos com notas: {alunos_com_notas}")
                print(f"Média geral: {media_geral:.2f}")
                print(f"Aprovados: {aprovados}")
                print(f"Reprovados: {alunos_com_notas - aprovados}")
                print(f"Taxa de aprovação: {(aprovados/alunos_com_notas)*100:.1f}%")
            else:
                print("Nenhum aluno tem notas registradas!")
        else:
            print("❌ Nenhum aluno cadastrado!")
            
    elif opcao == "7":
        print("👋 Obrigado por usar o sistema!")
        break
        
    else:
        print("❌ Opção inválida!")
```

#### Exemplo 3: Jogo de Palavras

```python
# Jogo de palavras
print("=== JOGO DE PALAVRAS ===")

# Dicionário de palavras por categoria
palavras = {
    "animais": ["cachorro", "gato", "elefante", "girafa", "leão"],
    "frutas": ["maçã", "banana", "laranja", "uva", "morango"],
    "cores": ["vermelho", "azul", "verde", "amarelo", "roxo"],
    "profissoes": ["médico", "professor", "engenheiro", "advogado", "dentista"]
}

pontuacao = {}
categoria_atual = None
palavra_atual = None

def escolher_palavra():
    import random
    categoria = random.choice(list(palavras.keys()))
    palavra = random.choice(palavras[categoria])
    return categoria, palavra

def verificar_palavra(tentativa, palavra):
    return tentativa.lower().strip() == palavra.lower()

# Loop principal do jogo
while True:
    print("\nEscolha uma opção:")
    print("1. Jogar")
    print("2. Ver pontuação")
    print("3. Sair")
    
    opcao = input("\nDigite sua opção (1-3): ")
    
    if opcao == "1":
        if not categoria_atual or not palavra_atual:
            categoria_atual, palavra_atual = escolher_palavra()
        
        print(f"\nCategoria: {categoria_atual}")
        print(f"Dica: A palavra tem {len(palavra_atual)} letras")
        
        tentativas = 0
        max_tentativas = 3
        
        while tentativas < max_tentativas:
            tentativa = input(f"\nTentativa {tentativas + 1}/{max_tentativas}: ")
            tentativas += 1
            
            if verificar_palavra(tentativa, palavra_atual):
                print(f"🎉 PARABÉNS! Você acertou!")
                
                # Atualizar pontuação
                jogador = input("Digite seu nome: ").strip()
                if jogador:
                    pontuacao[jogador] = pontuacao.get(jogador, 0) + 1
                    print(f"Pontuação atual de {jogador}: {pontuacao[jogador]}")
                
                categoria_atual, palavra_atual = escolher_palavra()
                break
            else:
                if tentativas < max_tentativas:
                    print("❌ Tente novamente!")
                else:
                    print(f"😔 Game Over! A palavra era '{palavra_atual}'")
                    categoria_atual, palavra_atual = escolher_palavra()
                    
    elif opcao == "2":
        if pontuacao:
            print("\n=== PONTUAÇÃO ===")
            # Ordenar por pontuação (decrescente)
            ranking = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)
            for i, (jogador, pontos) in enumerate(ranking, 1):
                print(f"{i}. {jogador}: {pontos} pontos")
        else:
            print("❌ Nenhuma pontuação registrada!")
            
    elif opcao == "3":
        print("👋 Obrigado por jogar!")
        break
        
    else:
        print("❌ Opção inválida!")
```

### Boas Práticas

#### ✅ Faça:
- **Use tuplas para dados imutáveis**: Coordenadas, configurações
- **Use dicionários para dados estruturados**: Informações com identificadores
- **Escolha chaves descritivas**: Nomes claros para as chaves
- **Use get() para acesso seguro**: Evite KeyError
- **Comente estruturas complexas**: Explique a organização dos dados

#### ❌ Evite:
- **Modificar tuplas**: Elas são imutáveis por design
- **Usar listas como chaves**: Apenas tipos imutáveis podem ser chaves
- **Dicionários muito aninhados**: Quebre em estruturas mais simples
- **Ignorar performance**: Tuplas são mais rápidas que listas para leitura

#### 🔧 Solução de Problemas Comuns:

#### Erro: "TypeError: unhashable type"
- **Causa**: Tentando usar lista como chave de dicionário
- **Solução**: Use tuplas ou strings como chaves

#### Erro: "KeyError"
- **Causa**: Acessando chave inexistente
- **Solução**: Use get() ou verifique se chave existe

#### Erro: "TypeError: 'tuple' object does not support item assignment"
- **Causa**: Tentando modificar tupla
- **Solução**: Use lista se precisar modificar

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Sistema de Agenda de Contatos Avançado**
   - Use dicionários para armazenar contatos
   - Implemente busca por nome, telefone, email
   - Adicione categorias de contatos
   - Gere relatórios de contatos

2. **Calculadora de Estatísticas com Tuplas**
   - Use tuplas para coordenadas e pontos
   - Calcule distância entre pontos
   - Implemente área de figuras geométricas
   - Trabalhe com conjuntos de dados

3. **Sistema de Biblioteca**
   - Gerencie livros com dicionários
   - Implemente sistema de empréstimo
   - Controle de usuários e prazos
   - Relatórios de livros mais populares

4. **Jogo de Quiz**
   - Use dicionários para perguntas e respostas
   - Implemente diferentes categorias
   - Sistema de pontuação
   - Ranking de jogadores

5. **Sistema de Configurações**
   - Use tuplas para configurações imutáveis
   - Dicionários para configurações mutáveis
   - Validação de configurações
   - Backup e restauração de configurações

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Strings Avançadas** - manipulação e formatação avançada de texto.

### O que você vai aprender:
- 📚 Métodos de string avançados
- 📚 Formatação de strings
- 📚 Expressões regulares básicas
- 📚 Manipulação de texto
- 📚 Validação de strings
- 📚 Processamento de dados textuais

---

**Pratique tuplas e dicionários! São fundamentais para estruturar dados! 🐍**

> 💡 **Dica**: Experimente criar estruturas de dados complexas combinando tuplas e dicionários. Isso vai ajudar a entender quando usar cada um.
