import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self,ai_settings, screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕底部中央,坐标(0,0)在屏幕左上角
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中储存浮点数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def  update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 向右移动飞船
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            # 向左移动飞船
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx