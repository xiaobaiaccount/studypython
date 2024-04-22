# 2024/3/23 17:05
import pygame
from pygame.sprite import Sprite

#通过使用精灵可以将相关元素进行编组，进而同时操作编组中的所有元素
class Bullet(Sprite):
    """一个岁飞船发射的子弹进行管理的类"""
    def __init__(self,ai_setting,screen,ship):
        """在飞船所在处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        #使用pygame.Rect() 类从空白开始创建一个矩形
        self.rect =pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        #子弹的初始位置取决于飞船当前的位置（子弹从飞船的头部射出去）
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数存储子弹的位置
        self.y = float(self.rect.y)

        #子弹的颜色和速度
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

