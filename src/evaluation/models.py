from django.db import models

class Evaluation(models.Model):
    nom = models.CharField(max_length=255)
    client_ponctuel = models.IntegerField()
    produit_pratique = models.IntegerField()
    prix_cher = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.nom
