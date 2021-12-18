DEFAULT_LIVES_COUNT = 5

ALLOWED_COMMANDS = [
    'start',
    'help',
    'show scores',
    'exit'
]


def show_commands():
    for i in ALLOWED_COMMANDS:
        print(i)


ALLOWED_MOVES = ('1', '2', '3')

SCORE = 0
B = 0
