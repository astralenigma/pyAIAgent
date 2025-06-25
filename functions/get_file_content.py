import os
from google.genai import types
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    abs_WD=os.path.abspath(working_directory)
    if(file_path.startswith("/")):
        abs_TD=os.path.abspath(file_path)
    else:
        if(file_path.startswith(".")):
            abs_TD=abs_WD
        else:
            abs_TD=os.path.join(abs_WD,file_path)
    
    if(not abs_TD.startswith(abs_WD) or file_path=="../"):
        return f'Error: Cannot read {file_path} as it is outside the permitted working directory'
    if(not os.path.isfile(abs_TD)):
        return f'Error: "{file_path}" is not a file'
    
    
    try:
        with open(abs_TD,"r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string)>=MAX_CHARS:
                file_content_string+=f"\n[...File {file_path} truncated at 10000 characters]"
            
    except Exception as FNFError:
        return f"Error: {FNFError}"
    return file_content_string
#print(get_file_content(".","lorem.txt"))

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of the file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read the contents from.",
            ),
        },
        required=["file_path"]
    ),
)