import pygame
from menu.menu import Menu
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")), (120, 70))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")), (50, 50))

class Tower():
    """
    Abstract class for towers
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        # define menu and buttons
        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")

        self.tower_imgs = []
        self.damage = 1

    def draw(self, win):
        """
        draws the tower
        @param win:
        @return:
        """
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

        # draw menu
        if self.selected:
            self.menu.draw(win)

    def draw_radious(self, win):
        if self.selected:
            # draw change circle
            surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        """
        returns if tower is has been clicked on and selects if it was clicked
        @param X: int
        @param Y: int
        @return: bool
        """
        img = self.tower_imgs[self.level - 1]
        if X <= self.x  - img.get_width() // 2 + self.width and X >= self.x - img.get_width() // 2:
            if Y <= self.y + self.height - img.get_height() // 2 and Y >= self.y - img.get_height() // 2:
                return True
        return False

    def sell(self):
        """
        call to sell the tower, returns sell price
        @return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        upgrade the tower for the given cost
        @return: None
        """
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage += 1

    def get_upgrade_cost(self):
        """
        return the upgraded cost, if 0 then can't upgrade anyomre
        @return: int
        """
        return self.price[self.level - 1]

    def move(self, x, y):
        """
        moves tower to given x and y
        @param x: int
        @param y: int
        @return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis >= 100:
            return False
        else:
            return True
