class Solution {
    public long numberOfPowerfulInt(long start, long finish, int limit, String s) {
        return countPowerfulIntegers(finish, limit,s) - countPowerfulIntegers(start - 1, limit,s);

    }
   private long countPowerfulIntegers(long chakraCap, int chakraLimit, String clanSymbol){
        String chakraFlow = Long.toString(chakraCap);
        int prefixLenght = chakraFlow.length() - clanSymbol.length();
        // if the chakra flow is too short to even hold the clan symbol - mission fails
        if(prefixLenght < 0){
            return 0;
        }
        long[][] rasenganScroll = new long[prefixLenght + 1][2];
        rasenganScroll[prefixLenght][0] = 1; //not bound the chakraCap
        rasenganScroll[prefixLenght][1] = chakraFlow.substring(prefixLenght).compareTo(clanSymbol) >= 0 ? 1 : 0; //bound the chakraCap

        for (int i = prefixLenght - 1; i >= 0; i--) {
            int currentChakra = chakraFlow.charAt(i) - '0';
            //if not tight to chakraCap
            rasenganScroll[i][0] = (chakraLimit + 1) * rasenganScroll[i+1][0];
            //if we are still in chakraCap, be careful
            if (currentChakra <= chakraLimit){
                rasenganScroll[i][1] = (long) currentChakra * rasenganScroll[i+1][0]+ rasenganScroll[i + 1][1];
            } else{
                rasenganScroll[i][1] = (long) (chakraLimit + 1) * rasenganScroll[i + 1][0];
            }
        }
        return rasenganScroll[0][1];
}




}   