from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self,card_number,card_holder):
        self.card_number=card_number
        self.card_holder=card_holder

    def processPayment(self, amount):
        print(f'Processing payment of ₹{amount} using credit card {self.card_number} of {self.card_holder}')
    
class PayPalPayment(PaymentMethod):
    def __init__(self,email):
        self.email=email

    def processPayment(self,amount):
        print(f'Processing payment of ₹{amount} using PayPal account {self.email}')

def process_user_payment(payment_method,amount):
    payment_method.processPayment(amount)


print("Choose a payment method:")
print("1. Credit Card")
print("2. PayPal")
choice=int(input("Enter your choice (1 or 2): "))

amount=float(input('Enter the amount to be paid: '))

if choice==1:
    card_number=input('Enter the card number: ')
    card_holder=input('Enter the card holder name: ')
    payment_method=CreditCardPayment(card_number,card_holder)

elif choice==2:
    email=input('Enter the email address: ')
    payment_method=PayPalPayment(email)

else:
    print('Invalid choice')
    exit()


process_user_payment(payment_method, amount)