import java.util.Scanner;

public class BinaryToString {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the decimal number: ");
        double num = scan.nextDouble();
        System.out.println("."+binaryToString(num));
    }

    static String binaryToString(double num){
        String ans = "";

        while(num != 0.0){
            double temp = num * 2;
            int wholePart = (int)temp;
            ans = ans.concat(Integer.toString(wholePart));
            num = temp - wholePart;
        }

        if (ans.length() > 32)
            ans = "ERROR";
        return ans;
    }
}