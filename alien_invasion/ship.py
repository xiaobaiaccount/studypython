# 2024/3/21 21:49
import pygame
from setting import Setting
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,ai_setting):
        """初始胡飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #飞船左右移动的标识
        self.moving_right = False
        self.moving_left = False

        #将屏幕中央的位置和底部对齐的位置传给了对象rect.centerx属性
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #可以存储小数的飞船中间位置坐标
        self.center = float(self.rect.centerx)

    def update(self):
        """更新飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        #根据self.center更新rect对象，self.rect.centerx只能存储整数
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        """在指定位置绘制飞船"""
        #根据self.rect 指定的位置将图像绘制到屏幕上
        self.screen.blit(self.image,self.rect)