# server/api.py
from flask import Flask, request, jsonify
from job_queue import JobQueue

app = Flask(__name__)
job_queue = JobQueue()

@app.route("/submit", methods=["POST"])
def submit():
    source = request.json.get("code")
    job_id = job_queue.add_job(source)
    return jsonify({"job_id": job_id})

@app.route("/result/<job_id>")
def result(job_id):
    return jsonify({
        "result": job_queue.get_result(job_id)
    })

if __name__ == "__main__":
    app.run(port=6000)
