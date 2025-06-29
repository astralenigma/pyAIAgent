import os
from google.genai import types
def get_files_info(working_directory, directory=None):
    abs_WD=os.path.abspath(working_directory)
    if(directory.startswith("/")):
        abs_TD=os.path.abspath(directory)
    else:
        if(directory.startswith(".")):
            abs_TD=abs_WD
        else:
            abs_TD=os.path.join(abs_WD,directory)
    
    if(not abs_TD.startswith(abs_WD) or directory=="../"):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if(not os.path.isdir(abs_TD)):
        return f'Error: "{directory}" is not a directory'
    dir_details=""
    for file in os.listdir(abs_TD):
        tfile=os.path.join(abs_TD,file)
        dir_details+=f"- {file}: file_size={os.path.getsize(tfile)} bytes, is_dir={os.path.isdir(tfile)}\n"
    return dir_details

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory.",
            ),
        },
    ),
)
