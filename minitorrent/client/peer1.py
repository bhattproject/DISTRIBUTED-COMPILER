from flask import Flask, request
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'peer1_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Full path to your g++ executable - update if needed
compiler = r"C:\Program Files (x86)\Dev-Cpp\MinGW64\bin\g++.exe"

@app.route('/compile', methods=['POST'])
def compile_file():
    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        output_file = os.path.splitext(filepath)[0] + ".exe"
        compile_cmd = f'"{compiler}" "{filepath}" -o "{output_file}"'
        result = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return f"Compilation successful! Executable: {output_file}"
        else:
            return f"Compilation failed:\n{result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(port=6001)
