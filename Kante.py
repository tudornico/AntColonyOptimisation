

class Kante :
    def __init__(self, start, ende, pheromone) :
        self.start = start
        self.ende = ende
        self.pheromone = pheromone

    def calculateDistance(self):
        return (self.start.x - self.ende.x**2 + self.start.y - self.ende.y**2)**0.5

    def __str__(self):
        return "Kante von " + str(self.start) + " nach " + str(self.ende) + " mit pheromone " + str(self.pheromone)
    def __repr__(self):
        return "Kante von " + str(self.start) + " nach " + str(self.ende) + " mit pheromone " + str(self.pheromone)