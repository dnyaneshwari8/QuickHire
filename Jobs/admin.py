from django.contrib import admin
from Jobs.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'posted_by',
                    'pay_rate', 'start_date', 'status', 'created_at','city',
                    'state','start_time','duration','address','description'
                    )

admin.site.register(Job, JobAdmin)