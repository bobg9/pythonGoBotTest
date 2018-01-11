#!/usr/bin/env python
# coding: utf-8

"""Goban made with Python, pygame and go.py.
This is a front-end for my go library 'go.py', handling drawing and
pygame-related activities. Together they form a fully working goban.
"""
import pygame

from dlgo.goboard import Board
from dlgo.gotypes import Point, Player

__author__ = "Aku Kotkavuo <aku@hibana.net>"
__version__ = "0.1"

from sys import exit

BACKGROUND = 'images/ramin.jpg'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class GuiBoard():

    @classmethod
    def draw(cls, board):
        """Draw the board to the background and blit it to the screen.
        The board is drawn by first drawing the outline, then the 19x19
        grid and finally by adding hoshi to the board. All these
        operations are done with pygame's draw functions.
        This method should only be called once, when initializing the
        board.
        """
        """Create, initialize and draw an empty board."""
        BOARD_SIZE = (board.num_rows*45, board.num_cols*45)
        screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
        background = pygame.image.load(BACKGROUND).convert()
        outline = pygame.Rect(40, 40, (board.num_rows-1)*40, (board.num_cols-1)*40)
        pygame.draw.rect(background, BLACK, outline, 3)

        # Outline is inflated here for future use as a collidebox for the mouse
        outline.inflate_ip(20, 20)
        #pygame.draw.circle(background,BLACK,((40 * 1),(40 * 1)),15,0)
        #pygame.draw.circle(background,BLACK,((40 * 2),(40 * 2)),15,0)
        #pygame.draw.circle(background,BLACK,((40 * 3),(40 * 3)),15,0)
        #pygame.draw.circle(background,BLACK,((40 * 3),(40 * 1)),15,0)
        #pygame.draw.circle(background,WHITE,((40 * 9),(40 * 9)),15,0)
        for i in range(board.num_cols-1):
            for j in range(board.num_rows-1):
                rect = pygame.Rect(40 + (40 * i), 40 + (40 * j), 40, 40)
                pygame.draw.rect(background, BLACK, rect, 1)
        for i in range(1, board.num_rows+1):
            for j in range(1, board.num_cols+1):
                player = board.get(Point(i, j))
                if player is not None:
                    if player == Player.black:
                        pygame.draw.circle(background,BLACK,((40 * (j)),(40 * (10-i))),15,0)
                    elif player == Player.white:
                        pygame.draw.circle(background,WHITE,((40 * (j)),(40 * (10-i))),15,0)
        screen.blit(background, (0, 0))
        pygame.display.update()


'''def main():
    while True:
        pygame.time.wait(250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and board.outline.collidepoint(event.pos):
                    x = int(round(((event.pos[0] - 5) / 40.0), 0))
                    y = int(round(((event.pos[1] - 5 ) / 40.0), 0))
                    stone = board.search(point=(x, y))
                    if stone:
                        stone.remove()
                    else:
                        added_stone = Stone(board, (x, y), board.turn())


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Goban')
    screen = pygame.display.set_mode(BOARD_SIZE, 0, 32)
    background = pygame.image.load(BACKGROUND).convert()
    board = GuiBoard(9, 9)
    main()'''