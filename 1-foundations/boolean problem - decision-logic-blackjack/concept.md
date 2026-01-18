This problem is about deciding whether a player should hit or stay in a simplified Blackjack game using basic conditional logic.

The main challenge is handling "aces", since an ace can count as either 1 or 11. The approach used here is to first assume aces are 11, 
and then reduce them to 1 only if the total goes above 21.

After calculating the best possible player total, the decision is made using simple rules:
I should hit if the total is very low (safe)
I should stay if the total is high (risk of bust)
For mid-range totals like between 12-16, use the dealer’s visible value to decide

This exercise helped reinforce separating calculation logic (the card values) from decision logic (hit vs stay logic).
