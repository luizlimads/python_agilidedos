class Words:
    def __init__(self, user_id, name, value):
        self.user_id = user_id
        self.name = name
        self.value = value

    def __str__(self):
        return f'{self.user_id} {self.name}'