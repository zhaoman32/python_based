# pygame游戏 外星人入侵

import pygame
from pygame.sprite import Group

from pygame_Alien.alien import Alien
from pygame_Alien.button import Button
from pygame_Alien.scoreboard import Scoreboard
from pygame_Alien.game_stats import GameStats
from pygame_Alien.ship import Ship
from pygame_Alien.settings import Setting
import pygame_Alien.game_functions as gf



def run_game():
    # 初始化游戏
    pygame.init()
    ai_setting = Setting()
    # 创造一个屏幕对象并展示
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建PLAY按钮
    play_button = Button(ai_setting, screen, "Play")
    # 创造一艘飞船
    ship = Ship(ai_setting, screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_setting, screen, ship, aliens)
    # 创建一个储存统计的实例
    stats = GameStats(ai_setting)
    # 创建一个记分牌
    sb = Scoreboard(ai_setting, screen, stats)



    # 游戏主循环, 一直在check_event和绘制screen
    while True:
        gf.check_events(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()