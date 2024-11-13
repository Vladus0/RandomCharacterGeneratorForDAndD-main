import random

classes = ["Воин", "Маг", "Паладин", "Лучник", "Варвар"]
races = ["Человек", "Эльф", "Гном", "Дворф", "Хоббит"]

def generate_character(class_choices, race_choices, min_stats, max_stats):
    name = f"Персонаж_{random.randint(1, 1000)}"  
    character_class = random.choice(class_choices)
    character_race = random.choice(race_choices)

    stats = {key: random.randint(min_stats[key], max_stats[key]) for key in min_stats}
    
    return {
        "Имя": name,
        "Класс": character_class,
        "Раса": character_race,
        "Характеристики": stats
    }

min_stats = {
    "Сила": 8,
    "Ловкость": 10,
    "Выносливость": 8,
    "Интелект": 8,
    "Мудрость": 8,
    "Харизма": 8
}

max_stats = {
    "Сила": 18,
    "Ловкость": 18,
    "Выносливость": 18,
    "Интелект": 18,
    "Мудрость": 18,
    "Харизма": 18
}

chosen_classes = ["Воин", "Маг", "Паладин", "Лучник", "Варвар"] 
chosen_races = ["Человек", "Эльф", "Гном", "Дворф", "Хоббит"] 

num_characters = 5
characters = [generate_character(chosen_classes, chosen_races, min_stats, max_stats) for _ in range(num_characters)]

for character in characters:
    print(character)

