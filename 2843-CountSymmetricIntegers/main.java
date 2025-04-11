class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            // Check if the number is symmetric
            if (isSymmetric(i)) {
                count++;
            }
        }
        return count;
    }

    public boolean isSymmetric(int n) {
        int sum1 = 0;
        int sum2 = 0;
        String str = String.valueOf(n);
        int len = str.length();
        
        if (len % 2 != 0) {
            return false; 
        }

        for (int i = 0; i < len / 2; i++) {
            sum1 += str.charAt(i) - '0';
            sum2 += str.charAt(len - i - 1) - '0';
        }
        return sum1 == sum2; 
    }
}