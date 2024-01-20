class Game:
    def __init__(self, id = None, user_id = None, words_id = None):
        self.id = id
        self.user_id = user_id
        self.words_id = words_id

    def __str__(self):
        attributes = vars(self)
        return ' '.join([f'{key}={value}' for key, value in attributes.items()])
