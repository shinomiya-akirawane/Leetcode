def maxProfit(prices: list[int]) -> int:
    s = [prices[0]]
    top = 0
    maxIncome = 0
    for price in prices[1:]:
        if len(s) == 0:
            s.append(price)
            top += 1
        if price >= s[top]:
            top += 1
            s.append(price)
            maxIncome = price - s[0]
        else:
            while s[top] > price and top >= 0:
                buy = s[0]
                curr = s.pop(top)
                maxIncome = max(maxIncome,curr-buy)
                top -= 1
                if top == -1:
                    break
            s.append(price)
            top += 1
    return maxIncome

maxProfit([3,2,6,5,0,3])