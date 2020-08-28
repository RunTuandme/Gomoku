'''
    This is a simple Gobang interface.
    By : RunTuandme
'''

coordinate_grid = {
    0:(  7.5,  37.5),   1:( 32.5,  37.5),   2:( 57.5,  37.5),   3:( 82.5,  37.5),   4:(107.5,  37.5),   5:(132.5,  37.5),   6:(157.5,  37.5),   7:(182.5,  37.5),   8:(207.5,  37.5),   9:(232.5,  37.5),  10:(257.5,  37.5),  11:(282.5,  37.5),  12:(307.5,  37.5),  13:(332.5,  37.5),  14:(357.5,  37.5), 
    15:(  7.5,  62.5),  16:( 32.5,  62.5),  17:( 57.5,  62.5),  18:( 82.5,  62.5),  19:(107.5,  62.5),  20:(132.5,  62.5),  21:(157.5,  62.5),  22:(182.5,  62.5),  23:(207.5,  62.5),  24:(232.5,  62.5),  25:(257.5,  62.5),  26:(282.5,  62.5),  27:(307.5,  62.5),  28:(332.5,  62.5),  29:(357.5,  62.5), 
    30:(  7.5,  87.5),  31:( 32.5,  87.5),  32:( 57.5,  87.5),  33:( 82.5,  87.5),  34:(107.5,  87.5),  35:(132.5,  87.5),  36:(157.5,  87.5),  37:(182.5,  87.5),  38:(207.5,  87.5),  39:(232.5,  87.5),  40:(257.5,  87.5),  41:(282.5,  87.5),  42:(307.5,  87.5),  43:(332.5,  87.5),  44:(357.5,  87.5), 
    45:(  7.5, 112.5),  46:( 32.5, 112.5),  47:( 57.5, 112.5),  48:( 82.5, 112.5),  49:(107.5, 112.5),  50:(132.5, 112.5),  51:(157.5, 112.5),  52:(182.5, 112.5),  53:(207.5, 112.5),  54:(232.5, 112.5),  55:(257.5, 112.5),  56:(282.5, 112.5),  57:(307.5, 112.5),  58:(332.5, 112.5),  59:(357.5, 112.5), 
    60:(  7.5, 137.5),  61:( 32.5, 137.5),  62:( 57.5, 137.5),  63:( 82.5, 137.5),  64:(107.5, 137.5),  65:(132.5, 137.5),  66:(157.5, 137.5),  67:(182.5, 137.5),  68:(207.5, 137.5),  69:(232.5, 137.5),  70:(257.5, 137.5),  71:(282.5, 137.5),  72:(307.5, 137.5),  73:(332.5, 137.5),  74:(357.5, 137.5), 
    75:(  7.5, 162.5),  76:( 32.5, 162.5),  77:( 57.5, 162.5),  78:( 82.5, 162.5),  79:(107.5, 162.5),  80:(132.5, 162.5),  81:(157.5, 162.5),  82:(182.5, 162.5),  83:(207.5, 162.5),  84:(232.5, 162.5),  85:(257.5, 162.5),  86:(282.5, 162.5),  87:(307.5, 162.5),  88:(332.5, 162.5),  89:(357.5, 162.5), 
    90:(  7.5, 187.5),  91:( 32.5, 187.5),  92:( 57.5, 187.5),  93:( 82.5, 187.5),  94:(107.5, 187.5),  95:(132.5, 187.5),  96:(157.5, 187.5),  97:(182.5, 187.5),  98:(207.5, 187.5),  99:(232.5, 187.5), 100:(257.5, 187.5), 101:(282.5, 187.5), 102:(307.5, 187.5), 103:(332.5, 187.5), 104:(357.5, 187.5), 
    105:(  7.5, 212.5), 106:( 32.5, 212.5), 107:( 57.5, 212.5), 108:( 82.5, 212.5), 109:(107.5, 212.5), 110:(132.5, 212.5), 111:(157.5, 212.5), 112:(182.5, 212.5), 113:(207.5, 212.5), 114:(232.5, 212.5), 115:(257.5, 212.5), 116:(282.5, 212.5), 117:(307.5, 212.5), 118:(332.5, 212.5), 119:(357.5, 212.5), 
    120:(  7.5, 237.5), 121:( 32.5, 237.5), 122:( 57.5, 237.5), 123:( 82.5, 237.5), 124:(107.5, 237.5), 125:(132.5, 237.5), 126:(157.5, 237.5), 127:(182.5, 237.5), 128:(207.5, 237.5), 129:(232.5, 237.5), 130:(257.5, 237.5), 131:(282.5, 237.5), 132:(307.5, 237.5), 133:(332.5, 237.5), 134:(357.5, 237.5), 
    135:(  7.5, 262.5), 136:( 32.5, 262.5), 137:( 57.5, 262.5), 138:( 82.5, 262.5), 139:(107.5, 262.5), 140:(132.5, 262.5), 141:(157.5, 262.5), 142:(182.5, 262.5), 143:(207.5, 262.5), 144:(232.5, 262.5), 145:(257.5, 262.5), 146:(282.5, 262.5), 147:(307.5, 262.5), 148:(332.5, 262.5), 149:(357.5, 262.5), 
    150:(  7.5, 287.5), 151:( 32.5, 287.5), 152:( 57.5, 287.5), 153:( 82.5, 287.5), 154:(107.5, 287.5), 155:(132.5, 287.5), 156:(157.5, 287.5), 157:(182.5, 287.5), 158:(207.5, 287.5), 159:(232.5, 287.5), 160:(257.5, 287.5), 161:(282.5, 287.5), 162:(307.5, 287.5), 163:(332.5, 287.5), 164:(357.5, 287.5), 
    165:(  7.5, 312.5), 166:( 32.5, 312.5), 167:( 57.5, 312.5), 168:( 82.5, 312.5), 169:(107.5, 312.5), 170:(132.5, 312.5), 171:(157.5, 312.5), 172:(182.5, 312.5), 173:(207.5, 312.5), 174:(232.5, 312.5), 175:(257.5, 312.5), 176:(282.5, 312.5), 177:(307.5, 312.5), 178:(332.5, 312.5), 179:(357.5, 312.5), 
    180:(  7.5, 337.5), 181:( 32.5, 337.5), 182:( 57.5, 337.5), 183:( 82.5, 337.5), 184:(107.5, 337.5), 185:(132.5, 337.5), 186:(157.5, 337.5), 187:(182.5, 337.5), 188:(207.5, 337.5), 189:(232.5, 337.5), 190:(257.5, 337.5), 191:(282.5, 337.5), 192:(307.5, 337.5), 193:(332.5, 337.5), 194:(357.5, 337.5), 
    195:(  7.5, 362.5), 196:( 32.5, 362.5), 197:( 57.5, 362.5), 198:( 82.5, 362.5), 199:(107.5, 362.5), 200:(132.5, 362.5), 201:(157.5, 362.5), 202:(182.5, 362.5), 203:(207.5, 362.5), 204:(232.5, 362.5), 205:(257.5, 362.5), 206:(282.5, 362.5), 207:(307.5, 362.5), 208:(332.5, 362.5), 209:(357.5, 362.5), 
    210:(  7.5, 387.5), 211:( 32.5, 387.5), 212:( 57.5, 387.5), 213:( 82.5, 387.5), 214:(107.5, 387.5), 215:(132.5, 387.5), 216:(157.5, 387.5), 217:(182.5, 387.5), 218:(207.5, 387.5), 219:(232.5, 387.5), 220:(257.5, 387.5), 221:(282.5, 387.5), 222:(307.5, 387.5), 223:(332.5, 387.5), 224:(357.5, 387.5), 
}

from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QLabel, QMessageBox,
QApplication, QToolTip, QPushButton)
from PyQt5.QtGui import (QIcon, QPixmap)
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QCoreApplication, Qt
from math import ceil
from easyengine import SampleEngine
from ABengine import AlphaBetaEngine

class DYYLGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.is_black_turn = [True]     # 可变对象
        self.game_over = False
        self.label_p = {}
        self.fen = '0' * 225            # '0'为空，'1'为黑棋，'2'为白棋
        self.history = [self.fen]
        self.black_engine = False
        self.white_engine = False
        
        self.initUI()

    def initUI(self):

        self.resize(390, 420)
        self.center()
        self.setWindowTitle('独饮一凉')
        self.setWindowIcon(QIcon('picture/茶.png'))
        self.setBoardMap()
        self.BuildLabel()
        self.setButtons()
        self.show()

    def center(self):
        # get window
        qr = self.frameGeometry()
        # get center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # show in center
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setBoardMap(self):
        pix = QPixmap('picture/棋盘.png')
        lb1 = QLabel(self)
        lb1.setGeometry(20, 50, 350, 350)
        lb1.setPixmap(pix)
        lb1.setScaledContents(True)

    def setButtons(self):
        newgame = QPushButton('新的对局', self)
        newgame.setToolTip('建立一盘新的对局')
        newgame.resize(newgame.sizeHint())
        newgame.move(10, 10)
        newgame.clicked.connect(self.BuildNewGame)

        undo = QPushButton('悔棋', self)
        undo.resize(undo.sizeHint())
        undo.move(90,10)
        undo.clicked.connect(self.Undo)

        computerblack = QPushButton('电脑执黑', self)
        computerblack.setCheckable(True)
        computerblack.resize(computerblack.sizeHint())
        computerblack.move(170, 10)
        computerblack.toggled.connect(self.BlackEngineOn)

        computerwhite = QPushButton('电脑执白', self)
        computerwhite.setCheckable(True)
        computerwhite.resize(computerwhite.sizeHint())
        computerwhite.move(250, 10)
        computerwhite.toggled.connect(self.WhiteEngineOn)

    @pyqtSlot()
    def BuildNewGame(self):
        self.is_black_turn[0] = True
        self.fen = '0' * 225
        for i in range(225):
            self.label_p['cross'+str(i)].setPixmap(QPixmap(''))
            self.label_p['cross'+str(i)].occupied = False
    
    def BlackEngineOn(self):
        if self.is_black_turn[0]:
            self.Engine()
        self.black_engine = True

    def WhiteEngineOn(self):
        if not self.is_black_turn[0]:
            self.Engine()
        self.white_engine = True

    def Engine(self):
        # 引擎计算
        obj = AlphaBetaEngine(self.fen, self.is_black_turn)
        dropped = obj.Run()  # 返回int类型，0-224

        # 显示棋子并占位
        if not self.label_p['cross'+str(dropped)].occupied:
            if self.is_black_turn[0]:
                piece = QPixmap('picture/黑色棋子.png')
            else:
                piece = QPixmap('picture/白色棋子.png')
            self.label_p['cross'+str(dropped)].setPixmap(piece)
            self.label_p['cross'+str(dropped)].setScaledContents(True)
        
        # 下一步
        self.NextStep(dropped)
            
    def Undo(self):
        if len(self.history) > 1:
            donefen = self.history.pop()
            self.fen = self.history[-1]
            for i in range(225):
                if self.fen[i] != donefen[i]:
                    self.label_p['cross'+str(i)].setPixmap(QPixmap(''))
                    self.label_p['cross'+str(i)].occupied = False
            self.SwitchTurn()

    def BuildLabel(self):
        for i in range(225):
            self.label_p['cross'+str(i)] = PieceLabel(self, i, self.is_black_turn)
            self.label_p['cross'+str(i)].setGeometry(coordinate_grid[i][0], coordinate_grid[i][1], 25, 25)
            # 将鼠标事件与交换行棋槽函数连接
            self.label_p['cross'+str(i)].switch_signal.connect(self.NextStep)

    def NextStep(self, cor_grid = None):
        self.UpdateFen(cor_grid)
        self.JudgeVictory(cor_grid)
        self.SwitchTurn()
        self.CheckEngine()

    def UpdateFen(self, cor_grid):
        if self.is_black_turn[0]:
            self.fen = self.fen[:cor_grid] + '1' + self.fen[cor_grid+1:]
        else:
            self.fen = self.fen[:cor_grid] + '2' + self.fen[cor_grid+1:]

        # 记录历史棋谱
        self.history.append(self.fen)

    def SwitchTurn(self):
        self.is_black_turn[0] = not self.is_black_turn[0]

    def CheckEngine(self):
        if self.is_black_turn[0] and self.black_engine:
            self.Engine()
        if self.is_black_turn[0] == False and self.white_engine:
            self.Engine()     
    
    def JudgeVictory(self, cor_grid):
        final_result = None

        if self.fen.count('1') < 5:
            return
        if self.fen.count('0') == 0:
            self.ResultMessage
        
        # 横向判定
        leftside = cor_grid - cor_grid % 15
        row = self.fen[leftside:leftside+15]
        # 纵向判定
        topside = cor_grid % 15
        line = self.fen[topside::15]
        # 左斜判定
        topleftside = cor_grid % 16 if cor_grid % 15 >= cor_grid % 16 \
            else (16 - cor_grid % 16) * 15
        topleft = self.fen[topleftside::16]
        if topleftside < 15:
            topleft = topleft[:15-topleftside]  # 除去斜侧换行左移的坐标
        # 右斜判定
        toprightside = cor_grid % 14 if cor_grid % 14 >= cor_grid % 15 \
            else cor_grid % 14 * 15 + 14
        topright = self.fen[toprightside::14]
        if toprightside < 15:
            topright = topright[:toprightside+1]    # 除去斜侧换行右移的坐标
        
        if any(self.fen[cor_grid]*5 in anydirections \
            for anydirections in [row, line, topleft, topright]):
            self.ResultMessage(is_draw = False)
    
    def ResultMessage(self, is_draw = None):
        if is_draw:
            winner = '和棋'
        elif self.is_black_turn[0]:
            winner = '黑棋赢'
        else:
            winner = '白棋赢'
        self.result = QMessageBox.information(self, '提示', winner)

class PieceLabel(QLabel):
    
    # 声明信号——传递交换行棋信号并判断胜负
    switch_signal = pyqtSignal(int)

    def __init__(self, parent = None, cor_grid = None, is_black_turn = [True]):
        super().__init__(parent)
        self.occupied = False
        self.is_black_turn = is_black_turn
        self.cor_grid = cor_grid

    def mousePressEvent(self, e):
        if not self.occupied:
            if self.is_black_turn[0]:
                piece = QPixmap('picture/黑色棋子.png')
            else:
                piece = QPixmap('picture/白色棋子.png')
            self.setPixmap(piece)
            self.setScaledContents(True)
            self.occupied = True

            # 发送信号
            self.switch_signal.emit(self.cor_grid)
         
if __name__ == '__main__':
    import sys
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ex = DYYLGUI()
    sys.exit(app.exec_())