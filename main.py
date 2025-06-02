import argparse
from src.chessboard_detection import detect_chessboard
from src.stockfish_integration import suggest_best_move

def main():
    parser = argparse.ArgumentParser(description="ChessEye - Chessboard AI")
    parser.add_argument('--image', required=True, help="Path to chessboard image")
    parser.add_argument('--stockfish', required=True, help="Path to Stockfish executable")
    args = parser.parse_args()

    warped_board = detect_chessboard(args.image)
    if warped_board is None:
        print("Failed to detect chessboard.")
        return

    # TODO: Add segmentation, classification, FEN builder here
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    best_move = suggest_best_move(fen, args.stockfish)
    print(f"Suggested best move: {best_move}")

if __name__ == "__main__":
    main()
