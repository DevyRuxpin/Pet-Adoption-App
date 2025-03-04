"""Flask app for adopt app."""

import os
from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from config import TestConfig, DevelopmentConfig

app = Flask(__name__)

# Use TestConfig if FLASK_ENV is 'testing', otherwise use DevelopmentConfig
app.config.from_object(
    TestConfig if os.environ.get('FLASK_ENV') == 'testing' 
    else DevelopmentConfig
)

connect_db(app)

# Move db.create_all() to only run when file is executed directly
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

toolbar = DebugToolbarExtension(app)

@app.route("/")
def list_pets():
    """List all pets."""
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))

    return render_template("pet_add_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))

    return render_template("pet_edit_form.html", form=form, pet=pet)

