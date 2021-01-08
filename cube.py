
class UnknownMoveError(Exception):
    
    def __init__(self, move: str):
        desc = f"Move {move} is not in the list of accepted moves ({MOVES})"

class Cube(object):

    def __init__(self):
     
        print("test")
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


    def apply_moves(self, move_list: list = []):
        for move in move_list:
            if move not in self._moves:
                raise UnknownMoveError(move)
            self._moves[move]()


    def move_f(self,):
        print("f")

    def move_fp(self,):
        print("fp")

    def move_f2(self,):
        print("f2")

    def move_r(self,):
        print("r")

    def move_rp(self,):
        print("rp")

    def move_r2(self,):
        print("r2")

    def move_u(self,):
        print("u")

    def move_up(self,):
        print("up")

    def move_u2(self,):
        print("u2")

    def move_b(self,):
        print("b")

    def move_bp(self,):
        print("bp")

    def move_b2(self,):
        print("b2")

    def move_l(self,):
        print("l")

    def move_lp(self,):
        print("lp")

    def move_l2(self,):
        print("l2")

    def move_d(self,):
        print("d")

    def move_dp(self,):
        print("dp")

    def move_d2(self,):
        print("d2")

