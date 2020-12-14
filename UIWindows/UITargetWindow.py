import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UITargetWindow(QWidget):
    def __init__(self, parent=None):
        super(UITargetWindow, self).__init__(parent)
        
        self.label = QLabel("Choose your target")
        self.label.setFont(QFont("Choose your target", 12))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_v = QLabel()
        self.Abstand_v.setFixedHeight(120)
        
        self.Abstand_button = QLabel()
        self.Abstand_button.setFixedWidth(10)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_4.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)        
        
        self.uC = QPushButton(self)
        self.uC.setIcon(QIcon(os.path.join('Images', 'MCU.png')))
        self.uC.setIconSize(QSize(200, 250))
        self.uC.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        self.FPGA = QPushButton(self)
        self.FPGA.setIcon(QIcon(os.path.join('Images', 'FPGA.png')))
        self.FPGA.setIconSize(QSize(200, 250))
        self.FPGA.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
    
        self.DK = QPushButton(self)
        self.DK.setIcon(QIcon(os.path.join('Images', 'question.png')))
        self.DK.setIconSize(QSize(200, 250))
        self.DK.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Abstand_button)
        self.horizontal_box[1].addWidget(self.uC)
        self.horizontal_box[1].addWidget(self.Abstand_button)
        self.horizontal_box[1].addWidget(self.FPGA)
        self.horizontal_box[1].addWidget(self.Abstand_button)
        self.horizontal_box[1].addWidget(self.DK)
        self.horizontal_box[1].addWidget(self.Abstand_button)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_v)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1)
        sublayout.addWidget(self.Abstand, 0, 2)
        self.horizontal_box[3].addLayout(sublayout)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)