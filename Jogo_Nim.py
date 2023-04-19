def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    elif n % (m+1) == 0:
        return m
    else:
        return n % (m+1)

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada < 1 or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            print("Você tirou", jogada, "peça(s).")
            vez_do_usuario = False
        else:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou", jogada, "peça(s).")
            vez_do_usuario = True
        n = n - jogada
        print("Agora restam", n, "peça(s) no tabuleiro.\n")
    if vez_do_usuario:
        print("Fim do jogo! O computador ganhou!")
    else:
        print("Fim do jogo! Você ganhou!")

def campeonato():
    rodada = 1
    placar_usuario = 0
    placar_computador = 0
    while rodada <= 3:
        print("**** Rodada", rodada, "****\n")
        resultado = partida()
        if resultado == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1
        rodada += 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")
    if placar_usuario > placar_computador:
        print("Você ganhou o campeonato!")
    elif placar_computador > placar_usuario:
        print("O computador ganhou o campeonato!")
    else:
        print("O campeonato terminou empatado!")
        
print("Bem-vindo ao jogo do NIM! Escolha: ")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opcao = int(input())
if opcao == 1:
    print("Você escolheu uma partida isolada!")
    partida()
else:
    print("Você escolheu um campeonato!")
    campeonato()
