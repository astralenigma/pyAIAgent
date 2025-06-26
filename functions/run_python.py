import os
import subprocess
from google.genai import types
def run_python_file(working_directory, file_path):
    if(not file_path.endswith(".py")):
        return f'Error: "{file_path}" is not a Python file.'
    abs_WD=os.path.abspath(working_directory)
    if(file_path.startswith("/")):
        abs_TD=os.path.abspath(file_path)
    else:
        if(file_path.startswith(".")):
            abs_TD=abs_WD
        else:
            abs_TD=os.path.join(abs_WD,file_path)
    
    if(not abs_TD.startswith(abs_WD) or file_path.startswith("../")):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if(not os.path.isfile(abs_TD)):
        return f'Error: File "{file_path}" not found'
    try:
        process =subprocess.run(["python3",abs_TD],timeout=30,capture_output=True )
    except Exception as e:
        return f"Error: executing Python file: {e}"
    output=[]
    if process.stdout:
        output.append(f'STDOUT: {process.stdout}\n')
    if process.stderr:
        output.append(f'STDERR: {process.stderr}\n') 
    if process.returncode!=0:
        output.append(f'Process exited with code {process.returncode}')
    if not (len(output)):
        output="No output produced."

    return output

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)