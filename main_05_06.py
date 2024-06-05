import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            if enemies - self.skill > 0:
                enemies -= self.skill
                print(f"{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов.")
            else:
                print(f"{self.name}, сражается {days} день(дня)..., осталось 0 воинов.")
                print(f"{self.name} одержал победу спустя {days} дней!")
                break
            time.sleep(1)


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()

print("Все битвы закончились!")


