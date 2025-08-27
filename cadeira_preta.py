# 1. Cabeçalho em Python:
# O cabeçalho fica no início do arquivo e normalmente é feito com comentários (#).
# Ele pode conter informações como autor, data, versão, descrição do script ou instruções especiais (ex: #!/usr/bin/env python3 ou encoding).
# Serve para dar contexto ou configurar o arquivo, mas não faz parte do código que roda.

# 2. Diferença entre arquivo e docstring:
# Um arquivo Python é o próprio código que você escreve (.py).
# Uma docstring é um texto entre aspas triplas """ ... """ usado dentro de arquivos, funções, classes ou módulos para documentar o que o código faz.
# Enquanto o arquivo contém todas as instruções, a docstring é somente documentação interna.

# 3. Para que serve uma docstring no Python:
# A docstring explica o funcionamento de módulos, funções ou classes, descrevendo parâmetros, retorno e comportamento.
# Ela pode ser acessada durante a execução com help() ou .__doc__ e serve para facilitar a leitura do código e gerar documentação automática.



# formate o cabeçalho deste arquivo após completar os exercícios abaixo:

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    ...

import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...

