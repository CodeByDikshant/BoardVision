# ChessEye

AI-powered chessboard recognition and analysis tool.

ChessEye detects chessboards from images, segments the board into squares, classifies pieces, builds the FEN notation, and integrates with Stockfish to suggest the best moves.

## Features

- Detect chessboard and warp to top-down view  
- Segment board into 64 squares  
- Classify each square’s piece (placeholder model included)  
- Build FEN string representing the position  
- Integrate with Stockfish chess engine for move suggestions

## How to set up and use ChessEye

1. **Clone this repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/ChessEye.git
   cd ChessEye
Install the required Python packages by running:

bash
Copy
Edit
pip install -r requirements.txt
Download the Stockfish chess engine from https://stockfishchess.org/download/, extract it, and note the path to the executable.

Run the ChessEye tool with your chessboard image and the Stockfish executable path:

bash
Copy
Edit
python main.py --image path/to/chessboard.jpg --stockfish path/to/stockfish_executable
Replace path/to/chessboard.jpg with the actual path of your input image, and path/to/stockfish_executable with the location of the Stockfish binary.

Check the output:

The program will print the detected board position in FEN notation.

It will also show the best move suggested by Stockfish.
