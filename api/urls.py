from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("product/((?P<pk>\d+)/)?", csrf_exempt(ProductView.as_view())),
	re_path("raw/((?P<pk>\d+)/)?", csrf_exempt(RawView.as_view())),
	re_path("rawForProduction/((?P<pk>\d+)/)?", csrf_exempt(RawForProductionView.as_view())),
	re_path("productAttr/((?P<pk>\d+)/)?", csrf_exempt(ProductAttrView.as_view())),
	re_path("client/((?P<pk>\d+)/)?", csrf_exempt(ClientView.as_view())),
	re_path("supplier/((?P<pk>\d+)/)?", csrf_exempt(SupplierView.as_view())),
	re_path("productOrder/((?P<pk>\d+)/)?", csrf_exempt(ProductOrderView.as_view())),
	re_path("rawOrder/((?P<pk>\d+)/)?", csrf_exempt(RawOrderView.as_view())),
	re_path("budget/((?P<pk>\d+)/)?", csrf_exempt(BudgetView.as_view())),
	re_path("damagedRaw/((?P<pk>\d+)/)?", csrf_exempt(DamagedRawView.as_view())),
	re_path("damagedProduct/((?P<pk>\d+)/)?", csrf_exempt(DamagedProductView.as_view())),
	re_path("productStock/((?P<pk>\d+)/)?", csrf_exempt(ProductStockView.as_view())),
	re_path("rawStock/((?P<pk>\d+)/)?", csrf_exempt(RawStockView.as_view())),

]