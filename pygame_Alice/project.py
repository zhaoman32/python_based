# pygame游戏 外星人入侵
import sys
import pygame
from pygame.sprite import Group

from pygame_Alice.ship import Ship
from pygame_Alice.settings import Setting
import pygame_Alice.game_functions as gf



def run_game():
    # 初始化游戏
    pygame.init()
    ai_setting = Setting()
    # 创造一个屏幕对象并展示
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alice Invasion")
    # 创造一艘飞船
    ship = Ship(ai_setting, screen)
    # 创建一个存储子弹的编组
    bullets = Group()


    # 游戏主循环
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_setting, screen, ship, bullets)


run_game()