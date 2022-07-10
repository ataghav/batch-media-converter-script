import os, sys, getopt, shutil, datetime

def main(argv):
    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
    # print ('Input file is: "', inputFile, '"')
    # print ('Output file is: "', outputFile, '"')
    copy_with_converted_videos(inputFile, outputFile)

def copy_with_converted_videos(srcDir, dstDir):
    shutil.copytree(srcDir, dstDir, ignore = shutil.ignore_patterns('*.mp4', '*.mkv'))

    startTime = datetime.datetime.now()
    conversionCounter = 0

    for subDir, dirs, files in os.walk(srcDir):
        for file in files:
            fileName, fileExtension =  os.path.splitext(file)
            if fileExtension == '.mp4' or fileExtension == '.mkv':
                inputFilePath = os.path.join(subDir,file)
                outputFilePath = inputFilePath.replace(srcDir,dstDir)
                command = './ffmpeg -i "' + inputFilePath + '" -vf scale=-1:720 -c:v libx264 -crf 18 -preset veryslow -c:a copy "' + outputFilePath + '"'
                os.system(command)
                conversionCounter = conversionCounter + 1

    finishTime = datetime.datetime.now()
    duration = finishTime - startTime
    print('In general ' + str(conversionCounter) + ' video files have been reencoded within ' + str(duration.seconds) + ' seconds')

if __name__ == "__main__":
    main(sys.argv[1:])