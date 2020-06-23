from termcolor import colored

from PawnPiece import Pawn, PieceColor

class ChessBoard:
	def __init__(self) -> None:
		self.BOARD_WIDTH = 7
		self.BOARD_HEIGHT = 7
		self.board = [[None for i in range(self.BOARD_WIDTH)] for j in range(self.BOARD_HEIGHT)]

	def addPiece(self, xCoordinate: int, yCoordinate: int, pieceColor: PieceColor) -> None:
		if pieceColor not in PieceColor:
			return

		if not self.isLegalPosition(xCoordinate, yCoordinate):
			return

		self.board[xCoordinate][yCoordinate] = Pawn(pieceColor)

	def isLegalPosition(self, xCoordinate: int, yCoordinate: int) -> bool:
		if (xCoordinate < 0 or yCoordinate < 0 or xCoordinate > self.BOARD_HEIGHT or yCoordinate > self.BOARD_WIDTH):
			return False
		return True

	def printBoard(self) -> None:
		print("")
		for i in range(self.BOARD_HEIGHT):
			for j in range(self.BOARD_HEIGHT):
				if (i + j) % 2 == 1:
					background = 'on_white'
				else:
					background = 'on_grey'

				color = 'magenta'
				if self.board[i][j] is None:
					cell = '   '
				if isinstance(self.board[i][j], Pawn):
					cell = ' P '
					if self.board[i][j].pieceColor is PieceColor.WHITE:
						color = 'cyan'

				print(colored(cell, color, background), end='')	
			print("")
		print("")

	def move_on_Board(self, xCoordinate: int, yCoordinate: int, newX: int, newY: int) -> bool:
		if not self.isLegalPosition(xCoordinate, yCoordinate) or not self.isLegalPosition(newX, newY):
			print("illegal poz")
			return False

		if self.board[xCoordinate][yCoordinate] is None:
			print("no piece")
			return False

		if self.board[newX][newY] is None:
			ret = self.board[xCoordinate][yCoordinate].move(xCoordinate, yCoordinate, newX, newY)
			if not ret:
				return ret
			self.board[newX][newY] = self.board[xCoordinate][yCoordinate]
			self.board[xCoordinate][yCoordinate] = None
			return ret

		if not self.board[newX][newY] is None:
			if self.board[newX][newY].pieceColor == self.board[xCoordinate][yCoordinate]:
				print("cant attack self")
				return False
			else:
				ret = self.board[xCoordinate][yCoordinate].attack(xCoordinate, yCoordinate, newX, newY)
				if not ret:
					return ret
				self.board[newX][newY] = self.board[xCoordinate][yCoordinate]
				self.board[xCoordinate][yCoordinate] = None
				return ret
		return False
		
board = ChessBoard()
board.printBoard()

for i in range(7):
	board.addPiece(5, i, PieceColor.WHITE)
	board.addPiece(1, i, PieceColor.BLACK)
board.printBoard()
print(board.move_on_Board(5, 0, 4, 0))
print(board.move_on_Board(1, 1, 3, 1))
board.printBoard()
print(board.move_on_Board(1, 1, 3, 1))
board.printBoard()
print(board.move_on_Board(4, 0, 3, 1))
board.printBoard()

