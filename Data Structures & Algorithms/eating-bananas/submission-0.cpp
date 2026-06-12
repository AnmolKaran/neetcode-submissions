class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());
        
        
        int lowestMid = piles.size();
        int res = high;
        while (low <= high){
            long long sum = 0;
            int mid = (low + high)/2;
            for (auto& element: piles){
                if (element % mid == 0){
                    sum += (element / mid);
                }
                else{
                    sum += (element / mid) + 1;
                    

                }

                
                

                
            }
            if (sum <= h){
                res = mid;
                high = mid -1;
            }
            else{
                low = mid + 1;
            }
            
            
        }
        return res;
    }
   
};
