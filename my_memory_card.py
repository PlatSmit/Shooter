#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

class Question():
    def __init__(self,question_,right_answer,wrong_1,wrong_2,wrong_3):
        self.question = question_
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

question_list = []
question_list.append(Question('Какой сегодня день недели','Пятница','Четверг','Вторник','Среда'))
question_list.append(Question('Из каких цветов состоит флаг Германии','жёлтый,красный,чёрный','зелёный,белый,красный','красный,синий,белый','чёрный,оранжевый,зелёный'))
question_list.append(Question('Сколько будет (28 - 14) * 2','28','0','228','14'))

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 240)
question = QLabel('Какой национальности не существует?')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
RadioGroupBox = QGroupBox("Варианты ответов")
layout_ans01 = QHBoxLayout()
layout_ans02 = QVBoxLayout()
layout_ans03 = QVBoxLayout()
layout_ans02.addWidget(rbtn_1)
layout_ans02.addWidget(rbtn_2)
layout_ans03.addWidget(rbtn_3)
layout_ans03.addWidget(rbtn_4)
layout_ans01.addLayout(layout_ans02)
layout_ans01.addLayout(layout_ans03)
RadioGroupBox.setLayout(layout_ans01)
main_layout = QVBoxLayout()
answer = QPushButton('Ответить')
AnsRadioBox = QGroupBox('Результат теста')
layout_ans11 = QHBoxLayout()
layout_ans12 = QHBoxLayout()
layout_ans13 = QVBoxLayout()
result = QLabel('Правильно/Неправильно')
right = QLabel('Правильный ответ')
layout_ans11.addWidget(result)
layout_ans12.addWidget(right, alignment = Qt.AlignHCenter)
layout_ans13.addLayout(layout_ans11)
layout_ans13.addLayout(layout_ans12)
AnsRadioBox.setLayout(layout_ans13)
AnsRadioBox.hide()
def show_question():
    AnsRadioBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
 
def show_result():
    RadioGroupBox.hide()
    AnsRadioBox.show()
    answer.setText('Следующий вопрос')
 
def show_start():
    if answer.text() == 'Ответить':
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
main_win.num_question = -1
shuffle(question_list)
def next_question():
    main_win.num_question += 1
    if main_win.num_question >= len(question_list):
        main_win.num_question = 0
    q = question_list[main_win.num_question]
    ask(q)

def click_OK():
    if answer.text() == 'Ответить':
        check_asnwer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    question.setText(q.question)
    right.setText(q.right_answer)
    show_question()
 
 
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    elif answers[1].isChecked or answers[2].isChecked or answers[3].isChecked():
        show_correct('Неверно!')
 
def show_correct(res):
    result.setText(res)
    show_result()
 
ask(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
answer.clicked.connect(check_answer)
main_layout.addWidget(question, alignment = Qt.AlignHCenter)
main_layout.addWidget(RadioGroupBox, alignment = Qt.AlignHCenter)
main_layout.addWidget(AnsRadioBox, alignment = Qt.AlignHCenter)
main_layout.addWidget(answer, alignment = Qt.AlignHCenter)
main_win.setLayout(main_layout)

main_win.show()
app.exec_()
