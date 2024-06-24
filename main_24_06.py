import pprint

print ('******************************************************************** 1 решение  функция. Проверена - работает!')
def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['module'] = obj.__class__.__module__
    return info

# Пример использования
number_info = introspection_info(42)
pprint.pprint(number_info)
#Этот код создает функцию introspection_info, которая принимает объект obj в качестве аргумента и возвращает словарь
# с информацией об объекте, включая его тип, атрибуты, методы и модуль.
print('**************************************************************************** И еще для примера !***************')
number_info = introspection_info(print)
pprint.pprint(number_info)

#  решение (оно активно) класс. Проверено - работает.

print('************************************************************** А теперь с использованием класса !**************')
class Introspector:
    def introspection_info1(self, obj):
        info = {'type': type(obj).__name__,
                'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
                'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
                'module': getattr(obj, '__module__', '__main__')}
        return info

# Пример использования
if __name__ == "__main__":
    obj = 42
    inspector = Introspector()
    object_info = inspector.introspection_info1(obj)
    pprint.pprint(object_info)