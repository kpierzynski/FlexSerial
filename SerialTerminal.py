from PySide6.QtWidgets import QPlainTextEdit

class SerialTerminal(QPlainTextEdit):
	def __init__(self):
		super().__init__()

		self.setLineWrapMode(QPlainTextEdit.NoWrap)

		self.head = 0

	def update_char(self, c):
		match c:
			case '\r':
				self.head -= len(self.toPlainText().split('\n').pop())
			case '\n':
				self.appendPlainText(c)
				self.head = len(self.toPlainText())-1
			case _:
				text = self.toPlainText()
				index = self.head
				text = text[:index] + c + text[index + 1:]
				self.head += 1
				self.setPlainText(text)