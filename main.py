from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout,QMessageBox, QRadioButton, QButtonGroup
from random import *

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
     self.question = question
     self. right_answer = right_answer
     self.wrong1 = wrong1
     self.wrong2 = wrong2
     self.wrong3 = wrong3



question_list = []
question_list.append(Question('государственый язык бразилии', "португальский", "англиский", 'португальский', 'бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', "зеленый", "красный", "белый", 'синий'))
question_list.append(Question('нациалальноя хижина якутов', "урсака", 'юрта', "иглу", "хат"))


app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('!!! САМЫЙ СЛОЖНЫЙ ВАПРОС В МИРЕ !!!')




RadioGroupBox = QGroupBox('вырианты обектов')


rbtn_1 = QRadioButton('Выриант 1')
rbtn_2 = QRadioButton('Выриант 2')
rbtn_3 = QRadioButton('Выриант 3')
rbtn_4 = QRadioButton('Выриант 4')


GroupBox = QButtonGroup()
GroupBox.addButton(rbtn_1)
GroupBox.addButton(rbtn_2)
GroupBox.addButton(rbtn_3)
GroupBox.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)



AnsGruopBox = QGroupBox('результат теста')
lb_correct = QLabel('Прав ты или нет')
lb_reaule = QLabel('ответ будет тут')




layout_res = QVBoxLayout()
layout_res.addWidget(lb_reaule, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGruopBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGruopBox)




layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGruopBox.show()
    btn_OK.setText('ответить')


def show_qestion():
    RadioGroupBox.show()
    AnsGruopBox.hide()
    btn_OK.setText('ответить')
    GroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    GroupBox.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    '''функция записывает значение вапроса и ответов в соответствуйшиу веджиты,
    при этом вириант ответов распределяетса случайном образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_qestion()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def ckeck_answer():
    'покозать результат - установим передфнный текст в натпись "ресультат" и покажте'
    if answers[0].isChecked():
        show_correct('верно')
        window.score += 1
        print('Статистика\n-всего вопросов', window.total, '\n-правельных ответов', window.score)
        print('рейтинг:', (window.spore/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно')   
            print('рейтинг:', (window.spore/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-всего вопросов', window.total, '\n-правельных ответов', window.score)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.text() == 'Ответить':
        ckeck_answer()
    else:
        next_question()



window = QWidget()
window.score = 0
window.total = 0
window.setLayout(layout_card)
window.setWindowTitle('Memoru card')


btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec()