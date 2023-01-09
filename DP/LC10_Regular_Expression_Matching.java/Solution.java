class Solution {
    public boolean isMatch(String s, String p) {
        return dfs(s,p,0,0);
    }
    public boolean dfs(String s, String p, int i, int j){
        if(i>=s.length()&&j>=p.length())
            return true;
        
        if(j>=p.length())
            return false;

        boolean smatch=i<s.length()&&(s.charAt(i)==p.charAt(j)||p.charAt(j)=='.');
    
        if (j+1<p.length()&&p.charAt(j+1)=='*'){
            return dfs(s,p,i,j+2) || (smatch&&dfs(s,p,i+1,j));
        }
        if(smatch)
            return dfs(s,p,i+1,j+1);

        return false;
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        System.out.println(sol.isMatch("ab", ".*"));
        System.out.println(sol.isMatch("aa", "a"));
        System.out.println(sol.isMatch("aa", "a*"));
    }
}