from flask import Flask, render_template, url_for

app = Flask(__name__)

# Данные о продуктах


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products/armatura')
def armatura_page():
    return render_template('armatura.html')

@app.route('/products/katanka')
def katanka_page():
    return render_template('katanka.html')

@app.route('/products/krug')
def krug():
    return render_template('krug.html')

@app.route('/products/list')
def list_product():
    return render_template('list.html')

@app.route('/products/profile')
def profile():
    return render_template('profile.html')

@app.route('/products/ugolok')
def ugolok():
    return render_template('ugolok.html')

@app.route('/products/shveller')
def shveller():
    return render_template('shveller.html')

@app.route('/products/balka')
def balka():
    return render_template('balka.html')

@app.route('/products/vgp')
def vgp():
    return render_template('vgp.html')

@app.route('/products/elektro')
def elektro():
    return render_template('elektro.html')

@app.route('/products/grch')
def grch():
    return render_template('grch.html')

@app.route('/products/holod')
def holod():
    return render_template('holod.html')

@app.route('/products/magistralnaya')
def magistralnaya():
    return render_template('magistralnaya.html')

@app.route('/products/vchshg')
def vchshg():
    return render_template('vchshg.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)
