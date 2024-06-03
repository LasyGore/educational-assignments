from threading import Thread
import time

s=time.time()

def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i+1)
#    print('Конец цикла счетчика')

def print_letters():
    for letter in 'abcdefghij':
        time.sleep(1)
        print(letter)
#    print('Конец цикла данных')

thread1 = Thread(target=print_numbers)
thread2 = Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


e=time.time()
print ((e-s), 'sec отработали оба потока')
print ('*************************************************')

