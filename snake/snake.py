import pygame
from pygame.locals import QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN
from square import Square
import data.dataUtils as data

class Snake:
    '''snake entity controled by the player'''
    body = []
    turns = {}
    alive = True
    def __init__(self, pos, color):
        self.color = color
        self.head = Square(pos, color)
        self.body.append(self.head)
        self.dir = [0, 1]

    def move(self):
        '''compute dir, elements to add in turns and movement of body squares'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            head_pos_key = ''.join(str(e) for e in self.head.pos[:])

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    self.dir = [-1, 0]
                    self.turns[head_pos_key] = self.dir
                elif event.key == K_RIGHT:
                    self.dir = [1, 0]
                    self.turns[head_pos_key] = self.dir
                elif event.key == K_UP:
                    self.dir = [0, -1]
                    self.turns[head_pos_key] = self.dir
                elif event.key == K_DOWN:
                    self.dir = [0, 1]
                    self.turns[head_pos_key] = self.dir

        for i, square in enumerate(self.body):
            square_pos_key = ''.join(str(e) for e in square.pos[:])
            rows = data.getConfig("rows")
            if square.dir[0] == -1 and square.pos[0] <= 0:
                self.alive = False
            elif square.dir[0] == 1 and square.pos[0] >= rows-1:
                self.alive = False
            elif square.dir[1] == 1 and square.pos[1] >= rows-1:
                self.alive = False
            elif square.dir[1] == -1 and square.pos[1] <= 0:
                self.alive = False
            elif self.head.pos in list(map(lambda z: z.pos, self.body[1:])):
                self.alive = False

            if square_pos_key in self.turns:
                turn = self.turns[square_pos_key]
                square.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(square_pos_key)
            else:
                # rows = data.getConfig("rows")
                # if square.dir[0] == -1 and square.pos[0] <= 0:
                #     self.alive = False
                # elif square.dir[0] == 1 and square.pos[0] >= rows-1:
                #     self.alive = False
                # elif square.dir[1] == 1 and square.pos[1] >= rows-1:
                #     self.alive = False
                # elif square.dir[1] == -1 and square.pos[1] <= 0:
                #     self.alive = False
                # elif self.head.pos in list(map(lambda z: z.pos, self.body[1:])):
                #     self.alive = False

                square.move(square.dir[0], square.dir[1])


    def reset(self, pos):
        '''reset the snake to new default attributes'''
        self.body = []
        self.turns = {}
        self.head = Square(pos, self.color)
        self.body.append(self.head)
        self.dir = [0, 1]


    def add_cube(self):
        '''add a square to the snake tail'''
        tail = self.body[-1]

        if tail.dir[0] == 1 and tail.dir[1] == 0:
            self.body.append(Square([tail.pos[0]-1, tail.pos[1]], self.color))
        elif tail.dir[0] == -1 and tail.dir[1] == 0:
            self.body.append(Square([tail.pos[0]+1, tail.pos[1]], self.color))
        elif tail.dir[0] == 0 and tail.dir[1] == 1:
            self.body.append(Square([tail.pos[0], tail.pos[1]-1], self.color))
        elif tail.dir[0] == 0 and tail.dir[1] == -1:
            self.body.append(Square([tail.pos[0], tail.pos[1]+1], self.color))

        self.body[-1].dir[0] = tail.dir[0]
        self.body[-1].dir[1] = tail.dir[1]

    def draw(self, surface):
        '''draw visual of the snake'''
        for i, square in enumerate(self.body):
            square.draw(surface)
