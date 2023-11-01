import sys

from PySide6.QtWidgets import QApplication

from FlexSerial import FlexSerial

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = FlexSerial()
	window.show()
	sys.exit(app.exec())
