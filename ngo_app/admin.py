from django.contrib import admin
from ngo_app.models import Volunteer
from .models import Contact
from ngo_app.models import Donation
class voleenterAdmin(admin.ModelAdmin):
    list_display=['vname','vphno','vemail','vaddress']

class ContactAdmin(admin.ModelAdmin):
    list_display =['cname', 'cemail','csubject','cmessage']



class DonationAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'payment_method', 'paid', 'created_at']

admin.site.register(Volunteer,voleenterAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Donation,DonationAdmin)