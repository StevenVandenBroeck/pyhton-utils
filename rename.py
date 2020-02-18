import os

fromPath = "D:\\Temp\\1"
toPath = "D:\\Temp\\2"

filenames = os.listdir(fromPath)

i = 1

for path, subdirs, files in os.walk(fromPath):
    for fromFilename in files:
        filePath = os.path.join(path, fromFilename)
        toFileName = os.path.join(toPath, "pico00" + str(i) + ".jpg")
        os.rename(filePath, toFileName)
        print(filePath + "  -->  " + toFileName)
        i = i+1
