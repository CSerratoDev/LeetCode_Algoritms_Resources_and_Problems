public class ArrayInsertions {
    public int number;
    public ArrayInsertions(int number) { this.number = number; }

    //get elements
    @Override
    public String toString() {
        return String.valueOf(number);
    }

    public void duplicateZeros(int[] arr) {
        for(int i = 0; i < arr.length - 1; i++){
            if(arr[i] == 0){
                for(int j = arr.length - 1; j > i; j--){
                    arr[j] = arr[j - 1];
                }
                arr[i] = 0;
                i++;
            }
        }
    }
}
