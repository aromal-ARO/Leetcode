class Solution {
    public void moveZeroes(int[] nums) {
        if(nums.length==0){
            return;
        }

        int nonZeroindex =0 ;
        for(int i =0;i<nums.length;i++){
            if(nums[i]!=0){
                nums[nonZeroindex] = nums[i];
                nonZeroindex++;
            }
        }
        while(nonZeroindex<nums.length){
            nums[nonZeroindex] =0;
            nonZeroindex++;
        }
    }
}