public class Template {

    private abstract class WorkerTemplate {
        public final void execute() {
            startWork();
            doWork();
            finishWork();
        }

        public void startWork() {
            System.out.println("Start working");
        }

        public abstract void doWork();

        public void finishWork() {
            System.out.println("Finish working");
        }

    }

    private class HRWorker extends WorkerTemplate {
        @Override
        public void doWork() {
            System.out.println("HR worker is working");
        }
    }

    private class DeveloperWorker extends WorkerTemplate {
        @Override
        public void doWork() {
            System.out.println("Developer worker is writing code");
        }
    }

    private class ManagerWorker extends WorkerTemplate {
        @Override
        public void doWork() {
            System.out.println("Manager worker is managing");
        }
    }

    public void testTemplate() {
        WorkerTemplate worker = new HRWorker();
        worker.execute();

        worker = new DeveloperWorker();
        worker.execute();

        worker = new ManagerWorker();
        worker.execute();
    }

    public static void main(String[] args) {
        Template template = new Template();
        template.testTemplate();
    }
}