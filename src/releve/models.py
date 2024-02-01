from django.db import models

class Releve(models.Model):
    leadershipIndividuel = models.IntegerField()
    leadershipEtatique = models.IntegerField()
    leadershipCivilisationnel = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    
