import pygame
import random
import numpy as np
from blob import Blob # Requires blob.py class to be in the same folder
import logging

'''
DEBUG   detailed information, only of interest when diagnosing problems
INFO    confirmation that things are working as expected
WARNING an indication that something unexpected happened, or indicative of some problems
ERROR   due to a more serious problem, the software has not been able to perform functions
CRITICAL    A serious error that may indicate inability to run
'''

logging.basicConfig(filename = 'logfile.log',level = logging.INFO) # Specify the level of debug

STARTING_BLUE_BLOBS = 15
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15

WIDTH = 800
HEIGHT = 600
STEP = [-4,4]

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class RedBlob(Blob): # Inherit from blobs
    # Define init params
    def __init__(self, x_bnd, y_bnd, step = [-1,2]):
        Blob.__init__(self,(255,0,0), x_bnd, y_bnd, step) # Must have self passed

class GreenBlob(Blob): # Inherit from blobs
    # Define init params
    def __init__(self, x_bnd, y_bnd, step = [-1,2]):
        Blob.__init__(self,(0,255,0), x_bnd, y_bnd, step) # Must have self passed

# Consider the blue blob the protagonist and define addition operation
class BlueBlob(Blob): # Inherit from blobs
    # Define init params
    def __init__(self, x_bnd, y_bnd, step = [-1,2]):
        Blob.__init__(self,(0,0,255), x_bnd, y_bnd, step) # Must have self passed

    def __add__(self,other_blob):
        logging.info('Blob add op {} + {}'.format(self, other_blob ))
        # Green adds size, red subtracts sizeRange
        if( other_blob.color == (255, 0, 0) ):
            # Red blob subtracts size (damage)
            self.size -= other_blob.size # Reduce size
            other_blob.size -= self.size
        elif( other_blob.color == (0, 255 , 0)):
            # Green blob adds size (healing)
            self.size += other_blob.size
            other_blob.size = 0
        elif( other_blob.color == (0, 0 , 255)):
            pass
        else:
            raise Exception('Tried to tried to combine unsupported colors')

def collision_handler(b_list):
    # Perform addition
    reds, greens, blues = b_list # Unpack

    # Perform addition for each in blue_blobs
    # Perform copies in order to not modify the original dictionary
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in reds, greens: # For each dictionary
            for other_blob_id, other_blob in other_blobs.copy().items(): # For each dictionary entry
                # Check if it is itself and pass
                logging.debug('Checking if blobs are touching {} + {}'.format(
                str(blue_blob.color), str(other_blob.color)
                ))
                if blue_blob == other_blob:
                    pass
                elif collision_check(blue_blob, other_blob):
                    blue_blob + other_blob
                    if other_blob.size <= 0:
                        del other_blobs[other_blob_id]
                    if blue_blob.size <= 0:
                        del blues[blue_id]
    return reds, greens, blues

def collision_check(blob1, blob2):
    # Distance vector
    v = np.array([blob1.x - blob2.x, blob1.y - blob2.y])

    if( np.linalg.norm(v) <= (blob1.size + blob2.size) ):
        return True
    else:
        return False

def draw_environment(blob_list_dict):
    game_display.fill(WHITE) # Clear the background

    reds, greens, blues = collision_handler(blob_list_dict)

    for blob_dict in reds, greens, blues: # Loop through all dictionary
        for blob_id in blob_dict:
            blob = blob_dict[blob_id] # Take the individual blob value using id
            pygame.draw.circle(game_display,blob.color,[blob.x, blob.y],blob.size)
            blob.move() # Update the position randomly
            blob.check_bounds()

    pygame.display.update()

    return reds, greens, blues

def main():


    red_blobs = [RedBlob(WIDTH,HEIGHT,STEP) for i in range(STARTING_RED_BLOBS)] # List comprehension for create list of red blobs
    red_blobs = dict(enumerate(red_blobs))

    green_blobs = [GreenBlob(WIDTH, HEIGHT, STEP) for i in range(STARTING_GREEN_BLOBS)]
    green_blobs = dict(enumerate(green_blobs))

    blue_blobs = [BlueBlob(WIDTH,HEIGHT,STEP) for i in range(STARTING_BLUE_BLOBS)] # List comprehension for creating list of blue blobs
    blue_blobs = dict(enumerate((blue_blobs))) # Change into a dictionary with numbers being ID's starting at 0

    print(blue_blobs[0])
    print(str(blue_blobs[0]))

    while True: # Infinite loop
        try:
            for event in pygame.event.get(): # Grab event from the queue
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            red_blobs, green_blobs, blue_blobs = draw_environment([red_blobs, green_blobs, blue_blobs])
            clock.tick(60) # Capping frames per second
            pygame.display.update
        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break

if __name__ == '__main__': ## __name__ is a special variable set to __main__ within this scope
    main()
