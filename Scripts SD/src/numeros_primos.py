import time
import threading

# retorna verdadeiro se o número for primo
def is_primo(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True

# conta quantos primos tem em um intervalo passado como parametro
def sem_thread(inicio, fim, numeros_primos, index):
    c = 0
    for n in range(int(inicio), int(fim)):
        if is_primo(n):
            c += 1

    numeros_primos[index] = c


# cria N thread para veficar se um intervalo numero primo
def com_thread(numero_de_thread):
    inicio = 10000
    fim = 99999
    split = (fim - inicio)/numero_de_thread # quantidade de número que cada thread vai verificar

    numeros_primos = [None] * numero_de_thread
    threads = [None] * numero_de_thread

    for i in range(numero_de_thread):
        threads[i] = threading.Thread(target=sem_thread, args=(inicio, inicio + split, numeros_primos, i))
        threads[i].start()
        inicio = inicio + split + 1
    
    for i in range(len(threads)):
        threads[i].join()
    
    return sum(numeros_primos)


inicio = time.time()

# sem thread
# numeros_primos = [None] 
# sem_thread(10000, 99999, numeros_primos, 0)
# c = numeros_primos[0]

# com thread
c = com_thread(4)

fim = time.time()

print(f'Foram encontrados {c} números primos em {fim - inicio:.2f} segundos')