import queue
import threading

class TaskManager:
    def __init__(self):
        self.tasks = queue.Queue()
        self.results = {}
    
    def add_task(self, task_id, code_file):
        """Add a compilation task"""
        self.tasks.put((task_id, code_file))
    
    def get_task(self):
        """Get a task for a client"""
        if not self.tasks.empty():
            return self.tasks.get()
        return None
    
    def store_result(self, task_id, result):
        """Store compilation results"""
        self.results[task_id] = result
