import os
from useeiopy.common import requiredModelFileEndings,log

def look_for_model_files(modelname,modelpath):
    log.info("Checking for presence of all required model files...")

    required_files = []
    for f in requiredModelFileEndings:
        required_file = modelname + f
        required_files.append(required_file)

    folder_contents = []
    if os.path.exists(modelpath):
        folder_contents = os.listdir(modelpath)
        missing_files= []
        for f in required_files:
            if f not in folder_contents:
                log.error("Missing " + f)
                missing_files.append(f)

        if len(missing_files)>0:
                log.error("If not already present, you must manually add or add with"
                          " useeior the following files"
                          " to the Model Builds/" + modelname + " folder before proceeding:\n"
                          +  str(missing_files))
                return -2
        else:
            return 0
    else:
        log.error("Required model folder is missing:" + modelpath)
        return -2
