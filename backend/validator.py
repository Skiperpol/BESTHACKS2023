from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    print(value.size)
    limit = 1048576
    if value.size > limit:
        pass
    else:
        pass