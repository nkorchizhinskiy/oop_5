from PyQt5.QtWidgets import QDialog, \
                            QTableWidget, \
                            QSpinBox, \
                            QLabel, \
                            QAbstractItemView, \
                            QTableWidgetItem,\
                            QAbstractItemDelegate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
from decimal import Decimal
from PyQt5 import QtCore




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
        
        self.spinbox = QSpinBox(self)
        self.spinbox.setMaximum(10)
        self.spinbox.setMinimum(1)
        self.spinbox.move(70, 30)
        
        #// Create Labels
        self.label_product = QLabel('Товар', self)
        self.label_price = QLabel('Цена', self)
        self.label_lot = QLabel('Количество', self)
        self.label_cost = QLabel('Стоимость', self)
        
        self.label_product.move(20, 80)
        self.label_price.move(20, 100)
        self.label_lot.move(5, 125)
        self.label_cost.move(5, 150)
        
        self.label_cost.setFont(self.font_label)
        self.label_price.setFont(self.font_label)
        self.label_lot.setFont(self.font_label)
        self.label_cost.setFont(self.font_label)
        
        # // No Edit Mode fo cells

        
        # // Resize cells in __init__
        for row in range(4):
            self.table.setRowHeight(row, 5)
        self.table.setColumnWidth(1, 5)
        
        #// SIGNALS
        self.spinbox.valueChanged.connect(self.creating_cell_in_table)

        
    def creating_cell_in_table(self):
        self.table.setColumnCount(self.spinbox.value())
        for row in range(4):
            self.table.setRowHeight(row, 5)
            for column in range(self.spinbox.value()):
                self.table.setColumnWidth(column, 5)  
                