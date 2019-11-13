import socket
import argparse

#cores
RED   = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"

#funcao responsavel pelos scan
def scan(alvo, porta):
    '''
        Verifica se a variavel porta é do tipo list;
        se porta for do tipo list, a variavel i (inicial) 
        recebe o menor valor da lista, e f (final) recebe o maior valor
    '''
    if type(porta) is list:
        i = min(porta) #i (inicial) recebe o menor valor da lista porta
        f = max(porta) #f (final) recebe o maior valor da lista porta
    else:
        i = porta #caso a variavel porta não seja do tipo lista, 
        f = porta #as variaveis recebem o memos valor
    
    for p in range(i, f+1): #gera numeros de i até f+1 ex: range(1, 5) = 1,2,3,4,5 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        s.settimeout(1)
        if s.connect_ex((alvo, p)) == 0:
            print('porta', p, GREEN + ' aberta' + RESET)
            s.close()
        else:
            print('porta', p, RED + 'fechada' + RESET)

#funcao responsavel por tratar argumentos
def argumentos():
    parser = argparse.ArgumentParser('pyscan.py')
    parser.add_argument('-a', '--alvo', required = True)
    parser.add_argument('-p', '--porta', required = True)

    args = parser.parse_args()

    if args.porta.find('-') != -1:
        args.porta = args.porta.split('-')

        if len(args.porta) > 2:
            print(RED + 'Passe apenas a porna inicial e a final ex: --porta 1-1000' + RESET)
            exit()
        else:
            try:
                args.porta[0] = int(args.porta[0])
                args.porta[1] = int(args.porta[1])
            except:
                print(RED + 'As portas devem ser numeros inteiros ex: --porta 1-1000' + RESET)
                exit()
    else:
        try:
            args.porta = int(args.porta)
        except:
            print(RED + 'As portas devem ser numeros inteiros ex: --porta 1-1000' + RESET)
            exit()

    return args

#MAIN

args = argumentos()

scan(args.alvo, args.porta)