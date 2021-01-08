
class UnknownMoveError(Exception):
    
    def __init__(self, move: str):
        desc = f"Move {move} is not in the list of accepted moves ({MOVES})"

class Cube(object):
    '''FRUBLD stands for Front Right Up Back Left Down'''

    def __init__(self):
        self.r_turn = [6, 2, -2, 4, 0, -4, 2, -2, -6]
        self.l_turn = [2, 4, 6, -2, 0, 2, -6, -4, -2]

        self._moves = {
            "F": self.move_f,
            "F'": self.move_fp,
            "F’": self.move_fp,
            "F2": self.move_f2,
            "R": self.move_r,
            "R'": self.move_rp,
            "R’": self.move_rp,
            "R2": self.move_r2,
            "U": self.move_u,
            "U'": self.move_up,
            "U’": self.move_up,
            "U2": self.move_u2,
            "B": self.move_b,
            "B'": self.move_bp,
            "B’": self.move_bp,
            "B2": self.move_b2,
            "L": self.move_l,
            "L'": self.move_lp,
            "L’": self.move_lp,
            "L2": self.move_l2,
            "D": self.move_d,
            "D'": self.move_dp,
            "D’": self.move_dp,
            "D2": self.move_d2,
         }

        self.faces = {
            # "F": ['f'] * 9,
            # "R": ['r'] * 9,
            "F": ['fron_A', 'fron_B', 'fron_C', 'fron_D', 'fron_E', 'fron_F', 'fron_G', 'fron_H', 'fron_I'],
            "R": ['righ_A', 'righ_B', 'righ_C', 'righ_D', 'righ_E', 'righ_F', 'righ_G', 'righ_H', 'righ_I'],
            "U": ['uppp_A', 'uppp_B', 'uppp_C', 'uppp_D', 'uppp_E', 'uppp_F', 'uppp_G', 'uppp_H', 'uppp_I'],
            "L": ['left_A', 'left_B', 'left_C', 'left_D', 'left_E', 'left_F', 'left_G', 'left_H', 'left_I'],
            "D": ['down_A', 'down_B', 'down_C', 'down_D', 'down_E', 'down_F', 'down_G', 'down_H', 'down_I'],
            "B": ['back_A', 'back_B', 'back_C', 'back_D', 'back_E', 'back_F', 'back_G', 'back_H', 'back_I'],
            # "U": ['u'] * 9,
            # "B": ['b'] * 9,
            # "L": ['l'] * 9,
            # "D": ['d'] * 9,
        }


    def apply_moves(self, move_list: list = []) -> None:
        for move in move_list:
            if move not in self._moves:
                raise UnknownMoveError(move)
            self._moves[move]()

    def turn_r(self, face: str) -> None:
        tmp_face = list(self.faces[face])
        self.faces[face] = [tmp_face[x + self.r_turn[x]] for x in range(0, 9)] 

    def turn_l(self, face: str) -> None:
        tmp_face = list(self.faces[face])
        self.faces[face] = [tmp_face[x + self.l_turn[x]] for x in range(0, 9)] 

    def turn_2(self, face: str) -> None:
        tmp_face = list(self.faces[face])
        self.faces[face] = [tmp_face[- 1 - x] for x in range(0, 9)] 

    def move_f(self,) -> None:
        print("f")
        # tmp_f = [self.faces['F'][x] for x in [0, 3, 6]]
        # tmp_d = [self.faces['D'][x] for x in [0, 3, 6]]
        # tmp_b = [self.faces['B'][x] for x in [0, 3, 6]]
        # tmp_u = [self.faces['U'][x] for x in [0, 3, 6]]
        # print(tmp_f)

    def move_fp(self,) -> None:
        print("fp")

    def move_f2(self,) -> None:
        print("f2")

    def move_r(self,) -> None:
        tmp_f = list(self.faces['F'])

        for x in [2, 5, 8]:
            self.faces['F'][x] = self.faces['D'][x]
            self.faces['D'][x] = self.faces['B'][x]
            self.faces['B'][x] = self.faces['U'][x]
            self.faces['U'][x] = tmp_f[x]

        self.turn_r('R')

    def move_rp(self,) -> None:
        tmp_f = list(self.faces['F'])

        for x in [2, 5, 8]:
            self.faces['F'][x] = self.faces['U'][x]
            self.faces['U'][x] = self.faces['B'][x]
            self.faces['B'][x] = self.faces['D'][x]
            self.faces['D'][x] = tmp_f[x]

        self.turn_l('R')

    def move_r2(self,) -> None:
        tmp_f = list(self.faces['F'])
        tmp_u = list(self.faces['U'])
        tmp_b = list(self.faces['B'])
        tmp_d = list(self.faces['D'])

        for x in [-3, 0, 3]:
            self.faces['F'][5 + x] = tmp_b[5 - x]
            self.faces['U'][5 + x] = tmp_d[5 - x]
            self.faces['B'][5 + x] = tmp_f[5 - x]
            self.faces['D'][5 + x] = tmp_u[5 - x]

        self.turn_2('R')

    def move_u(self,) -> None:
        tmp_f = [self.faces['F'][x] for x in [0, 1, 2]]
        tmp_l = [self.faces['L'][x] for x in [0, 1, 2]]
        tmp_b = [self.faces['B'][x] for x in [0, 1, 2]]
        tmp_r = [self.faces['R'][x] for x in [0, 1, 2]]

        self.faces['F'][0:3] = tmp_r
        self.faces['L'][0:3] = tmp_f
        self.faces['B'][0:3] = tmp_l
        self.faces['R'][0:3] = tmp_b

        self.turn_r('U')

    def move_up(self,) -> None:
        tmp_f = [self.faces['F'][x] for x in [0, 1, 2]]
        tmp_l = [self.faces['L'][x] for x in [0, 1, 2]]
        tmp_b = [self.faces['B'][x] for x in [0, 1, 2]]
        tmp_r = [self.faces['R'][x] for x in [0, 1, 2]]

        self.faces['F'][0:3] = tmp_l
        self.faces['L'][0:3] = tmp_b
        self.faces['B'][0:3] = tmp_r
        self.faces['R'][0:3] = tmp_f

        self.turn_l('U')

    def move_u2(self,) -> None:
        tmp_f = [self.faces['F'][x] for x in [0, 1, 2]]
        tmp_l = [self.faces['L'][x] for x in [0, 1, 2]]
        tmp_b = [self.faces['B'][x] for x in [0, 1, 2]]
        tmp_r = [self.faces['R'][x] for x in [0, 1, 2]]

        self.faces['F'][0:3] = tmp_b
        self.faces['L'][0:3] = tmp_r
        self.faces['B'][0:3] = tmp_f
        self.faces['R'][0:3] = tmp_l

        self.turn_2('U')

    def move_b(self,) -> None:
        print("b")


    def move_bp(self,) -> None:
        print("bp")

    def move_b2(self,) -> None:
        print("b2")

    def move_l(self,) -> None:
        tmp_f = list(self.faces['F'])

        for x in [0, 3, 6]:
            self.faces['F'][x] = self.faces['U'][x]
            self.faces['U'][x] = self.faces['B'][x]
            self.faces['B'][x] = self.faces['D'][x]
            self.faces['D'][x] = tmp_f[x]

        self.turn_r('L')

    def move_lp(self,) -> None:
        tmp_f = list(self.faces['F'])

        for x in [0, 3, 6]:
            self.faces['F'][x] = self.faces['D'][x]
            self.faces['D'][x] = self.faces['B'][x]
            self.faces['B'][x] = self.faces['U'][x]
            self.faces['U'][x] = tmp_f[x]

        self.turn_l('L')

    def move_l2(self,) -> None:
        tmp_f = list(self.faces['F'])
        tmp_u = list(self.faces['U'])
        tmp_b = list(self.faces['B'])
        tmp_d = list(self.faces['D'])

        for x in [-3, 0, 3]:
            self.faces['F'][3 + x] = tmp_b[3 - x]
            self.faces['U'][3 + x] = tmp_d[3 - x]
            self.faces['B'][3 + x] = tmp_f[3 - x]
            self.faces['D'][3 + x] = tmp_u[3 - x]

        self.turn_2('L')

    def move_d(self,) -> None:
        tmp_f = [self.faces['F'][x] for x in [6, 7, 8]]
        tmp_l = [self.faces['L'][x] for x in [6, 7, 8]]
        tmp_b = [self.faces['B'][x] for x in [6, 7, 8]]
        tmp_r = [self.faces['R'][x] for x in [6, 7, 8]]

        self.faces['F'][6:9] = tmp_l
        self.faces['L'][6:9] = tmp_b
        self.faces['B'][6:9] = tmp_r
        self.faces['R'][6:9] = tmp_f

        self.turn_l('D')

    def move_dp(self,) -> None:
        tmp_f = [self.faces['F'][x] for x in [6, 7, 8]]
        tmp_l = [self.faces['L'][x] for x in [6, 7, 8]]
        tmp_b = [self.faces['B'][x] for x in [6, 7, 8]]
        tmp_r = [self.faces['R'][x] for x in [6, 7, 8]]

        self.faces['F'][6:9] = tmp_r
        self.faces['L'][6:9] = tmp_f
        self.faces['B'][6:9] = tmp_l
        self.faces['R'][6:9] = tmp_b

        self.turn_r('D')

    def move_d2(self,) -> None:
        tmp_f = [self.faces['F'][x] for x in [6, 7, 8]]
        tmp_l = [self.faces['L'][x] for x in [6, 7, 8]]
        tmp_b = [self.faces['B'][x] for x in [6, 7, 8]]
        tmp_r = [self.faces['R'][x] for x in [6, 7, 8]]

        self.faces['F'][6:9] = tmp_b
        self.faces['L'][6:9] = tmp_r
        self.faces['B'][6:9] = tmp_f
        self.faces['R'][6:9] = tmp_l

        self.turn_2('D')

