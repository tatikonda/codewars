def duty_free(price, discount, holiday_cost):
    discount_saved = price * (discount/100)
    return int(holiday_cost / discount_saved)

print(duty_free(17, 10, 500))