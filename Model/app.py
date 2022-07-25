from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'I will Clear Amazon InterView, Working Real Time'


@app.route('/success/<int:marks>')
def success(score):
    return 'You have Passed in the Examination '+str(score)


@app.route('/moderate/<int:marks>')
def moderate(marks):
    return 'You have scores moderate in the Examination i.e '+str(marks)


@app.route('/results/<int:marks>')
def InterView(marks):

    if marks < 80:
        return 'Next time You are Definately Gonna Crack MAANG'
    else:
        return redirect(url_for(success, score=marks))


if __name__ == '__main__':
    app.run(debug=True)
