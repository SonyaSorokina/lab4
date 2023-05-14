from flask import Flask, render_template, request
app = Flask(__name__)
global fio, group, question, i
i = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        global fio, group, question, i
        fio = request.form.get('fio')
        group = request.form.get('group')
        question = request.form.get('question')
        i = i + 1
        new_zapis()
    return render_template('index.html', ans="Спасибо за ваш ответ, "+fio+"!")
def new_zapis():
    global fio, group, question, i
    with open("text.txt", "a") as file:
        file.write("Запись №" + str(i) + "\n")
        file.write("ФИО студента: " + fio + "\n")
        file.write("Группа: " + group + "\n")
        file.write("Доволен ли своими оценками? " + question + "\n")
        file.write("\n")

def start():
    app.run(debug=True)