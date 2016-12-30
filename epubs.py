import zipfile

def isZip(filename):
    return zipfile.is_zipfile(filename)

def open(filename):
    if isZip(filename):
        return zipfile.ZipFile(filename, mode = "r")

def contentExists(epub, filename):
    try:
        epub.read(filename)
        return True
    except KeyError:
        return False
