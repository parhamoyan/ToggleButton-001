# ///////////////////////////////////////////////////////////////
#
# Copyright 2021 by Parham Oyan and Oleg Frolov
# All rights reserved.
#
# ///////////////////////////////////////////////////////////////

import sys

from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())