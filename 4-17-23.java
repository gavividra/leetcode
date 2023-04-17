/*

118. Pascal's Triangle
Easy
9.7K
316
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

*/

class Solution {
    public List<List<Integer>> generate(int numRows) {
        /*
        List<List<Integer>> pascal = new List<List<Integer>>();
        if(numRows > 1){
            pascal.add([1]);
        }
        if(numRows > 2){
            pascal.add([1,1])
        }
        if(numRows > 3){
            for(int i=2; i<numRows; i++){
                List<Integer> list = new List<Integer>(1);
                List<Integer> prev = pascal[i-1];
                int index = i-1;
                while(prev[index]!=null){
                    list.add(prev[index]+prev[index-1]);
                    index += 1;
                }
            }
        }
        return pascal;
        */

        int n = numRows;

        List<List<Integer>> result = new ArrayList<>();
        List<Integer> prevList = null; // temp for prev row

        // for each row
        for (int r = 1; r <= n; r++) {
            List<Integer> list = new ArrayList<>();

            // for each col
            for (int c = 1; c <= r; c++) {
                // first and last item, print 1
                if (c == 1 || c == r) {
                    list.add(1);
                } else {
                    // for the middle items, we get from the prev row
                    list.add(prevList.get(c - 2) + prevList.get(c - 1));
                }
            }

            result.add(list);
            prevList = list;
        }


        return result;
    }
}
