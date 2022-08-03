import pygame
from .constants import PINK, BLUE, SQUARE_SIZE, GREY, CROWN

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0 
        self.y = 0
        self.cal_pos()

    def cal_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #this crowns the king piece
    def make_king(self):
        self.king = True


    #this creates the players
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE) #larger cirle
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) #smaller circle
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.cal_pos()   

    def __repr__(self):
            return str(self.color)