from __future__ import unicode_literals

from django.db import models

class SNP(models.Model):
    trait = models.CharField(max_length=255, default = 'trait')
    type_snps  = models.CharField(max_length=255, choices = [('functional', 'Functional'), ('tag', 'Tag')], default = 'type')
    rsid = models.CharField(max_length=255,default = 'rsid')
    reference = models.CharField(max_length=255, default = 'NONE')
    chrom = models.CharField(max_length=255, default = 'chrom')
    start = models.IntegerField(default = 0)
    end = models.IntegerField(default = 0)
    chrom_start_end = models.CharField(max_length=255, default = 'chrom:start-end')
