# •	12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
class Payment:
    def process_payment(self):
        return "Payment processed"
class CreditCardPayment(Payment):
    def process_payment(self):
        return "Credit card payment processed"
class PayPalPayment(Payment):
    def process_payment(self):
        return "PayPal payment processed"
class BitcoinPayment(Payment):
    def process_payment(self):
        return "Bitcoin payment processed"
obj = CreditCardPayment()
print(obj.process_payment())
obj = PayPalPayment()
print(obj.process_payment())
obj = BitcoinPayment()
print(obj.process_payment())
