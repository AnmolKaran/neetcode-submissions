class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> data;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        
        // bool satisfied = false;
        // for (auto& val : data[key]){
        //     if (val[0] == timestamp){
        //         val[1] = value;
        //         return;
        //     }
            
        // }
        data[key].push_back({timestamp, value});
        return; 
        
    }
    
    string get(string key, int timestamp) {
        vector<pair<int,string>> keyData = data[key];
        if (keyData.size() == 0 || keyData[0].first > timestamp){
            return "";
        }
        int l = 0;
        int r = keyData.size()-1;
        
        while (l < r){
            int mid = (l+ r+1)/2;
            if (keyData[mid].first == timestamp){
                return keyData[mid].second;
            }
            if (keyData[mid].first < timestamp){
                l = mid ;
            }
            else{
                r = mid-1;
            }
        
        }

        return keyData[l].second;
        
        
        
    }
};
