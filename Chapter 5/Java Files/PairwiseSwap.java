import java.util.Scanner;

public class PairwiseSwap {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number: ");
        int num = scan.nextInt();
        System.out.println(""+pairSwap(num));
    }

    static int pairSwap(int num){
        return ((num & 0xaaaaaaaa) >>> 1 | (num & 0x55555555) << 1);
    }
}