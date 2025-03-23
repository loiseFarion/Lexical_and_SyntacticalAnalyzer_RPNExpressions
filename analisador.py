# Helena Kuchinski Ferreira
# Loise Andruski Farion
# Grupo Projeto Compilador 1
import sys
import re
import logging
from antlr4 import *
from SintaticoLexer import SintaticoLexer
from SintaticoParser import SintaticoParser
from SintaticoListener import SintaticoListener
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
import matplotlib.pyplot as plt
import antlr4 

# Definição de constantes para representar dado
parentesesA = "ParentesesAberto"
numInteiro = "Inteiro"
numFloat = "Float"
opAritmetico = "OperadorAritmetico"
opRelacionais = "OperadorRelacional"
opBusca = "OperadorDeBusca"
opAtribuicao = "OperadorAtribuicao"
parentesesF = "ParenteseFechado"
fim = "Fim"
memVer = "MEM"
resVer = "RES"
If = "if"
Else = "else"
For = "for"
ERRO = "ERRO"
constante = "Constante"


# Analisador Lexico
def mefparentesesA(dado, expressao, contador, stringTokens, index):
  if dado == '(':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(parentesesA)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefparentesesF(dado, expressao, contador, stringTokens, index)


def mefparentesesF(dado, expressao, contador, stringTokens, index):
  if len(expressao) - 1 == contador:
    if dado == ')':
      string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(parentesesF)
      stringTokens.append(string)
      mefFim(contador, stringTokens, index)
  elif dado == ')':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(parentesesF)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefNum(dado, expressao, contador, stringTokens, index)


def mefNum(dado, expressao, contador, stringTokens, index):
  numTemp = dado.replace('.', '', 1)
  if dado.isdigit() or numTemp.isdigit():
    dado = float(dado)
    if isinstance(dado, float) and dado.is_integer():
      dado = int(dado)
    string = str(dado) + ' / ' + str(type(dado)) + ' / '
    if type(dado) == float:
      string += str(numFloat)
    elif type(dado) == int:
      string += str(numInteiro)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefOperador(dado, expressao, contador, stringTokens, index)


def mefOperador(dado, expressao, contador, stringTokens, index):
  if dado in ['+', '-', '*', '|', '/', '%', '^']:
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(opAritmetico)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefMEM(dado, expressao, contador, stringTokens, index)


def mefMEM(dado, expressao, contador, stringTokens, index):
  if dado == 'MEM':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(memVer)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefRES(dado, expressao, contador, stringTokens, index)


def mefRES(dado, expressao, contador, stringTokens, index):
  if dado == 'RES':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(resVer)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefIf(dado, expressao, contador, stringTokens, index)


def mefIf(dado, expressao, contador, stringTokens, index):
  if dado == 'if':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(If)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefElse(dado, expressao, contador, stringTokens, index)


def mefElse(dado, expressao, contador, stringTokens, index):
  if dado == 'else':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(Else)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefFor(dado, expressao, contador, stringTokens, index)


def mefFor(dado, expressao, contador, stringTokens, index):
  if dado == 'for':
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(For)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefComparador(dado, expressao, contador, stringTokens, index)


def mefComparador(dado, expressao, contador, stringTokens, index):
  opRela = ['==', '<', '>', '<=', '>=', '!=']
  opBus = ['in', 'not in']
  opAtri = ['=', '+=', '-=', '*=', '/=', '%=', '^=', '|=']

  if dado in opRela:
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(opRelacionais)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  elif dado in opBus:
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(opBusca)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  elif dado in opAtri:
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(opAtribuicao)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefConstantes(dado, expressao, contador, stringTokens, index)


def mefConstantes(dado, expressao, contador, stringTokens, index):
  constantes = ['i', 'range', ':']
  if dado in constantes:
    string = str(dado) + ' / ' + str(type(dado)) + ' / ' + str(constante)
    stringTokens.append(string)
    contador += 1
    dado = expressao[contador]
    mefResto(dado, expressao, contador, stringTokens, index)
  else:
    mefERRO(dado, expressao, contador, stringTokens, index)


def mefResto(dado, expressao, contador, stringTokens, index):
  if len(expressao) - 1 == contador:
    mefparentesesF(dado, expressao, contador, stringTokens, index)
  else:
    mefparentesesA(dado, expressao, contador, stringTokens, index)


def mefFim(contador, stringTokens, index):
  listaIndexValidos.append(index)
  contador = 0
  finalString = ' '
  string = str(finalString) + ' / ' + str(type(finalString)) + ' / ' + str(fim)
  stringTokens.append(string)
  return stringTokens, listaIndexValidos, contador


def mefERRO(dado, expressao, contador, stringTokens, index):
  while contador > 0:
    stringTokens.pop()
    contador -= 1
  contador = 0
  expressaoInvalida = ' '.join(expressao)
  erro = print("Erro léxico na linha:", index + 1, "na expressão:",
               expressaoInvalida)
  return contador, expressaoInvalida


# Analisador Sintático
class MeuErrorListener(ErrorListener):

  def __init__(self, inputString, linhas):
    super().__init__()
    self.inputString = inputString.replace('\n', '')
    self.linhas = linhas

  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    print(
        f"Erro na linha {self.linhas} na expressão: {self.inputString}, descrição do erro: {msg}"
    )


def analisadorSintatico(input_expr, i):
  input_stream = InputStream(input_expr)
  lexer = SintaticoLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = SintaticoParser(stream)
  parser.removeErrorListeners()
  parser.addErrorListener(MeuErrorListener(input_expr, i))
  tree = parser.program()
  print(tree.toStringTree(recog=parser))

nomeArquivo = sys.argv[1]
nomeArquivo = nomeArquivo.lower()

if not nomeArquivo.endswith(".txt"):
  nomeArquivo += ".txt"
aberturaArquivo = False
try:
  arquivoTxt = open(nomeArquivo, "r")
  linhas = arquivoTxt.readlines()
  aberturaArquivo = True
except:
  print("Erro ao abrir o arquivo")

if aberturaArquivo == True:
  expressaoConta = []
  for expressao in linhas:
    expressao = expressao.replace(',', '.')
    expressaoSplit = []
    dado = re.findall(r'\(|\)|\d+(?:\.\d+)?|\d+|[^\(\) ]+', expressao)
    dadoSemNovaLinha = [t.replace('\n', '') for t in dado]
    dadoSemEspacos = [t for t in dadoSemNovaLinha if t.strip()]
    expressaoSplit.extend(dadoSemEspacos)
    expressaoConta.append(expressaoSplit)

  index = 0
  contador = 0
  stringTokens = []
  listaIndexValidos = []

print('Análise Lexica:\n')

while index < len(expressaoConta):
  i = expressaoConta[index][0]
  mefparentesesA(i, expressaoConta[index], contador, stringTokens, index)
  index += 1
print('\nString de Tokens: ', stringTokens, '\n')

print('Análise Sintática:\n')
for i in listaIndexValidos:
  expTemp = linhas[i]
  if 'for' in expTemp:
    expTemp = re.sub(r'\b(for\b)', r'$ $ \1', expTemp)
  elif 'if' in expTemp:
    expTemp = re.sub(r'\b(if\b)', r'$ $ \1', expTemp)
  elif 'RES' in expTemp:
    expTemp = re.sub(r'(\d+)\s+(RES)', r'$ \1 \2', expTemp)

  analisadorSintatico(expTemp, i + 1)
  print('\n')
