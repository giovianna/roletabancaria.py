# ROLETA ALEATÓRIA DE QUEM VAI PAGAR A CONTA

import random

names_string = input('Digite o nome de todos que estão dividindo a conta:\n')

names = names_string.split(", ")

random_choice = random.choice(names).capitalize()


print(f'Quem vai pagar a conta é {random_choice}!')
