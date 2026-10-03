class Solution {

    public String encode(List<String> strs) {
        // StringBuilder result = new StringBuilder();
        String result = "";
        for (String s: strs){
            // result.append(s.length()).append("#").append(s);
            // result = result.concat(String.valueOf(s.length()));
            // result = result.concat("#");
            // result = result.concat(s);
            result += String.valueOf(s.length()) + "#" + s;
        }
        return result;
        // return result.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> result = new ArrayList<>();
        int i = 0;
        while (i < str.length()){
            int j = i;
            while(str.charAt(j) != '#'){
                j++;
            }
            int length = Integer.valueOf(str.substring(i, j));
            i = j + 1 + length;
            // String word = str.substring(j + 1, j + 1 + length);
            result.add(str.substring(j + 1, i));
            // i += j + 1 + length;
        }
        return result;
    }
}
