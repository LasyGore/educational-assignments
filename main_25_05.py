
def create_operation(operation):
    if operation == "mult":
        def mul(x, y):
            return x * y
        return mul
    elif operation == "div":
        def div (x, y):
            return x // y
        return div

my_func_mult = create_operation("mult")
print(my_func_mult(8,4))
print ('*** 1 ***')

my_func_mult = create_operation("div")
print(my_func_mult(8,4))
print ('*** 2 ***')


multiply = lambda x, y: x ** y
print(multiply(2, 10))
print ('*** 3 ***')
def multiply_def(x, y):
   return x ** y
print(multiply_def(2, 10))
print ('*** 4 ***')

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        return self.a * self.b

rectangle = Rect(6, 8)
area = rectangle()
print(area)
print('*** 5 ***')