import argparse
from src.chessboard_detection import detect_chessboard
from src.segment_squares import segment_board
from src.piece_classification import classify_squares
from src.fen_builder import build_fen
from src.stockfish_integration import suggest_best_move
import cv2

def main():
    parser = argparse.ArgumentParser(description="ChessEye - Chessboard AI")
    parser.add_argument('--image', required=True, help="Path to chessboard image")
    parser.add_argument('--stockfish', required=True, help="Path to Stockfish executable")
    args = parser.parse_args()

    warped_board = detect_chessboard(args.image)
    if warped_board is None:
        print("Failed to detect chessboard.")
        return

    squares = segment_board(warped_board)
    piece_classes = classify_squares(squares)
    fen = build_fen(piece_classes)

    print(f"Detected FEN: {fen}")

    best_move = suggest_best_move(fen, args.stockfish)
    print(f"Suggested best move: {best_move}")

if __name__ == "__main__":
    main()
