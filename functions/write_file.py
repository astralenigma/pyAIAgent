import os
def write_file(working_directory, file_path, content):
    abs_WD=os.path.abspath(working_directory)
    if(file_path.startswith("/")):
        abs_TD=os.path.abspath(file_path)
    else:
        if(file_path.startswith(".")):
            abs_TD=abs_WD
        else:
            abs_TD=os.path.join(abs_WD,file_path)
    
    if(not abs_TD.startswith(abs_WD) or file_path=="../"):
        return f'Error: Cannot list {file_path} as it is outside the permitted working directory'
    try:
        if(not os.path.exists(os.path.dirname(abs_TD))):
            os.makedirs(os.path.dirname(abs_TD),exist_ok=True)
        with open(abs_TD, "w+") as f:
            f.write(content)
    except Exception as error:
        return f'Error: {error}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'