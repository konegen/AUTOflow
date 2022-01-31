''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.GUILayout.UIDataloaderWindow import *


def DataloaderWindow(self):
    """Activates the GUI window of the data loader.

    Before the GUI is activated, the previous window is checked. If
    "Next" is pressed and pruning and/or quantization have been
    selected as optimization algorithms, it is checked whether the
    entries are correct and complete. If everything is correct the
    GUI gets activated. If not a message box appears with a warning.
    With the dropdown menu you can select whether the training data
    should be transferred in a file or folder.
    """

    self.Window3 = UIDataloaderWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)

    if self.data_loader_path != None:
        self.set_data_loader_label(self.Window3)

    self.Window3.select_data_browse.clicked.connect(lambda: self.get_data_loader(self.Window3))

    self.Window3.Back.clicked.connect(lambda: nextWindow(self, "Back"))
    self.Window3.Next.clicked.connect(lambda: nextWindow(self, "Next"))
    
    self.setCentralWidget(self.Window3)
    self.show()



def nextWindow(self, n):
    if n == "Back":
        self.OptiWindow()
    
    elif n == "Next":
        self.data_loader_path = self.Window3.data_path.text()
        
        if self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            
            msg.setText("Please enter a data loader.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return   

        self.LoadWindow()