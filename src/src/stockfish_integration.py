import chess
import chess.engine

def suggest_best_move(fen, stockfish_path):
    board = chess.Board(fen)
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    engine.quit()
    return result.move
