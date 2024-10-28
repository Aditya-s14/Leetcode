int removeDuplicates(int* nums, int numsSize) {
    int unique = 0;
    for(int j=1;j<numsSize;j++)
    {
        if(nums[j]!=nums[unique])
        {
            unique++;
            nums[unique]=nums[j];
        }

    }
    return unique+1;
    
}