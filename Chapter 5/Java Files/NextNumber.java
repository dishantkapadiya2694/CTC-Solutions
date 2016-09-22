import java.util.Scanner;

public class NextNumber {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number: ");
        int num = scan.nextInt();
        nextNumber(num);
    }

    static void nextNumber(int num){
        int onesInNum = countOnes(Integer.toBinaryString(num));
        boolean found = false;
        int chance = num+1;
        while(!found){
            if (onesInNum == countOnes(Integer.toBinaryString(chance))){
                System.out.println("Number larger then "+num+" and having same number of 1s is "+chance+".");
                found = true;
            }
            else
                chance++;
        }
        chance = num - 1;
        found = false;
        while(!found && chance >= 0)
        {
            if (onesInNum == countOnes(Integer.toBinaryString(chance))){
                System.out.println("Number smaller then "+num+" and having same number of 1s is "+chance+".");
                found = true;
            }
            else
                chance--;
        }
    }

    static int countOnes(String binaryNumber){
        int count = 0;
        char[] arr = binaryNumber.toCharArray();

        for(char temp:arr){
            if(temp == '1'){
                count++;
            }
        }

        return count;
    }
}