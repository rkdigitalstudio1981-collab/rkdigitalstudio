import random

class AIDriver:
    def __init__(self, name):
        self.name = name
        self.speed = random.uniform(120, 220)
        self.aggression = random.uniform(0.5, 1.0)
        self.position = 0.0

    def update(self, player_speed):
        diff = player_speed - self.speed
        if diff > 10:
            self.speed += self.aggression * random.uniform(0.5, 1.5)
        else:
            self.speed -= random.uniform(0.2, 0.6)
        self.position += self.speed * 0.016
        return {'name': self.name, 'speed': self.speed, 'position': self.position}

if __name__ == '__main__':
    ai = AIDriver('AI_1')
    for _ in range(10):
        print(ai.update(150))
