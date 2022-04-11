from random import random

from Kante import Kante


from matplotlib import pyplot as plt


class PossibleRoads:
    def __init__(self):

        x = [random() for i in range(100)]
        y = [random() for i in range(100)]
        nodes = []
        for iterator in range(100):
            nodes.append((x[iterator], y[iterator]))  # x and y are the coordinates of the nodes

        plt.scatter(x, y)
        plt.show()
        self.possibleRoads = []
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                self.possibleRoads.append(Kante(nodes[i], nodes[j],0.1))


    def getPossibleRoads(self):
        return self.possibleRoads

def main():
    possibleRoads = PossibleRoads()
    print(possibleRoads.getPossibleRoads())
main()
