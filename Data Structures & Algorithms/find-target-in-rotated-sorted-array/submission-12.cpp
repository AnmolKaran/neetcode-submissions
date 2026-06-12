class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left =0;
        int right = nums.size()-1;
        while (left <= right){
            //cout << to_string(left) + " " + to_string(right)  + "\n";




            int mid = (left + right)/2;
            if (target == nums[mid]){
                return mid;
            }
            
            // cout << " " + to_string(mid);
            if (nums[right] < nums[mid]){
                if (target>= nums[left] && target< nums[mid]){
                    right = mid-1;
                }else{
                    left  = mid+1;
                }
            }

            else{
                if (target >= nums[mid ] && target <= nums[right]){
                    left = mid + 1;

                }
                else { 
                    right = mid -1;
                }
            }
        }
        return -1;
    }
};
