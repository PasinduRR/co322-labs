import java.util.Scanner;

public class LCS {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int p = scanner.nextInt();
        int q = scanner.nextInt();

        String[] l = new String[p];
        String[] m = new String[q];

        for (int i = 0; i < p; i++) {
            l[i] = scanner.next();
        }

        for (int i = 0; i < q; i++) {
            m[i] = scanner.next();
        }

        int[][] dpArray = new int[p + 1][q + 1];

        int x = lcs(l, m, p, q, dpArray);
        String[] lcs = new String[x];

        int i = p;
        int j = q;
        int index = x - 1;

        while (i > 0 && j > 0) {
            if (l[i - 1].equals(m[j - 1])) {
                lcs[index] = l[i - 1];
                index--;
                i--;
                j--;
            } else if (dpArray[i][j - 1] > dpArray[i - 1][j]) {
                j--;
            } else {
                i--;
            }
        }

        for (int k = 0; k < x; k++) {
            System.out.print(lcs[k] + " ");
        }

        scanner.close();
    }

    private static int lcs(String[] array1, String[] array2, int m, int n, int[][] dpArray) {
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (array1[i - 1].equals(array2[j - 1])) {
                    dpArray[i][j] = 1 + dpArray[i - 1][j - 1];
                } else {
                    dpArray[i][j] = Math.max(dpArray[i - 1][j], dpArray[i][j - 1]);
                }
            }
        }

        return dpArray[m][n];
    }
}
