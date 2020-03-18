from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def traning(prof):
    return render_template('science.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list.html', list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    return render_template('answer.html', slovar={'title': 'анкета',
                                                  'surname': 'Wathy',
                                                  'name': 'Mark',
                                                  'education': 'выше среднего',
                                                  'profession': 'штурман марсохоад',
                                                  'sex': 'male',
                                                  'motivation': 'Всегда мечтал застрять на Марсе!',
                                                  'ready': 'True'})


if __name__ == '__main__':
    app.run()
