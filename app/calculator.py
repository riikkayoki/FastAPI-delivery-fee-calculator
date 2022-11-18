class Calculator:
    def __init__(self, cart_value, delivery_distance, amount_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.amount_of_items = amount_of_items
        self.time = time
        self.delivery_fee = 0

    # def get_total_delivery_fee(self):
    #     pass
    #     The delivery fee can never be more than 15€, including possible surcharges.

    # def get_small_order_fee(self):
    #     pass
    #     If the cart value is less than 10€,
    #     a small order surcharge is added to the delivery price.
    #     The surcharge is the difference between the cart value and 10€.
    #     For example if the cart value is 8.90€,
    #     the surcharge will be 1.10€

    # def get_delivery_fee_by_distance(self):
    #     pass
    #     A delivery fee for the first 1000 meters (=1km) is 2€.
    #     If the delivery distance is longer than that,
    #     1€ is added for every additional 500 meters,
    #     that the courier needs to travel before reaching the destination.
    #     Even if the distance would be shorter than 500 meters,
    #     the minimum fee is always 1€.

    # def get_extra_fee_if_over_four_items(self):
    #     pass

    # def get_free_delivery(self):
    #     pass
    #     The delivery is free (0€) when the cart value is equal or more than 100€.

    # def get_friday_rush_hour_fee(self):
    #     pass
    #     During the Friday rush (3 - 7 PM UTC),
    #     the delivery fee (the total fee including possible surcharges)
    #      will be multiplied by 1.1x.
