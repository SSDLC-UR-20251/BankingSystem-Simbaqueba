from _datetime import datetime
import re

import unicodedata


def normalize_input(data):
    data = (unicodedata.normalize("NFKC", data))

    return data

# valido el email
def validate_email(email):
    email = normalize_input(email)
    if email[email.find("@"):] == "@urosario.edu.co": return True

    return False


# valido la edad
def validate_dob(dob):
    if (2025 - int(dob[:4])) > 16: return True
    return False


# valido el usuario
def validate_user(user):
    if all(caracter.isalpha() or caracter == '.' for caracter in user): return True
    return False


# valido el dni
def validate_dni(dni):
    if (all(caracter.isdigit() for caracter in dni)) and (len(dni) <=10) and (dni[0] is "1"): return True

    return False


# valido la contraseña
def validate_pswd(pswd):
    pswd = str(pswd)
    cont = True
    if (len(pswd)) < 8 or (len(pswd)) > 35: cont = False

    if not (any(c.islower() for c in pswd) and any(c.isupper() for c in pswd) and any(c.isdigit() for c in pswd)): cont = False

    minicont = False
    especiales = ["#", "*", "@", "$", "%", "&", "-", "!", "+", "=", "?"]
    for i in especiales:
        if i in pswd: minicont = True
    if minicont == False: cont = False

    return cont


def validate_name(name):
    return True
