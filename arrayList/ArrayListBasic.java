package arrayList;

import java.util.ArrayList;

public class ArrayListBasic {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        System.out.println(arr);
        arr.add(1, 5);
        System.out.println(arr);
        arr.remove(1);
        System.out.println(arr);
        System.out.println(arr.get(1));
        System.out.println(arr.size());
        System.out.println(arr.contains(3));
        System.out.println(arr.indexOf(3));
        System.out.println(arr.isEmpty());
        arr.clear();
        System.out.println(arr);
        System.out.println(arr.isEmpty());
        ArrayList<Object> arr2 = new ArrayList<>();
        arr2.add(1);
        arr2.add("Hello");
        arr2.add(3.14);
        System.out.println(arr2);
    }   
}
