from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-it'  # غيّر المفتاح ده

# كلمة السر الصحيحة
CORRECT_PASSWORD = '143'

# ============ الصفحات العامة ============

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/journey')
def journey():
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))
    return render_template('journey.html')

@app.route('/message')
def message():
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))
    return render_template('message.html')


# ============ نظام الدخول ============

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == CORRECT_PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))  # هنا عدّلنا المسافة
        else:
            return render_template('login.html', error='كلمة السر غير صحيحة ❌')

    # لو المستخدم بالفعل داخل، يروح مباشرة
    if session.get('logged_in'):
        return redirect(url_for('journey'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login_page'))


# ============ تشغيل التطبيق ============
if __name__ == "__main__":
    app.run(debug=True)
