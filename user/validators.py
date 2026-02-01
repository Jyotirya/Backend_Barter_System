from django.core.exceptions import ValidationError

def domain_validator(value):
    if not (value.endswith('@gmail.com') or value.endswith('@iitb.ac.in')):
        raise ValidationError('This email does not belong to IITB! Please use a valid IITB email.')