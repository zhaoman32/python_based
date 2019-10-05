class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ships_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 30
        # 外星人设置
        self.fleet_drop_speed = 2  # 外星人掉下来的速度
        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        # 记分
        self.alien_points = 50
        # 外星人点数的提高速度
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        # fleet_direction = 1向右移  -1向左移
        self.fleet_direction = 1

    def increase_speed(self):
        # 提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)