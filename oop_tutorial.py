import pygame
import random

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3


WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

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

def draw_environment(blob_list_dict):
    game_display.fill(WHITE) # Clear the background

    for blob_dict in blob_list_dict: # Loop through all dictionary
        for blob_id in blob_dict:
            blob = blob_dict[blob_id] # Take the individual blob value using id
            pygame.draw.circle(game_display,blob.color,[blob.x, blob.y],blob.size)
            pygame.display.update()
            blob.move() # Update the position randomly

def main():
    blue_blobs = [Blob(BLUE) for i in range(STARTING_BLUE_BLOBS)] # List comprehension for creating list of blue blobs
    blue_blobs = dict(enumerate((blue_blobs))) # Change into a dictionary with numbers being ID's starting at 0
    red_blobs = [Blob(RED) for i in range(STARTING_RED_BLOBS)] # List comprehension for create list of red blobs
    red_blobs = dict(enumerate(red_blobs))
    while True: # Infinite loop
        for event in pygame.event.get(): # Grab event from the queue
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs,red_blobs])
        clock.tick(60) # Capping frames per second
        # update



if __name__ == '__main__': ## __name__ is a special variable set to __main__ within this scope
    main()
