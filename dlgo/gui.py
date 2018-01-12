#!/usr/bin/env python
# coding: utf-8

import pygame


from dlgo.gotypes import Point, Player

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
        for i in range(board.num_cols-1):
            for j in range(board.num_rows-1):
                rect = pygame.Rect(40 + (40 * i), 40 + (40 * j), 40, 40)
                pygame.draw.rect(background, BLACK, rect, 1)
        for i in range(1, board.num_rows+1):
            for j in range(1, board.num_cols+1):
                player = board.get(Point(i, j))
                if player is not None:
                    if player == Player.black:
                        pygame.draw.circle(background,BLACK,((40 * (j)),(40 * (board.num_cols-i+1))),15,0)
                    elif player == Player.white:
                        pygame.draw.circle(background,WHITE,((40 * (j)),(40 * (board.num_cols-i+1))),15,0)
        screen.blit(background, (0, 0))
        pygame.display.update()

