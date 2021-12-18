import settings as settings
from exceptions import GameOver, EnemyDown, InvalidLiteral
from models import Player, Enemy, Scores


def play():
    level = 1
    player_name = input('Enter Player name! \n')
    print(f"Welcome! {player_name}\n")
    player = Player(player_name)
    enemy_name = 'Enemy'
    enemy = Enemy(enemy_name, level)

    while True:
        command = input(
            f"{player_name}, Please enter \"START\" to start the game\n"
            f"or enter \"HELP\" to enter setup\n")

        if command == "start":
            print(f'Your enemy name is Sergant_Pecalniy!')
            while True:

                try:

                    player.allowed_attack = input('Chose a team to attack: '
                                                  '\'1\' - Witch, \'2\' - Robber,'
                                                  ' \'3\' - Rogue \n')
                    player.attack(enemy)
                    print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                    player.allowed_attack = input('Chose a team to defence: '
                                                  '\'1\' - Witch, \'2\' - Warrior,'
                                                  ' \'3\' - Robber \n')
                    player.defence(enemy)
                    print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                except EnemyDown:
                    player.score += 5
                    player.level += 1
                    level += 1
                    print(f'\n---------------------------------------------------------\n'
                          f' You killed {enemy_name}. Your score: '
                          f'{player.score}. Level: {player.level}.\n'
                          f'---------------------------------------------------------\n')
                    enemy_name = 'Sergant_Pechalniy'
                    enemy = Enemy(enemy_name, level)
                    print(f'\nYour enemy name is {enemy_name}!\n')
                except InvalidLiteral:
                    print('\nONLY 3 classes of fighters!!! 1-2-3\n')

        elif command == "help":
            settings.show_commands()

        elif command == "show scores":
            print('\n')
            Scores.show_score()
            print('\n')

        elif command == "exit":
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        play()
        print('GAME OVER')
        print('Score :', settings.SCORE)
        file = open('score.txt', 'a')
        file.write(f"Name: {Player.__name__}, Scores: {settings.SCORE}" + '\n')
        file.close()
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye')