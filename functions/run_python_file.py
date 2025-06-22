import os
import subprocess
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
    output=""
    if process.stdout:
        output+=f'STDOUT: {process.stdout}\n'
    if process.stderr:
        output+=f'STDERR: {process.stderr}\n'
    if process.returncode!=0:
        output+=f'Process exited with code {process.returncode}'
    if not (len(output)):
        output="No output produced."

    return output