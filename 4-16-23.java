/*
9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

*/

class Solution {
    public boolean isPalindrome(int x) {
        
        // Integer to a string
        String s = String.valueOf(x);
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) != s.charAt(s.length()-i-1)){
                return false;
            }
        }
        return true;
        

        // Integer isn't converted to a string
        int reverse = 0;
        int temp = x;
        if(x<0){
            return false;
        }
        while(temp>0){
            int reminder = temp%10;
            reverse = 10*reverse + reminder;
            temp=temp/10;
        }
        if(x == reverse){
            return true;
        }
        return false;
    }
}
