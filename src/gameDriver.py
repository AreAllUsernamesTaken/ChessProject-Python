from pieces import *
from ChessBoard import ChessBoard
from PieceColor import PieceColor

# add standard pieces to a board
def loadStandardGame(board: ChessBoard) -> None:
	# Add pawns
	for i in range(board.BOARD_WIDTH):
		pawn = Pawn(PieceColor.BLACK)
		xy = '7' + chr(ord('a') + i)
		board.addPiece(xy, pawn)
		pawn = Pawn(PieceColor.WHITE)
		xy = '2' + chr(ord('a') + i)
		board.addPiece(xy, pawn)
	rook = Rook(PieceColor.BLACK)
	board.addPiece('8a', rook)
	board.addPiece('8h', rook)
	rook = Rook(PieceColor.WHITE)
	board.addPiece('1a', rook)
	board.addPiece('1h', rook)
	knight = Knight(PieceColor.BLACK)
	board.addPiece('8b', knight)
	board.addPiece('8g', knight)
	knight = Knight(PieceColor.WHITE)
	board.addPiece('1b', knight)
	board.addPiece('1g', knight)
	bishop = Bishop(PieceColor.BLACK)
	board.addPiece('8c', bishop)
	board.addPiece('8f', bishop)
	bishop = Bishop(PieceColor.WHITE)
	board.addPiece('1c', bishop)
	board.addPiece('1f', bishop)
	queen = Queen(PieceColor.BLACK)
	board.addPiece('8d', queen)
	queen = Queen(PieceColor.WHITE)
	board.addPiece('1d', queen)
	king = King(PieceColor.BLACK)
	board.addPiece('8e', king)
	king = King(PieceColor.WHITE)
	board.addPiece('1e', king)

def main():
	board = ChessBoard()
	loadStandardGame(board)
	board.printBoard()
	print("Enter moves as coordinates pair (eg: 7a to 6a")
	print("Type 'quit' to exit!")
	print("White starts!")

	while True:
		start = input("start: ")
		end = input("end: ")
		if start.lower() == 'quit' or end.lower() == 'quit':
			break
		board.moveOnBoard(start, end)
		board.printBoard()
		print("Next player turn!")

if __name__ == "__main__":
    main()