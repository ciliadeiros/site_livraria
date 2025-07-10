from flask import Flask, render_template #, request, redirect, url_for, session, make_response, flash
# from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
#cria o app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Roda o app
if __name__ == '__main__':
    app.run(debug=True)