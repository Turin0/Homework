import queue
import threading
import time


class Table:
    def __init__(self, num):
        self.num = num
        self.is_busy = False


class Cafe:
    def __init__(self, tables_):
        self.queue = queue.Queue()
        self.tables = tables_

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 50:
            print(f'Посетитель номер {customer_number} прибыл.', flush=True)
            customer_thread = Customer(customer_number, self)
            customer_thread.start()
            customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if self.queue.full():
                print(f'Посетитель номер {customer.name} ожидает столик', flush=True)
                self.queue.put(customer)
                self.queue.get()
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer.name} cел за стол {table.num}.', flush=True)
                time.sleep(5)
                table.is_busy = False
                print(f'Посетитель номер {customer.name} покушал и ушёл.', flush=True)


class Customer(threading.Thread):
    def __init__(self, num, cafe_):
        super().__init__()
        self.name = num
        self.cafe = cafe_

    def run(self):
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
table4 = Table(4)
table5 = Table(5)
tables = [table1, table2, table3, table4, table5]


cafe = Cafe(tables)
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
