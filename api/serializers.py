from rest_framework import serializers


try:

    from apps.product.models import Product
    from apps.product.models import Raw
    from apps.product.models import RawForProduction
    from apps.product.models import ProductAttr
    from apps.orders.models import Client
    from apps.orders.models import Supplier
    from apps.orders.models import ProductOrder
    from apps.orders.models import RawOrder
    from apps.orders.models import Budget
    from apps.orders.models import DamagedRaw
    from apps.orders.models import DamagedProduct
    from apps.stock.models import ProductStock
    from apps.stock.models import RawStock

except:
    pass 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Product
        except:
            pass    
        fields = '__all__'

class RawSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Raw
        except:
            pass    
        fields = '__all__'

class RawForProductionSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = RawForProduction
        except:
            pass    
        fields = '__all__'

class ProductAttrSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ProductAttr
        except:
            pass    
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Client
        except:
            pass    
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Supplier
        except:
            pass    
        fields = '__all__'

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ProductOrder
        except:
            pass    
        fields = '__all__'

class RawOrderSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = RawOrder
        except:
            pass    
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Budget
        except:
            pass    
        fields = '__all__'

class DamagedRawSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = DamagedRaw
        except:
            pass    
        fields = '__all__'

class DamagedProductSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = DamagedProduct
        except:
            pass    
        fields = '__all__'

class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ProductStock
        except:
            pass    
        fields = '__all__'

class RawStockSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = RawStock
        except:
            pass    
        fields = '__all__'

