from .models import *
from cart.models import  Cart

def view_all(request):
	try:
		cart = Cart.objects.get(id=request.session.get('user_cart_id'))
	except:
		cart = {'notfound': "Products not found!"}
	context = {
		'categories':Category.objects.all(),
		'tags':Tag.objects.all(),
		'cart':cart,
		'random_products':Product.objects.all().order_by('?')
	}
	return context