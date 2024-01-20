class Words:
    id: int
    user_id: int 
    name: str
    value: str

    def __init__(self, id = None, user_id = None, name = None, value = None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.value = value

    def __str__(self):
        attributes = vars(self)
        return ' '.join([f'{key}={value}' for key, value in attributes.items()])
