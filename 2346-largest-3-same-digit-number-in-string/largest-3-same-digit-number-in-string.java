class Solution {
    public String largestGoodInteger(String num) {
        String result = "";

        for(int i=0;i+2<num.length();i++)
        {
            char c = num.charAt(i);
            if(c==num.charAt(i+1) && c==num.charAt(i+2))
            {
                String candidate = num.substring(i,i+3);
                if(candidate.compareTo(result)>0)
                {
                    result = candidate;
                }
            }
        }
        return result;
    }
}