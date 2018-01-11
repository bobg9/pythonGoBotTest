from dlgo import goboard, gotypes
from dlgo.agent.naive import RandomBot
from dlgo.utils import print_board, point_from_coords, print_move


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = RandomBot()

    while not game.is_over():
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(game.next_player, move)


if __name__ == '__main__':
    main()