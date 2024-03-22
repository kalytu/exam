import random

def gra():
    var = ["правда", "дія"]
    var_dey = ["піти", "встати", "сісти", "попити", "поїсти"]
    var_prav = ["скільки тобі років?", "їв(ла) сьогодні?", "хочеш спати", "як тебе звуть?", "що робиш?"]
    
    vibor = random.choice(var)
    otv = input("введіть 'правда' чи 'дія': ")
    
    if otv == 'правда':
        otv_prav = random.sample(var_prav, 1)[0]
        print(otv_prav)
    else:
        otv_dey = random.sample(var_dey, 1)[0]
        print(otv_dey)
    
    again = input('продовжити гру? так або ні:')
    return again

while True:
    again = gra()
    if again.lower() != 'так':
        break
