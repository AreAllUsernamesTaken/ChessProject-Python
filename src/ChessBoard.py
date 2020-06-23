from termcolor import colored
from pieces import *
from PieceColor import PieceColor

class ChessBoard:
	# Init chess board 8x8
	def __init__(self) -> None:
		self.BOARD_WIDTH = 8
		self.BOARD_HEIGHT = 8
		self.board = [[None for i in range(self.BOARD_WIDTH)] for j in range(self.BOARD_HEIGHT)]

	# Convert from chess coordinates (eg. "2a") to array coordinates (eg: "60")
	def getCoordinates(self, buf: str) -> (int, int):
		# In case of error return invalid coordinates (will trigger out of board error)
		if len(buf) != 2 or not buf[1].isalpha() or not buf[0].isnumeric():
			return (-1, -1)

		x = 8 - int(buf[0])
		y = ord(str.lower(buf[1])) - ord('a')
		return (x, y)

	# Add a piece to the board
	def addPiece(self, start: str, piece: ChessPiece) -> bool:
		(xCoordinate, yCoordinate) = self.getCoordinates(start)
		if not isinstance(piece, ChessPiece):
			print("ERROR: only chess pieces can be added to the board.")
			return False

		if not self.isLegalPosition(xCoordinate, yCoordinate):
			print("ERROR: {} is not a valid coordinate".format(start))
			return False
		if not self.board[xCoordinate][yCoordinate] == None:
			print("ERROR: cell at {} is not empty".format(start))
			return False
		self.board[xCoordinate][yCoordinate] = piece
		return True

	# Check if coordinates are within board boundries
	def isLegalPosition(self, xCoordinate: int, yCoordinate: int) -> bool:
		if (xCoordinate < 0 or yCoordinate < 0 or xCoordinate >= self.BOARD_HEIGHT or\
		    yCoordinate >= self.BOARD_WIDTH):
			return False
		return True

	# Helper function: terminal "GUI"
	def printBoard(self) -> None:
		print("")
		print("   ", end='')
		for i in range(ord('a'), ord('i')):
			print(" {} ".format(chr(i)), end ='')
		print("")
		for i in range(self.BOARD_HEIGHT):
			print(" {} ".format(self.BOARD_HEIGHT - i), end ='')
			for j in range(self.BOARD_HEIGHT):
				if (i + j) % 2 == 1:
					background = 'on_white'
				else:
					background = 'on_grey'
				
				cell = '   '
				color = 'magenta'
				if not self.board[i][j] is None:
					cell = self.board[i][j].print()
					if self.board[i][j].pieceColor is PieceColor.WHITE:
						color = 'cyan'
				print(colored(cell, color, background), end='')	
			print("")
		print("")

	# Method will validate if the move is valid. If so, piece will be moved from start to end.
	# Otherwise an error is displayed and game state does not change.
	def moveOnBoard(self, start: str, end: str) -> bool:
		(xCoordinate, yCoordinate) = self.getCoordinates(start)
		(newX, newY) = self.getCoordinates(end)

		# Verify coordinates are valid (in game board)
		if not self.isLegalPosition(xCoordinate, yCoordinate) or not self.isLegalPosition(newX, newY):
			print("ERROR: one of positions {} or {} is outside the game board!".format(start, end))
			return False

		# Verify start cell is not empty
		if self.board[xCoordinate][yCoordinate] is None:
			print("ERROR: there is no piece at {}!".format(start))
			return False

		# Verify player is not attacking himself.
		if self.board[newX][newY] is not None and\
		   self.board[newX][newY].pieceColor == self.board[xCoordinate][yCoordinate].pieceColor:
			print("ERROR: pieces at {} and {} belong to same player!".format(start, end))
			return False

		# Verify piece at {start} can move to given coordinates
		ret = self.board[xCoordinate][yCoordinate].move(xCoordinate, yCoordinate, newX, newY)
		# Special case for pawn: it can move ahead, but it can only attack diagonally.
		if ret and isinstance(self.board[xCoordinate][yCoordinate], Pawn):
			if self.board[newX][newY] is not None:
				print("ERROR: cell at {} is not empty!.".format(end))
				return False
		if not ret:
			# pawns have special attack move
			if isinstance(self.board[xCoordinate][yCoordinate], Pawn):
				ret = self.board[xCoordinate][yCoordinate].attack(xCoordinate, yCoordinate, newX, newY)
			if not ret:
				print("ERROR: piece at {} is a {} and can not be moved to {}!"\
					.format(start, type(self.board[xCoordinate][yCoordinate]).name, end))
				return ret

		ret = self.board[xCoordinate][yCoordinate].collisionCheck(xCoordinate, yCoordinate, newX, newY, self.board)
		if ret:
			print("ERROR: path from {} to {} is obstructed!".format(start, end))
			return not ret

		self.board[newX][newY] = self.board[xCoordinate][yCoordinate]
		self.board[xCoordinate][yCoordinate] = None		
		return True
