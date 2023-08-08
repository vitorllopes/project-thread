import threading
import time

# Constantes
N = int(input("Digite a quantidade de times: "))
Y = int(input("Digite a quantidade de questões: "))

sem = threading.Semaphore()

# Lista para manter o progresso das equipes
progresso = [0] * N


# Função para imprimir mensagens de status
def imprimir_status(equipe, membro, questao, status):
    print(f"Equipe {equipe}, membro {membro}, questão {questao}: {status}")


# Função para a etapa de entendimento
def compreensao(equipe, membro, questao):
    time.sleep(0.5)  # Simula o tempo necessário para entender a questão
    imprimir_status(equipe, membro, questao, "Compreendida")


# Função para a etapa de implementação
def implementacao(equipe, membro, questao):
    time.sleep(1)  # Simula o tempo necessário para implementar a questão
    imprimir_status(equipe, membro, questao, "Implementada")


# Função para o ciclo de trabalho de um membro do time
def membro_da_equipe(equipe, membro):
    for questao in range(Y):
        sem.acquire()
        imprimir_status(equipe, membro, questao, "Pensando")
        compreensao(equipe, membro, questao)
        implementacao(equipe, membro, questao)
        sem.release()


# Função para simular a competição
def competicao():
    threads = []

    for equipe in range(N):
        for membro in range(3):
            t = threading.Thread(target=membro_da_equipe, args=(equipe, membro))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()


# Executa a competição
competicao()
