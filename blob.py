## Blob class for import modularity testing
import random

class Blob:
    # Set initial variables
    def __init__(self, color, x_bnd, y_bnd, stepRange = [-1,2], sizeRange = [4,8]):
        self.x_bnd = x_bnd
        self.y_bnd = y_bnd
        self.x = random.randrange(0, self.x_bnd) # Inside the window for hte game
        self.y = random.randrange(0, self.y_bnd) # Inside the window
        self.size = random.randrange(sizeRange[0],sizeRange[1]) # Size of the blob
        self.color = color
        self.x_bnd = x_bnd
        self.y_bnd = y_bnd
        self.stepRange = stepRange

    def move(self):
        self.x += random.randrange(self.stepRange[0],self.stepRange[1])
        self.y += random.randrange(self.stepRange[0],self.stepRange[1])

    def check_bounds(self):
        # Boundary conditions so blobs don't move out of bounds
        if self.x < 0: self.x = 0
        elif self.x > self.x_bnd: self.x = self.x_bnd

        if self.y < 0: self.y = 0
        elif self.y > self.y_bnd: self.y = self.y_bnd
