from flask import Flask, request, render_template_string
import os
import requests

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Add this root route to serve a basic upload form
@app.route('/', methods=['GET'])
def index():
    return render_template_string('''
        <h2>Upload a file to distribute compilation</h2>
        <form action="/distribute_compile" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <input type="submit" value="Upload and Distribute">
        </form>
    ''')

@app.route('/distribute_compile', methods=['POST'])
def distribute_compile():
    file = request.files['file']
    filename = file.filename
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    peers = ["http://localhost:6001/compile", "http://localhost:6002/compile"]
    results = []
    for peer in peers:
        with open(path, 'rb') as f:
            try:
                r = requests.post(peer, files={'file': (filename, f)})
                results.append(f"Peer {peer} → {r.text}")
            except Exception as e:
                results.append(f"Peer {peer} → Error: {str(e)}")
    return "<br>".join(results)

if __name__ == '__main__':
    app.run(port=5000)
