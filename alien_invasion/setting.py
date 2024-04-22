# 2024/3/20 7:29
class Setting():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
      """初始化游戏的设置"""
      #屏幕设置
      self.screen_width = 1200
      self.screen_height = 800
      self.bg_color = (230,230,230)
      #飞船的设置
      self.ship_limit = 2

      #子弹的设置
      self.bullet_width = 2000
      self.bullet_height = 15
      self.bullet_color = 60,60,60
      self.bullet_allowed = 3

      #外星人设置
      self.alien_drop = 50
      #增加速度
      self.increase_factor = 5
      self.initialize_dynamic_setting()

      #增加子弹的分值
      self.score_scale = 1.1

    def initialize_dynamic_setting(self):
         self.ship_speed_factor = 2
         self.bullet_speed_factor = 3
         self.alien_speed_factor = 0.5

         # fleet_direction为1表示向右移，-1表示向左移
         self.fleet_direction = 1
         #每个外星人的点数
         self.alien_score = 50


    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.increase_factor
        self.bullet_speed_factor *= self.increase_factor
        self.alien_speed_factor *= self.increase_factor
        self.alien_score  = int(self.alien_score * self.score_scale)


