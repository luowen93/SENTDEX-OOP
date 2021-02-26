class Blob:

    # Set initial variables
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH) # Inside the window for hte game
        self.y = random.randrange(0, HEIGHT) # Inside the window
        self.size = random.randrange(4,8) # Size of the blob
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1,2) # Don't really understand what's happening here
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH

        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT
