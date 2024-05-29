from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# towns = [
#     {"name": "Sample Town", "date": "2001-01-01", "id": 0},
#     {"name": "Another sample Town", "date": "2001-01-01", "id": 1},
#     {"name": "Last sample Town", "date": "2001-01-01", "id": 2}
# ]


class Town(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    date = db.Column(db.String)
        
    def __repr__(self):
        return f'<Town {self.id} / {self.date}> {self.name}'


@app.route("/")
def index():
    towns = Town.query.all()
    print(towns)
    return render_template("index.html", list=towns)


@app.route("/add", methods=["POST"])
def add():
    name = request.form['name']
    date = request.form['date']
    data = {"name": name, "date": date}
    town = Town(**data)
    db.session.add(town)
    db.session.commit()
    #towns.append({"name": name, "date": date, "done": False})
    return redirect(url_for("index"))
    
    
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    #town = towns[index]
    town = Town.query.get(index+1)
    if request.method == "POST":
        town.name = request.form["name"]
        town.date = request.form["date"]
        db.session.commit()
        # town['name'] = request.form["name"]
        # town['date'] = request.form["date"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", town=town, index=index)


@app.route("/delete/<int:index>", methods=["GET"])
def delete(index):
    #del towns[index]
    count = Town.query.filter(Town.id == index+1).delete()
    if count:
        print("Deleted")
    db.session.commit()
    return redirect(url_for("index"))
    
        
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)