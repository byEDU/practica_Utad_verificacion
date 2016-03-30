from board import Board
from controler import Controler

if __name__ == "__main__":
    c1 = Controler()
    c1.header()
    while not c1.exit:
        c1.menu()



