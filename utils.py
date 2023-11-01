from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QStatusTipEvent
  
def show_status_bar_message(sender, message):
	QApplication.sendEvent(sender, QStatusTipEvent(message))