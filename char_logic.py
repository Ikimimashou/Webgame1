# char_logic.py

class Character:
    def __init__(self):
        self.objects = []

    def spawn_object(self, x, y):
        obj = {'x': x, 'y': y}
        self.objects.append(obj)

    def get_objects(self):
        return self.objects
