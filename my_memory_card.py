#создай приложение для запоминания информации
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QRadioButton,QMessageBox,QHBoxLayout, QGroupBox, QPushButton, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_ans, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []

question_list.append(Question('Государственный язык Бразилии?','Португальский','Английский','Испанский','Бразильский'))
question_list.append(Question('Какого штата нет в Амереке?','Небраска','Орегон','Висконсин','Чикаго'))
question_list.append(Question('Национальная хижина якутов?','Ураса','Юрта','Иглу','Хата'))

#создание приложения и главного окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory cards')
#создание виджетов главного окна
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')

#win = QLabel('МОЛОДЕЦ!')
ratn = QGroupBox('Варианты ответов')
question = QLabel("Какой национальности не существует?")
ok = QPushButton('Ответить')
layout_main = QVBoxLayout()

#win.hide()

line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_3 = QHBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

ratn.setLayout(layout_ans1)

radio_group = QButtonGroup()
radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)

ANS = QGroupBox('Результат теста')
result = QLabel('прав ли ты или нет?')
correct = QLabel('Тут будет ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment = Qt.AlignHCenter, stretch = 2)
ANS.setLayout(layout_res)

ANS.hide()

line_1.addWidget(question, alignment =  (Qt.AlignHCenter | Qt.AlignVCenter))
line_2.addWidget(ratn)
line_2.addWidget(ANS)
line_3.addWidget(ok, stretch = 2)

line_3.addStretch(1)

layout_main.addLayout(line_1, stretch = 2)
layout_main.addLayout(line_2, stretch = 8)
layout_main.addStretch(1)
layout_main.addLayout(line_3, stretch = 1)
layout_main.setSpacing(5)

answer = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_ans)
    answer[1].setText(q.wrong_1)
    answer[2].setText(q.wrong_2)
    answer[3].setText(q.wrong_3)
    question.setText(q.question)
    correct.setText(q.right_ans)
    show_question()

def next_question():
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def check():
    if answer [0].isChecked():
        result.setText('Правильно!')
    else:
        result.setText('Не правильно')
    show_result()

def show_result():
    ratn.hide()
    ANS.show()
    ok.setText('Следующий вопрос')

def show_question():
    ratn.show()
    ANS.hide()
    ok.setText('Ответить')

    radio_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radio_group.setExclusive(True)

def start_test():
    if ok.text() == 'Ответить':
        check()
    else:
        next_question()


next_question()

#win.show()
#ANS.hide()
#ratn.hide()

window.setLayout(layout_main)

ok.clicked.connect(start_test)

#Запуск
window.setLayout(layout_main)
window.show()
app.exec()