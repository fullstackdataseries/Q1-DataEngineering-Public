import time
import random
import json
from faker import Faker
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
import concurrent

# Initialize Faker
fake = Faker()

# Constants and Setup
NUM_RECORDS = 10000
PRODUCTS = {f"Product_{i}": round(random.uniform(5, 100), 2) for i in range(1, 11)}
USER_IDS = [fake.unique.random_int(min=10000, max=99999) for _ in range(1000)]  # Some repeating users
START_DATE = datetime(2016, 1, 1)
END_DATE = datetime(2023, 12, 31)
DATE_RANGE = END_DATE - START_DATE

# Helper functions
def random_date_generator(start, range_in_days):
    """Generate a random datetime between start date and end date"""
    random_days = random.randrange(range_in_days.days)
    random_date = start + timedelta(days=random_days)
    return random_date.isoformat()

def create_transaction(transaction_id):
    """Create a fake transaction record"""
    user_id = random.choice(USER_IDS)
    session_id = fake.uuid4()
    timestamp = random_date_generator(START_DATE, DATE_RANGE)
    total_amount = 0
    products = []

    for _ in range(random.randint(1, 5)):  # Each transaction can have multiple products
        product_id, price = random.choice(list(PRODUCTS.items()))
        quantity = random.randint(1, 3)
        products.append({
            "ProductID": product_id,
            "Quantity": quantity,
            "Price": price
        })
        total_amount += price * quantity

    tax_amount = round(total_amount * 0.07, 2)  # Assume 7% tax rate
    shipping_amount = round(random.uniform(5, 20), 2)
    discounts = round(random.uniform(1, 10), 2)
    total_amount = round(total_amount + tax_amount + shipping_amount - discounts, 2)

    return {
        "EventType": "TransactionComplete",
        "Timestamp": timestamp,
        "TransactionID": transaction_id,
        "UserID": user_id,
        "SessionID": session_id,
        "TotalAmount": total_amount,
        "TaxAmount": tax_amount,
        "ShippingAmount": shipping_amount,
        "Discounts": discounts,
        "Products": products,
        "PaymentType": random.choice(["Visa", "MasterCard", "Amex", "PayPal"]),
        "ShippingAddress": fake.address(),
        "BillingAddress": fake.address()
    }
    
# Main function to generate transactions using ThreadPoolExecutor
def generate_transactions(num_records):
    transactions = []
    # Generate unique transaction IDs ahead of time
    transaction_ids = list(range(1, num_records + 1))

    # Use ThreadPoolExecutor to parallelize the creation of transactions
    with ThreadPoolExecutor(max_workers=None) as executor:  # Adjust max_workers based on your system
        future_to_transaction = {executor.submit(create_transaction, tid): tid for tid in transaction_ids}
        for future in concurrent.futures.as_completed(future_to_transaction):
            try:
                transaction = future.result()
                transactions.append(transaction)
            except Exception as exc:
                print(f'Generated an exception: {exc}')
                
    return transactions


import pathlib
start = time.time()
transactions = generate_transactions(NUM_RECORDS)

# Check if path exists otherwise mkdir
data_path = pathlib.Path(pathlib.Path(__file__).absolute().parent.parent, 'data')
data_path.mkdir(parents=True, exist_ok=True)
with open(f'{data_path}/transactions_multithreaded.json', 'w') as f:
    json.dump(transactions, f)
end = time.time()
print('took {} seconds to generate {} records'.format(end - start, NUM_RECORDS))

# Generate the data
# transactions = [create_transaction(transaction_id) for transaction_id in range(1, NUM_RECORDS+1)]
