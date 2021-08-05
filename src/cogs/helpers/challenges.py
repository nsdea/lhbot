# local
from . import config

import random
import discord

def math():
    """Returns a math problem and its answer."""
    problems = [
        f'{random.randint(10, 20)} - {random.randint(0, 10)}',
        f'{random.randint(0, 10)} + {random.randint(0, 10)}',
        f'{random.randint(1, 5)} * {random.randint(1, 4)}',
    ]
    problem = random.choice(problems)
    text = f'Berechne folgendes: **`{problem}`**'
    correct = str(eval(problem))
    return [text, correct]

def number():
    """Returns a number as a text and its digit-number."""
    problem = ''
    correct = ''

    for _ in range(random.randint(2, 4)):
        number_texts = ['null', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun']
        number = random.randint(0, 9)
        correct += str(number)
        problem += number_texts[number] + ' '

    text = f'Gib die Zahl für: **`{problem}`** (ohne Leertasten!) ein.\n\n**Beispiel:**\n> Wenn die Aufgabe *eins drei drei sieben* wäre, solltest du folgendes schreiben: \n> 1337'.replace(' `', '`')
    return [text, correct]

def highlow():
    """Returns a number with descriptive text and the correct answer."""
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    correct = '>' if a > b else '<'

    text = f'Ist **{a}** größer (>) oder kleiner (<) als **{b}**?\n\n> Schreibe entweder *>* oder *<*!'
    return [text, correct]

def get_challenge():
    """Returns a question and the correct answer."""
    return random.choice([math(), number(), highlow()])

def get_challenge_with_embed():
    """Returns a shiny looking verification embed (list index [0]) and the correct answer (list index [1]) :)."""
    c = get_challenge()
    embed = discord.Embed(color=config.load()['design']['colors']['primary'], title='Verifizierung', description=c[0]).set_footer(text=f'Schreibe die Antwort einfach in den Kanal! Du hast {config.load()["system"]["verification"]["timeout_seconds"]} Sekunden Zeit.', icon_url='https://yt3.ggpht.com/ytc/AKedOLTY7JZ9TbI_ZftKkSvHXXzMuFxJM16i4ly4Ako-dA=s176-c-k-c0x00ffffff-no-rj')
    return embed, c[1] # returns the <discord Embed> object and the correct answer

if __name__ == '__main__':
    print('\n'.join(get_challenge()))