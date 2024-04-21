
from flask import Flask
from router.productRouter import product_view
from router.invoiceRouter import invoice
from router.orderRouter import order

app = Flask(__name__)




# Optional URL prefix
app.register_blueprint(product_view)
app.register_blueprint(invoice, url_prefix='/api/invoice')
app.register_blueprint(order, url_prefix='/api/order')


if __name__ == "__main__":
    app.run(debug=True)