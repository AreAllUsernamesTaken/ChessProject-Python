import unittest, sys, os, random

sys.path.append(os.path.abspath('../src'))
import ChessBoard, pieces
from PieceColor import PieceColor

class TestChessBoard(unittest.TestCase):

    def testBoardSize(self):
        board = ChessBoard.ChessBoard()
        self.assertEqual(board.BOARD_WIDTH, 8)
        self.assertEqual(board.BOARD_HEIGHT, 8)
        for i in range(board.BOARD_WIDTH):
            for j in range (board.BOARD_HEIGHT):
                self.assertEqual(board.board[i][j], None)


    def testGetCoordinates(self):
        board = ChessBoard.ChessBoard()
        for i in range(10):
            x = random.randint(0, board.BOARD_HEIGHT)
            y = random.randint(0, board.BOARD_WIDTH)
            buf = str(8 - x) + chr(ord('a') + y)
            (x1, y1) = board.getCoordinates(buf)
            self.assertEqual((x, y), (x1, y))
        for i in range(10):
            x = random.randint(board.BOARD_HEIGHT + 2, 100)
            y = random.randint(board.BOARD_WIDTH + 1, 26)
            buf = str(x) + chr(ord('a') + y)
            (x1, y1) = board.getCoordinates(buf)
            self.assertEqual((x1, y1), (-1, -1))
    
    def testAddPiece(self):
        board = ChessBoard.ChessBoard()
        pawn1 = pieces.Pawn(PieceColor.WHITE)
        pawn2 = pieces.Pawn(PieceColor.BLACK)
        rook1 = pieces.Rook(PieceColor.WHITE)
        rook2 = pieces.Rook(PieceColor.BLACK)
        bishop1 = pieces.Bishop(PieceColor.BLACK)
        bishop2 = pieces.Bishop(PieceColor.WHITE)
        knight1 = pieces.Knight(PieceColor.BLACK)
        knight2 = pieces.Knight(PieceColor.WHITE)
        queen1 = pieces.Queen(PieceColor.BLACK)
        queen2 = pieces.Queen(PieceColor.WHITE)
        king1 = pieces.King(PieceColor.BLACK)
        king2 = pieces.King(PieceColor.WHITE)
        self.assertTrue(board.addPiece('2a', pawn1))
        self.assertTrue(board.addPiece('7a', pawn2))
        self.assertTrue(board.addPiece('1a', rook1))
        self.assertTrue(board.addPiece('8a', rook2))
        self.assertTrue(board.addPiece('8b', knight1))
        self.assertTrue(board.addPiece('1b', knight2))
        self.assertTrue(board.addPiece('8c', bishop1))
        self.assertTrue(board.addPiece('1c', bishop2))
        self.assertTrue(board.addPiece('8d', queen1))
        self.assertTrue(board.addPiece('1d', queen2))
        self.assertTrue(board.addPiece('8e', king1))
        self.assertTrue(board.addPiece('1e', king2))

        #try to add piece at invalid coordinates
        self.assertFalse(board.addPiece('9e', king2))
        self.assertFalse(board.addPiece('9a', king2))

        #try to add piece at non empty cell
        self.assertFalse(board.addPiece('1d', queen2))
        self.assertFalse(board.addPiece('1e', king2))


if __name__ == '__main__':
    unittest.main()

    board = ChessBoard()
    board.printBoard()