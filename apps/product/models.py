from django.utils.translation import gettext_lazy as _
from django.db import models
from decimal import Decimal
from ..stock.models import ProductStock, RawStock


class Raw(models.Model):
    stock = models.ForeignKey(
        RawStock, on_delete=models.CASCADE, verbose_name=_("Stock")
    )
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    unit_price = models.DecimalField(
        _("Unit Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    amount = models.DecimalField(
        _("Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    created_at = models.DateTimeField(
        _("Created Data"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Material")
        verbose_name_plural = _("Raw Materials")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    stock = models.ForeignKey(
        ProductStock, on_delete=models.CASCADE, verbose_name=_("Stock")
    )
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    unit_price = models.DecimalField(
        _("Unit Price"), null=True, blank=True, decimal_places=2, max_digits=10
    )
    amount = models.DecimalField(
        _("Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(1),
    )
    created_at = models.DateTimeField(
        _("Created Data"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class RawForProduction(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
        related_name="raws",
    )
    raw = models.ForeignKey(
        Raw,
        on_delete=models.CASCADE,
        verbose_name=_("Raw Material"),
        related_name="products",
    )
    quantity_for_prod = models.IntegerField(
        _("Quantity Required for Production"), default=1
    )
    created_at = models.DateTimeField(
        _("Created Data"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Material for Production")
        verbose_name_plural = _("Raw Material for Production")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.product)


class ProductAttr(models.Model):
    product = models.ForeignKey(Product, related_name="attr", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Product Attr")
        verbose_name_plural = _("Product Attrs")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")

    def __str__(self):
        return f"{self.name} - {self.value}"
