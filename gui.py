import sys
from PyQt4 import QtCore, QtGui, uic

class MainWindow(QtGui.QMainWindow):
   def __init__(self,parent=None):
      QtGui.QMainWindow.__init__(self,parent)
      self.ui = uic.loadUi("gui/mainWindow.ui")
      self.ui.show()
      self.character = None
      self.connect(self.ui.powersList, QtCore.SIGNAL('currentTextChanged(QString)'), self.displayPowerDetails)

      self.connect(self.ui.atWillCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.encounterCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.dailyCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)

      self.connect(self.ui.standardCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.moveCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.minorCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)

   def setCharacter(self,character):
      self.character = character
      self.loadPowers()

   def loadPowers(self):
      if not self.character: return
      self.ui.powersList.clear()

      frequency = []
      if self.ui.atWillCheck.isChecked(): frequency.append('at-will')
      if self.ui.encounterCheck.isChecked(): frequency.append('encounter')
      if self.ui.dailyCheck.isChecked(): frequency.append('daily')

      action = []
      if self.ui.standardCheck.isChecked(): action.append('standard')
      if self.ui.moveCheck.isChecked(): action.append('move')
      if self.ui.minorCheck.isChecked(): action.append('minor')

      for power in self.character.getPowers(frequency=frequency,action=action):
         self.ui.powersList.addItem(power)

   def displayPowerDetails(self,power):
      power = str(power)

      if not power:
         self.ui.powerText.setText('')
         self.ui.powerImageLabel.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage()))
         return

      self.character.usePower(power,output=False)
      self.ui.powerText.setText(self.character.powers[power].text())
      imageName = 'gui/'+power+'.jpeg'
      image = QtGui.QImage(imageName) if QtCore.QFileInfo(imageName).isReadable() else QtGui.QImage()
      self.ui.powerImageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
