import java.util.Scanner;

public class FlipBitToWin {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int num;
        System.out.print("Enter number: ");
        num = scan.nextInt();
        System.out.println("Maximum number of ones can be "+flipBitToWin(num)+".");
    }

    static int flipBitToWin(int num){
        int maxLength = 0;

        int previousLength = 0;
        int currentLength = 0;

        while(num != 0){
            if ((num & 1) == 1){
                currentLength++;
            }
            else if((num & 1) == 0){
                if (maxLength < previousLength + currentLength + 1){
                    maxLength = previousLength + currentLength + 1;
                }
                previousLength = currentLength;
                currentLength = 0;
            }
            num /= 2;
        }
        maxLength = Integer.max(previousLength + currentLength + 1, maxLength);

        return maxLength;
    }
}