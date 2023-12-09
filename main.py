from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500, 200)
lbl = QLabel("Скільки буде 2+2?")
lbl2 = QLabel("Скільки буде 1+3?")
ans1 = QRadioButton("4")
ans2 = QRadioButton("14")
ans3 = QRadioButton("1")
ans4 = QRadioButton("0")

main_line = QVBoxLayout()
main_line.addWidget(lbl )

hline = QHBoxLayout()
hline.addWidget(ans1)
hline.addWidget(ans2)

h2line = QHBoxLayout()
h2line.addWidget(ans3)
h2line.addWidget(ans4)

main_line.addLayout(hline)
main_line.addLayout(h2line)
main_line.addWidget(lbl2)

ans5 = QRadioButton("4")
ans6 = QRadioButton("14")
ans7 = QRadioButton("1")
ans8 = QRadioButton("0")

h3line = QHBoxLayout()
h3line.addWidget(ans5)
h3line.addWidget(ans6)

h4line = QHBoxLayout()
h4line.addWidget(ans7)
h4line.addWidget(ans8)

main_line.addLayout(h3line)
main_line.addLayout(h4line)

def true_var_1():
    msg = QMessageBox()
    msg.setText('Правильно')
    msg.exec()

def False_var_1():
    msg = QMessageBox()
    msg.setText('Не правилно')
    msg.exec()

ans1.clicked.connect(true_var_1)
ans2.clicked.connect(False_var_1)
ans3.clicked.connect(False_var_1)
ans4.clicked.connect(False_var_1)

ans5.clicked.connect(true_var_1)
ans6.clicked.connect(False_var_1)
ans7.clicked.connect(False_var_1)
ans8.clicked.connect(False_var_1)

window.setLayout(main_line)
window.show()
app.exec()