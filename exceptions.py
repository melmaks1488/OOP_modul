
class GameOver(Exception):
    def __str__(self):
        print('GameOver')


class Score:

    def __init__(self, score):
        self.score = score

        with open('scores.txt ') as sorter:
            lines = [line.split('Scores: ') for line in sorter]
        file = open("scores.txt ", 'w')

        for line in sorted(lines, key=lambda x: int(x[1]), reverse=True)[:10]:
            file.write('Scores: '.join(line))


class EnemyDown(Exception):
    pass


class InvalidLiteral(Exception):
    pass