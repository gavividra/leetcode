// leetcode #69

class Solution {
    public int mySqrt(int x) {
        int root = 0;
        if(x==1 || x==2){
            return 1;
        }
        for(double i=0; i<=x; i++){
            if(i*i == x){
                root = (int)(i);
                break;
            }
            else if(i*i > x){
                root = (int)(i-1);
                break;
            }
        }
        return root;
    }
}
