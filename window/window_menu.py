import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.SysFont("Arial", 20)
        self.bg = pygame.image.load("bikers_game_img/background/menu.png")

        self.button = pygame.image.load("bikers_game_img/menu_objects/Button.png")

        self.button_menu_language = ['Играть', 'Oynamak', 'Play']
        self.button_menu_settings = ['Настройки', 'Ayarlar', 'settings']
        self.button_menu_quit = ['Выйти', 'oyundan çık', 'quit']

    def run(self, entered_language=0):
        clock = pygame.time.Clock()

        button_img = pygame.image.load("bikers_game_img/menu_objects/Button.png")

        button_menu_rect = button_img.get_rect(topleft=(650, 50))
        button_settings_rect = button_img.get_rect(topleft=(650, 150))
        button_quit_rect = button_img.get_rect(topleft=(650, 250))

        while True:
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_menu_rect.collidepoint(event.pos):
                        return "game"
                    if button_settings_rect.collidepoint(event.pos):
                        return "settings"
                    if button_quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                # if event.type == pygame.QUIT:
                #     pygame.quit()
                #     exit()

            self.screen.blit(button_img, button_menu_rect)
            self.screen.blit(self.font.render(f"{self.button_menu_language[entered_language]}", True, (255, 255, 255)), (745, 100))

            self.screen.blit(button_img, button_settings_rect)
            self.screen.blit(self.font.render(f"{self.button_menu_settings[entered_language]}", True, (255, 255, 255)), (745, 200))

            self.screen.blit(button_img, button_quit_rect)
            self.screen.blit(self.font.render(f"{self.button_menu_quit[entered_language]}", True, (255, 255, 255)), (745, 300))

            # self.screen.blit(self.button, (650, 50))
            # self.screen.blit(self.button, (650, 200))
            # self.screen.blit(self.button, (650, 350))

            pygame.display.flip()
            clock.tick(60)