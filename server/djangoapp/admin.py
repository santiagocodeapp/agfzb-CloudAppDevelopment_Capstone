# from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here


from re import U
from django.contrib import admin
from .models import User, Positions, Players, Report, IMG_Teams

# Register your models here.
admin.site.register(User)
admin.site.register(Positions)
admin.site.register(Players)
admin.site.register(Report)
admin.site.register(IMG_Teams)