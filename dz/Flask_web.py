from flask import Flask
from generator import fib
app = Flask(__name__)  

@app.route("/")     #декоратор функция, которая принимает и возвращает функцию
def hello_world():
    return "<p>Hello, World!</p>"   #html заголовки - <p>

@app.route("/fibonachi")
def fibonachi_start():
    return "Write after URL '/number!'"

@app.route("/fibonachi/<int:n>")    #если правильно вводим значения, то выполняется
def fibonachi_number(n):
    return list(fib(n))     #list - выдает нормальное развертывание массива

@app.errorhandler(404)
def page_not_found(e):  #е=404
    return "Oops! Try to enter a '/fibonachi/number!'"