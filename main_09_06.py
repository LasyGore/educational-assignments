import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        customer_id = 1
        while customer_id <= 21:
            print(f"Посетитель номер {customer_id} прибыл")
            self.serve_customer(customer_id)
            customer_id += 1
            time.sleep(1)  # Новый посетитель приходит каждую секунду

    def serve_customer(self, customer_id):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer_id} сел за стол {table.number}")
                threading.Thread(target=self.customer_service, args=(customer_id, table)).start()
                return
        self.queue.append(customer_id)
        print(f"Посетитель номер {customer_id} ожидает свободный стол")

    def customer_service(self, customer_id, table):
        time.sleep(5)  # Время обслуживания посетителя - 5 секунд
        print(f"Посетитель номер {customer_id} покушал и ушёл")
        table.is_busy = False
        if self.queue:
            next_customer = self.queue.pop(0)
            print(f"Посетитель номер {next_customer} сел за стол {table.number}")
            threading.Thread(target=self.customer_service, args=(next_customer, table)).start()

print ('Обслужим  двадцать одного клиента!!!')
# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]


# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

