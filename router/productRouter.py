# from controllers.productcontrollers import *
from controllers.productcontrollers import *

from flask import Blueprint,jsonify,Response,request

# Define your sub-app logic in a separate file (e.g., sub_app.py)
product_view = Blueprint('product', __name__,url_prefix='/product')



@product_view.route("/", methods=['GET','POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_products()
    elif request.method == 'POST':
        data = request.get_json()
        if isinstance(data,list) and all(isinstance(item, dict) and 'product_name' in item and 'price' in item and 'quantity' in item and 'category' in item for item in data):

            responses = []
            for product_data in data:
                try:
                    product = save_product(product_data['product_name'],product_data['price'],product_data['quantity'],product_data['category'])
                    responses.append(product)
                except Exception as e:
                    responses.append({'error':str(e)})
            return jsonify(responses)
        else:
            return jsonify({'error': 'Invalid request'}),400
    else:
        return Response({'error': 'Method not allowed'},status=405)



@product_view.route("/<product_id>", methods=['GET','PATCH','DELETE'])
def get_or_update_or_delete_product(product_id):
    if request.method == 'GET':
        try:
            return get_product_with_id(product_id,False)
        except:
            return Response(f'product not found',status=404)
    elif request.method == 'PATCH':
        data = request.get_json()
        return Response(save_product(product_name=data['product_name'],price=data['price'],quantity=data['quantity'],category=data['category'],product_id=product_id))
    elif request.method == 'DELETE':
        return Response(delete_product(product_id),'delete successfull')
    else:
        return None
    
