from window.window_game import Game
from window.window_menu import Menu
from window.window_settings import Settings
import pygame


class CoreGame:

    def __init__(self):
        pygame.init()

        """ Код окна """
        self.screen = pygame.display.set_mode((1000, 500))
        self.entered_language = 0
        self.state_window = "menu"

        """ Окна """
        self.game = Game(self.screen)
        self.settings = Settings(self.screen)
        self.menu = Menu(self.screen)


    def run(self):
        while True:
            if self.state_window == "menu":
                self.state_window = self.menu.run(self.entered_language)
            if self.state_window == "settings":
                self.state_window, self.entered_language = self.settings.run(self.entered_language)
            if self.state_window == "game":
                self.state_window = self.game.run(self.entered_language)