class Calculator:
    def __init__(self, cart_value, delivery_distance, amount_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.amount_of_items = amount_of_items
        self.time = time
        self.delivery_fee = 0

    def get_small_order_fee(self):
        """If the cart value is less than 1000,
            a small surcharge is added to the delivery price.

        Returns:
            True: if cart value is less than 1000
            False: if cart value is greater than 1000.
        """
        if self.cart_value < 1000:
            self.delivery_fee += 1000 - self.cart_value
            return True
        return False

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
