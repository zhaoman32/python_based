import pygame
from pygame.sprite import Sprite


class Alice(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alice,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alice.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角附近,边距为alice宽度
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
