''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from src.GUILayout.UILoadWindow import *


def LoadWindow(self):
    """Activates the GUI window to create the project.

    Before the GUI is activated, the previous window is checked. If
    pruning and/or quantization have been selected as optimization
    algorithms, it is checked whether a data loader was selected.
    If everything is correct the GUI gets activated. If not
    a message box appears with a warning. When the load button is
    selected, the optimization algorithms are applied if any are
    selected. Also, the model is converted and the files are created.
    """
    self.Window5 = UILoadWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.model_path, self.project_name, self.output_path, self.data_loader_path, self.optimizations, self.prun_type, self.prun_factor_dense, self.prun_factor_conv, self.prun_acc_type, self.prun_acc, self.quant_dtype, self.separator, self.csv_target_label, self.target, self)
    
    if isinstance(self.model_memory, int):
        self.Window5.model_memory.setText(str(self.model_memory))

    
    self.Window5.back.clicked.connect(lambda:nextWindow(self, "Back", self.optimizations, self.Window5))
    
    self.Window5.load.clicked.connect(lambda:nextWindow(self, "Next", self.optimizations, self.Window5))
    
    self.Window5.prune_model.request_signal.connect(lambda:self.convert_create(self.Window5))
    self.Window5.conv_build_load.request_signal.connect(lambda:self.terminate_thread(self.Window5))
    
    self.Window5.finish.clicked.connect(self.close)
    
    self.setCentralWidget(self.Window5)
    self.show()



def nextWindow(self, n, optimizations, CurWindow):
    """
    Defines which one is the next window to open if you
    press "Back". If optimization algorithms were previously
    selected, the data loader is the next window otherwise
    the optimization window.

    Args:
        n:              Go forward or go back
        optimizations:  Selected optimization algorithms
        CurWindow:      GUI window from which the function is executed
    """
    if n == "Back":
        try:
            self.model_memory = int(self.Window5.model_memory.text())
        except:
            self.model_memory = None

        if optimizations:
            self.DataloaderWindow()
        else:
            self.OptiWindow()
    
    elif n == "Next":
        reply = QMessageBox.question(self, 'Create Project', 'Do you want to create the project?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.model_pruning(CurWindow)
        else:
            return