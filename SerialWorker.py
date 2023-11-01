import serial
from PySide6.QtCore import QThread, Signal

from serial.serialutil import SerialException

class Worker(QThread):
	new_data = Signal(str)
	status = Signal(str)

	def __init__(self, port, baudrate, parent=None):
		super().__init__(parent)

		self.serial = serial.Serial()
		self.serial.port = port
		self.serial.baudrate = baudrate

		try:
			self.serial.open()
		except (FileNotFoundError, SerialException) as e:
			raise IOError(f'Cannot find given port.')

	def run(self):
		cnt = 0
		try:
			while not self.isInterruptionRequested():
				cnt += 1
				if not (cnt % 330000):
					self.serial.write('bananaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\r\nxd\r'.encode('utf-8'))
				if self.serial.inWaiting() > 0:
					data = self.serial.read(self.serial.inWaiting())
					self.new_data.emit(data.decode("utf-8"))
		except IOError as e:
			self.status.emit(str(f"Unable to read from {self.serial.port} port."))
		except TypeError as e:
			if self.serial.port:
				self.status.emit(f"Incorrent port name: {self.serial.port}.")
			else:
				self.status.emit(f"Port name cannot be empty.")
		finally:
			self.serial.close()