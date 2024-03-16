import random

def gra():
    var = ["правда", "дія"]
    var_dey = ["піти", "встати", "сісти", "попити", "поїсти"].split()
    var_prav = ["скільки тобі років?", "їв(ла) сьогодні?", "хочеш спати", "як тебе звуть?", "що робиш?"].split()
    vibor = random.choice(var)
    otv = input("введіть 'правда' чи 'дія': ")
    
    if otv == 'правда':
       otv_prav = random.choice(var_prav)
       print(otv_prav)
    else:
       otv_dey = random.choice(var_dey)
       print(otv_dey)

gra()
