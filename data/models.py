# models.py
from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    USER_CHOICE = (
        ('Session', 'Session'),
        ('Click', 'Click'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="customuser")
    IP = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    type = models.CharField(max_length=255, choices=USER_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Users Data'

    def __str__(self):
        return f"{self.IP} - {self.type}"
