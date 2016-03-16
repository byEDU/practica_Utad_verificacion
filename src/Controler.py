from random import randint
from Board import Board

class Controler:
    def __init__(self):
        self.turn = randint(1,2)
        self.board = Board()
        self.isGameFinished = False
    def cambiarTurno(self):
        if self.turn == 1:
            self.turn = 2
        else: self.turn = 1
    def playMake(self):
        answer = []
        file1 = -1
        while file1 < 1 or file1 > 3:
            print "Introduce la fila a insertar(1, 2 o 3)"
            file1 = input()

        answer.append(file1)

        numSticks = -1
        while numSticks < 0 or numSticks > self.board.numSticks | numSticks > self.board.numSticksAvaliable(file1):
            print "Introduce un numero valido de palitos para eliminar"
            numSticks = input()

        answer.append(numSticks)
        return answer

    def gameFinished(self):
        winner = 0
        if self.board.numSticks == 1:
            self.isGameFinished = True
            if self.turn == 1:

                return 2
            else:
                return 1
        elif self.board.numSticks == 0:
            self.isGameFinished = True
            return self.turn

    def play(self):
        winner = 0
        print '''
            $$$$$$$$\ $$\                                           $$\ $$\   $$\                                $$$$$$\                                    $$\
            \__$$  __|$$ |                                          $$ |\__|  $$ |                              $$  __$$\                                   $$ |
               $$ |   $$$$$$$\   $$$$$$\         $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$\    $$$$$$\   $$$$$$$\       $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$ |
               $$ |   $$  __$$\ $$  __$$\       $$  __$$\  \____$$\ $$ |$$ |\_$$  _|  $$  __$$\ $$  _____|      $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ $$ |
               $$ |   $$ |  $$ |$$$$$$$$ |      $$ /  $$ | $$$$$$$ |$$ |$$ |  $$ |    $$ /  $$ |\$$$$$$\        $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |\__|
               $$ |   $$ |  $$ |$$   ____|      $$ |  $$ |$$  __$$ |$$ |$$ |  $$ |$$\ $$ |  $$ | \____$$\       $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
               $$ |   $$ |  $$ |\$$$$$$$\       $$$$$$$  |\$$$$$$$ |$$ |$$ |  \$$$$  |\$$$$$$  |$$$$$$$  |      \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ $$\
               \__|   \__|  \__| \_______|      $$  ____/  \_______|\__|\__|   \____/  \______/ \_______/        \______/  \_______|\__| \__| \__| \_______|\__|
                                                $$ |
                                                $$ |
                                                \__|
            '''
        raw_input("Press Enter to continue....")
        self.board.paint()
        while(not self.isGameFinished):
            print "Es el turno del jugador " + str(self.turn)
            answer = self.playMake()
            self.board.crossOut(answer[0], answer[1])
            self.board.paint()
            winner = self.gameFinished()

        print "HA GANADO EL JUGADOR " + str(winner)





