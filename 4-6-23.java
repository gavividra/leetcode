// leetcode #169

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
