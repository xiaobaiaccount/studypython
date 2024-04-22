# 2024/3/20 7:19
import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import GameScore
from shield import Shield
import pygame.mixer

def run_game():
    #初始化游戏
    pygame.init()
    #初始化音效
    pygame.mixer.init()
    #创建子弹音效
    sounld_bullet = pygame.mixer.Sound('music/Bullet.mp3')
    #设置射击的音量
    sounld_bullet.set_volume(0.5)
    # 创建一个Setting对象
    ai_setting = Setting()
    #创建一个屏幕对象
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    #设置屏幕的标题
    pygame.display.set_caption("Alien Invasion")
    #创建飞船
    ship = Ship(screen,ai_setting)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个用于存储外星人的编组
    aliens = Group()
    #创建外星人对象
    gf.create_fleet(screen,ai_setting,aliens,ship)
    #创建游戏设置重置对象
    stats = GameStats(ai_setting)
    #创建 play按钮
    play_button = Button(screen,"Play")
    #创建飞船编组（不能在这里创建飞船编组,这样的话ships中的数量只会一直增加，无法减少，因为只有add）
    #ships = Group()
    #创建得分
    gamescore = GameScore(screen,ai_setting,stats)
    #创建盾牌编组
    shields = Group()
    shield = Shield(screen,ai_setting,ship)
    shields.add(shield)

    #开始游戏的主循环
    while True:
        #使用监听方法
        gf.check_events(ship, ai_setting, screen, bullets,play_button,stats,aliens,gamescore,sounld_bullet)
        if stats.game_active:
           #先监听飞船的移动事件再重新绘制飞船
           ship.update()
           gf.update_bullets(aliens, bullets, screen, ai_setting, ship,stats,gamescore,shields)
           gf.update_aliens(ai_setting, aliens, ship, stats, bullets, screen,gamescore)
        gf.update_screen(ai_setting,screen,ship,bullets,aliens,play_button,stats,gamescore,shields)

run_game()