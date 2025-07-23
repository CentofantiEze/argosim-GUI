# main.py
import sys
from PyQt6.QtWidgets import QApplication

from main_window import SimulationApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimulationApp()
    window.resize(900, 1000)
    window.show()
    sys.exit(app.exec())
