# CoreApp/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(WhyChooseUs)
admin.site.register(Review)
admin.site.register(Contact)
