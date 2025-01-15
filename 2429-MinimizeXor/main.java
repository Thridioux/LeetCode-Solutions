class Solution {
    public int minimizeXor(int num1, int num2) {
        int count = Integer.bitCount(num2); // Number of set bits needed

        int res = 0;
        // Retain set bits of num1 from highest to lowest, as long as count > 0
        for (int i = 31; i >= 0 && count > 0; i--) {
            if ((num1 & (1 << i)) != 0) { // If bit i is set in num1
                count--; // Decrease the count of needed set bits
                res |= (1 << i); // Set the same bit in res
            }
        }

        // Set additional bits from lowest to highest until count == 0
        for (int i = 0; i < 32 && count > 0; i++) {
            if ((res & (1 << i)) == 0) { // If bit i is not already set in res
                count--; // Decrease the count of needed set bits
                res |= (1 << i); // Set the bit in res
            }
        }

        return res;
    }
}
