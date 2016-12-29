import zipfile

def isZip(filename):
    return zipfile.is_zipfile(filename)

def openEpubZip(filename):
    if isZip(filename):
        return zipfile.ZipFile(filename, mode = "r")

def contentExists(epub, filename):
    try:
        epub.read(filename)
        return True
    except KeyError:
        return False

def findAndReplace(inputEpub, epubName, find, replace):
    outputEpub = zipfile.ZipFile("findAndReplaced-" + epubName, mode = "w")
    index = 1
    filename = "index_split_" + str(index).zfill(3) + ".html"
    while contentExists(inputEpub, filename):
        print("Reading file " + filename)
        currentText = inputEpub.read(filename)
        currentText = currentText.replace(find, replace)
        outputEpub.writestr(filename, currentText)
        index += 1
        filename = "index_split_" + str(index).zfill(3) + ".html"
    for file in inputEpub.infolist():
        if file.filename not in outputEpub.namelist():
            inputFile = inputEpub.read(file.filename)
            outputEpub.writestr(file, inputFile)
    outputEpub.close()

epubName = "refer-to-epub-filename-here"
epubZip = openEpubZip(epubName)
findAndReplace(epubZip, epubName, "enter text to be replaced here", "and what it needs to be replaced with here")
epubZip.close()
print("ended")