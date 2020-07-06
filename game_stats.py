class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        #High score should never be reset.
        f = open("highscore.txt", "r")
        self.high_score = f.read()
        f.close()


    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
