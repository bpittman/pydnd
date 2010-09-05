import sys
from PyQt4 import QtGui, uic

class MainWindow(QtGui.QMainWindow):
   def __init__(self,parent=None):
      QtGui.QMainWindow.__init__(self,parent)
      self.ui = uic.loadUi("gui/mainWindow.ui")
      self.ui.show()
      self.character = None

   def setCharacter(self,character):
      self.character = character
      self.loadPowers()

   def loadPowers(self):
      if not self.character: return
      for power in self.character.powers:
         self.ui.powersList.addItem(power)


