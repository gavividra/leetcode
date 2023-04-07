/**
leetcode #169

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

**/
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            if(dict.containsKey(nums[i])){
                dict.replace(nums[i], dict.get(nums[i])+1);
            }
            else{
                dict.put(nums[i],1);
            }
        }
        int value = nums[0];
        for(int i : dict.keySet()){
            if(dict.get(i) > dict.get(value)){
                value = i;
            }
        }
        return value;
    }
}
