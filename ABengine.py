'''
    By : RunTuandme
'''

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

class Node:
    def __init__(self, state: list = None, is_black_turn = True):
        self.board = state      # 二维棋盘数组1, board[0]为棋盘第一行：[['01000010...'],[...]...]
        self.is_black_turn = is_black_turn
                
class AlphaBetaEngine:

    def __init__(self, fen: str = None, is_black_turn = [True]):
        self.fen = fen          # 一维棋盘数组：'00120110020...'
        self.is_black_turn = is_black_turn
        self.board = []         # 二维棋盘数组1, board[0]为棋盘第一行：[['01000010...'],[...]...]（通用）
        self.div_board = []     # 二维棋盘数组2，div_board[0]为棋盘第一行：[['0','1','0',...],[...]...] （仅在判断局面结束计算中用到）

        self.board = self.FenTo2d(self.fen)
        self.div_board = self.DivideBoard(self.board)
        self.Run()

    def FenTo2d(self, fen_x: str) -> list:
        # aim_board:[['01000010...'],[...]...]
        aim_board = []
        for i in range(0, 225, 15):
            aim_board.append(self.fen[i:i+15])
        return aim_board

    def Div2dToFen(self, div_board_x: list) -> str:
        # aim_fen:'00120110020...'
        aim_fen = ''
        for line in div_board_x:
            for each_piece in line:
                aim_fen += each_piece
        return aim_fen

    def DivideBoard(self, board_x: list) -> list:
        # board_x:[['01000010...'],[...]...]
        # aim_board:[['0','1','0',...],[...]...]
        aim_board = []
        for line in board_x:
            each = []
            for i in line:
                each.append(i)
            aim_board.append(each)
        return aim_board

    def PiecesDivide(self, board_fen: list = None) -> list:
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
                
    def Get4L(self, state: list = None, line = 0, column = 0) -> list:
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

    def Pick(self, line_state: list, black_turn = True) -> int:
        # 功能：与shape_score列表匹配，返回设定评估分值

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

    def evaluation(self, state: list = None, is_black_turn = True) -> int:
        # 评估函数
        # 功能：计算某局面下黑（白）棋分数，正数代表当前局面 turn 方为优势
        copy_board = state.copy()
        pieces = self.PiecesDivide(copy_board)

        black_score = 0
        white_score = 0

        for p in pieces[1]:
            all_directions = self.Get4L(copy_board, p[0], p[1])
            black_score += self.Pick(all_directions, black_turn = True)
        for p in pieces[2]:
            all_directions = self.Get4L(copy_board, p[0], p[1])
            white_score += self.Pick(all_directions, black_turn = False)
        
        if is_black_turn:
            return black_score - white_score
        else:
            return white_score - black_score

    def Moves(self, state: list = None, is_black_turn = True) -> dict:
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
        # return max(values, key = values.get)
            
    def Judge5(self, s: str) -> bool:
        # 功能：给定字符串s，判断是否有五子连珠
        black = '11111'
        white = '22222'
        if black in s:
            return True
        elif white in s:
            return True
        else:
            return False

    def GameOver(self, board: list) -> bool:
        # board：二维棋盘数组1, board[0]为棋盘第一行：[['01000010...'],[...]...]
        # board_x：二维棋盘数组2，board_x[0]为棋盘第一行：[['0','1','0',...],[...]...]
        # 功能：判断游戏是否结束
        board_x = self.DivideBoard(board)
        db = np.array(board_x)

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
        
        if '0' not in self.Div2dToFen(board_x):
            return True

        return False

    def ChildBoard(self, state: list, move: tuple, is_black_turn: bool) -> list:
        # move: (3,4) ; state: 当前局面(board)
        # 功能：根据落子位置生成新board
        # return：board
        copy_board = state.copy()
        if copy_board[move[0]][move[1]] == '0':
            if is_black_turn:
                copy_board[move[0]]= copy_board[move[0]][:move[1]] + '1' + copy_board[move[0]][move[1]+1:]
            else:
                copy_board[move[0]]= copy_board[move[0]][:move[1]] + '2' + copy_board[move[0]][move[1]+1:]
            return copy_board

    def AlphaBeta(self, state: list, depth: int, is_black_turn: bool, 
                  alpha = float('-inf'), beta = float('inf'), 
                  turn_max_player = True) -> int:
        # 极大值极小值搜索 + αβ剪枝
        if depth == 0 or self.GameOver(state):
            return self.evaluation(state = state, is_black_turn = is_black_turn)
        
        if turn_max_player:
            max_eval = float('-inf')
            for each_move in self.Moves(state = state, is_black_turn = True):
                child = self.ChildBoard(state, each_move, is_black_turn)
                eval = self.AlphaBeta(child, depth - 1, not is_black_turn, alpha, beta, False)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for each_move in self.Moves(state = state, is_black_turn = False):
                child = self.ChildBoard(state, each_move, is_black_turn)
                eval = self.AlphaBeta(child, depth - 1, not is_black_turn, alpha, beta, True)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
                min_eval = min(min_eval, eval)
            return min_eval
        

    def Minimax(self, state: list, depth: int, is_black_turn: bool, turn_max_player = True) -> int:
        # 极大极小值搜索
        if depth == 0 or self.GameOver(state):
            return self.evaluation(state = state, is_black_turn = is_black_turn)
        
        if turn_max_player:
            max_eval = float('-inf')
            for each_move in self.Moves(state = state, is_black_turn = True):
                child = self.ChildBoard(state, each_move, is_black_turn)
                eval = self.Minimax(child, depth - 1, not is_black_turn, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for each_move in self.Moves(state = state, is_black_turn = False):
                child = self.ChildBoard(state, each_move, is_black_turn)
                eval = self.Minimax(child, depth - 1, not is_black_turn, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def MakeNextMove(self, state, is_black_turn):
        # state：当前局面(board)
        # 功能： 选择下一步棋子的最佳招法
        # return： e.g(1,2)
        copy_board = state.copy()
        # 方案一： 一层Minimax搜索
        # moves = self.Moves(copy_board, is_black_turn)
        # move = max(moves, key = moves.get)  # 取moves中value最大的招法
        # 方案二： 多层Minimax搜索
        score = self.Minimax(copy_board, 2, is_black_turn)
        moves = self.Moves(copy_board, is_black_turn)
        move = list(moves.keys())[list(moves.values()).index(score)]    # 按值查找第一步招法表键值
        # 方案三： 深层AlphaBeta搜索
        # score = self.AlphaBeta(copy_board, 10, is_black_turn)
        # moves = self.Moves(copy_board, is_black_turn)
        # move = list(moves.keys())[list(moves.values()).index(score)]    # 按值查找第一步招法表键值
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