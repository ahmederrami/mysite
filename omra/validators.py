from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')