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

import numpy as np
                
class AlphaBetaEngine:

    def __init__(self, fen = None, is_black_turn = [True]):
        self.fen = fen
        self.is_black_turn = is_black_turn
        self.board = []         # 建立二维棋盘数组1：[['01000010...'],[...]...]
        self.div_board = []     # 建立二维棋盘数组2：[['0','1','0',...],[...]...]

        self.FenTo2d()
        self.DivideBoard()
        self.Run()

    def FenTo2d(self):
        # board:[['01000010...'],[...]...]
        for i in range(0, 225, 15):
            self.board.append(self.fen[i:i+15])

    def DivideBoard(self):
        # board:[['01000010...'],[...]...]
        # div_board:[['0','1','0',...],[...]...]
        self.div_board = []
        for line in self.board:
            each = []
            for i in line:
                each.append(i)
            self.div_board.append(each)

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
                
    def Get4L(self, state = None, line = 0, column = 0):
        # 功能：取某一点的横、竖、左斜、右斜方向的棋子列表
        # return: [横，竖，左斜，右斜]

        aim = []
        aim.append(state[line])

        col = ''
        for x in state:
            col += x[column]
        aim.append(col)

        pos_x, pos_y = line, column
        left = ''
        while pos_x > 0 and pos_y > 0:
            left += state[pos_x][pos_y]
            pos_x -= 1
            pos_y -= 1
        pos_x, pos_y = line, column
        while pos_x < 15 and pos_y < 15:
            left += state[pos_x][pos_y]
            pos_x += 1
            pos_y += 1
        aim.append(left)

        pos_x, pos_y = line, column
        right = ''
        while pos_x > 0 and pos_y < 15:
            right += state[pos_x][pos_y]
            pos_x -= 1
            pos_y += 1
        pos_x, pos_y = line, column
        while pos_x < 15 and pos_y > 0:
            right += state[pos_x][pos_y]
            pos_x += 1
            pos_y -= 1
        aim.append(right)

        return aim

    def Pick(self, line_state, black_turn = True):
        # 功能：与shape_score列表匹配

        score = 0
        if black_turn:
            for x in line_state:
                for shape, v in shape_score_black.items():
                    if x.find(shape) != -1:
                        score += v
        else:
            for x in line_state:
                for shape, v in shape_score_white.items():
                    if x.find(shape) != -1:
                        score += v
        return score

    def evaluation(self, state = None, is_black_turn = True):
        # 评估函数
        # 功能：计算某局面下黑（白）棋分数

        pieces = self.PiecesDivide(state)

        black_score = 0
        white_score = 0

        for p in pieces[1]:
            all_directions = self.Get4L(state, p[0], p[1])
            black_score += self.Pick(all_directions, black_turn = True)
        for p in pieces[2]:
            all_directions = self.Get4L(state, p[0], p[1])
            white_score += self.Pick(all_directions, black_turn = False)
        
        if is_black_turn:
            return black_score - white_score
        else:
            return white_score - black_score

    def Moves(self, state = None, is_black_turn = True):
        # 功能: 返回state局面下策略价值
        # return：(dict) e.g{(1,2):300,(3,3):350,...}

        pieces = self.PiecesDivide(state)
        values = {}

        if is_black_turn:
            dropped = '1'
        else:
            dropped = '2'
        
        for p in pieces[0]:
            copy = state.copy()
            copy[p[0]] = copy[p[0]][:p[1]] + dropped + copy[p[0]][p[1]+1:]
            score = self.evaluation(copy, is_black_turn)
            values.update({p:score})

        return values

        return max(values, key = values.get)
            
    def Judge5(self, s):
        # 功能：给定字符串s，判断是否有五子连珠
        black = '11111'
        white = '22222'
        if black in s:
            return True
        elif white in s:
            return True
        else:
            return False

    def GameOver(self):
        # 功能：判断游戏是否结束
        db = np.array(self.div_board)

        # 横
        for line in db:
            judge = ''
            for elem in line:
                judge += elem
            if self.Judge5(judge):
                return True

        # 纵
        for i in range(15):
            judge = ''
            for elem in db[:,i]:
                judge += elem
            if self.Judge5(judge):
                return True

        # 左斜
        for i in range(21):
            judge = ''
            for elem in db.diagonal(i-10):
                judge += elem
            if self.Judge5(judge):
                return True
        
        # 右斜
        for i in range(21):
            judge = ''
            for elem in np.diag(np.fliplr(db),i-10):
                judge += elem
            if self.Judge5(judge):
                return True
        
        if '0' not in self.fen:
            return True

        return False

    def UpdateBoard(self, state, move, is_black_turn):
        # move: (3,4) ; state: 当前局面(board)
        # 功能：根据落子位置生成新board
        # return：board
        if state[move[0]][move[1]] == '0':
            if is_black_turn:
                state[move[0]]= state[move[0]][:move(1)] + '1' + state[move[0]][move[1]+1:]
            else:
                state[move[0]]= state[move[0]][:move(1)] + '2' + state[move[0]][move[1]+1:]
            return state

    def Negamax(self, state, depth, alpha, beta, is_black_turn = True):
        # 极大值极小值搜索 + αβ剪枝
        if self.GameOver() or depth == 0:
            return self.evaluation(state, is_black_turn)
        pieces = self.PiecesDivide(state)   # 生成合理招法
        copy_board = state.copy()
        
        while pieces[0] != []:
            # 生成下一步
            move = self.MakeNextMove(state, is_black_turn)
            copy_board = self.UpdateBoard(copy_board, move, is_black_turn)
            is_black_turn = not is_black_turn
            val = -self.Negamax(copy_board, depth-1, -alpha, -beta, is_black_turn)
            if val >= beta:
                return beta
            if val > alpha:
                alpha = val
        
        return alpha

    def MakeNextMove(self, state, is_black_turn):
        # state：当前局面(board)
        # 功能： 选择下一步棋子的最佳招法
        # return： e.g(1,2)
        copy_board = state.copy()
        moves = self.Moves(copy_board, is_black_turn)
        move = max(moves, key = moves.get)  # 取moves中value最大的招法
        return move

    def Run(self):
        if self.fen == '0' * 225:
            return 112

        move = self.MakeNextMove(self.board, self.is_black_turn[0])
        return move[0] * 15 + move[1]

    

if __name__ == '__main__':
    fen = '2'+'0'*100+'1'*2+'0'*122
    ex = AlphaBetaEngine(fen, [False])
    a = 0