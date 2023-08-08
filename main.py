import threading
import time
sem = threading.Semaphore()

n = int(input('Digite a quantidade de panelas: '))
m = int(input('Digite a quantidade de frigideiras: '))


def func1():
    while True:
        sem.acquire()

        global n
        count = 0

        if( n >= 3):
            for i in range(3):
                n -= 1
                count += 1
                print(f'A boca está com {count} panela(s)')
            count = 0
        
        elif(n == 2):
            for i in range(2):
                n -= 1
                count += 1
                print(f'A boca está com {count} panela(s)')
            count = 0

        elif(n == 1):
            n -= 1
            count += 1
            print(f'A boca está com {count} panela(s)')
            count = 0
        
        sem.release()
        time.sleep(1)
        if n == 0:
            break
    
def func2():
    while True:
        sem.acquire()
        
        global m
        count = 0 

        if (m >= 3):
            for j in range(3):
                m -= 1
                count += 1
                print(f'A boca está com {count} frigideira(s)')
            count = 0

        elif (m == 2):
            for j in range(2):
                m -= 1
                count += 1
                print(f'A boca está com {count} frigideira(s)')
            count = 0

        elif (m == 1):
            m -= 1
            count += 1
            print(f'A boca está com {count} frigideira(s)')
            count = 0

        sem.release()
        time.sleep(1)
        if m == 0:
            break

t = threading.Thread(target = func1)
t.start()
t2 = threading.Thread(target = func2)
t2.start()