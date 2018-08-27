from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

class SignUpForm(FlaskForm):

      states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

      firstName = StringField("first name: ", validators=[DataRequired(message="must enter a first name"),
                                              Length(max=20)])
      lastName = StringField("last name: ", validators=[DataRequired(message="must enter a last name"),
                                                Length(max=20)])
      password = PasswordField("password: ", validators=[DataRequired(message="must enter a password"),
                                                Length(min=12, max=50, message="must be at least 12 characters")])
      password2 = PasswordField("confirm password: ", validators=[DataRequired(message="must enter a password"),
                                                Length(min=12, max=50, message="must be at least 12 characters"),
                                                EqualTo("password", message="Passwords Must Match")])
      email = StringField("email:", validators=[DataRequired(message="must enter an email address"),
                                                            Email(message="not a valid email address"),
                                                             Length(max=50)])
      address = StringField("address:", validators=[DataRequired(message="must enter an address"),
                                                   Length(max=50)])
      city = StringField("city:", validators=[DataRequired(message="must enter a city"),
                                                Length(max=50)])
      state = SelectField("state:", choices=[(i,i) for i in states])
      zipCode = IntegerField("zip code:", validators=[DataRequired(message="must enter a zip code")])
      phoneNumber = IntegerField("phone number:", validators=[DataRequired(message="must enter a phone number")])
      submit = SubmitField("submit")