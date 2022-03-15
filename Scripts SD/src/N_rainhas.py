
tabuleiro = [['R', '-', '-', '-'],['-','-','R','-'], ['-','-','-','-'], ['-','R','-','-']]

def print_tabuleiro(tabuleiro):
    for i in tabuleiro:
        print(i)

def valida_posicao(tabuleiro, n, posicao_rainha):
    # verifica se esxiste rainha na mesma linha
    if 'R' in tabuleiro[posicao_rainha[0]]:
        return False

    # verifica se tem rainha na mesma coluna
    if 'R' in [x[posicao_rainha[1]] for x in tabuleiro]:
        return False

    # verifica diagonais
    

    for i in n:
        for j in n:
            pass


n = 4
print_tabuleiro(tabuleiro)