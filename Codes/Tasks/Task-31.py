class product:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price
    
    def update_quantity(self,quantity):
        self.quantity=quantity

    def get_total_price(self):
        return self.price*self.quantity

    def __str__(self):
        return f'{self.name}: ₹{self.price} x {self.quantity} = ₹{self.get_total_price()}'

class shopping_cart:
    def __init__(self):
        self.cart={}

    def add_product(self,product):
        if product.name in self.cart:
            existing_product=self.cart[product.name]
            existing_product.update_quantity(existing_product.quantity+product.quantity)
        else:
            self.cart[product.name]=product

    def remove_product(self,product_name):
        if product_name in self.cart:
            del self.cart[product_name]
        else:
            print('Product not found in the cart')

    def calculate_total(self):
        total=0
        for product in self.cart.values():
            total+=product.get_total_price()
        return total
    
    def __str__(self):
        if not self.cart:
            return 'Cart is empty'
        cart_contents='\n'.join(str(product) for product in self.cart.values())
        total_price=self.calculate_total()
        return f"Shopping Cart:\n{cart_contents}\nTotal Price: ₹{total_price:.2f}"




if __name__=='__main__':
    cart=shopping_cart()

    while True:
        print("\nOptions:")
        print("1. Add a product")
        print("2. Remove a product")
        print("3. View cart")
        print("4. Calculate total price")
        print("5. Exit")

        choice=input("Enter your choice (1-5): ")

        if choice=="1":
            name=input('Enter product name: ')
            price=int(input('Enter price: '))
            quantity=int(input('Enter quantity: '))
            product=product(name,quantity,price)
            cart.add_product(product)
            print(f"Added {quantity} of {name} to the cart.")

        elif choice=="2":
            name=input('Enter product name: ')
            cart.remove_product(name)

        elif choice=="3":
            print(cart)

        elif choice=="4":
            print(f"Total Price: ₹{cart.calculate_total():}")
       
        elif choice=="5":
            break

        else:
            print('Invalid choice.')