# server/worker_monitor.py
import time

class WorkerMonitor:
    def __init__(self):
        self.workers = {}

    def heartbeat(self, worker_id):
        self.workers[worker_id] = time.time()

    def get_active_workers(self, timeout=10):
        now = time.time()
        return {
            wid: t for wid, t in self.workers.items()
            if now - t < timeout
        }
