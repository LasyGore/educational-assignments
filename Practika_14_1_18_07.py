from datetime import datetime


class SuperDate(datetime):
    # Создаем словарь соответствия номера месяца и его сезона
    seasons = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter"
    }

    def get_season(self):
        # Получаем номер месяца из даты
        month = self.month
        return self.seasons[month]

    def get_time_of_day(self):
        # Получаем час из даты
        hour = self.hour
        if 6 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 18:
            return "Day"
        elif 18 <= hour < 24:
            return "Evening"
        else:
            return "Night"


# Пример использования класса SuperDate
a = SuperDate(2024, 7, 18, 13)
print(a.get_season())
print(a.get_time_of_day())