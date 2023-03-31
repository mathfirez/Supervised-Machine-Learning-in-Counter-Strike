from awpy import DemoParser
import os
import time

# Records the start time for the execution of the script
globalStartTime = time.time()

# Lists all files from the directory
allFiles = os.listdir(os.curdir)
demoFiles = []

# First assessment of the size of the files list
initialNumOfFiles = len(allFiles)

# Excludes forom the parsing process all files that do not have .dem extension
for i in range(initialNumOfFiles):
    if allFiles[i][-4:] == '.dem':
        demoFiles.append(allFiles[i])
    else:
        pass

# Definitive size of the demo list
numOfDemos = len(demoFiles)

print("####################################")
print("Starting Batch Parser")
print("####################################")

# Starts the parsing for all .dem files in the directory
for i in range(numOfDemos):
    startTime = time.time()
    currentFileName = str(i) + "_" + demoFiles[i].replace('.dem', '')
    demo_parser = DemoParser(demofile=demoFiles[i], demo_id=currentFileName, parse_rate=128)
    data = demo_parser.parse()
    endTime = time.time()
    print("Parsing files: " + str((i+1)) + " out of " + str(numOfDemos) + " files done. Last file:" + currentFileName + " | Parsing time: " + str(endTime - startTime) + "s.")

# Records when the script execution is complete
globalEndTime = time.time()
print("Parsing complete! Total time elapsed: " + str(globalEndTime - globalStartTime) + "s.")