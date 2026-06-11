class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int top = 0; 
        int bot = matrix.size()-1;
        int row = -1;

        while (top <=bot){
            int mid = (top + bot)/2;
            if (matrix[mid][0] == target) return true;
            if (matrix[mid][0] < target) { row = mid; top = mid + 1; }
            else bot = mid - 1;
        }
        if (row ==-1){return false;}
        int left = 0;
        int right = matrix[0].size()-1;
        while (left <= right){
            int mid = (left + right)/2;
            if (matrix[row][mid] == target){
                return true;
            }
            if (matrix[row][mid]< target){
                left = mid+1;
            }
            else if (matrix[row][mid]> target){
                right = mid-1;
            }
        }
        return false;
    }
};
