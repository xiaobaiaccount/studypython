# 2024/4/4 12:09
class GameStats():
    def __init__(self,ai_setting):
        """跟踪游戏的统计信息"""
        self.ai_setting = ai_setting
        self.game_active = False
        #不可重置的最高得分
        self.game_high_score = 0
        self.read_high_score()
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 0

    def read_high_score(self):
        # 读取文件中的最高分
        filename = 'high_score.txt'
        try:
           with open(filename, 'r') as file:
               high_score_message = file.read()
               if high_score_message:
                   self.game_high_score = int(high_score_message)
        except FileNotFoundError:
            pass