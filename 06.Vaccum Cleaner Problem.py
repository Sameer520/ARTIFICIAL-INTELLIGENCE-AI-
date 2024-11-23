import random
class environment:
    def room(self):
        self.grid=[[random.randint(0,1) for i in range(2)] for _ in range(2)]
        self.pos=[0,0]
    def is_clean(self):
        return all(cell==0 for row in self.grid for cell in row)
    def move_vaccum(self,direction):
        x,y=self.pos
        if direction=="RIGHT":
            self.pos=[x,y+1]
        elif direction=="LEFT":
            self.pos=[x,y-1]
        elif direction=="DOWN":
            self.pos=[x+1,y]
        elif direction=="UP":
            self.pos=[x-1,y]
    def clean(self):
        x,y=self.pos
        if self.grid[x][y]==0:
            print(f"[{x}][{y}] is Already Clean")
        else:
            print("Dust Found Cleaning")
            self.grid[x][y]=0
            print(f"[{x}][{y}] is Cleaned")
    def display_grid(self):
        for row in self.grid:
            print(row)
class vaccum_cleaner:
    def __init__(self,environment):
        self.e=environment
    def start_clean(self):
        print("Initial Room:")
        self.e.display_grid()
        while not self.e.is_clean():
            self.e.clean()
            if self.e.pos==[0,0]:
                self.e.move_vaccum("RIGHT")
            elif self.e.pos==[0,1]:
                self.e.move_vaccum("DOWN")
            elif self.e.pos==[1,1]:
                self.e.move_vaccum("LEFT")
            elif self.e.pos==[1,0]:
                self.e.move_vaccum("UP")
        print("Cleaning Completed")
        self.e.display_grid()
e=environment()
e.room()
vaccum1=vaccum_cleaner(e)
vaccum1.start_clean()
                
