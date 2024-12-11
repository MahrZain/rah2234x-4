from django.db import models

class CustomUser(models.Model):
    # Define choices as a tuple of tuples
    USER_CHOICE = (
        ('Session', 'Session'),  # First value stored in DB, second displayed in forms/admin
        ('Click', 'Click'),
    )
    class Meta:
        verbose_name_plural = 'Users Data'

    IP = models.CharField(max_length=255)  # Field for storing IP addresses
    type = models.CharField(max_length=255, choices=USER_CHOICE)  # Dropdown for type
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp for creation

    def __str__(self):
        return f"{self.IP} - {self.type}"  # String representation for the admin interface
