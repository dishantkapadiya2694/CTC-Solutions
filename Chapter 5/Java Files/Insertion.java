import java.util.Scanner;

public class Insertion {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter N, M, i and j");
        int n = scan.nextInt();
        int m = scan.nextInt();
        int i = scan.nextInt();
        int j = scan.nextInt();
        int ans = insertion(n, m, i, j);
        System.out.println(Integer.toBinaryString(ans));
    }

    static int insertion(int n, int m, int i, int j){
        int mask = (~0 << j) + ((1 << (i - 1)) - 1);
        n = n & mask;
        m = m << (i - 1);
        return n + m;
    }
}