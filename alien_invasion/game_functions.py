# 2024/3/23 11:22
import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullet(bullets,ai_setting,screen,ship,sounld_bullet):
    if(ai_setting.bullet_allowed != 0 and len(bullets) < ai_setting.bullet_allowed):
        # 创建一个子弹并将其加入到编组bullets中
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)
        sounld_bullet.play()

def start_game(stats,aliens,bullets,screen,ai_setting,ship,gamescore):
    """游戏开始"""
    if  not stats.game_active:
        #重置游戏
        stats.reset_stats()
        #重绘得分、等级板、飞船数
        gamescore.prep_level()
        gamescore.prep_score()
        gamescore.prep_ships()

        ai_setting.initialize_dynamic_setting()
        stats.game_active = True
        #游戏开始的时候让光标不可见
        pygame.mouse.set_visible(False)

        aliens.empty()
        bullets.empty()

        create_fleet(screen,ai_setting,aliens,ship)
        ship.center_ship()

def check_keydown_events(event,ship,ai_setting,screen,bullets,stats,aliens,gamescore,sounld_bullet):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets,ai_setting,screen,ship,sounld_bullet)
    elif event.key == pygame.K_p:
        start_game(stats, aliens, bullets, screen, ai_setting, ship,gamescore)


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship, ai_setting, screen, bullets,play_button,stats,aliens,gamescore,sounld_bullet):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #将最高分写入到文件中
            filename = 'high_score.txt'
            with open(filename,'w') as file:
                file.write(str(stats.game_high_score))

            #退出游戏时，关闭混音器
            pygame.mixer.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             check_keydown_events(event,ship,ai_setting,screen,bullets,stats,aliens,gamescore,sounld_bullet)
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
             mouse_x,mouse_y = pygame.mouse.get_pos()
             check_play_button(mouse_x, mouse_y, play_button, stats, aliens, bullets, screen, ai_setting, ship,
                               gamescore)

def check_play_button(mouse_x,mouse_y,play_button,stats,aliens,bullets,screen,ai_setting,ship,gamescore):
    button_clicked  = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked:
        #重置游戏
        start_game(stats, aliens, bullets, screen, ai_setting, ship,gamescore)

def check_high_score(stats,gamescore):
    # 判断当前得分是否比最高得分大(如果是更新最高得分)
    if stats.score > stats.game_high_score:
        stats.game_high_score = stats.score
        # 重绘最高得分板
        gamescore.prep_high_score()

def start_new_level(stats,gamescore):
    """开始一个新等级"""
    # 每消灭一群外星人等级就加一,重绘等分板
    stats.level += 1
    gamescore.prep_level()

def  check_bullet_alien_collisions(bullets, aliens,screen, ai_setting,ship,stats,gamescore):
    # 检查是否右子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    # True True 是删除子弹和外星人  False True 子弹 不会消失，外星人会消失
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    #统计子弹与外星人的碰撞次数，然后累计分数
    if collisions :
        for aliens in collisions.values():
            stats.score += ai_setting.alien_score * len(aliens)
            gamescore.prep_score()
        #适时更新最高得分
        check_high_score(stats, gamescore)

    if len(aliens) == 0:
        bullets.empty()
        start_new_level(stats,gamescore)
        ai_setting.increase_speed()
        create_fleet(screen, ai_setting, aliens, ship)

def check_bullet_shield(shields,bullets):
    """检查盾牌和子弹之间发生碰撞，如果发生了子弹消失"""
    pygame.sprite.groupcollide(bullets, shields, True, False)

def update_bullets(aliens,bullets,screen,ai_setting,ship,stats,gamescore,shields):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()

    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_shield(shields, bullets)
    check_bullet_alien_collisions(bullets, aliens, screen, ai_setting, ship,stats,gamescore)


def get_number_aliens_x(ai_setting,alien_width):
    """计算可以绘制的外星人数量"""
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x= int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_rows_number(ai_setting,alien_height,ship):
    """计算可以绘制的外星人数量"""
    available_space_y = ai_setting.screen_height - 3 * alien_height - ship.rect.height
    number_aliens_y= int(available_space_y/(2*alien_height))
    return number_aliens_y

#self.rect.x表示矩形对象左上角x的坐标
#self.rect.width表示矩形对象的宽度
#self.rect.y和self.rect.height同理
def create_alien(screen,ai_setting,aliens,alien_number_x,alien_number_y):
    #创建外星人,此时外星人的 self.x = float(self.rect.x),初始化的时候赋的值
    alien = Alien(screen,ai_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    #此时用下面的语句给alien.rect.x赋值，而self.x一直都是创建时初始化的值，所以update的时候self.rect.x的值一直都是初始值self.x
    #所以只要一移动，那么每行上面的外星人的self.rect.x都是一样的，那么就会发生重叠
    #alien.rect.x = alien_width + 2 * alien_width * alien_number_x

    alien.x= alien_width + 2 * alien_width * alien_number_x
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * alien_number_y
    aliens.add(alien)

def create_fleet(screen,ai_setting,aliens,ship):
    #创建一个外星人
    alien = Alien(screen,ai_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    #先计算可以创建多少个外星人
    number_aliens_x = get_number_aliens_x(ai_setting,alien_width)
    number_aliens_y = get_rows_number(ai_setting,alien_height,ship)
    #循环创建那么多外星人
    for alien_number_y in range(number_aliens_y):
       for alien_number_x in range(number_aliens_x):
           create_alien(screen,ai_setting,aliens,alien_number_x,alien_number_y)

def change_fleet_direction(ai_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.alien_drop
    ai_setting.fleet_direction *= -1

def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break

def ship_hip(stats,aliens,bullets,screen,ai_setting,ship,gamescore):
    if stats.ships_left > 0:
       stats.ships_left -= 1
       # 重新绘制飞船数
       gamescore.prep_ships()

        #因为stats.ships_left > 0 所以只有接下来还有机会的时候才会走下面的步骤
       # (也就是如果在这更新最高得分得有下次机会才行，所以不能在这写更新最高得分)
       if stats.ships_left > 0:
          #准备下一轮
          aliens.empty()
          bullets.empty()

          create_fleet(screen, ai_setting, aliens, ship)
          ship.center_ship()

          # 暂停0.5秒
          sleep(1)
       else:
           stats.game_active = False
           # 游戏结束的时候让光标可见
           pygame.mouse.set_visible(True)


def check_alien_bottom(aliens,screen,stats,bullets,ai_setting,ship,gamescore):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hip(stats, aliens, bullets, screen, ai_setting, ship,gamescore)
            break  #停止循环

def update_aliens(ai_setting,aliens,ship,stats,bullets,screen,gamescore):
    """外星人左右移动，如果外星人到达边缘，那么向下移动并且改为移动方向"""
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    check_alien_bottom(aliens, screen, stats, bullets, ai_setting, ship,gamescore)

    for alien in aliens.copy():
        if alien.rect.bottom <= 0:
            bullets.remove(alien)

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hip(stats, aliens, bullets, screen, ai_setting, ship,gamescore)

def update_screen(ai_setting,screen,ship,bullets,aliens,play_button,stats,gamescore,shields):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环是都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    #让编组中的外星人绘制出来
    aliens.draw(screen)
    shields.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    #显示字体
    gamescore.show_score()

    #让最近绘制的屏幕可见
    pygame.display.flip()

