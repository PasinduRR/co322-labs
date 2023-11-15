/**
 * Simple sorting algorithms and their performance 
 * Reg: E/19/310
 *
 */

public class Sort {

    //create an array of given size and populate it with random data  
    static int [] create_rand_data(int size_of_array) {
        int [] data = new int[size_of_array];
        int i;
        for(i=0; i < data.length; i++)
            data[i] = (int)(Math.random() * 100);
        return data;
    }

    //create an array of given size and populate it with worst data arrangement 
    static int [] create_worst_data(int size_of_array) {
        int [] data = new int[size_of_array];
        int i;
        for(i=0; i < data.length; i++)
            data[i] = data.length - i;
        return data;
    }

    //create an array of given size and populate it with best data arrangement 
    static int [] create_best_data(int size_of_array) {
        int [] data = new int[size_of_array];
        int i;
        for(i=0; i < data.length; i++)
            data[i] = i;
        return data;
    }

    // function to swap. Would be useful since all need this 
    static void swap(int []d, int i, int j) {
        int tmp = d[i];
        d[i] = d[j];
        d[j] = tmp;
    }

    // check if the soring worked on the array 
    static boolean isSorted(int [] data) {
        int i;
        for(i=1; i < data.length; i++)
            if(data[i] < data[i-1]) break;
        return (i == data.length);
    }

    // If you want just display the array as well :) 
    static void display(int []data) {
        System.out.println("=======");
        for(int i=0; i < data.length; i++)
            System.out.print(data[i] + "  ");
        System.out.println("\n=======");
    }


    /**********************************************************
     *     Implementation of sorting algorithms               *
     *********************************************************/
    static void bubble_sort(int [] data)  {
        // Implement
        int n = data.length;

        for(int i = 0; i<n-1; i++){
            if(isSorted(data)){
                break;
            }
            for(int j = 0; j<n-1; j++)
                if (data[j]>data[j+1]) {
                    swap(data, j, j+1);
            }
        }
    }

    static void selection_sort(int [] data) {
        // Implement
        int n = data.length;
        for(int i = 0; i<n-1; i++){
            int minIndex = i;
            if (isSorted(data)) {
                break;
            }
            for(int j = i+1; j<n; j++){
                if(data[j] < data[minIndex]){
                    minIndex = j;
                }
            }
            swap(data, i, minIndex);
        }
    }

    static void insertion_sort(int [] data) {
        // Implement
        int n = data.length;
        int value;
        int position;

        for (int i = 0; i < n; i++) {
            value = data[i];
            position = i;

            while (position > 0 && data[position-1] > value) {
                swap(data, position, position-1);
                position -= 1;
            }
        }
    }
    
    public static void main(String [] args) {
        // create arrays of different size populate with data
        // measure the time taken by different algorithms to
        // sort the array.
        // Think about effects of caches, other apps running etc.

        int size = 20;

        int [] dataSet = create_rand_data(size);
        int [] dataSetNew = {0,  80,  66,  22,  64,  6,  50,  3,  32,  20,  63,  60,  13,0,22,-1};
        int [] bestDataSet = create_best_data(size);
        int [] worstDataSet = create_worst_data(size);

        display(dataSet);
        long startTime = System.currentTimeMillis();
        insertion_sort(dataSet);
        long endTime = System.currentTimeMillis();
        long runTime = endTime - startTime;
        display(dataSet);
        System.out.println("Runtime in Selection Sort: " +runTime +" ms");
        
    }
}