
abstract class WorkerTemplate {
    startWork() {
        console.log("Start working");
    }
    abstract doWork();

    finishWork() {
        console.log("Finish working");
    }

    execute() {
        this.startWork();
        this.doWork();
        this.finishWork();
    }
}

class HRWorker extends WorkerTemplate {
    doWork() {
        console.log("HR worker is hiring");
    }
}

class ManagerWorker extends WorkerTemplate {
    doWork() {
        console.log("Manager worker is hiring");
    }
}

class DeveloperWorker extends WorkerTemplate {
    doWork() {
        console.log("Developer worker is writing code");
    }
}

const testWorkerTemplate = () => {
    let worker: WorkerTemplate = new HRWorker();
    worker.execute();

    worker = new DeveloperWorker();
    worker.execute();

    worker = new ManagerWorker();
    worker.execute();


}

testWorkerTemplate();