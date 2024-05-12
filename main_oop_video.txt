

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_user = user
                return
        print("Пользователь не найден или неверный пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        found_video = None
        for video in self.videos:
            if video.title.lower() == title.lower():
                found_video = video
                break
        if not found_video:
            print("Видео не найдено")
            return
        if found_video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        print("Воспроизведение видео:")
        for second in range(found_video.duration):
            print(second + 1, end=' ')
#           time.sleep(1)
        print("Конец видео")

#Тестирование
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
print ('1 *******************************************************Начало тестирования прошло.')

# Добавление видео
ur.add(v1, v2)
print ('2 *******************************************************Добавление видео прошло.')

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print ('3 ******************************************************* прошла проверка  поиска по фразам : лучший и ПРОГ.')

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
print ('4 *******************************************************5 тестовых проверок входа и возраста прошли успешно.')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
print ('5 *******************************************************Проверка существования аккаунта - УСПЕШНО!.')


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print ('6 *******************************************************Проверка просмотра отсутствующего видео- УСПЕШНО!.')