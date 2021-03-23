from django.core.exceptions import ValidationError

def longitud(value):
    if len(value) < 6:
        raise ValidationError('El nombre de usuario debe contener al menos 6 caracteres')
        return value
    elif len(value) > 12:
        raise ValidationError('El nombre de usuario debe contener maximo 12 caracteres')
        return value

    else:
        return value
def alfanumerico(value):
    if value.isalnum() == False:
        raise ValidationError('El nombre de usuario puede contener solo letras y numeros')
        return value
    else:
        return value

def validate_nombre(value):
    if len(value) == " ":
        return True

    elif " " == True :
        raise ValidationError(
            _('%(value)s Ya esta creada esta Unidad'),
            code="invalid",
            params={'value': value}, )
    else:
        return value

def validar_espacios(value):
    if value.count == '':
        raise ValidationError(
            _(' agregar cosas correctas'),
            code="invalid",
            params={'value': value}, )
    else:
        return value == True


def longitudPassword(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres')
        return value
    elif len(value) > 15:
        raise ValidationError('La contraseña debe tener maximo 15 caracteres')
        return value

    else:
        return value


def minuscula(value):
        letras_minuscula=False
        for carac in value:
            if carac.islower()==True:
                letras_minuscula=True
        if not letras_minuscula:
            raise ValidationError('La contraseña debe tener al menos una minuscula')
            return value
        else:
            return value

def mayuscula(value):
        letras_mayuscula=False
        for carac in value:
            if carac.isupper()==True:
                letras_mayuscula=True
        if not letras_mayuscula:
            raise ValidationError('La contraseña debe tener al menos una mayuscula')
            return value
        else:
            return value

def numero(value):
        num=False
        for carac in value:
            if carac.isdigit()== True:
                num=True

        if not num:
            raise ValidationError('La contraseña debe tener al menos un numero')
            return value
        else:
            return value

def espacios(value):
        if value.count(" ")> 0:
            raise ValidationError('La contraseña no puede contener espacios en blanco')
            return value
        else:
            return value


def espaciosusu(value):
    if value.count(" ") > 0:
        raise ValidationError('El usuario no puede contener espacios en blanco')
        return value
    else:
        return value

def alfanumericoPassword(value):
    if value.isalnum() == False:
        raise ValidationError('La contraseña puede contener solo letras y numeros')
        return value
    else:
        return value
