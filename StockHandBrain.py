import asyncio
from pickle import NONE
import chess
import chess.engine




engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\tombu\OneDrive\Documents\Chess Engine\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")

board = chess.Board()


pieceDict = {
    'p': "pawn",
    'n': "knight",
    'b': "Bishop",
    'r': "rook",
    'q': "queen",
    'k': "king"
}



def checkMove(move):
    try: 
        board.parse_san(move)
        return True
    except:
        return False

while True:
    computer = engine.play(board, chess.engine.Limit(time=0.1))
    startSquare = chess.parse_square(str(computer.move)[0:2])
    print(pieceDict[str(board.piece_at(startSquare)).lower()])
    move = input("input your move: ")
    
    while (checkMove(move) == False):
        print("illegal move try again")
        move = input("input your move: ")
        
    board.push_san(str(move))
    print(board)

engine.quit()