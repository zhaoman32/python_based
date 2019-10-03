class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ships_limit = 3
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 30
        # 外星人设置
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 10 #外星人掉下来的速度
        # fleet_direction = 1向右移  -1向左移
        self.fleet_direction = 1
