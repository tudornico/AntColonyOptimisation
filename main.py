import hashlib

import matplotlib.pyplot as plt
import random


x = [random.randint(1, 100) for n in range(100)]
y = [random.randint(1, 100) for n in range(100)]

nodes = []
for iterator in range(100):
    nodes.append((x[iterator], y[iterator]))  # x and y are the coordinates of the nodes

plt.scatter(x, y)
plt.show()

#start node is going to be nodes[0]

class AntColonyAlgorithm:
    def __init__(self, nodes, alpha, beta, rho, Q):
        self.nodes = nodes
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.decay = 0.9
        self.pheromone = [[1 for i in range(len(nodes))] for j in range(len(nodes))]
    def getDistance(self, node1, node2):
        return ((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)**0.5

    def getPheromone(self, node1, node2):
        return self.pheromone[self.getNodePosition(node1)][self.getNodePosition(node2)]
    #finds the node position in the list
    def getNodePosition(self, node):
        for i in range(len(self.nodes)):
            if self.nodes[i] == node:
                return i
    #update pheromone with formula
    def updatePheromone(self, node1, node2):

        # hold account for pheromone decay
        for  i in range(len(self.pheromone)):
            for j in range(len(self.pheromone[i])):
                self.pheromone[i][j] = self.decay * self.pheromone[i][j]

        # update pheromone with the formula
        self.pheromone[self.getNodePosition(node1)][self.getNodePosition(node2)] = (1 - self.rho) * self.getPheromone(
            node1, node2) + self.rho * self.Q

    def calculateMetaHeuristic(self, node1, node2):
        if(node1 != node2):
         return self.getPheromone(node1, node2)**self.alpha * self.getDistance(node1, node2)**self.beta
        else:
            return 0

    def pickNextNode(self, currentNode,visitedCities):
        #calculate the metaheuristic for each node
        metaHeuristic = [self.calculateMetaHeuristic(currentNode, self.nodes[i]) for i in range(len(self.nodes))]
        #calculate the sum of the metaheuristic
        sumMetaHeuristic = sum(metaHeuristic)
        #calculate the probability for each node

        probability = [metaHeuristic[i] / sumMetaHeuristic for i in range(len(self.nodes))]
        #pick a node with the probability
        #while not picking from the visited cities
        while True:
            #pick random node from the list with the probability from probability list

            nextNode = self.nodes[self.pickNode(probability)]

            if nextNode not in visitedCities:
                return nextNode

    def pickNode(self, probability):
        #pick a node with the probability
        x = random.uniform(0, 1)
        cumulativeProbability = 0.0
        for i in range(len(probability)):
            cumulativeProbability += probability[i]
            if x < cumulativeProbability:
                return i
    # we are going to run the algorithm for all the cities for one ant
    def run(self):
        #start node is going to be nodes[0]
        currentNode = self.nodes[0]
        visitedCities = []
        #we are going to run the algorithm for all the cities only once
        # we need to keep track of the cities we have visited

        for i in range(len(self.nodes)):
            nextNode = self.pickNextNode(currentNode ,visitedCities)
            visitedCities.append(nextNode)
            self.updatePheromone(currentNode, nextNode)
            currentNode = nextNode


        self.plotVisitedCities(visitedCities)
    # also make the lines between the cities
    def plotVisitedCities(self, visitedCities):
        x = [self.nodes[i][0] for i in range(len(visitedCities))]
        y = [self.nodes[i][1] for i in range(len(visitedCities))]
        plt.plot(x, y)
        #add to the plot the lines between the cities
        # colour the start and end node

        for i in range(len(visitedCities) - 1):
            plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], color='red')
        plt.scatter(self.nodes[0][0], self.nodes[0][1], color='green')
        plt.show()
        print(visitedCities )
        print("this is the distance of the tour")
    # run the run() function for iterations
    def runForIterations(self, iterations):
        for i in range(iterations):
            self.run()
            print(self.pheromone[0])

def main():
    # create an object of the class AntColonyAlgorithm
    # nodes is the list of nodes
    # alpha is the importance of the pheromone
    # beta is the importance of the distance
    # rho is the importance of the heuristic
    # Q is the pheromone constant
    #choose good constants according to the distance
    #the distance is the distance between the cities

    aca = AntColonyAlgorithm(nodes, alpha=1, beta=1, rho=0.5, Q=100)
    # run the algorithm for iterations
    aca.runForIterations(iterations=3)

main()