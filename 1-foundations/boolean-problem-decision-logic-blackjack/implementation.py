def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    # calculate best possible total firstly
    total = player_total + player_low_aces + player_high_aces * 11

    # I decrease the ace value from high to low only based on total value, so using while loop
    while total > 21 and player_high_aces > 0:
        total -= 10
        player_high_aces -= 1

    # decision rules using if's
    if total <= 11:  #this is done if total very less, even if I add 10 it will be 21
        return True
    if total >= 17: #this is done if total is greater than the dealer's range, so staying to avoid risk
        return False
    if dealer_total >= 7: #this is done if total between 12 - 17, and dealer has above 7, so dealer may win anytime, so taking risk of hit
        return True

    return False
