import os

for folderName, subfolders, filenames in os.walk('.'):
    #print('The current folder is ' + folderName)

    #for subfolder in subfolders:
        #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        if folderName.endswith('migrations') and filename.endswith('.py'):
            if not filename.startswith('__init__'):
                #print('FILE INSIDE ' + folderName + ': '+ folderName+'/' + filename)
                os.unlink(folderName+'/'+filename)
        if folderName.endswith('migrations/__pycache__') and filename.endswith('.pyc'):
            #print('FILE INSIDE ' + folderName + ': '+ folderName+'/' + filename)
            os.unlink(folderName+'/'+filename)