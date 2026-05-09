from window.window_game import Game
from window.window_menu import Menu
import pygame


class CoreGame:

    def __init__(self):
        pygame.init()

        """ Код окна """
        self.screen = pygame.display.set_mode((1000, 500))
        self.state_window = "game"

        """ Окна """
        self.game = Game(self.screen)
        self.menu = Menu(self.screen)

    def run(self):
        while True:
            if self.state_window == "menu":
                self.state_window = self.menu.run()
            if self.state_window == "game":
                self.state_window = self.game.run()