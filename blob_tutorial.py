import pygame
import random
from blob import Blob  # Requires blob.py class to be in the same folder

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
STEP = [-4, 4]

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):  # Inherit from blobs
    # Define init params
    def __init__(self, x_bnd, y_bnd, step=[-1, 2]):
        super().__init__((0, 0, 255), x_bnd, y_bnd, step)

    def move_fast(self):
        self.x += random.randrange(-6, 6)
        self.y += random.randrange(-6, 6)


def draw_environment(blob_list_dict):
    game_display.fill(WHITE)  # Clear the background

    for blob_dict in blob_list_dict:  # Loop through all dictionary
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]  # Take the individual blob value
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            # blob.move() # Update the position randomly
            blob.move_fast()
            blob.check_bounds()

    pygame.display.update()


def main():
    # List comprehension for creating list of blue blobs
    blue_blobs = [BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]
    # Change into a dictionary with numbers being ID's starting at 0
    blue_blobs = dict(enumerate((blue_blobs)))
    # List comprehension for create list of red blobs
    red_blobs = [BlueBlob(WIDTH, HEIGHT, STEP) for i in range(STARTING_RED_BLOBS)]
    red_blobs = dict(enumerate(red_blobs))
    while True:  # Infinite loop
        for event in pygame.event.get():  # Grab event from the queue
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)  # Capping frames per second
        # update


if __name__ == '__main__':  # __name__ is a special variable set to __main__ within this scope
    main()
