"""
This is a module containing the Agent class. This class includes all the properties and behaviour of our agents.
"""

import random
class Agent(): 
    #initialising x,y,environment,agents
    #the default values of y and x are None
    def __init__(self, environment, agents, y = None, x = None):
        """
        Initialise the agent.
        
        environment -- a raster file in which the agents are located
        agents -- all the agents in the environment
        neighbourhood -- the surrounding area of the agent 
        y -- y coordinate of the agent's location
        x -- x coordinate of the agent's location
        """
        
        self.x=x
        self.y=y
        self.environment = environment
        self.store = 0 
        self.agents = agents
        self.neighbourhood = neighbourhood
        
        #if x and y data are missing then randomised values will be given to x and y variables
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
    
   #define move method      
    def move(self):
        """
        Moves the agent in the environment
        """
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    #define eat method
    def eat(self): 
        """
        The Agent eats the environment
        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    
    #define distance function            
    def distance_between(self,agents):
        """
        A function which calculates and returns the distance between agents
        """
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5 
         
                
    #define share_with_neighbours method
    def share_with_neighbours(self, neighbourhood):
        """
        The agent interacts with other agents in its neighbourhood
        """
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                total = self.store + agent.store
                ave = total /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
    
           