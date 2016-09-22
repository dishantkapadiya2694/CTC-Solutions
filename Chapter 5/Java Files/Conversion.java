import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number 1: ");
        int num1 = scan.nextInt();
        System.out.print("Enter number 2: ");
        int num2 = scan.nextInt();
        System.out.println("Minimum number of flips required are "+ countFLips(num1, num2)+".");
    }
    
    static int countFLips(int num1, int num2){
        int count = 0;
        System.out.print(""+ (num1^num2));
        for(int i = num1 ^ num2; i != 0; i >>>= 1){
            if((i & 1) == 1)
                count++;
        }
        return count;
    }
}