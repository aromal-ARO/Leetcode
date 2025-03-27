class Solution {
    public int maxArea(int[] height) {
        int Max_Area =0;
        int left =0;
        int right = height.length -1;

        while(left < right){
                Max_Area = Math.max(Max_Area,(right-left)*Math.min(height[left],height[right]));
            if(height[left]<height[right]){
                left++;
            }
            else{
                right--;
            }

        }

        return Max_Area;
        
    }
}