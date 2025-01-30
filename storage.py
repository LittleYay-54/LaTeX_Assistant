# storing initial code here from the previous project, sLaTeX
# it wasn't much but it might be useful later? idk

# -- || -- main.py -- || --
# import sys
# from PyQt5.QtWidgets import QApplication
# from gui import MainWindow
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec_())

# -- || -- gui.py -- || --
# from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
# from PyQt5.QtGui import QPixmap, QPainter
# from PyQt5.QtCore import Qt, QPoint
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("sLaTeX")
#         self.setGeometry(100, 100, 800, 600)
#
#         # -- canvas --
#         self.canvas = QLabel(self)
#         self.canvas.setGeometry(10, 10, 780, 480)
#         self.canvas.setPixmap(QPixmap(780, 480))
#         self.canvas.pixmap().fill(QtCore.Qt.white)
#
#         # -- pen button --
#         self.pen_button = QPushButton("Pen", self)
#         self.pen_button.setGeometry(10, 500, 60, 30)
#         self.pen_button.clicked.connect(self.switch_to_pen)
#
#         # -- eraser button --
#         self.eraser_button = QPushButton("Eraser", self)
#         self.eraser_button.setGeometry(80, 500, 60, 30)
#         self.eraser_button.clicked.connect(self.switch_to_eraser)
#
#         # -- clear button --
#         self.clear_button = QPushButton("Clear", self)
#         self.clear_button.setGeometry(150, 500, 60, 30)
#         self.clear_button.clicked.connect(self.clear_canvas)
#
#         # -- convert to latex button --
#         self.convert_button = QPushButton("Convert to LaTeX", self)
#         self.convert_button.setGeometry(220, 500, 120, 30)
#         self.convert_button.clicked.connect(self.convert_to_latex)
#
#         # -- initializing cursor as lifted pen --
#         self.last_point = QPoint()
#         self.drawing = False
#         self.pen_color = Qt.black
#         self.pen_width = 3
#
#     def switch_to_pen(self):
#         self.pen_color = Qt.black
#         self.pen_width = 3
#
#     def switch_to_eraser(self):
#         self.pen_color = Qt.white
#         self.pen_width = 10
#
#     def clear_canvas(self):
#         # fills the pixmap with white
#         self.canvas.pixmap().fill(QtCore.Qt.white)
#         self.canvas.update()
#
#     def convert_to_latex(self):
#         print("example latex code")
#
#     def mousePressEvent(self, event):
#         if event.button() == QtCore.Qt.LeftButton:
#             self.drawing = True
#             self.last_point = event.pos()
#
#     def mouseMoveEvent(self, event):
#         if event.buttons() & Qt.LeftButton and self.drawing:
#             painter = QPainter(self.canvas.pixmap())
#             painter.setPen(QtGui.QPen(self.pen_color, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
#             painter.drawLine(self.last_point, event.pos())
#             self.last_point = event.pos()
#             self.canvas.update()
#
#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.drawing = False
