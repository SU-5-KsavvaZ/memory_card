from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QButtonGroup, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox
from random import shuffle
from random import randint

class Question():
    def __init__(self, question1, right, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
q_list = list()
q_list.append(Question('Сколько вёдер в стаке?', '16', '64', '1', '8'))
q_list.append(Question('Значение спавнрейта враждебных мобов в одиночке?', '79', '90', '70', '15'))
q_list.append(Question('Сколько всего музыкальных дисков?', '14', '11', '10', '15'))
q_list.append(Question('Сколько единиц урона можно нанести пустой рукой при критическом ударе?', '1.5', '2', '1', '0.5'))
q_list.append(Question('Какой предмет быстрее ломается?', 'Золотая лопата', 'Золотой топор', 'Незеритовая мотыга', 'Деревянная лопата'))
q_list.append(Question('Если не ударить скелета рукой, то пёс побежит на него. Почему?', 'Любит грызть косточки', 'Врёте вы всё, не бывает такого!', 'Скелеты ненавидят собак и стреляют первыми', 'Это старый баг'))
def quest():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    pbtn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def s_result():
    AnswerGroupBox.show()
    RadioGroupBox.hide()
    pbtn.setText('Следующий вопрос')

def test():
    if pbtn.text() == 'Ответить':
        check_ans()
    elif pbtn.text() == 'Следующий вопрос':
        next()
        quest()


app = QApplication([])
main_win = QWidget()
main_win.resize(600, 300)
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
layout_main = QVBoxLayout()

RadioGroupBox = QGroupBox("Варианты объектов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
pbtn = QPushButton('Ответить')

buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q : Question):
    shuffle(buttons)
    buttons[0].setText(q.right)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)
    question.setText(q.question1)
    truth_ans.setText(q.right)


def show_correct(res):
    result.setText(res)
    s_result()
    
main_win.total = 0
main_win.score = 0

def check_ans():
    if buttons[0].isChecked():
        show_correct('правильно')
        main_win.total += 1
        main_win.score += 1
        print('Статистика\n - всего вопросов', main_win.total, '\n - правильный ответов:', main_win.score)
        print('Рейтинг: ', str((main_win.score/main_win.total)*100) + '%')
    else:
        if buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():    
            show_correct('Неверно')
            main_win.total += 1
            print('Статистика\n - всего вопросов', main_win.total, '\n - правильный ответов:', main_win.score)
            print('Рейтинг: ', str((main_win.score/main_win.total)*100)+'%')

def next():
    cur_question = randint(0, len(q_list)-1)
    ask(q_list[cur_question])



RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnswerGroupBox = QGroupBox('Результаты теста')
result = QLabel('Верно/неверно')
truth_ans = QLabel('Правильный ответ')
layoutout = QVBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans_OK = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout_ans_OK.addStretch(1)
layout_ans_OK.addWidget(pbtn, stretch=2)
layout_ans_OK.addStretch(1)

layoutout.addWidget(result)
layoutout.addWidget(truth_ans, alignment = Qt.AlignCenter)




RadioGroupBox.setLayout(layout_ans1)
AnswerGroupBox.setLayout(layoutout)
layout_main.addWidget(question, alignment= Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox, alignment= Qt.AlignCenter)
layout_main.addWidget(AnswerGroupBox, alignment= Qt.AlignCenter)
layout_main.addLayout(layout_ans_OK)

AnswerGroupBox.hide()


main_win.setLayout(layout_main)
main_win.show()
ask(q_list[0])
pbtn.clicked.connect(test)
app.exec_()
