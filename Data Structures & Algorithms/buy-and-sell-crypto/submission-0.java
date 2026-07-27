class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit =0;
        int profit;
        int minprice= Integer.MAX_VALUE;

        for (int i = 0; i<(prices.length);i++){
          if (prices[i]< minprice){
            minprice = prices[i];
          }
          else{
            profit = prices[i]-minprice;
            maxprofit = Math.max(maxprofit,profit);
          }
        }
    return maxprofit;


    }
}