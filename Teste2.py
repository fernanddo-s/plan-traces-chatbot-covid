with open('./files/plan-traces-teste.txt', 'r') as arquivo:
    for linha in arquivo:
        valores_numericos = [int(valor) for valor in linha.strip().split(':')]
        print(valores_numericos)