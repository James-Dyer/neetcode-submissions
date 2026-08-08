func maxProfit(prices []int) int {
	var buy int
    var res int

	for sell := 0; sell < len(prices); sell++ {
        if prices[buy] < prices[sell] {
            profit := prices[sell] - prices[buy]
            res = max(res, profit)
        } else {
            buy = sell
        }
    }

    return res
		
}
