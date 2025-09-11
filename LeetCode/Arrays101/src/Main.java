public class Main {
    public static void main(String[] args) {
        SquareNumbers[] squareNumbersList = new SquareNumbers[10];

        for (int i = 0; i < squareNumbersList.length; i++) {
            squareNumbersList[i] = new SquareNumbers(i);
        }

        for (SquareNumbers i : squareNumbersList) {
            System.out.println("Square:" + i.square());
        }

        ArrayInsertions[] arrayAppend = new ArrayInsertions[6];

        for (int i = 0; i < 3; i++) {
            arrayAppend[i] = new ArrayInsertions(i);
        }

        for (int i = 0; i < arrayAppend.length; i++) {
            System.out.println("Index: " + i + " contains " + arrayAppend[i]);
        }
    }

}


