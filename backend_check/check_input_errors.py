from pyisemail import is_email


def user_input_errors(name, lastname, email, movil):
    if not name or not name.isalpha():
        return f'El campo nombre es incorrecto'

    if not lastname or not lastname.isalpha():
        return f'El campo apellido es incorrecto'

    if not movil or not movil.startswith('09') or not len(movil) == 10:
        return f'El numero de celular es incorrecto'

    if not email or not is_email(email, check_dns=True):
        return f'El campo email es incorrecto'

    return None