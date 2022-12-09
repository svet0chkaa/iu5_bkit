import pytest
from time import time
from generator import fib
class cm_timer: #для замера времени работы функции
    def __enter__(self):    #время на входе
        self.__time_begin = time()
    def __exit__(self, type, value, traceback): #время на выходе
        print(time() - self.__time_begin)

c = 100000

def test_fib_1():
    assert [i for i in fib(5)] == [0, 1, 1, 2, 3]   #добавляем проверку на ошибку (тестирование)
def test_fib_2():
    assert [i for i in fib(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def test_fib_3():
    assert [i for i in fib(0)] == []

def test_fib_time_1():
    print("Вычисление с ленивыми выражениями")
    with cm_timer():
        temp = fib(c)
    assert list(fib(c)) == [i for i in fib(c)]
def test_fib_time_2():
    print("Вычисление с обычными выражениями")
    with cm_timer():
        temp = [i for i in fib(c)]
    assert [i for i in fib(c)] == list(fib(c))

if __name__ == "__main__":
    test_fib_time_1()
    test_fib_time_2()