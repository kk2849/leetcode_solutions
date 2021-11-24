class Solution {
    public boolean isPalindrome(int x) {
        if (x<0) {
            return false;
        }
        int rev = 0;
        int copy = x;
        while(copy != 0){
            rev = rev*10+copy%10;
            copy /= 10;
        }
        if (rev == x) {
            return true;
        }
        else {
            return false;
        }
    }
}