import numpy as np 
import pandas as pd
import argparse
import re


def initial_table(varis):
    num_v = len(varis)

    dados = []
    for i in range(2**num_v):
        linha = np.binary_repr(i, width=num_v)
        dados.append([int(x) for x in linha])
    
    return pd.DataFrame(dados, columns=varis)

def salvar(tabela):
    while True:
        exc = str(input('Salvar a tabela verdade em excel? [S/N] ')).upper().strip()
        if 'S' == exc:
            nome = str(input('Nome do arquivo excel: '))
            tabela.to_excel(nome+'.xlsx', index = False)
            break
        elif 'N' == exc:
            break
        else:
            print('Erro, tente de novo.')

def main(args):

    logics = args.input
    logics = logics.replace(' ', '').upper()
    varis = [x[1] for x in re.findall('\([A-Z]\)', logics)]
    varis = sorted(list(dict.fromkeys(varis)))

    tabela = initial_table(varis)


    while True:
        change=0
        Not = re.findall('NOT\([^(]*?\)', logics)
        if Not:
            change +=1
            for i in Not:
                pos = i[4:-1]
                new_col = f'[¬{pos}]'
                tabela[new_col] = tabela[pos] * (-1) +1  # 1 ->  -1  -> 0;  0 -> 0 -> 1
                logics = logics.replace(i, new_col)
        
        And = re.findall('\([^()]*?\)AND\([^()]*?\)', logics)
        if And:
            change +=1
            for i in And:
                pos = i[1:-1].split(')AND(')
                assert len(pos) == 2
                new_col = f'[{pos[0]}*{pos[1]}]'
                tabela[new_col] = np.bitwise_and(tabela[pos[0]], tabela[pos[1]])
                logics = logics.replace(i, new_col)
                
        Or = re.findall('\([^()]*?\)X?OR\([^()]*?\)', logics)
        if Or:
            change +=1
            for i in Or:
                if ')OR(' in i:
                    pos = i[1:-1].split(')OR(')
                    assert len(pos) == 2
                    new_col = f'[{pos[0]}+{pos[1]}]'
                    tabela[new_col] = np.bitwise_or(tabela[pos[0]], tabela[pos[1]])
                    logics = logics.replace(i, new_col)
                elif ')XOR(' in i:
                    pos = i[1:-1].split(')XOR(')
                    assert len(pos) == 2
                    new_col = f'[{pos[0]}⊕{pos[1]}]'
                    tabela[new_col] = np.bitwise_xor(tabela[pos[0]], tabela[pos[1]])
                    logics = logics.replace(i, new_col)

        if change == 0:
            break

    print(f'''{12*'='}PREVIEW{12*'='}\n\n{tabela}''')
    
    salvar(tabela)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', default=None, type=str, help="Insira o circuito booleano.")

    args = parser.parse_args()
    
    if args.input == None: 
        print('''
    Por favor, insira um input para o programa, após -i ou --input, exemplo:

    python logicGates.py -i "NOT((((A)AND(B))OR(NOT(C)))AND(D))"''')
    else:
        main(args)
