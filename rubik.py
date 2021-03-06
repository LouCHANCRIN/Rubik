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
        for key in cube.faces:
            print(key, ":", f"{cube.faces[key][0:3]}'\n    {cube.faces[key][3:6]}\n    {cube.faces[key][6:9]}", f"({len(cube.faces[key])})")
