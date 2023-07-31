public class SingleDimensionArray {
  int arr[] = null;

  public SingleDimensionArray(int sizeOfArray) {
    arr = new int[sizeOfArray];
    for (int i=0; i<arr.length; i++) {
      arr[i] = Integer.MIN_VALUE;
    }
  }

  public void insert(int location, int valueToBeInserted) {
    try {
        if (arr[location] == Integer.MIN_VALUE) {
            arr[location] = valueToBeInserted;
            System.out.println("Successfully inserted");
          } else {
            System.out.println("This cell is already occupied");
          }
       } catch (ArrayIndexOutOfBoundsException e) {
         System.out.println("Invalid index to access array!");
      }
  }


  // Array Traversal

  public void traverseArray() {
    try {
        for (int i = 0; i < arr.length; i++) {
          System.out.print(arr[i] + " ");
      }
    } catch (Exception e) {
      System.out.println("Array no longer exists!");
    }

  }

  //Search for an element in the given Array
	public void searchInArray(int valueToSearch) {
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] == valueToSearch) {
        System.out.println("Value is found at the index of " + i);
        return;
      }
    }
    System.out.println(valueToSearch + " is not found");
  }

  // Delete value from Array
  public void deleteValue(int valueToDeleteIndex) {
    try {
      arr[valueToDeleteIndex] = Integer.MIN_VALUE;
      System.out.println("The value has been deleted successfully");

    } catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("The value that is provided is not in the range of array");

    }
  }

}
