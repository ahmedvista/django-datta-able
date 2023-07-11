from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("Product/((?P<pk>\d+)/)?", csrf_exempt(ProductView.as_view())),
	re_path("Raw/((?P<pk>\d+)/)?", csrf_exempt(RawView.as_view())),
	re_path("RawForProduction/((?P<pk>\d+)/)?", csrf_exempt(RawForProductionView.as_view())),
	re_path("ProductAttr/((?P<pk>\d+)/)?", csrf_exempt(ProductAttrView.as_view())),
	re_path("Client/((?P<pk>\d+)/)?", csrf_exempt(ClientView.as_view())),
	re_path("Supplier/((?P<pk>\d+)/)?", csrf_exempt(SupplierView.as_view())),
	re_path("ProductOrder/((?P<pk>\d+)/)?", csrf_exempt(ProductOrderView.as_view())),
	re_path("RawOrder/((?P<pk>\d+)/)?", csrf_exempt(RawOrderView.as_view())),
	re_path("Budget/((?P<pk>\d+)/)?", csrf_exempt(BudgetView.as_view())),
	re_path("DamagedRaw/((?P<pk>\d+)/)?", csrf_exempt(DamagedRawView.as_view())),
	re_path("DamagedProduct/((?P<pk>\d+)/)?", csrf_exempt(DamagedProductView.as_view())),
	re_path("ProductStock/((?P<pk>\d+)/)?", csrf_exempt(ProductStockView.as_view())),
	re_path("RawStock/((?P<pk>\d+)/)?", csrf_exempt(RawStockView.as_view())),

]