import pygame
import os
pygame.font.init()

star = pygame.image.load(os.path.join("game_assets", "star.png"))

class Button:
    """
    Button class for menu object
    """
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        """
        returns if the position has collided with the menu
        @param X: int
        @param Y: int
        @return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class Menu:
    """
    menu for holding items
    """
    def __init__(self, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans, 40")

    def add_btn(self, img, name):
        """
        adds button to menu
        @param img: surface
        @param name: str
        @return: None
        """
        self.items += 1
        btn_x = self.x - self.bg.get_width() / 2 + 10
        btn_y = self.y - 120 + 10
        self.buttons.append(Button(btn_x, btn_y, img, name))

    def draw(self, win):
        """
        draws buttons and menu bg
        @param win: surface
        @return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width() / 2, self.y - 120))
        for item in self.buttons:
            item.draw(win)

    def click(self, X, Y):
        """
        returns if the position has collided with the menu
        @param X: int
        @param Y: int
        @return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def get_clicked(self, X, Y):
        """
        return the clicked item from the menu
        @param X: int
        @param Y: int
        @return: str
        """
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name
        return None
