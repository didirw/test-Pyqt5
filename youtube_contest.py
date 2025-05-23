#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,QWidget,QRadioButton,
    QLabel,QVBoxLayout,QHBoxLayout,QMessageBox)



def show_win():
    v_window =QMessageBox()
    v_window.setText('Yesssssssssssssssssssssssssssssss')
    v_window.exec()
def show_no():
    v_window =QMessageBox()
    v_window.setText('нет  ')
    v_window.exec()
#создание приложения и главного окна
app = QApplication([])
window =QWidget()
window.resize(1000,500)
window.setWindowTitle('Crazy People')
window.move(300,100)
question =QLabel ('что?')

bt1 = QRadioButton('человек')
bt1.clicked.connect(show_no)
bt2 = QRadioButton('пелмень')
bt2.clicked.connect(show_no)
bt3 = QRadioButton('амёба')
bt3.clicked.connect(show_no)
bt4 = QRadioButton('млекопитающие')
bt4.clicked.connect(show_win)

v_l =QVBoxLayout()
h_1 =QHBoxLayout()
h_2 =QHBoxLayout()
h_3 =QHBoxLayout()
h_1.addWidget(question,alignment=Qt.AlignCenter)
h_2.addWidget(bt1,alignment=Qt.AlignCenter)
h_2.addWidget(bt2,alignment=Qt.AlignCenter)
h_3.addWidget(bt3,alignment=Qt.AlignCenter)
h_3.addWidget(bt4,alignment=Qt.AlignCenter)
v_l.addLayout(h_1)
v_l.addLayout(h_2)
v_l.addLayout(h_3)






window.setLayout(v_l)




window.show()
app.exec()
 #создание виджетов главного окна
 
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 