from pywebio.input import input as pw_input
from pywebio.output import put_success

animal_like = pw_input('Введіть улюблену тварину >>>').lower().title().strip()
animal_name = pw_input('Введіть кличку тварини >>>').lower().title().strip()

is_dog = 'собака' == animal_like
dog_emodji = '\U0001F415'

is_cat = 'кіт' == animal_like
cat_emodji = '\U0001F408'

is_hamster = 'хомяк' == animal_like
hamster_emodji = '\U0001F439'

is_fish = 'риба' == animal_like
fish_emodji = '\U0001F41F'

is_turtle = 'черепаха' == animal_like
turtle_emodji = '\U0001F422'

can_pet_swim = False
if animal_like == is_fish or animal_like == is_turtle:
    can_pet_swim = True

if animal_like == is_fish or animal_like == is_turtle:
    put_success(f'Купіть акваріум для {animal_name}')

if is_dog:
    put_success(f'{animal_name}- обожнюю собак, особливо великих {dog_emodji}')

if is_cat:
    put_success(f'{animal_name}- вони дуже милі та пухнасті {cat_emodji}')

if is_hamster:
    put_success(f'{animal_name}- хомяки такі крихітні {hamster_emodji}')

if is_fish:
    put_success(f'{animal_name}- за ними достатньо легко доглядати {fish_emodji}')

if is_turtle:
    put_success(f'{animal_name}- у них буже міцний панцир {turtle_emodji}')

else:
    put_success(f'Дуже цікаве та гарне імя {animal_name} \U0001F60D')