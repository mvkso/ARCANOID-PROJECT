import pygame


class Assets:
    """Przechowuje zasoby."""

    def load():
        """Wczytuje zasoby z dysku."""
        pygame.init()
        pygame.mixer.init(44100, -16, 2, 2048)
        Assets.failure_sound = pygame.mixer.Sound("assets/lose.wav")
        Assets.brick_collision_sound = pygame.mixer.Sound("assets/hit.wav")
        Assets.winning_sound = pygame.mixer.Sound("assets/win.wav")
        Assets.main_menu_song = pygame.mixer.Sound("assets/menu.wav")
        Assets.ball_bounce_sound = pygame.mixer.Sound("assets/bounce.wav")
        Assets.icon = pygame.image.load("assets/rocket.png")
        Assets.interface = pygame.image.load("assets/interface.png")
        Assets.cosmos = pygame.image.load("assets/cosmos.png")
        Assets.ball_image = pygame.image.load("assets/ball.png")
        Assets.brick_image = pygame.image.load("assets/brick.png")
        Assets.font = pygame.font.Font(None, 72)
        Assets.font_2 = pygame.font.Font(None, 72)
        Assets.font_3 = pygame.font.Font(None, 45)
        Assets.font_4 = pygame.font.Font(None, 72)
        Assets.font_5 = pygame.font.Font(None, 72)

