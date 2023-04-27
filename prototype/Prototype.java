import java.util.ArrayList;

public class Prototype {
    // here is a mock dataSet that will wait 5 sec to construct an object to
    // simulate a heavy I/O operation
    private class DataSet implements Cloneable {
        int id;
        ArrayList<Integer> data;

        public DataSet() {
            try {
                System.out.println("Loading data from disk...");
                Thread.sleep(5000);
                data = new ArrayList<>();
                id = 0;
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // copy constructor
        public DataSet(DataSet d) {
            this.id = d.id;
            this.data = new ArrayList<>(d.data);
        }

        @Override
        protected Object clone() {
            DataSet clone = null;
            try {
                clone = (DataSet) super.clone();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
            clone.data = new ArrayList<Integer>(this.data);
            return clone;
        }
    }

    public void testPrototype() {
        // Wait 5 sec to construct an object
        DataSet d1 = new DataSet();

        // Clone the object (vid copy constructor)
        DataSet d2 = new DataSet(d1);

        // Clone the object (vid clone method)
        DataSet d3 = (DataSet) d1.clone();

        // Test the deep copy
        d1.data.add(1);
        d2.data.add(2);
        d3.data.add(3);

        System.out.println("d1: " + d1.data);
        System.out.println("d2: " + d2.data);
        System.out.println("d3: " + d3.data);
    }

    public static void main(String[] args) {
        Prototype p = new Prototype();
        p.testPrototype();
    }
}