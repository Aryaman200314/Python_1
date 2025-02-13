import json
All_orders = []
data = {
    'orders': [
        {
            'order_id': 'O001',
            'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'},
            'items': [
                {'product_id': 'P001', 'name': 'Laptop', 'price': 999.99, 'quantity': 1},
                {'product_id': 'P002', 'name': 'Mouse', 'price': 25.99, 'quantity': 2}
            ],
            'shipping_address': '123 Main St, Springfield, IL'
        },
        {
            'order_id': 'O002',
            'customer': {'id': 'C002', 'name': 'Jane Smith', 'email': 'jane@example.com'},
            'items': [
                {'product_id': 'P003', 'name': 'Phone', 'price': 599.99, 'quantity': 1}
            ],
            'shipping_address': '456 Oak St, Seattle, WA'
        },
        {
            'order_id': 'O003',
            'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'},
            'items': [
                {'product_id': 'P004', 'name': 'Headphones', 'price': 149.99, 'quantity': 1},
                {'product_id': 'P005', 'name': 'Keyboard', 'price': 99.99, 'quantity': 1}
            ],
            'shipping_address': '123 Main St, Springfield, IL'
        }
    ]
}

for order in data ['orders']:
    order_id = order['order_id']
    customer_Name = order['cutomer']['name']
    shipping_address = order['shipping_address']
    total_price = 0

    for item in order['item']:
        product_name = item['name']
        price = item['price']
        quantity = item['quantity']

        total_value = price * quantity
        total_order_value = total_order_value + total_value
        total_quantity = total_quantity + quantity

        All_orders.append({
            "Order ID": order_id,
            "Customer Name": customer_Name,
            "Product name": product_name,
            "Product price": price,
            "Quantity": quantity,
            "Total value" : total_value,
            "shipping address" : shipping_address
        })

        discount = total_order_value * 0.10 if total_order_value > 100 else 0

        shipping_cost = total_quantity * 5


        