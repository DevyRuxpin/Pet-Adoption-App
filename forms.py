"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired(message="Pet name cannot be blank")],
    )

    species = SelectField(
        "Species",
        choices=[
            ("cat", "Cat"),
            ("dog", "Dog"),
            ("porcupine", "Porcupine")
        ],
        validators=[InputRequired(message="Please select a species")]
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Please provide a valid URL")],
    )

    age = IntegerField(
        "Age",
        validators=[
            Optional(),
            NumberRange(
                min=0,
                max=30,
                message="Age must be between 0 and 30"
            )
        ],
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
            Length(
                min=10,
                message="Notes must be at least 10 characters long"
            )
        ],
    )

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Please provide a valid URL")],
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            Optional(),
            Length(
                min=10,
                message="Notes must be at least 10 characters long"
            )
        ],
    )

    available = BooleanField("Available?")
