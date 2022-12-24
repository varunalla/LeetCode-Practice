package Arrays;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

public class LC981_Time_Based_Key_Value_Store {
    public static void main(String[] args) {
        TimeMap timeMap=new TimeMap();
        timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
        System.out.println(timeMap.get("foo", 1));         // return "bar"
        System.out.println(timeMap.get("foo", 3));         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
        timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
        System.out.println(timeMap.get("foo", 4));         // return "bar2"
        System.out.println(timeMap.get("foo", 5));         // return "bar2"

        
        System.out.println("--------------------------------------");
        timeMap=new TimeMap();
        timeMap.set("love", "high", 10);  // store the key "foo" and value "bar" along with timestamp = 1.
        timeMap.set("love", "low", 20);  // store the key "foo" and value "bar" along with timestamp = 1.
        
        System.out.println(timeMap.get("love", 5));         // return "bar"
        System.out.println(timeMap.get("love", 10));         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
        System.out.println(timeMap.get("love", 15));         // return "bar2"
        System.out.println(timeMap.get("love", 20));
        System.out.println(timeMap.get("love", 25));   
     /*    int[] nums=new int[]{10,20};
        System.out.println(findLocation(nums, 5));
        System.out.println(findLocation(nums, 10));
        System.out.println(findLocation(nums, 15));
        System.out.println(findLocation(nums, 20));
        System.out.println(findLocation(nums, 25));
System.out.println("-------------------------------------------------");
         nums=new int[]{1,4};
        System.out.println(nums[findLocation(nums, 1)]);
        System.out.println(nums[findLocation(nums, 3)]);
        System.out.println(nums[findLocation(nums, 4)]);
        System.out.println(nums[findLocation(nums, 5)]);*/
    }
    public static int findLocation(int[] nums, int key){
        int min=0;
        int max=nums.length-1;
        while(min<max){
            int mid=min+(max-min)/2;
            //System.out.println("mid "+mid);
            if(nums[mid]==key){
                return mid;
            }
            if(nums[mid]<key){
                min=mid+1;
            }
            else{
                max=mid;
            }
        }
        if(min>0&&key<nums[min])
            return min-1;
        return min;
    }
}


class TimeMap {

    TreeMap<String,TreeMap<Integer,String>> cache;
    public TimeMap() {
        cache=new TreeMap<>();
    }
    

    public void set(String key, String value, int timestamp) {
        TreeMap<Integer,String> map=this.cache.getOrDefault(key,new TreeMap<>());
        map.put(timestamp,value);
        this.cache.put(key,map);
    }
    
    public String get(String key, int timestamp) {
        String result="";
        if(this.cache.containsKey(key)){
            TreeMap<Integer,String> map=this.cache.get(key);
            Integer floor=map.floorKey(timestamp);
            if(floor!=null)
                result=map.get(floor);
        }
        return result;
    }
}