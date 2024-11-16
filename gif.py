#!/usr/bin/env python3
"""Show animated gif with a transparent background on the screen."""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
w = QLabel()
w.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # transparent window
w.setAttribute(Qt.WA_TranslucentBackground)

movie = QMovie('anime-noted.gif')
w.setMovie(movie)
movie.start()


# center
w.adjustSize()  # update w.rect() now
w.move(2404, 1282)
w.show()
sys.exit(app.exec_())