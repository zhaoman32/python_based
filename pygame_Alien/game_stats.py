class GameStats():
    #  跟踪统计游戏信息
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        # 初始化信息
        self.reset_stats()
        # 游戏一开始处于非活动状态
        self.game_active = False
        # 在任何情况下都不得重置最高得分
        with open('high_score', 'r+') as file:
            high = file.readline().strip('\n')
            if high == '':
                high = '0'
        self.high_score = int(high)

    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
