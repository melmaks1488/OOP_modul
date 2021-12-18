from random import randint

from settings import DEFAULT_LIVES_COUNT, ALLOWED_MOVES

from exceptions import EnemyDown, GameOver, InvalidLiteral


class Enemy:

    lives = 1
    level = 1

    def __init__(self, name, level):
        self.name = name
        self.lives = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self, player_obj):
        self.lives -= 1
        if self.lives <= 0:
            self.level += 1
            raise EnemyDown
        player_obj.score += 1


class Player:

    allowed_attack = 0
    score = 0
    lives = DEFAULT_LIVES_COUNT
    level = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fight(attack, defense):
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            return 1
        elif (attack == 1 and defense == 3) or (attack == 2 and defense == 1) or (attack == 3 and defense ==2):
            return -1
        else:
            return 0

    @staticmethod

    def input_comand(text_var: str) -> int:
        while True:
            num = input(text_var)
            if num == '1':
                return 1
            elif num == '2':
                return 2
            elif num == '3':
                return 3
            else:
                print('Input is incorrect!')

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()

    def attack(self, enemy_obj):
        if self.allowed_attack in ALLOWED_MOVES:
            result = self.fight(int(self.allowed_attack), enemy_obj.select_attack())

            if result == 0:
                print("Its a Draw")
            elif result == 1:
                print("You attacked successfully!")
                enemy_obj.decrease_lives(self)
            else:
                print("You missed!")
        else:
            raise InvalidLiteral

    def defence(self, enemy_obj):
        defence_player = Player.input_comand('select defence')
        res = self.fight(enemy_obj.select_attack(), defence_player)
        if res == 0:
            return 'its a draw'
        elif res == -1:
            return 'He missed'
        else:
            self.decrease_lives()
            return 'His attack successfully'


class Scores:

    @staticmethod
    def show_score():
        with open('score.txt ', 'a+') as scores:
            sort_scores = sorted(scores.readlines(), reverse=True, key=lambda score: int(score[:2]))
            scores = [i.split() for i in sort_scores]
            scores_table = range(1, 11 if len(scores) > 10 else len(scores) + 1)
            for i in zip(scores_table, scores):
                print(f'{i[0]}. {i[1][1]} : {i[1][0]} | {i[1][2]} {i[1][3]}')











