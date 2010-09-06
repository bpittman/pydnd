import sys
from PyQt4 import QtCore, QtGui, uic

class MainWindow(QtGui.QMainWindow):
   def __init__(self,parent=None):
      QtGui.QMainWindow.__init__(self,parent)
      self.ui = uic.loadUi("gui/mainWindow.ui")
      self.ui.show()
      self.character = None

      self.connect(self.ui.powersTree, QtCore.SIGNAL('itemSelectionChanged()'), self.displayPowerDetails)

      self.connect(self.ui.atWillCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.encounterCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.dailyCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)

      self.connect(self.ui.standardCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.moveCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.minorCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.interruptCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)

      self.connect(self.ui.usedCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)
      self.connect(self.ui.unusedCheck, QtCore.SIGNAL('stateChanged(int)'), self.loadPowers)

      self.connect(self.ui.weaponCombo,QtCore.SIGNAL('activated(QString)'),self.equipWeapon)

      self.connect(self.ui.usedButton,QtCore.SIGNAL('clicked()'),self.usePower)
      self.connect(self.ui.unusedButton,QtCore.SIGNAL('clicked()'),self.unusePower)

      self.connect(self.ui.shortRestButton,QtCore.SIGNAL('clicked()'),self.shortRest)
      self.connect(self.ui.extendedRestButton,QtCore.SIGNAL('clicked()'),self.extendedRest)

   def setCharacter(self,character):
      self.character = character
      self.loadPowers()
      self.loadWeapons()

   def loadPowers(self):
      if not self.character: return
      self.ui.powersTree.clear()

      atWills = QtGui.QTreeWidgetItem(['at-will'])
      encounters = QtGui.QTreeWidgetItem(['encounter'])
      dailies = QtGui.QTreeWidgetItem(['daily'])
      self.ui.powersTree.addTopLevelItems([atWills,encounters,dailies])

      frequency = []
      if self.ui.atWillCheck.isChecked(): frequency.append('at-will')
      if self.ui.encounterCheck.isChecked(): frequency.append('encounter')
      if self.ui.dailyCheck.isChecked(): frequency.append('daily')

      action = []
      if self.ui.standardCheck.isChecked(): action.append('standard')
      if self.ui.moveCheck.isChecked(): action.append('move')
      if self.ui.minorCheck.isChecked(): action.append('minor')
      if self.ui.interruptCheck.isChecked(): action.append('interrupt')

      usage = []
      if self.ui.unusedCheck.isChecked(): usage.append('unused')
      if self.ui.usedCheck.isChecked(): usage.append('used')

      for power in self.character.getPowers(frequency=frequency,action=action,usage=usage):
         if self.character.powers[power].frequency == 'at-will':
            QtGui.QTreeWidgetItem(atWills,[power])
         if self.character.powers[power].frequency == 'encounter':
            QtGui.QTreeWidgetItem(encounters,[power])
         if self.character.powers[power].frequency == 'daily':
            QtGui.QTreeWidgetItem(dailies,[power])
      self.ui.powersTree.expandAll()

   def usePower(self):
      power = self.getCurrentPower()
      if power:
         self.character.powers[power].setUsed(True)
         self.loadPowers()

   def unusePower(self):
      power = self.getCurrentPower()
      if power:
         self.character.powers[power].setUsed(False)
         self.loadPowers()

   def shortRest(self):
      if self.character: self.character.shortRest()
      self.loadPowers()

   def extendedRest(self):
      if self.character: self.character.extendedRest()
      self.loadPowers()

   def loadWeapons(self):
      if not self.character: return
      for weapon in self.character.weapons:
         self.ui.weaponCombo.addItem(weapon)
      if 'main' in self.character.equipped:
         index = self.ui.weaponCombo.findText(self.character.equipped['main'])
         if index >= 0:
            self.ui.weaponCombo.setCurrentIndex(index)

   def getCurrentPower(self):
      selection = self.ui.powersTree.selectedItems()
      if len(selection):
         power = str(selection[0].text(0))
         return power if power in self.character.powers else None

   def equipWeapon(self,weapon):
      if not self.character or not weapon: return
      weapon = str(weapon)
      self.character.setEquip(main=weapon)
      self.displayPowerDetails()

   def displayPowerDetails(self):
      power = self.getCurrentPower()
      if not power:
         self.ui.powerText.setText('')
         self.ui.powerImageLabel.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage()))
         return

      self.character.getPowerStats(power,output=False)
      self.ui.powerText.setText(self.character.powers[power].text())
      imageName = 'gui/'+power+'.jpeg'
      image = QtGui.QImage(imageName) if QtCore.QFileInfo(imageName).isReadable() else QtGui.QImage()
      self.ui.powerImageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
