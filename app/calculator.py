
class Calculator:
    """A class to calculate the delivery fee based on the given parameters.
    """

    def __init__(self, cart_value, delivery_distance, amount_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.amount_of_items = amount_of_items
        self.time = time
        self.delivery_fee = 2_00

    def get_total_delivery_fee(self):
        """Calculates the total delivery fee for order.

        Returns:
            int: self.delivery_fee
        """
        self.get_small_order_fee()
        self.get_delivery_fee_by_distance()
        self.get_extra_fee_if_over_four_items()
        self.get_free_delivery()
        self.get_friday_rush_hour_fee()
        self.get_maximum_delivery_fee()
        return self.delivery_fee

    def get_small_order_fee(self):
        """If the cart value is less than 1000,
            a small surcharge is added to the delivery price.
        """
        if self.cart_value < 1000:
            self.delivery_fee += 10_00 - self.cart_value

    def get_delivery_fee_by_distance(self):
        """
        A delivery fee for the first 1000 meters (=1km) is 2€.
        If the delivery distance is longer than that,
        1€ is added for every additional 500 meters
        Even if the distance would be shorter than 500 meters,
        the minimum fee is always 1€.
        """
        if self.delivery_distance > 1000:
            for index in range(1000, self.delivery_distance):
                if index % 500 == 0:
                    self.delivery_fee += 1_00

    def get_extra_fee_if_over_four_items(self):
        """If the number of items is five or more,
            an additional 50 cent surcharge is added for each item above four.
        """

        if self.amount_of_items > 4:
            for _ in range(4, self.amount_of_items):
                self.delivery_fee += 5

    def get_free_delivery(self):
        """The delivery is free (0€) when the cart value is equal or more than 100€."""

        if self.cart_value >= 1000:
            self.delivery_fee = 0

    def get_friday_rush_hour_fee(self):
        """During the Friday rush (3 - 7 PM UTC),
        the total delivery fee will be multiplied by 1.1x.
        """
        if self.time.weekday() == 4 and 15 <= self.time.hour <= 19:
            self.delivery_fee *= 1.1
            self.delivery_fee = int(self.delivery_fee)

    def get_maximum_delivery_fee(self):
        """The delivery fee can never be more than 15€, including possible surcharges
        """
        self.delivery_fee = min(self.delivery_fee, 1500)
