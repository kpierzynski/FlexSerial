from PySide6.QtWidgets import (
	QMainWindow,
	QVBoxLayout,
	QHBoxLayout,
	QPushButton,
	QWidget,
	QComboBox,
)

from utils import show_status_bar_message
from PortSettings import PortSettings
from SerialWorker import Worker
from SerialTerminal import SerialTerminal


class FlexSerial(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Flex Serial 2")
		self.setGeometry(100, 100, 400, 400)
		self.statusbar = self.statusBar()

		self.container = QWidget(self)
		self.setCentralWidget(self.container)

		self.layout = QVBoxLayout(self.container)

		self.port_settings = PortSettings()
		self.layout.addWidget(self.port_settings)

		self.text_field = SerialTerminal()
		self.text_field.setReadOnly(True)
		self.layout.addWidget(self.text_field)

		self.start_button = QPushButton("Start", self)
		self.start_button.clicked.connect(self.start_serial)
		self.layout.addWidget(self.start_button)

		self.pause_button = QPushButton("Pause", self)
		self.pause_button.setEnabled(False)
		self.pause_button.clicked.connect(self.pause_serial)
		self.layout.addWidget(self.pause_button)

		self.isReading = False

		show_status_bar_message( self, f"Waiting for action. Found {self.port_settings.get_ports_count()} ports.")

	
	def closeEvent(self, event):
		try:
			self.worker.requestInterruption()
		except AttributeError:
			pass

	def update_text_field(self, data):
		if not self.isReading:
			return

		for c in data:
			self.text_field.update_char(c)
					
	def handle_serial_error(self, status):
		show_status_bar_message(self, status)
		self.start_button.setEnabled(True)
		self.pause_button.setEnabled(False)

	def start_serial(self):
		port, baudrate = self.port_settings.get_serial_information()

		try:
			self.isReading = True

			self.worker = Worker(port, baudrate, self)
			self.worker.new_data.connect(self.update_text_field)
			self.worker.status.connect(self.handle_serial_error)
			self.worker.start()

			self.start_button.setEnabled(False)
			self.pause_button.setEnabled(True)

			show_status_bar_message(self, f'Opened port {port} at {baudrate} speed.')
		except (NameError, IOError) as e:
			self.isReading = False
			show_status_bar_message(self, f'Unable to spawn serial worker. {e}')

	def pause_serial(self):
		self.worker.requestInterruption()
		self.isReading = False
		self.start_button.setEnabled(True)
		self.pause_button.setEnabled(False)
		show_status_bar_message(self, f'Paused port.')
		return