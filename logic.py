from smtplib import quoteaddr
from tabnanny import check
from tkinter import Spinbox
from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QSpinBox, \
                            QLabel, \
                            QAbstractItemView, \
                            QTableWidgetItem,\
                            QAbstractItemDelegate, \
                            QVBoxLayout,\
                            QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
from decimal import Decimal
from PyQt5 import QtCore
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np



class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(600, 400)
        self.setWindowTitle('Лабораторная 5')
        self.font_label = QFont('Times New Roman', 10)

        self.table = QTableWidget(self)
        self.table.resize(420, 120)
        self.table.move(70, 50)
        self.table.setRowCount(4)
        self.table.setColumnCount(1)
        self.table.setVerticalHeaderLabels(['Товар', 'Цена', 'Количество', 'Стоимость'])
        
        self.button = QPushButton('Нажать', self)
        self.button.clicked.connect(self.draw)

        self.spinbox = QSpinBox(self)
        self.spinbox.setMaximum(10)
        self.spinbox.setMinimum(1)
        self.spinbox.move(70, 30)
        self.table.setMinimumSize(420, 120)

        # // No Edit Mode fo cells

        # // Resize cells in __init__
        for row in range(4):
            self.table.setRowHeight(row, 5)
        self.table.setColumnWidth(1, 5)

        #// SIGNALS
        self.spinbox.valueChanged.connect(self.creating_cell_in_table)
        self.table.cellChanged.connect(self.calculate_values)

        #// Canvas
        self.figure = plt.figure(facecolor = '#FFD7C4') 
        self.canvas = FigureCanvas(self.figure)
        
        #// Layout
        layout = QVBoxLayout()
        layout.addWidget(self.spinbox)
        layout.addWidget(self.table)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        

    def creating_cell_in_table(self):
        self.table.setColumnCount(self.spinbox.value())
        for row in range(4):
            self.table.setRowHeight(row, 5)
            for column in range(self.spinbox.value()):
                self.table.setColumnWidth(column, 5)
    
    def calculate_values(self):
        if self.check_values():
            for column in range(self.spinbox.value()):
                summ = 0
                for row in range(3):
                    summ += float(self.table.item(row, column).text())
                self.table.blockSignals(True)
                self.table.setItem(3, column, QTableWidgetItem(str(summ)))
                self.table.blockSignals(False)

    def check_values(self):
        """Get values from person input in table"""
        is_empty = False
        for row in range(3):
            for column in range(self.spinbox.value()):
                try:
                    temp_value = self.table.item(row, column).text()
                except Exception:
                    is_empty = True
        if not is_empty:
            return True
        else:
            return False
                
        
    def draw(self):
        self.canvas.
        value_list = []
        for i in range(self.spinbox.value()):
            value_list.append(float(self.table.item(3, i).text()))
        y = np.array(value_list)
        print(value_list)
        plt.pie(y, autopct='%1.1f%%', shadow=True, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"}, rotatelabels=True)
        self.canvas.draw()
