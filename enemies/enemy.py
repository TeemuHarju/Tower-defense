import pygame
import math

class Enemy:
    imgs = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222), (973, 284), (1046, 366), (1022, 458), (894, 502), (740, 514), (580, 552), (148, 551), (85, 452), (52, 345), (1, 335)]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0

    def draw(self, win):
        """
        Draws the enemy with the given images
        @param win: surface
        @return:None
        """

        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count > len(self.imgs):
            self.animation_count = 0
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        Returns if the position has hiut enemy
        @param x: int
        @param y: int
        @return: Bool
        """
        if X <= self.x + self.width and Y >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        @return: None
        """
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.move_count += 1
        dirn = (x2 - x1, y2 - y1)

        move_x, move_y = (self.x + dir[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        #got to next point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            

        self.x = move_x
        self.y = move_y

    def hit(self):
        """
        Returns if an enemy has died and removes one health each call
        @return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True