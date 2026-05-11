import pygame

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 20)
        self.bg = pygame.image.load("bikers_game_img/background/menu.png")

        """Кнопки"""
        self.music_off_on = False

        self.language = ['Русский', 'Türk', 'Английский']
        self.music_text_language = ['вкл/выкл музыку', 'açık/kapalı müzik', 'off/on music']
        self.accept_button_language = ['Применить', 'Uygulamak', 'Accept']
        self.menu_button_language = ['Обратно в меню', 'Menüye geri dön', 'back to menu']
        self.entered_language = 0


    def run(self):
        clock = pygame.time.Clock()

        button_left = pygame.image.load("bikers_game_img/menu_objects/left.png")
        button_right = pygame.image.load("bikers_game_img/menu_objects/right.png")
        button_true = pygame.image.load("bikers_game_img/menu_objects/true.png")
        button_false = pygame.image.load("bikers_game_img/menu_objects/false.png")
        button = pygame.image.load("bikers_game_img/menu_objects/Button.png")

        button_menu_left = button_left.get_rect(topleft=(550, 50))
        button_menu_right = button_right.get_rect(topleft=(750, 50))
        button_music_on_off = button_true.get_rect(topleft=(550, 200))

        button_menu = button.get_rect(topleft=(100, 200))
        button_accept = button.get_rect(topleft=(100, 300))

        while True:
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_menu_left.collidepoint(event.pos):
                        if self.entered_language < len(self.language) - 1: self.entered_language += 1
                    if button_menu_right.collidepoint(event.pos):
                        if self.entered_language > 0: self.entered_language -= 1
                    if button_music_on_off.collidepoint(event.pos):
                        if self.music_off_on: self.music_off_on = False
                        elif not self.music_off_on: self.music_off_on = True
                    if button_menu.collidepoint(event.pos):
                        return "menu"

            # off/on music
            self.screen.blit(button_true if self.music_off_on else button_false, button_music_on_off)
            self.screen.blit(self.font.render(f"{self.music_text_language[self.entered_language]}", True, (255, 255, 255)), (625, 220))

            # settings music
            self.screen.blit(button_left, button_menu_left)
            self.screen.blit(self.font.render(f"{self.language[self.entered_language]}", True, (255, 255, 255)), (640, 70))
            self.screen.blit(button_right, button_menu_right)

            # button menu
            self.screen.blit(button, button_menu)
            self.screen.blit(self.font.render(f"{self.menu_button_language[self.entered_language]}", True, (255, 255, 255)), (150, 250))

            # button accept
            self.screen.blit(button, button_accept)
            self.screen.blit(self.font.render(f"{self.accept_button_language[self.entered_language]}", True, (255, 255, 255)), (150, 350))


            pygame.display.flip()
            clock.tick(60)