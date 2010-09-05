import sys
from PyQt4 import QtCore, QtGui, uic

class MainWindow(QtGui.QMainWindow):
   def __init__(self,parent=None):
      QtGui.QMainWindow.__init__(self,parent)
      self.ui = uic.loadUi("gui/mainWindow.ui")
      self.ui.show()
      self.character = None
      self.connect(self.ui.powersList, QtCore.SIGNAL('currentTextChanged(QString)'), self.displayPowerDetails)

   def setCharacter(self,character):
      self.character = character
      self.loadPowers()

   def loadPowers(self):
      if not self.character: return
      for power in self.character.powers:
         self.ui.powersList.addItem(power)

   def displayPowerDetails(self,power):
      power = str(power)
      self.character.usePower(power,output=False)
      self.ui.powerText.setText(self.character.powers[power].text())

