from django.contrib import admin

# Register your models here.
from .models import Fish,Product,Food,Orders
admin.site.register(Fish)
admin.site.register(Product)
admin.site.register(Food)
admin.site.register(Orders)