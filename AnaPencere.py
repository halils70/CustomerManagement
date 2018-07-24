import sys
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore
from Sources.CariMain import Ui_MainWindow
import PyQt5.uic


class AnaPencere(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(AnaPencere, self).__init__()
        Ui_MainWindow.__init__(self)
        self.win_stok_yarat = 0
        self.win_cari_yarat = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_Cik.triggered.connect(self.closeEventFromAction)
        self.ui.actionCari_Hesaplar.triggered.connect(self.call_cari_window)
        self.ui.actionStok_islemleri.triggered.connect(self.call_stok_window)
        #self.setWindowFlags(PyQt5.QtCore.Qt.CustomizeWindowHint() & ~PyQt5.QtCore.Qt.WindowCloseButtonHint)

    def call_cari_window(self):
        if self.win_cari_yarat == 0:
            self.win_cari_yarat = 1
            self.win_cari = self.ui.mdiArea.addSubWindow(self.ui.subwindow_Cari_Hesap)
            self.win_cari.resize(900, 600)
            #self.win_cari.setWindowFlag(PyQt5.QtCore.Qt.CustomizeWindowHint)
            #self.win_cari.setWindowFlag(PyQt5.QtCore.Qt.WindowCloseButtonHint)
            self.win_cari.show()

    def call_stok_window(self):
        if self.win_stok_yarat == 0:
            self.win_stok_yarat = 1
            win_stok = self.ui.mdiArea.addSubWindow(self.ui.subwindow_Stok_islemleri)
            win_stok.resize(900, 500)
            win_stok.show()

    def closeEvent(self, event):
        msgBox = PyQt5.QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Uygulama çıkış!")
        msgBox.setText("Uygulamadan çıkmak istediğinizden emin misiniz?")
        msgBox.setStandardButtons(PyQt5.QtWidgets.QMessageBox.Cancel | PyQt5.QtWidgets.QMessageBox.Yes | PyQt5.QtWidgets.QMessageBox.No);
        msgBox.setDefaultButton(PyQt5.QtWidgets.QMessageBox.No);
        if msgBox.exec_() == PyQt5.QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def closeEventFromAction(self):
        msgBox = PyQt5.QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Uygulama çıkış!")
        msgBox.setText("Uygulamadan çıkmak istediğinizden emin misiniz?")
        msgBox.setStandardButtons(PyQt5.QtWidgets.QMessageBox.Cancel | PyQt5.QtWidgets.QMessageBox.Yes | PyQt5.QtWidgets.QMessageBox.No);
        msgBox.setDefaultButton(PyQt5.QtWidgets.QMessageBox.No);
        if msgBox.exec_() == PyQt5.QtWidgets.QMessageBox.Yes:
            self.PyQt5.QtWidgets.QApplication.closeAllWindows()
        else:
            return

class main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    myWin = AnaPencere()
    myWin.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
