def get_order_details(order) -> str:
    return f"Order ID: {order.order_id}\nProduct: {order.product.name}\nQuantity: {order.quantity}\nTotal Price: {order.get_total_price()}"


def get_order_total_price(order):
    return order.product.price * order.quantity


def get_product_details(product) -> str:
    return f"Product ID: {product.product_id}\nName: {product.name}\nPrice: {product.price}"
