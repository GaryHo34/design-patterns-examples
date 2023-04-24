from typing import Protocol, Optional

class WorkerTemplate(Protocol):
    def start_work(cls) -> None: 
        print("Starting work")
    
    def stop_work(cls) -> None:
        print("Stopping work")

    def do_work(cls) -> None:
        pass

    def execute(self) -> None:
        self.start_work()
        self.do_work()
        self.stop_work()
        
class HRWorker(WorkerTemplate):
    def do_work(self) -> None:
        print("HR worker is working")

class ITWorker(WorkerTemplate):
    def do_work(self) -> None:
        print("IT worker is working")

class Manager(WorkerTemplate):
    def do_work(self) -> None:
        print("Manager is working")

if __name__ == '__main__':
    work: WorkerTemplate = HRWorker()
    work.execute()

    work = ITWorker()
    work.execute()

    work = Manager()
    work.execute()