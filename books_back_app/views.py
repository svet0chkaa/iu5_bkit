from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# ordersData =

def getOrdersData():
    return [
            {'title': 'Печать', 'id': 1, 'src': 'images/pechat.jpg', 'info': 'Стоимость услуги зависит от количества страниц и варьируется от 10р. до 500р.', 'rates':[{'title': '1-10 страниц', 'price': '10р.'}, {'title': '50-100 страниц', 'price': '200р.'}, {'title': 'до 300 страниц', 'price': '500р.'}],},
            {'title': 'Брошюрирование', 'id': 2, 'src': 'images/brosh.jpg', 'info': 'Стоимость услуги зависит от количества страниц и варьируется от от 500р. до 2000р.', 'rates':[{'title': 'До 6 листов', 'price': '500р.'}, {'title': 'До 10 листов', 'price': '1000р.'}, {'title': 'До 30 листов', 'price': '2000р.'}],},
            {'title': 'Дизайн обложки', 'id': 3, 'src': 'images/dizain.jpg', 'info': 'Стоимость услуги зависит от сложности дизайна. Цена от 10000р. до 25000р.', 'rates':[{'title': 'Простой дизайн', 'price': '10000р.'}, {'title': 'Средний дизайн', 'price': '17000р.'}, {'title': 'Сложный дизайн', 'price': '25000р.'}],},
            {'title': 'Реклама', 'id': 4, 'src': 'images/rekl.jpg', 'info': 'Цена услуги от 50000р. до 100000р.', 'rates':[{'title': 'На 10 дней', 'price': '50000р.'}, {'title': 'На 30 дней', 'price': '75000р.'}, {'title': 'На 60 дней', 'price': '100000р.'}],},
            {'title': 'Подарки на заказ', 'id': 5, 'src': 'images/pidarok.jpg', 'info': 'Подарки делятся на три категории 1000р. до 5000р.', 'rates':[{'title': 'Недорогие подарки', 'price': '1000р.'}, {'title': 'Средние подарки', 'price': '2500р.'}, {'title': 'Дорогие подарки', 'price': '5000р.'}],},
        ]

def GetOrders(request):
    query = request.GET.get("ord")
    print(query)
    ords = getOrdersData()
    res = []
    
    for ord in ords:
        if (query is not None):
            if query.lower() in ord["title"].lower():
                res.append(ord)
        else:
            res = ords
        

    # return res

    return render(request, 'orders.html', {'data' : {
        'orders': res,
        'query_c': query
    }})

def GetOrder(request, id):
    ordersData = getOrdersData()
    order = next((sub for sub in ordersData if sub['id'] == id), None)
    if order:
        print(order['rates'])
    else:
        print("Not found")
    return render(request, 'order.html', {'data' : {
        'order': order
    }})

# def searchGroups(group_name):
#     groups = getGroups()
    
#     res = []
    
#     for group in groups:
#         if group_name.lower() in group["group_name"].lower():
#             res.append(group)

#     return res