# pygame游戏 外星人入侵
import sys
import pygame
from pygame_Alice.ship import Ship
from pygame_Alice.settings import Setting


def run_game():
    # 初始化游戏
    pygame.init()
    ai_setting = Setting()
    # 创造一个屏幕对象并展示
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alice Invasion")
    # 创造一艘飞船
    ship = Ship(screen)


    # 游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(ai_setting.bg_color)
        ship.blitme()

        # 使屏幕可见
        pygame.display.flip()


run_game()