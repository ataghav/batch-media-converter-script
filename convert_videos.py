import os
import shutil

srcDir = '/Volumes/memory/tut/DS_Algo'
dstDir = '/Users/ataghavizad/Documents/Encode/DS_Algo'

# stream = stream()

shutil.copytree(srcDir, dstDir, ignore = shutil.ignore_patterns('*.mp4', '*.mkv'))

conversionCounter = 0

for subDir, dirs, files in os.walk(srcDir):
    for file in files:
        print (os.path.join(subDir, file))
        print ("file = " + file)
        fileName, fileExtension =  os.path.splitext(file)
        print ("name = " + fileName)
        print ("extension = " + fileExtension)
        if fileExtension == '.mp4' or fileExtension == '.mkv':
            inputFilePath = os.path.join(subDir,file)
            outputFilePath = inputFilePath.replace(srcDir,dstDir)
            command = './ffmpeg -i "' + inputFilePath + '" -vf scale=-1:720 -c:v libx264 -crf 18 -preset veryslow -c:a copy "' + outputFilePath + '"'
            os.system(command)
            conversionCounter = conversionCounter + 1

print('In general ' + str(conversionCounter) + ' video files have been converted')