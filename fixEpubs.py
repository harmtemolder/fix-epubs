import epubs
import zipfile

def findAndReplace(inputEpub, epubName, find, replace):
    outputEpub = zipfile.ZipFile("findAndReplaced-" + epubName, mode = "w")
    index = 1
    filename = "index_split_" + str(index).zfill(3) + ".html"
    while epubs.contentExists(inputEpub, filename):
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

epubName = "original-Covey, Stephen R. - The 7 Habits of Highly Effective People.epub"
epubZip = epubs.open(epubName)
#findAndReplace(epubZip, epubName, "enter text to be replaced here", "and what it needs to be replaced with here")
epubZip.close()
print("ended")