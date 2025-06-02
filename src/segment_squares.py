import cv2

def segment_board(warped_image):
    """
    Input: warped top-down image of chessboard
    Output: list of 64 square images (row-wise from top-left to bottom-right)
    """
    squares = []
    height, width = warped_image.shape[:2]
    square_size_x = width // 8
    square_size_y = height // 8

    for row in range(8):
        for col in range(8):
            x_start = col * square_size_x
            y_start = row * square_size_y
            square = warped_image[y_start:y_start + square_size_y, x_start:x_start + square_size_x]
            squares.append(square)
    return squares
