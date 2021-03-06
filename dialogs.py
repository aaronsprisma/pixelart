#!/usr/bin/env python
#coding: utf-8

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

## Vista/View
class NewFileDialog(QtGui.QDialog):
	"""
	La ventanita que se abre cuando queremos crear un archivo nuevo.
	"""

	def __init__(self, Parent=None):

		super(NewFileDialog,self).__init__(Parent)

		dimensionGroup = QtGui.QGroupBox("Dimension")
		dimensionLayout = QtGui.QVBoxLayout()
		w = QtGui.QSpinBox(dimensionGroup)
		w.setValue(32)
		h = QtGui.QSpinBox(dimensionGroup)
		h.setValue(32)
		dimensionLayout.addWidget(w)
		dimensionLayout.addWidget(h)
		dimensionGroup.setLayout(dimensionLayout)

		backgroundGroup = QtGui.QGroupBox("Background")
		backgroundLayout = QtGui.QVBoxLayout()
		r1 = QtGui.QRadioButton("Transparent")
		r1.setChecked(True)
		self.r2 = QtGui.QRadioButton("Color:")
		self.cButton = QtGui.QPushButton()
		self.cButton.clicked.connect(self.getColor)
		colorLayout = QtGui.QHBoxLayout()
		colorLayout.addWidget(self.r2)
		colorLayout.addWidget(self.cButton)
		backgroundLayout.addWidget(r1)
		#backgroundLayout.addWidget(r2)
		backgroundLayout.addLayout(colorLayout)
		backgroundGroup.setLayout(backgroundLayout)

		buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
		#buttonBox.accepted.connect(self.accept)
		buttonBox.accepted.connect(Parent.createNewImage)
		buttonBox.rejected.connect(self.reject)
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(dimensionGroup)
		mainLayout.addWidget(backgroundGroup)
		mainLayout.addWidget(buttonBox)
		self.setLayout(mainLayout)
		self.setWindowTitle("Create new image")
		self.initUI()

		# Definim les senyals
		newfile = pyqtSignal([int],[int],['QColor'])

	def initUI(self):

		self.show()

	def getColor(self):

		color = QtGui.QColorDialog.getColor(Qt.green, self)
		if color.isValid(): 
			self.r2.setChecked(True)
			self.cButton.setStyleSheet("QPushButton {"
										"background: " + color.name() +";"
										"}")
			self.cButton.setText(color.name())
			self.cButton.setPalette(QtGui.QPalette(color))
			self.cButton.setAutoFillBackground(True)

	def accept(self):

		super(NewFileDialog,self).accept()