import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Idee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100), nullable=False)
    beschreibung = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Idee {self.titel}>'


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titel = request.form.get('titel', '').strip()
        beschreibung = request.form.get('beschreibung', '').strip()
        if titel and beschreibung:
            neue_idee = Idee(titel=titel, beschreibung=beschreibung)
            db.session.add(neue_idee)
            db.session.commit()
        return redirect(url_for('index'))

    ideen = Idee.query.order_by(Idee.id.desc()).all()
    return render_template('index.html', ideen=ideen)


@app.route('/loeschen/<int:id>', methods=['POST'])
def loeschen(id):
    idee = Idee.query.get_or_404(id)
    db.session.delete(idee)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)