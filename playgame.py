from windows import DYYLGUI
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

class game(DYYLGUI):
    def __init__(self):
        super().__init__()

        self.is_black_turn = True
        self.game_over = False
        
        #Run()

    #def Run(self):

    def SwitchTurn(self):
        if self.is_black_turn:
            self.is_black_turn = False
        else:
            self.is_black_turn = True
            
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = game()
    sys.exit(app.exec_())