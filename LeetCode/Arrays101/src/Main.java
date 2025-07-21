public class Main {
    public static void main(String[] args) {
        SquareNumbers[] squareNumbersList = new SquareNumbers[10];

        for (int i = 0; i < squareNumbersList.length; i++) {
            squareNumbersList[i] = new SquareNumbers(i);
        }

        for (SquareNumbers i : squareNumbersList) {
            System.out.println("Square:" + i.square());
        }
    }
}


