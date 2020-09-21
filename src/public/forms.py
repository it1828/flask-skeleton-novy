import re

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField,SelectField, FloatField
from wtforms.validators import EqualTo, Email, InputRequired, Length, NumberRange

from ..data.models import User, LogUser
from ..fields import Predicate

def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)

def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)

def safe_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None


class LogUserForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')

class secti(Form):
    hodnota1 = IntegerField("vlozHodnotu1", validators=[InputRequired(message="vyzadovano")])
    hodnota2 = IntegerField("vlozHodnotu2", validators=[InputRequired(message="vyzadovano")])
class masoform(Form):
    typ=SelectField('Typ', choices=[(1, "Hovezi"), (2, "Veprove")], default=2)

class formulartest(Form):
    a = FloatField("Strana a", validators=[InputRequired(message="vyzadovano"), NumberRange(min=0.01, message="Musi byt vetsi jak 0.01")])
    b = FloatField("Strana b", validators=[InputRequired(message="vyzadovano"), NumberRange(min=0.01, message="Musi byt vetsi jak 0.01")])
    c = FloatField("Strana c", validators=[InputRequired(message="vyzadovano"),NumberRange(min=0.01, message="Musi byt vetsi jak 0.01")])

    oo=SelectField("Typ vypoctu", choices=[(1, "Obvod"), (2, "Obsah")], default=2)
    obrazec=SelectField("Obrazec", choices=[(1, "Ctverec A"), (2, "Obdelnik AB"), (3, "Trojuhelnik ABC")], default=1)