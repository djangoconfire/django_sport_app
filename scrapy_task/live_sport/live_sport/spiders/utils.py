# Strip  whitespaces
def strip_whitespace(value):
    return ' '.join(value.split())

def strip_unicode(value):
    return value.encode('ascii', 'ignore').strip()
