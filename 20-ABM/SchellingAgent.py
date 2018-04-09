"""
gde 4.2.2018
Adapted from Project Mesa Schelling Model example: 
https://github.com/projectmesa/mesa-schelling-example/blob/master/analysis.ipynb
but changed to run stand-alone. 
""" 

import random

class SchellingAgent():
    '''
    Schelling segregation agent
    '''
    def __init__(self, pos, grid, agent_type):
        '''
         Create a new Schelling agent.

         Args:
            pos: (x, y) Agent initial location.
            grid: a grid of the city, where 0=empty, 1=minority, 2=majority 
            agent_type: Indicator for the agent's type (minority=1, majority=2)
        '''
        self.pos = pos
        self.grid = grid
        self.type = agent_type
        
        self.grid[pos[0]][pos[1]] = self.type
        
    
    def calculate_similarity(self, similarity):
        '''
        Calculates the similarity ratio for the agent.  Defined as:
            similarity = neighbors of same type / total (non-empty) neighbors
        ''' 
        same_type_neighbors =0
        
        neighbors = [(x-1, y+1), (x, y+1), (x+1, y+1)
                     (x-1, y),           , (x+1, y)
                     (x-1,y-1), (x, y-1), (x+1, y-1)]
                      
        for nx, ny in neighbors:
            if nx in range (0,nx):
            if ny in range (0,ny):
        
        print('Implement calculate_similarity()')

    def is_happy(self): 
        '''
        The agent is happy if at least 30% of its neighbors are of the same type.True/false 
        '''
        if self.calculate_similarity() < .3
            self.is_happy = False
        elif self.similarity > 1 
            print ("error")
        else
            self.is_happy = True
        
        print('Implement is_happy()')
        
    def move(self):
        '''
        Moves the agent to a randomly selected empty square. 
        calculate cumulative average bin maybe run random pick random within
        update pos and grid
        get a list of the empty squares
       '''
        empty = []

        if (not self.is_happy)
            for x in range (0,rows)
                for y in range (0, cols)
                    if self.grid[x][y] == 0
                        empty.append((x,y))
            
            cum_prob = 0
            cum_prob_array = []
            for i in range (0, len(empty)):
                cum_prob += 1 / len(empty)
                cum_prob_array.append(cum_prob)
                
            rand = random.random()
            for i in range(0, len(cum_prob_array):
                if rand < cumprob_array[i]:
                           new_pos = empty_squares{i}
                           break
                           
            self.grid[self.pos[0]][self.pos[1]]=0
                           
                           self.pos = new_pos
                                      
                
                
                
                
        print('Implement move')
        