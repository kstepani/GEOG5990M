import random
class Agent(): 
    #initialising x,y,environment,agents
    def __init__(self, environment, agents, neighbourhood, y, x):
        self.x=x
        self.y=y
        self.environment = environment
        self.store = 0 
        self.agents = agents
        self.neighbourhood = neighbourhood
        
        
   #define move method      
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    #define eat method
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    
    
    #define distance function            
    def distance_between(self,agents):
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5 
         
                
    #define share_with_neighbours method
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                total = self.store + agent.store
                ave = total /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))
    
           