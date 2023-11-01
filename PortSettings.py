from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton

import serial.tools.list_ports
from utils import show_status_bar_message


class PortSettings(QWidget):
	def __init__(self):
		super().__init__()

		self.baudrates = [
			4800,
			9600,
			19200,
			28800,
			38400,
			57600,
			76800,
			115200,
			230400,
			460800,
			676000,
			921600,
		]
		
		self.layout = QVBoxLayout(self)
		self.setLayout(self.layout)

		self.baud_list = QComboBox(self)
		self.layout.addWidget(self.baud_list)

		self.port_layout = QHBoxLayout(self)
		self.port_list = QComboBox(self)
		self.port_layout.addWidget(self.port_list, 1)
		self.refresh_button = QPushButton("Refresh", self)
		self.port_layout.addWidget(self.refresh_button)

		self.layout.addLayout(self.port_layout)

		self.layout.setContentsMargins(0, 0, 0, 0)

		self.populate_ports()
		self.populate_baudrates()

		self.serial_port = serial.Serial()
		self.baudrate = self.baudrates[1]
		self.port = self.port_list.currentText()

		self.baud_list.currentIndexChanged.connect(self.set_baudrate)
		self.port_list.currentIndexChanged.connect(self.set_port)
		self.refresh_button.clicked.connect(self.populate_ports)

	def set_baudrate(self):
		self.baudrate = self.baud_list.currentText()
		print(self.baudrate)

	def set_port(self):
		self.port = self.port_list.currentText()
		print(self.port)

	def populate_ports(self):
		self.port_list.clear()
		ports = list(serial.tools.list_ports.comports())
		for port in ports:
			self.port_list.addItem(port.device)

		show_status_bar_message(self, f"Refreshing ports. Found {len(ports)} ports.")

	def get_ports_count(self):
		return len(list(serial.tools.list_ports.comports()))

	def populate_baudrates(self):
		self.baud_list.clear()
		for baud in self.baudrates:
			self.baud_list.addItem(str(baud))

	def get_serial_information(self):
		return self.port, self.baudrate

