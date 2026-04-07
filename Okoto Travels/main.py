from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, String, Float


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# DEFINE TRAVEL PACKAGE MODEL
class Package(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    destination: Mapped[str] = mapped_column(String(250), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    image_url: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    all_packages = db.session.execute(db.select(Package)).scalars().all()
    return render_template("index.html", packages=all_packages)

@app.route("/add_dummy")
def add_dummy():
    db.session.query(Package).delete()
    db.session.commit()
    p1 = Package(
        destination="Santorini, Greece",
        price=2500.00,
        description="White-washed walls and deep blue seas. The ultimate romantic getaway.",
        image_url="https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?q=80&w=800"
    )
    p2 = Package(
        destination="Bali, Indonesia",
        price=1800.00,
        description="Explore tropical jungles, ancient temples, and serene beaches.",
        image_url="https://images.unsplash.com/photo-1537996194471-e657df975ab4?q=80&w=800"
    )
    p3 = Package(
        destination="Tokyo, Japan",
        price=3200.00,
        description="Experience the perfect blend of neon future and ancient tradition.",
        image_url="https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?q=80&w=800"
    )

    db.session.add_all([p1, p2, p3])
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add_package", methods=["GET", "POST"])
def add_package():
    if request.method == "POST":
        new_package = Package(
            destination=request.form.get("destination"),
            price=float(request.form.get("price")),
            description=request.form.get("description"),
            image_url=request.form.get("image_url")
        )
        db.session.add(new_package)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/delete")
def delete():
    db.session.query(Package).delete()
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

