import colorama  #Добавляет цвета в терминал
from colorama import Fore, Back, Style #Fore- отвечает за цвет текста.Back-за обрамление.Style-стиль текста
print(Fore.BLACK + "чёрный текст")
print(Style.BRIGHT + "жирный шрифт")
print(Style.DIM + "мение жирный шрифт")
print(Back.MAGENTA + "цветной фон")
print(Style.RESET_ALL, end='')
print("вернуться в нормальное состояние сейчас")