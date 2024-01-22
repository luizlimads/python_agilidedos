class Game_Details:
    def __init__(self, game_id = None, user_id = None, line=None, hits = None, miss = None):
        self.game_id = game_id
        self.user_id = user_id
        self.line =line
        self.hits = hits
        self.miss = miss
    
    def __str__(self):
        attributes = vars(self)
        return ' '.join([f'{key}={value}' for key, value in attributes.items()])
