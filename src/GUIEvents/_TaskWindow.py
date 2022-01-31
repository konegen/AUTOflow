"""This is a splittet method from the Mainwindow class which contain the logic for the TaskWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UITaskWindow import *

        
def TaskWindow(self, n):
    """Define Logic for the TaskWindow GUI

    Retrieves the parameter class and set the data path, project path and output path

    Args:
      self:
        self represents the instance of the class.
      parameter:
        A parameter class with all the parameter we change and need to start the project
      

    Returns:


    Raises:
      IOError: An error occurred accessing the parameterset.
    """
    if n == "Next":
        
        self.project_name = self.AutoMLDataWindow.Projekt_Name.text()
        self.output_path_ml = self.AutoMLDataWindow.Output_Pfad.text()
        self.data_loader_path_ml = self.AutoMLDataWindow.Daten_Pfad.text()
            
    if self.project_name == "" or self.output_path_ml == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
         
        msg.setText("Please enter your data")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        
        return
    
    if n == "Back":
        
        if "Params" in self.constraints:
            self.params_factor = float(self.Window3.Params_factor.text())
        if "Floats" in self.constraints:
            self.floats_factor = float(self.Window3.Floats_factor.text())
        if "Complex" in self.constraints:
            self.complex_factor = float(self.Window3.Complex_factor.text())

    print(self.data_loader_path_ml)
    
    
    self.Window2 = UITaskWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    
    self.Window2.ImageClassification.clicked.connect(lambda:self.ConstraintsWindow("Next","imageClassification"))
    self.Window2.ImageRegression.clicked.connect(lambda:self.ConstraintsWindow("Next","imageRegression"))
    self.Window2.TextClassification.clicked.connect(lambda:self.ConstraintsWindow("Next","textClassification"))
    self.Window2.TextRegression.clicked.connect(lambda:self.ConstraintsWindow("Next","textRegression"))
    self.Window2.DataClassification.clicked.connect(lambda:self.ConstraintsWindow("Next","dataClassification"))
    self.Window2.DataRegression.clicked.connect(lambda:self.ConstraintsWindow("Next","dataRegression"))

    
    self.Window2.Back.clicked.connect(self.AutoMLData)
    
    self.setCentralWidget(self.Window2)
    self.show()