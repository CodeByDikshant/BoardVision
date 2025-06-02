def build_fen(piece_classes):
    """
    Input: List of 64 piece classes (row-wise from top-left)
    Output: FEN string for the board position
    """
    fen_rows = []
    for row in range(8):
        fen_row = ""
        empty_count = 0
        for col in range(8):
            piece = piece_classes[row*8 + col]
            if piece == 'empty':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_map = {
                    'wP': 'P', 'wR': 'R', 'wN': 'N', 'wB': 'B', 'wQ': 'Q', 'wK': 'K',
                    'bP': 'p', 'bR': 'r', 'bN': 'n', 'bB': 'b', 'bQ': 'q', 'bK': 'k',
                }
                fen_row += fen_map.get(piece, '')
        if empty_count > 0:
            fen_row += str(empty_count)
        fen_rows.append(fen_row)
    fen = "/".join(fen_rows) + " w KQkq - 0 1"  # Assume white to move & default castling rights
    return fen
