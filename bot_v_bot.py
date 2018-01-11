import time

import pygame

from dlgo import gotypes
from dlgo.agent.naive import RandomBot
from dlgo.gamestate import GameState
from dlgo.gui import GuiBoard
from dlgo.utils import print_move, print_board


def main():
    board_size = 9
    pygame.init()
    pygame.display.set_caption('Goban')

    game = GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: RandomBot(),
        gotypes.Player.white: RandomBot(),
    }
    while not game.is_over():
        #time.sleep(0.3)

        print(chr(27) + "[2J")
        print_board(game.board)
        GuiBoard.draw(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(game.next_player, bot_move)
    input("Press Enter to continue...")


if __name__ == '__main__':
    main()