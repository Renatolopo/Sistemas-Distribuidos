from time import sleep
import threading

def print_num(lista, thread):
    while len(lista) > 0:
        sleep(0.5)
        print(f'A Thread {thread} imprimiu {lista.pop(0)}')
        


threads = []
lista = [x for x in range(0, 101)]
for i in range(4):
    t = threading.Thread(target=print_num, args=(lista, i+1))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

