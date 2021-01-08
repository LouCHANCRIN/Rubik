import sys
import logging
from cube import Cube


def random_moves():
    print("random") 

if __name__ == "__main__":
    cube = Cube()
    if len(sys.argv) == 1:
        logging.warning("No parameters passed, randomly moving the cube")
        cube.random_moves()
    else:
        if len(sys.argv) > 2:
            logging.warning(f"Too much parameters, ignoring all except {sys.argv[1]}")
        moves = sys.argv[1].split(' ')
        cube.apply_moves(moves)
