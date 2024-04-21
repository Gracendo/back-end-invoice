
from flask import Flask, jsonify, request
from models.products import Product

def get_all_products():
    try:
        products = Product.read()
        return [product.toJSON() for product in products]
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def get_product_with_id(product_id,returnObject=True):
    
    try:
        product = Product.read(product_id)
        if product is None:
            return f"product with ID {product_id} does not exist"
        return product.toJSON() if not returnObject else product
    except Exception as e:
        return jsonify({'error':str(e)})

def save_product(product_name,quantity,price,category,product_id=None):
    if product_id is not None:
        product = get_product_with_id(product_id,returnObject=True)

        if product is not None:
            product.product_name=product_name
            product.price=price
            product.quantity=quantity
            product.category=category

            product.save()

            return f'product with ID {product_id} created with success'
        else:
            raise Exception(f'No product with ID {product_id}')
    else:
        new_product = Product(product_name=product_name,price=price,quantity=quantity,category=category)
        new_product.save()
        return new_product if isinstance(new_product, dict) else new_product.toJSON()


def delete_product(product_id):
    try:
        product = get_product_with_id(product_id)
        if product is not None:
            Product.delete(product_id)
        return f"product with ID {product_id} deleted with success"
    except Exception as e:
        return jsonify({'error': str(e)}), 500