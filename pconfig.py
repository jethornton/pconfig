#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, platform
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from help import Ui_Dialog as helpDialog
from about import Ui_about as aboutDialog
import helptext, utilities

class App(QMainWindow):
	def __init__(self):
		super(App, self).__init__()
		uic.loadUi("pconfig.ui", self)
		self.version = '0.0'
		self.setWindowTitle('Parallel Port Configuration Tool Version {}'.format(self.version))
		self.show()
		self.setup()

	def setup(self):
		self.nameLE.textChanged.connect(utilities.onConfigNameChanged)


	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionNew_triggered(self):
		self.statusbar.showMessage('File New')


	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionOpen_triggered(self):
		self.statusbar.showMessage('File Open')


	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionCheck_triggered(self):
		self.statusbar.showMessage('File Check')


	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionBuild_triggered(self):
		self.statusbar.showMessage('File Build')

	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionExit_triggered(self):
		exit()

	@pyqtSlot()
	def on_actionGeneralHelp_triggered(self):
		self.help(20)

	@pyqtSlot()
	def on_actionTabHelp_triggered(self):
		self.help(self.tabWidget.currentIndex())

	@pyqtSlot()
	def on_actionAbout_triggered(self):
		pcStats = platform.uname()
		dialog = QtWidgets.QDialog()
		dialog.ui = aboutDialog()
		dialog.ui.setupUi(dialog)
		#dialog.ui.label.setText(text)
		dialog.ui.versionLB.setText('Version {}'.format(self.version))
		dialog.ui.systemLB.setText(pcStats.system)
		dialog.ui.releaseLB.setText('Kernel {}'.format(pcStats.release))
		dialog.ui.machineLB.setText('Processor {}'.format(pcStats.machine))
		if sys.maxsize > 2**32: # test for 64bit OS
			dialog.ui.bitsLB.setText('64 bit OS')
		else:
			dialog.ui.bitsLB.setText('32 bit OS')
		dialog.exec_()


	def help(self, index):
		dialog = QtWidgets.QDialog()
		dialog.ui = helpDialog()
		dialog.ui.setupUi(dialog)
		dialog.ui.label.setText(helptext.descriptions(index))
		dialog.exec_()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
