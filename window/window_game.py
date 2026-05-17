import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen

        """ Код окна """
        self.button = pygame.image.load("bikers_game_img/menu_objects/Button.png")
        self.bg = pygame.image.load("bikers_game_img/background/back.png")
        self.font = pygame.font.SysFont("Arial", 20)
        self.font_hp = pygame.font.SysFont("Arial", 34)

        """ Игроки """
        self.one_player_jump = pygame.image.load("bikers_game_img/player/pl_1_jump.png")
        self.one_player = pygame.image.load("bikers_game_img/player/pl_1.png")

        self.two_player_jump = pygame.image.load("bikers_game_img/player/pl_2_jump.png")
        self.two_player = pygame.image.load("bikers_game_img/player/pl_2.png")

        self.tree_player_jump = pygame.image.load("bikers_game_img/player/pl_3_jump.png")
        self.tree_player = pygame.image.load("bikers_game_img/player/pl_3.png")

        self.four_player_jump = pygame.image.load("bikers_game_img/player/pl_4_jump.png")
        self.four_player = pygame.image.load("bikers_game_img/player/pl_4.png")

        self.p1_platform = pygame.image.load("bikers_game_img/platform/platform_1.png")
        self.p2_platform = pygame.image.load("bikers_game_img/platform/platform_2.png")
        self.p3_platform = pygame.image.load("bikers_game_img/platform/platform_3.png")
        self.p4_platform = pygame.image.load("bikers_game_img/platform/platform_4.png")

        self.hp_platform_bg = pygame.image.load("bikers_game_img/menu_objects/bg_hp.png")

        self.button_up = pygame.transform.scale(pygame.image.load("bikers_game_img/menu_objects/button_up.png"), (150, 150))

        """ Переменные """
        self.hp_platform_one = 100
        self.hp_platform_two = 100

        self.start_animation_one = 0
        self.start_animation_two = 0
        self.state_platform_one = 1
        self.state_platform_two = 1
        self.table_pos = 0
        self.speed = 5

        self.button_back_menu = ['Обратно в меню' ,'Menüye geri dön' ,'Back to menu' ]

        self.jump_one_player = False
        self.jump_two_player = False

    def platform_mechanics(self, player):
        setattr(self, f"hp_platform_{player}", getattr(self, f"hp_platform_{player}") - 10)

        hp = getattr(self, f"hp_platform_{player}")

        if 80 <= hp <= 100:
            setattr(self, f"state_platform_{player}", 1)
        elif 70 <= hp < 80:
            setattr(self, f"state_platform_{player}", 2)
        elif 40 <= hp < 70:
            setattr(self, f"state_platform_{player}", 3)
        elif 0 <= hp < 40:
            setattr(self, f"state_platform_{player}", 4)
        else:
            print("Вы выиграли")

        setattr(self, f"jump_{player}_player", True)
        setattr(self, f"start_animation_{player}", pygame.time.get_ticks())


    def run(self, entered_language=0):
        while True:

            self.screen.blit(self.bg, (-200, 0))
            button = pygame.image.load("bikers_game_img/menu_objects/bg_name.png")

            one_player = pygame.transform.flip(self.tree_player, True, False)
            one_player_jump = pygame.transform.flip(self.tree_player_jump, True, False)

            two_player = pygame.transform.flip(self.four_player, False, False)
            two_player_jump = pygame.transform.flip(self.four_player_jump, False, False)

            button_back_menu = button.get_rect(topleft=(400, 40))

            # button control for player
            button_up_one_player = button.get_rect(topleft=(50, 300))
            button_up_two_player = button.get_rect(topleft=(800, 300))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.platform_mechanics("one")
                    if event.key == pygame.K_l:
                        self.platform_mechanics("two")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_back_menu.collidepoint(event.pos):
                        return "menu"
                    if button_up_one_player.collidepoint(event.pos):
                        self.platform_mechanics("one")
                    if button_up_two_player.collidepoint(event.pos):
                        self.platform_mechanics("two")

            # PLAYER 1
            if self.jump_one_player:
                if self.start_animation_one + 150 < pygame.time.get_ticks():
                    self.jump_one_player = False
                    self.screen.blit(one_player, (200, 110))
                else:
                    self.screen.blit(one_player_jump, (200, 110))
            else:
                self.screen.blit(one_player, (200, 110))

            # PLAYER 2
            if self.jump_two_player:
                if self.start_animation_two + 150 < pygame.time.get_ticks():
                    self.jump_two_player = False
                    self.screen.blit(two_player, (550, 110))
                else:
                    self.screen.blit(two_player_jump, (550, 110))
            else:
                self.screen.blit(two_player, (550, 110))

            self.screen.blit(button, button_back_menu)
            self.screen.blit(self.font.render(f"{self.button_back_menu[entered_language]}", True, (255, 255, 255)), (450, 58))

            # HP Players one
            self.screen.blit(self.hp_platform_bg, (50, -60))
            self.screen.blit(self.font_hp.render(f"{self.hp_platform_one}", True, (255, 255, 255)), (150, 50))

            # HP Players two
            self.screen.blit(self.hp_platform_bg, (700, -60))
            self.screen.blit(self.font_hp.render(f"{self.hp_platform_two}", True, (255, 255, 255)), (800, 50))

            # platform for one_player
            self.screen.blit(getattr(self, f"p{self.state_platform_one}_platform"), (200, 200))

            # platform for one_player
            self.screen.blit(getattr(self, f"p{self.state_platform_two}_platform"), (550, 200))

            self.screen.blit(self.button_up, button_up_one_player)
            self.screen.blit(self.button_up, button_up_two_player)

            pygame.display.flip()
            pygame.time.Clock()