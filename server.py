from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def traning(prof):
    if "строитель" in prof.lower() or "инженер" in prof.lower():
        return render_template('engineer.html')
    return render_template('science.html')


if __name__ == '__main__':
    app.run()
