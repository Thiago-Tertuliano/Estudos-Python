# Aula 11: Tratamento de Exceções

## 🎯 Objetivos da Aula

- Entender o que são exceções e por que tratá-las
- Dominar o uso de try/except para capturar erros
- Aprender sobre diferentes tipos de exceções
- Compreender o uso de finally e else
- Praticar o uso de raise para lançar exceções
- Criar exceções customizadas
- Implementar tratamento de erros robusto

## 📚 Conteúdo Detalhado

### O que são Exceções?

Exceções são eventos que ocorrem durante a execução de um programa e interrompem o fluxo normal. Em Python, as exceções são objetos que representam erros e podem ser capturadas e tratadas.

#### Por que tratar exceções?
- **Robustez**: Evitar que o programa pare inesperadamente
- **Experiência do usuário**: Dar feedback apropriado sobre erros
- **Debugging**: Identificar e corrigir problemas
- **Recuperação**: Tentar resolver problemas automaticamente
- **Logging**: Registrar erros para análise posterior
- **Validação**: Verificar dados de entrada

### Tratamento Básico de Exceções

#### Try/Except Simples:
```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except:
    print("Ocorreu um erro!")
```

#### Try/Except Específico:
```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Digite um número válido!")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
except Exception as e:
    print(f"Erro inesperado: {e}")
```

#### Try/Except/Else:
```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Digite um número válido!")
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
else:
    # Executa apenas se não houver exceção
    print(f"Resultado: {resultado}")
    print("Operação realizada com sucesso!")
```

#### Try/Except/Finally:
```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
except PermissionError:
    print("Erro: Sem permissão para ler o arquivo!")
finally:
    # Sempre executa, mesmo se houver exceção
    try:
        arquivo.close()
        print("Arquivo fechado.")
    except:
        pass  # Ignora erro se arquivo não foi aberto
```

### Tipos de Exceções Comuns

#### ValueError:
```python
try:
    idade = int(input("Digite sua idade: "))
    print(f"Idade: {idade}")
except ValueError:
    print("Erro: Digite um número válido!")
```

#### TypeError:
```python
try:
    texto = "Python"
    resultado = texto + 5  # Erro: não pode somar string com int
except TypeError:
    print("Erro: Tipos incompatíveis para operação!")
```

#### IndexError:
```python
try:
    lista = [1, 2, 3, 4, 5]
    elemento = lista[10]  # Erro: índice fora do range
except IndexError:
    print("Erro: Índice fora do range da lista!")
```

#### KeyError:
```python
try:
    dicionario = {"nome": "João", "idade": 25}
    valor = dicionario["cidade"]  # Erro: chave não existe
except KeyError:
    print("Erro: Chave não encontrada no dicionário!")
```

#### FileNotFoundError:
```python
try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
```

#### PermissionError:
```python
try:
    with open("/etc/passwd", "w") as arquivo:
        arquivo.write("teste")
except PermissionError:
    print("Erro: Sem permissão para escrever no arquivo!")
```

### Múltiplos Except

#### Tratando Diferentes Exceções:
```python
def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except TypeError:
        print("Erro: Argumentos devem ser números!")
        return None
    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

# Testando a função
print(dividir_numeros(10, 2))      # 5.0
print(dividir_numeros(10, 0))      # Erro: Divisão por zero!
print(dividir_numeros("10", 2))    # Erro: Argumentos devem ser números!
```

#### Usando Tuplas para Múltiplas Exceções:
```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except (ValueError, ZeroDivisionError) as e:
    if isinstance(e, ValueError):
        print("Erro: Digite um número válido!")
    else:
        print("Erro: Divisão por zero!")
```

### Finally e Else

#### Finally - Sempre Executa:
```python
def processar_arquivo(nome_arquivo):
    arquivo = None
    try:
        arquivo = open(nome_arquivo, "r")
        conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado!")
        return None
    finally:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado.")

# Testando
resultado = processar_arquivo("teste.txt")
```

#### Else - Executa Apenas se Não Houver Exceção:
```python
def validar_email(email):
    try:
        if "@" not in email:
            raise ValueError("Email deve conter @")
        if "." not in email:
            raise ValueError("Email deve conter domínio válido")
    except ValueError as e:
        print(f"Email inválido: {e}")
        return False
    else:
        print("Email válido!")
        return True

# Testando
emails = ["usuario@email.com", "email_invalido", "usuario@"]
for email in emails:
    validar_email(email)
```

### Raise - Lançando Exceções

#### Raise Simples:
```python
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    if idade > 120:
        raise ValueError("Idade muito alta!")
    return "Idade válida"

# Testando
try:
    resultado = verificar_idade(-5)
except ValueError as e:
    print(f"Erro: {e}")
```

#### Raise com Exceção Específica:
```python
def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo!")
    return numero ** 0.5

# Testando
try:
    resultado = calcular_raiz_quadrada(-4)
    print(f"Raiz quadrada: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
```

#### Re-raise (Relançar Exceção):
```python
def processar_dados(dados):
    try:
        resultado = int(dados)
        return resultado
    except ValueError:
        print("Erro ao processar dados, relançando exceção...")
        raise  # Relança a exceção original

# Testando
try:
    resultado = processar_dados("abc")
except ValueError:
    print("Exceção capturada no nível superior")
```

### Exceções Customizadas

#### Criando Exceção Personalizada:
```python
class ErroValidacao(Exception):
    """Exceção personalizada para erros de validação"""
    pass

class ErroNegocio(Exception):
    """Exceção personalizada para erros de negócio"""
    def __init__(self, mensagem, codigo_erro=None):
        self.mensagem = mensagem
        self.codigo_erro = codigo_erro
        super().__init__(self.mensagem)

def validar_senha(senha):
    if len(senha) < 8:
        raise ErroValidacao("Senha deve ter pelo menos 8 caracteres!")
    
    if not any(c.isupper() for c in senha):
        raise ErroValidacao("Senha deve conter pelo menos uma letra maiúscula!")
    
    if not any(c.isdigit() for c in senha):
        raise ErroValidacao("Senha deve conter pelo menos um número!")
    
    return "Senha válida!"

def processar_pedido(valor):
    if valor <= 0:
        raise ErroNegocio("Valor do pedido deve ser positivo!", "VALOR_INVALIDO")
    
    if valor > 10000:
        raise ErroNegocio("Pedido muito alto, requer aprovação!", "PEDIDO_ALTO")
    
    return "Pedido processado com sucesso!"

# Testando exceções customizadas
try:
    resultado = validar_senha("abc")
except ErroValidacao as e:
    print(f"Erro de validação: {e}")

try:
    resultado = processar_pedido(15000)
except ErroNegocio as e:
    print(f"Erro de negócio: {e.mensagem} (Código: {e.codigo_erro})")
```

### Exemplos Práticos Avançados

#### Exemplo 1: Sistema de Validação Robusto

```python
# Sistema de validação robusto
print("=== SISTEMA DE VALIDAÇÃO ROBUSTO ===")

class ErroValidacao(Exception):
    pass

class ErroFormato(Exception):
    pass

def validar_cpf(cpf):
    """Valida formato de CPF"""
    # Remove caracteres não numéricos
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf_limpo) != 11:
        raise ErroFormato("CPF deve ter 11 dígitos")
    
    if cpf_limpo == cpf_limpo[0] * 11:
        raise ErroValidacao("CPF não pode ter todos os dígitos iguais")
    
    return True

def validar_email(email):
    """Valida formato de email"""
    if '@' not in email:
        raise ErroFormato("Email deve conter @")
    
    if '.' not in email:
        raise ErroFormato("Email deve conter domínio válido")
    
    if email.count('@') > 1:
        raise ErroFormato("Email deve conter apenas um @")
    
    return True

def validar_telefone(telefone):
    """Valida formato de telefone"""
    # Remove caracteres não numéricos
    telefone_limpo = ''.join(filter(str.isdigit, telefone))
    
    if len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
        raise ErroFormato("Telefone deve ter 10 ou 11 dígitos")
    
    return True

def validar_formulario(dados):
    """Valida formulário completo"""
    erros = {}
    
    # Validar CPF
    if 'cpf' in dados:
        try:
            validar_cpf(dados['cpf'])
        except (ErroFormato, ErroValidacao) as e:
            erros['cpf'] = str(e)
    
    # Validar email
    if 'email' in dados:
        try:
            validar_email(dados['email'])
        except ErroFormato as e:
            erros['email'] = str(e)
    
    # Validar telefone
    if 'telefone' in dados:
        try:
            validar_telefone(dados['telefone'])
        except ErroFormato as e:
            erros['telefone'] = str(e)
    
    if erros:
        raise ErroValidacao(f"Formulário inválido: {erros}")
    
    return "Formulário válido!"

# Testando o sistema
dados_teste = {
    'cpf': '123.456.789-00',
    'email': 'usuario@email.com',
    'telefone': '(11) 99999-9999'
}

try:
    resultado = validar_formulario(dados_teste)
    print(f"✅ {resultado}")
except ErroValidacao as e:
    print(f"❌ {e}")
```

#### Exemplo 2: Sistema de Arquivos com Tratamento de Erros

```python
# Sistema de arquivos com tratamento de erros
print("=== SISTEMA DE ARQUIVOS ===")

import os
import json
from datetime import datetime

class ErroArquivo(Exception):
    pass

class ErroPermissao(Exception):
    pass

def ler_arquivo_safe(caminho):
    """Lê arquivo com tratamento de erros"""
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        raise ErroArquivo(f"Arquivo '{caminho}' não encontrado")
    except PermissionError:
        raise ErroPermissao(f"Sem permissão para ler '{caminho}'")
    except UnicodeDecodeError:
        raise ErroArquivo(f"Erro de codificação no arquivo '{caminho}'")
    except Exception as e:
        raise ErroArquivo(f"Erro inesperado ao ler '{caminho}': {e}")

def escrever_arquivo_safe(caminho, conteudo):
    """Escreve arquivo com tratamento de erros"""
    try:
        # Criar diretório se não existir
        diretorio = os.path.dirname(caminho)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)
        
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        return True
    except PermissionError:
        raise ErroPermissao(f"Sem permissão para escrever em '{caminho}'")
    except Exception as e:
        raise ErroArquivo(f"Erro ao escrever '{caminho}': {e}")

def processar_arquivo_json(caminho):
    """Processa arquivo JSON com tratamento de erros"""
    try:
        conteudo = ler_arquivo_safe(caminho)
        dados = json.loads(conteudo)
        return dados
    except json.JSONDecodeError as e:
        raise ErroArquivo(f"Erro no formato JSON: {e}")
    except ErroArquivo:
        raise
    except Exception as e:
        raise ErroArquivo(f"Erro inesperado: {e}")

def salvar_log(mensagem, arquivo_log="app.log"):
    """Salva log com tratamento de erros"""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {mensagem}\n"
        
        with open(arquivo_log, 'a', encoding='utf-8') as arquivo:
            arquivo.write(log_entry)
    except Exception as e:
        print(f"Erro ao salvar log: {e}")

# Testando o sistema
def testar_sistema_arquivos():
    # Teste 1: Ler arquivo existente
    try:
        conteudo = ler_arquivo_safe("teste.txt")
        print("✅ Arquivo lido com sucesso")
    except ErroArquivo as e:
        print(f"❌ {e}")
        salvar_log(f"Erro ao ler arquivo: {e}")
    
    # Teste 2: Escrever arquivo
    try:
        dados = {"nome": "João", "idade": 25}
        conteudo_json = json.dumps(dados, indent=2)
        escrever_arquivo_safe("dados.json", conteudo_json)
        print("✅ Arquivo escrito com sucesso")
    except (ErroArquivo, ErroPermissao) as e:
        print(f"❌ {e}")
        salvar_log(f"Erro ao escrever arquivo: {e}")
    
    # Teste 3: Processar JSON
    try:
        dados = processar_arquivo_json("dados.json")
        print(f"✅ JSON processado: {dados}")
    except ErroArquivo as e:
        print(f"❌ {e}")
        salvar_log(f"Erro ao processar JSON: {e}")

# Executando testes
testar_sistema_arquivos()
```

#### Exemplo 3: Sistema de Conexão com Banco de Dados

```python
# Sistema de conexão com banco de dados
print("=== SISTEMA DE CONEXÃO COM BANCO ===")

class ErroConexao(Exception):
    pass

class ErroConsulta(Exception):
    pass

class ErroTransacao(Exception):
    pass

class BancoDeDados:
    def __init__(self):
        self.conectado = False
        self.dados = {}  # Simulando banco de dados
    
    def conectar(self):
        """Simula conexão com banco de dados"""
        try:
            # Simulando possível erro de conexão
            import random
            if random.random() < 0.3:  # 30% de chance de erro
                raise ConnectionError("Servidor indisponível")
            
            self.conectado = True
            print("✅ Conectado ao banco de dados")
            return True
        except ConnectionError as e:
            raise ErroConexao(f"Erro de conexão: {e}")
        except Exception as e:
            raise ErroConexao(f"Erro inesperado na conexão: {e}")
    
    def desconectar(self):
        """Desconecta do banco de dados"""
        self.conectado = False
        print("🔌 Desconectado do banco de dados")
    
    def executar_consulta(self, query):
        """Executa uma consulta"""
        if not self.conectado:
            raise ErroConexao("Não conectado ao banco de dados")
        
        try:
            # Simulando processamento da consulta
            if "SELECT" in query.upper():
                return {"resultado": "dados simulados"}
            elif "INSERT" in query.upper():
                return {"mensagem": "Registro inserido"}
            elif "UPDATE" in query.upper():
                return {"mensagem": "Registro atualizado"}
            elif "DELETE" in query.upper():
                return {"mensagem": "Registro deletado"}
            else:
                raise ErroConsulta("Query não reconhecida")
        except Exception as e:
            raise ErroConsulta(f"Erro na consulta: {e}")
    
    def executar_transacao(self, queries):
        """Executa múltiplas queries em uma transação"""
        if not self.conectado:
            raise ErroConexao("Não conectado ao banco de dados")
        
        resultados = []
        try:
            for query in queries:
                resultado = self.executar_consulta(query)
                resultados.append(resultado)
            
            print("✅ Transação executada com sucesso")
            return resultados
        except Exception as e:
            print("❌ Transação falhou, fazendo rollback")
            raise ErroTransacao(f"Erro na transação: {e}")

def operacao_banco_dados():
    """Executa operações no banco de dados"""
    db = BancoDeDados()
    
    try:
        # Tentar conectar
        db.conectar()
        
        # Executar consultas
        consultas = [
            "SELECT * FROM usuarios",
            "INSERT INTO usuarios (nome, email) VALUES ('João', 'joao@email.com')",
            "UPDATE usuarios SET ativo = true WHERE id = 1"
        ]
        
        resultados = db.executar_transacao(consultas)
        print("Resultados:", resultados)
        
    except ErroConexao as e:
        print(f"❌ Erro de conexão: {e}")
        salvar_log(f"Erro de conexão: {e}")
    except ErroConsulta as e:
        print(f"❌ Erro na consulta: {e}")
        salvar_log(f"Erro na consulta: {e}")
    except ErroTransacao as e:
        print(f"❌ Erro na transação: {e}")
        salvar_log(f"Erro na transação: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        salvar_log(f"Erro inesperado: {e}")
    finally:
        # Sempre desconectar
        db.desconectar()

# Executando o sistema
operacao_banco_dados()
```

### Boas Práticas

#### ✅ Faça:
- **Use exceções específicas** em vez de Exception genérica
- **Capture exceções no nível apropriado** - não muito alto, não muito baixo
- **Sempre use finally** para limpeza de recursos
- **Documente exceções** que sua função pode lançar
- **Use logging** para registrar erros importantes

#### ❌ Evite:
- **Capturar exceções muito genéricas** sem tratamento específico
- **Ignorar exceções** com pass vazio
- **Capturar exceções muito cedo** - deixe propagar quando apropriado
- **Usar exceções para controle de fluxo** - use if/else para lógica normal

#### 🔧 Solução de Problemas Comuns:

#### Erro: "UnboundLocalError"
- **Causa**: Variável usada antes de ser definida
- **Solução**: Inicialize variáveis ou use nonlocal/global

#### Erro: "AttributeError"
- **Causa**: Tentando acessar atributo que não existe
- **Solução**: Verifique se o objeto tem o atributo antes de usar

#### Erro: "KeyError"
- **Causa**: Tentando acessar chave que não existe no dicionário
- **Solução**: Use get() ou verifique se a chave existe

## 🛠️ Exercícios

Execute o arquivo `exercicios.py` para praticar os conceitos desta aula.

### Exercícios Propostos:

1. **Sistema de Validação de Dados**
   - Crie exceções customizadas para diferentes tipos de erro
   - Implemente validação robusta de formulários
   - Use try/except para tratar diferentes cenários
   - Implemente logging de erros

2. **Sistema de Arquivos Seguro**
   - Implemente operações de arquivo com tratamento de erros
   - Crie backup automático em caso de erro
   - Valide integridade de arquivos
   - Implemente recuperação de dados

3. **Sistema de Conexão de Rede**
   - Simule conexões com APIs externas
   - Implemente retry automático em caso de falha
   - Trate diferentes tipos de erro de rede
   - Implemente timeout e fallback

4. **Sistema de Cache com Tratamento de Erros**
   - Implemente cache com tratamento de erros
   - Trate erros de memória e disco
   - Implemente limpeza automática em caso de erro
   - Use finally para garantir limpeza

5. **Sistema de Logs Avançado**
   - Implemente diferentes níveis de log
   - Trate erros de escrita de log
   - Implemente rotação de arquivos de log
   - Use exceções customizadas para diferentes tipos de erro

## 🔗 Próxima Aula

Na próxima aula, vamos aprender sobre **Projeto Final** - integrando todos os conceitos aprendidos.

### O que você vai aprender:
- 📚 Integração de todos os conceitos
- 📚 Desenvolvimento de projeto completo
- 📚 Boas práticas de programação
- 📚 Debugging e otimização
- 📚 Documentação de código
- 📚 Próximos passos no aprendizado

---

**Pratique tratamento de exceções! São fundamentais para programas robustos! 🐍**

> 💡 **Dica**: Sempre pense em "e se algo der errado?" ao escrever código. Isso vai ajudar a criar programas mais robustos e confiáveis.
