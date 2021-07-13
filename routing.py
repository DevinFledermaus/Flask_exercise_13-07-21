from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    if name == "Devin":
        return redirect(url_for('admin', name=name))
    else:
        return redirect(url_for('guest', name=name))


@app.route('/admin/<name>')
def admin(name):
    return "I am the admin. My name is %s" % name


@app.route('/guest/<name>')
def guest(name):
    return "I am on the guest page \n My name is %s" % name


@app.route('/payments/<int:sal>')
def payment(sal):
    if sal > 5000:
        return redirect("https://www.fnb.co.za/")
    else:
        return redirect("https://www.sahomeloans.com/")


if __name__ == '__main__':
    app.debug = True
    app.run()
