from health import Health


class Vito_ganyada(Health):
    
    def __init__(self):
        self.score = 500

    def current_health(self):
        return self.score

    def to_dict(self):
        return super().to_dict()
