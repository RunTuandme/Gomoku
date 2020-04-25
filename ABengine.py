shape_score_black = {
    '11111'  : 99999,
    '011110' : 9999,
    '11110'  : 200,
    '01111'  : 200,
    '11011'  : 200,
    '10111'  : 200,
    '11101'  : 200,
    '01110'  : 300,
    '010110' : 300,
    '011010' : 300,
    '10101'  : 100,
    '001100' : 50,
    '01010'  : 50
    }

shape_score_white = {
    '22222'  : 99999,
    '022220' : 9999,
    '22220'  : 200,
    '02222'  : 200,
    '22022'  : 200,
    '20222'  : 200,
    '22202'  : 200,
    '02220'  : 300,
    '020220' : 300,
    '022020' : 300,
    '20202'  : 100,
    '002200' : 50,
    '02020'  : 50
    }
                
class AlphaBetaEngine:

    def __init__(self, fen = None, is_black_turn = [True]):
        self.fen = fen
        self.is_black_turn = is_black_turn
        self.board = []         # 建立二维棋盘数组

        self.FenTo2d()
        self.PiecesDivide()

    def FenTo2d(self):
        for i in range(0, 225, 15):
            self.board.append(self.fen[i:i+15])

    def PiecesDivide(self, board_fen = None):
        # 功能：计算所有合法落子、黑棋、白棋位置
        # return：(list)[[legal_moves],[black_pieces],[white_pieces]]
        # e.g[[(1,2),(1,0),...],[(3,4),(3,0),...],[(2,1),(0,2),...]]

        legal_moves = []
        black_pieces = []
        white_pieces = []

        for i in range(15):
            for j in range(15):
                pos = (i, j)
                if board_fen[i][j] == '0':
                    legal_moves.append(pos)
                elif board_fen[i][j] == '1':
                    black_pieces.append(pos)
                else:
                    white_pieces.append(pos)
        
        return [legal_moves, black_pieces, white_pieces]
                
    def Get4L(self, line, column):
        # 功能：取某一点的横、竖、左斜、右斜方向的棋子列表
        # return: [横，竖，左斜，右斜]

        aim = []
        aim.append(self.board[line])

        col = ''
        for x in self.board:
            col += x[column]
        aim.append(col)

        pos_x, pos_y = line, column
        left = ''
        while pos_x > 0 and pos_y > 0:
            left += self.board[pos_x][pos_y]
            pos_x -= 1
            pos_y -= 1
        pos_x, pos_y = line, column
        while pos_x < 15 and pos_y < 15:
            left += self.board[pos_x][pos_y]
        aim.append(left)

        pos_x, pos_y = line, column
        right = ''
        while pos_x > 0 and pos_y < 15:
            right += self.board[pos_x][pos_y]
            pos_x -= 1
            pos_y -= 1
        pos_x, pos_y = line, column
        while pos_x < 15 and pos_y > 0:
            right += self.board[pos_x][pos_y]
        aim.append(right)

        return aim

    def Pick(self, line_state, black_turn = True):
        # 功能：与shape_score列表匹配

        score = 0
        if self.black_turn:
            for x in line_state:
                for shape in shape_score_black:
                    if x.find(shape):
                        score += shape.value
        else:
            for x in line_state:
                for shape in shape_score_white:
                    if x.find(shape):
                        score += shape.value
        return score

    def evaluation(self, state = None, is_black_turn = True):
        # 评估函数
        # 功能：计算某局面下黑（白）棋分数

        pieces = self.PiecesDivide(state)

        black_score = 0
        white_score = 0

        for p in pieces[1]:
            all_directions = self.Get4L(p[0], p[1])
            black_score += self.Pick(all_directions, black_turn = is_black_turn)
        for p in pieces[2]:
            all_directions = self.Get4L(p[0], p[1])
            white_score += self.Pick(all_directions, black_turn = is_black_turn)
        
        if is_black_turn:
            return black_score - white_score
        else:
            return white_score - black_score

if __name__ == '__main__':
    fen = '0' * 225
    ex = AlphaBetaEngine(fen, [True])
    