def ler_arquivo_transicoes(file_path):
    with open(file_path, 'r') as file:
        linhas = file.readlines()
    
    planos = {}
    plano_atual = None
    
    for linha in linhas:
        linha = linha.strip()
        if linha.startswith("Plan trace"):
            plano_atual = linha
            planos[plano_atual] = []
        elif linha:
            planos[plano_atual].append(linha)
    
    return planos

def ler_arquivo_condicoes(file_path):
    with open(file_path, 'r') as file:
        linhas = file.readlines()
    
    condicoes = {}
    
    for linha in linhas:
        linha = linha.strip()
        if linha:
            estado, condicao = linha.split(": ", 1)
            condicoes[estado] = condicao
    
    return condicoes

def adicionar_condicoes(planos, condicoes):
    resultado = []
    
    for plano, transicoes in planos.items():
        resultado.append(plano)
        resultado.extend(transicoes)
        resultado.append("")
        
        estados = set()
        for transicao in transicoes:
            origem, destino, _ = transicao.split(":")
            estados.add(origem)
            estados.add(destino)
        
        for estado in sorted(estados, key=int):
            estado_str = str(estado)
            if estado_str in condicoes:
                resultado.append(f"{estado_str}: {condicoes[estado_str]}")
    
    return resultado

arquivo_transicoes = './src/plan-traces.txt'
arquivo_condicoes = './src/condicoes.txt'

planos = ler_arquivo_transicoes(arquivo_transicoes)
condicoes = ler_arquivo_condicoes(arquivo_condicoes)
resultado = adicionar_condicoes(planos, condicoes)

with open('./src/resultado_transicoes_condicoes.txt', 'w') as file:
    for linha in resultado:
        file.write(linha + "\n")


