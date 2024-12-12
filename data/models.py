from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    USER_CHOICE = (
        ('Session', 'Session'),  
        ('Click', 'Click'),
    )

    class Meta:
        verbose_name_plural = 'Users Data'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    IP = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)  # Supports all IPs (IPv4 and IPv6)
    type = models.CharField(max_length=255, choices=USER_CHOICE) 
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.IP} - {self.type}"
