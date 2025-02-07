import sqlite3
import random
import datetime


class OrderController:
    def __init__(self, db_connection):
        self.db_connection = db_connection  # Injected DB Connection

    def process_order(self, user_id, restaurant_id, items, payment_type, delivery_address, special_requests):
        # Validate inputs (primitive obsession everywhere)
        if not isinstance(user_id, int) or not isinstance(restaurant_id, int) or not isinstance(items, list) or not isinstance(payment_type, str):
            raise ValueError("Invalid input types")

        if len(items) == 0:
            return {"status": "error", "message": "No items in order"}

        # Fetch user details
        cursor = self.db_connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        user = cursor.fetchone()
        if not user:
            return {"status": "error", "message": "User not found"}

        # Fetch restaurant details
        cursor.execute(f"SELECT * FROM restaurants WHERE id = {restaurant_id}")
        restaurant = cursor.fetchone()
        if not restaurant:
            return {"status": "error", "message": "Restaurant not found"}

        # Check restaurant opening hours (we assume an awful date format)
        current_hour = datetime.datetime.now().hour
        open_hour = int(restaurant[3].split('-')[0])
        close_hour = int(restaurant[3].split('-')[1])

        if current_hour < open_hour or current_hour > close_hour:
            return {"status": "error", "message": "Restaurant is closed"}

        # Check if user is blacklisted (terrible security risk)
        cursor.execute(f"SELECT * FROM blacklist WHERE user_id = {user_id}")
        if cursor.fetchone():
            return {"status": "error", "message": "User is blacklisted"}

        # Special offer: If ordering exactly 3 burgers, give a 10% discount
        discount = 0
        burger_count = sum(1 for item in items if "burger" in item.lower())
        if burger_count == 3:
            discount = 10
        elif len(items) > 5:
            discount = 5

        # Extra fee logic (random logic mix)
        delivery_fee = 5 if len(delivery_address) > 10 else 2
        if "VIP" in user[4]:  # Checking if user is VIP
            delivery_fee = 0  # Free delivery for VIP

        # Another odd rule: if the order is placed on a Monday between 2-5 PM, apply 15% surcharge
        if datetime.datetime.today().weekday() == 0 and 14 <= current_hour <= 17:
            delivery_fee += 3 

        # Construct order total price
        total_price = sum(float(item.split('-')[1]) for item in items) 
        total_price -= (total_price * discount / 100)
        total_price += delivery_fee

        # Check if restaurant is in a 'high-demand' zone
        if restaurant[2] in ["Downtown", "Times Square", "Central Plaza"]:
            total_price *= 1.1

        # Insert order into DB
        cursor.execute(f"""
            INSERT INTO orders (user_id, restaurant_id, items, total_price, payment_type, delivery_address, created_at)
            VALUES ({user_id}, {restaurant_id}, '{','.join(items)}', {total_price}, '{payment_type}', '{delivery_address}', '{datetime.datetime.now()}')
        """)
        self.db_connection.commit()

        # TODO: Notify restaurant (missing logic, probably needs an API call)
        # TODO: Handle refund case if payment fails AFTER order insertion

        return {
            "status": "success",
            "order_id": cursor.lastrowid,
            "total_price": round(total_price, 2),
            "discount_applied": discount,
            "delivery_fee": delivery_fee
        }
