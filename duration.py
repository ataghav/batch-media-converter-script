import os, sys, getopt, shutil, datetime, subprocess

def main(argv):
    rootPath = ''
    fileType = ''
    message = 'duration.py -p <root path> -t <media extension type>'
    try:
        opts, args = getopt.getopt(argv,"hp:t:",["path=","type="])
        # opts, args = getopt.getopt(argv,"hp:t:",["path=","type="])

    except getopt.GetoptError:
        print("exc")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (message)
            sys.exit()
        elif opt in ("-p", "--path"):
            rootPath = arg
        elif opt in ("-t", "--type"):
            fileType = arg
    # print ('rootPath is: "', rootPath, '"')
    # print ('fileExtension is: "', fileExtension, '"')
    calc_total_duration(rootPath, fileType)


def calc_total_duration(rootPath, fileType):
    for subDir, dirs, files in os.walk(rootPath):
        for file in files:
            fileName, fileExtension =  os.path.splitext(file)
            if fileExtension == '.' + fileType: # or fileExtension == '.mkv':
                mediaFilePath = os.path.join(subDir,file)
                command = './ffprobe -v quiet -of csv=p=0 -show_entries format=duration "' + mediaFilePath + '"'
                # result = subprocess.run(['ffprobe', '-v', 'quiet', '-of', 'csv=p=0', '-show_entries' 'format=duration', mediaFilePath], capture_output = True, text = True).stdout
                os.system(command)
                # print(command)
                # print(result)


if __name__ == "__main__":
    main(sys.argv[1:])

