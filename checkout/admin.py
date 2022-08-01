from django.contrib import admin
from .models import OrderLineItem, Order

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'line_item_total',
    )

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'date',
        'email',
        'full_name',
        'order_total',
    )

    ordering = ('-date',)
    fields = (
        'date',
        'order_number',
        'order_total',
        'full_name',
        'email',
        'phone_number',
        'house_name',
        'street_address_1',
        'street_address_2',
        'city',
        'post_code',
        'country',
        'original_cart',
        'stripe_pid',
    )
    readonly_fields = (
        'order_number',
        'date',
        'order_total',
        'original_cart',
        'stripe_pid',
    )
    inlines = (OrderLineItemAdminInline,)

admin.site.register(Order, OrderAdmin)