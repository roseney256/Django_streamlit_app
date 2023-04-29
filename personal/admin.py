from django.contrib import admin
from personal.models import Question, Farm, Cattle, Pasture, ManureManagement, EmissionFactor, Emission

# Register your models here.
admin.site.register(Cattle)
admin.site.register(Pasture)
admin.site.register(ManureManagement)
admin.site.register(Farm)
admin.site.register(EmissionFactor)
admin.site.register(Emission)



admin.site.register(Question)