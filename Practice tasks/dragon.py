from random import randint
from colorama import Fore, init

init(autoreset=True)
hit_count = 0
hero_health = 100
dragon_health = 500
hero_name = input("Введите имя героя: ")
while True:
    hero_armor = int(input(f"Введите уровень брони {hero_name} (от 0 до 100): "))
    if 0 <= hero_armor <= 100:
        break
    else:
        print("Нерерное значение брони! введите число от 0 до 100")
hero_armor = hero_armor / 100

while True:
    hero_damage = randint(14, 18)
    hero_crit = randint(1, 4)
    print(Fore.GREEN + f"\nЗдоровье {hero_name}: {hero_health}")
    print(Fore.RED + f"Здоровье дракона: {dragon_health}")
    input("\nВаш ход! Нажмите enter для удара")
    print(f"Вы атакуете дракона")
    if hero_crit == 4:
        print(Fore.BLUE + f"Критическое попадание! Вы наносите {hero_damage * 2} единиц урона")
        dragon_health -= hero_damage * 2
    else:
        print(Fore.GREEN + f"Вы наносите {hero_damage} единиц урона")
        dragon_health -= hero_damage
    hit_count += 1
    if dragon_health <= 0:
        victory = True
        break

    dragon_damage = randint(8, 12)
    dragon_hit = randint(1, 4)
    print(Fore.GREEN + f"\nЗдоровье {hero_name}: {hero_health}")
    print(Fore.RED + f"Здоровье дракона: {dragon_health}")
    input("\nХод дракона! Нажмите enter для продолжения")
    print("Дракон атакует вас")
    if dragon_hit == 4:
        print(Fore.RED + f"Дракон попал по вам и нанёс {dragon_damage} единиц урона!")
        print(Fore.GREEN + f"Ваша броня поглотила {int(dragon_damage * hero_armor)} единиц урона!")
        hero_health -= int(dragon_damage * (1 - hero_armor))
    else:
        print(Fore.YELLOW + "Дракон не попал по вам")
    if hero_health <= 0:
        victory = False
        break

if victory:
    print(Fore.GREEN + f"\nВы победили! Вы нанесли {hit_count} ударов")
else:
    print(Fore.RED + "\nВы проиграли")
