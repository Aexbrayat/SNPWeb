from django.contrib import admin
from models import *

class SNPAdmin(admin.ModelAdmin):
     list_display = ('rsid', 'type_snps', 'trait', 'chrom', 'start', 'end', )
    
admin.site.register(SNP, SNPAdmin)

