from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import sys
import cowsay
def get_side_rad(prompt = "Введите значение стороны"):
    print(prompt)
    try:
        side_str = sys.argvp
    except:
        side_str = input()
    while True:
        try:
            side = float(side_str)
        except:
            print("Введены неправильные данные.")
            side_str = input()
        else:
            return side
def get_color(termpt):
    print("Введите какОГО цвета будущий", termpt)
    return str(input())
def main():
    print("Выберете тип ввода:\n1 - с клавиатуры в консоли\n2 - вариант 19\n3 - вывод динозавра!")
    while True:
        choise = int(input())
        if choise == 1 or choise == 2 or choise == 3:
            break
        else:
            print("Введено неверное значение. Введите 1 или 2")
    
    if choise == 1:
        r  = Rectangle(get_color("прямоугольник"), get_side_rad(), get_side_rad())
        c = Circle(get_color("круг"), get_side_rad("Введите радиус"))
        s = Square(get_color("квадрат"), get_side_rad())
        print(r, c, s, sep = "\n")
    elif choise == 3:
        print(cowsay.get_output_string('trex', 'Hello (extinct) World'))

    else:
        print(Rectangle("синего", 19, 19))
        print(Circle("зеленого", 19))
        print(Square("красного", 19))
    
if __name__ == "__main__":
    main()