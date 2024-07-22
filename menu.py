from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
import subprocess
# from main import level

app = QApplication([])
with open("stile.css","r") as file:
    app.setStyleSheet(file.read())
with open("lvl.txt","r") as file:
    lvl = file.read()


window = QWidget()
timeset = QLineEdit(window)
lvlscore = QLabel("Best Score "+ (lvl),window)
window.resize(500,500)
window.setWindowTitle("меню")
btn1 = QPushButton("старт",window)
btn2 = QPushButton("ввйті",window)
# line = QVBoxLayout()
# line.addWidget(btn1)
# line.addWidget(btn2)
# window.setLayout(line)
btn1.move(125,150)
btn2.move(125,350)
timeset.move(325,100)
timeset.setPlaceholderText("set adding time")
lvlscore.move(75,100)
btn1.setCursor(Qt.PointingHandCursor)
btn2.setCursor(Qt.PointingHandCursor)
def exit():
    app.quit()
btn2.clicked.connect(exit)
def startgame():
    subprocess.Popen(["python","main.py"])
    app.quit()
    with open("timer.txt","w") as file:
        file.write(timeset.text())
btn1.clicked.connect(startgame)







window.show()
app.exec()
