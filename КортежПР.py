


def Star():
    print("1.Сумма элементов списка")
    print("2.Поиск наибольшего элемента")
    print("3.Удаление дубликатов")
    print("4.Объединение списков")
    print("5.Поиск элемента в кортеже")
    print("6.Слияние кортежей")
    print("7.Удаление элемента из кортежа")
    print("8.Подсчет элементов в кортеже")

    print("Выберите действие:")
    a = int(input())
    SelectedCase(a)

from collections import Counter
def SelectedCase(id):
    List1 = [1, 4, 5, 6, 7, 8, 2, 4, 3, 4, 5, 6, 7, 8]
    List2 = [1, 5, 3, 12]
    food = ("cucumber", "bananas", "tomatoes", "apple")
    if id == 1:
        print("Сумма чисел:", sum(List1))
        Star()
    if id == 2:
        print ("Наибольший элемент:", max(List1))
        Star()
    if id == 3:
        print ("Уникальные элементы:", set(List1))
        Star()
    if id == 4: 
        dvaspiska = List1 + List2 
        print ("Объединенный список:", str(dvaspiska))
        Star()
    if id == 5:
        index = food.index("apple")
        print("Индекс:", index)
        Star()
    if id == 6:
        dvakortega = List1 + List2 
        print("Два кортежа:", dvakortega)
        Star()
    if id == 7:
        print("кортеж")
        print(List1)
        print("Укажите элемент который надо удалить:")
        i = int(input())
        List1.remove(i)
        print(List1)
        Star()
    if id == 8:
        z = List1
        print(str(Counter(z)))
        Star()

Star()