"""
Author: James Michelson
Purpose: To calculate if a customer is eligable for a 10% discount on either Tuesday or Wednesday by determining the day of the week and the amount sent.
"""
from datetime import datetime

DISCOUNT_RATE = 0.1
SALES_TAX_RATE = 0.06

subtotal = 0
quantity = 1


while quantity != 0:
    quantity = int(input("What is the quantity? "))
    if quantity != 0:
        price = float(input("What is the price? "))
        subtotal += price * quantity

discount = 0
sales_tax = SALES_TAX_RATE * subtotal

total = subtotal + sales_tax

day = datetime.weekday(datetime.now())

print("Order details:")
print(f"Subtotal: ${subtotal:.2f}")

if day == 1 or day == 2:
    if subtotal >= 50:
        discount = subtotal * DISCOUNT_RATE
        subtotal -= discount
        print(f"Discount: ${discount:.2f}")
    else:
        print(f"Spend {(50 - subtotal):.2f} more dollars for a 10% discount!")

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")