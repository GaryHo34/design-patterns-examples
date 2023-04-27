# Prototype Pattern

Prototype Pattern is a creational design pattern that lets you copy existing objects instead of making new ones and customize them accordingly. Prototype is useful when the cost of creating a new object is expensive or complicated. For example, a data list needs to frequently read data from different sources, such as a database, a file, or a network. We can use the prototype pattern to create a prototype object and clone it to get a new object with the data we want.

In java, a class implements the `Cloneable` interface to indicate to the `Object.clone()` method that it is legal for that method to make a field-for-field copy of instances of that class.

```java

public class DataList implements Cloneable {
    private List<String> data = new ArrayList<>();

    public DataList() {
        loadData();
    }

    public void loadData() {
        // load data from database, file or network
    }

    public List<String> getData() {
        return data;
    }

    @Override
    public DataList clone() throws CloneNotSupportedException {
        DataList clone = (DataList) super.clone();
        return clone;
    }
}
```

Note that the `clone()` method is a shallow copy, which means that the object itself is cloned, but the reference to the object is not cloned. If the object contains a reference to another object, the reference will be copied, but the object it refers to will not be copied. If you want to do a deep copy, you need to clone the object it refers to.

```java
public class DataList implements Cloneable {
    private List<String> data = new ArrayList<>();

    public DataList() {
        loadData();
    }

    public void loadData() {
        // load data from database, file or network
    }

    public List<String> getData() {
        return data;
    }

    @Override
    public DataList clone() throws CloneNotSupportedException {
        DataList clone = (DataList) super.clone();
        clone.data = new ArrayList<>(this.data);
        return clone;
    }
}
```

Copy construtors are a good alternative to the prototype pattern. The copy constructor is a special constructor that takes an object of the same class as a parameter and copies the values of all its fields to the new object.