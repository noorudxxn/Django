from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):

    products = [
        {
            "name": "Laptop",
            "price": 50000,
            "category": "Electronics"
        },
        {
            "name": "Mobile",
            "price": 20000,
            "category": "Electronics"
        },
        {
            "name": "Notebook",
            "price": 50,
            "category": "Stationery"
        }
    ]

    return Response(products)