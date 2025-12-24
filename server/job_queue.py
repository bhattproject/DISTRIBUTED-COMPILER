# server/job_queue.py
import queue
import uuid

class JobQueue:
    def __init__(self):
        self.jobs = queue.Queue()
        self.results = {}

    def add_job(self, source_code):
        job_id = str(uuid.uuid4())
        self.jobs.put((job_id, source_code))
        return job_id

    def get_job(self):
        if self.jobs.empty():
            return None
        return self.jobs.get()

    def save_result(self, job_id, output):
        self.results[job_id] = output

    def get_result(self, job_id):
        return self.results.get(job_id, "PENDING")
