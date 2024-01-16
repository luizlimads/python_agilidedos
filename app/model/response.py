class Default_Response:
    bool_response: bool
    data: dict

    def __init__(self, bool_response = False, data = None,*args, **kwargs):
        self.bool_response = bool_response
        self.data = data