'''对事件的响应'''
import pygame
import sys
from time import sleep

from pygame_Alien.bullet import Bullet
from pygame_Alien.alien import Alien


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    # 响应按下键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # 响应松开键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets,  mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_events(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets,  mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    # 如果处于非活动状态，绘制Play
    if not stats.game_active:
        play_button.draw_button()
    # 使屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 检查子弹是否击中了外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    # 生成新的外星人群
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_setting, screen, ship, aliens):
    # 创建外星人群
    # 先创建一个外星人，并计算一行可以容纳多少外星人
    alien = Alien(ai_setting, screen)
    number_alien_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_row(ai_setting, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_setting, alien_width):
    # 计算每行可以容纳多少外星人
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_row(ai_settings, ship_height, alien_height):
    # 计算屏幕可以增加多少行外星人
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_row = int(available_space_y / (2 * alien_height))
    return number_row


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print("ship hit!!!")
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    # 外星人到达边缘时，采取措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_setting, screen, stats, sb, ship, aliens, bullets):

    if stats.ships_left > 0:
        # 飞船剩余数减1
        stats.ships_left -= 1
        # 更新记分牌
        sb.prep_ships()
        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        # 创建一批新新外星人
        create_fleet(ai_setting, screen, ship, aliens)
        # 把飞船放置在底部中央
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    # 检查是否最高分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        with open('high_score', 'w+') as file:
            file.write(str(stats.high_score))
        sb.prep_high_score()


