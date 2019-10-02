'''对事件的响应'''
import pygame
import sys

from pygame_Alice.bullet import Bullet


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    # 响应按下键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ship,bullets)




def check_keyup_events(event, ship):
    # 响应松开键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(ai_setting, screen, ship, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)



def update_screen(ai_settings, screen, ship, bullets):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()

    ship.blitme()

    # 使屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

