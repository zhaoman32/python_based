class GameStats():
    #  跟踪统计游戏信息
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        # 初始化信息
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit
