from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# ================= SERVICES =================
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="FontAwesome class")
    animation = models.CharField(max_length=100, blank=True, help_text="Optional animation class")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# ================= PORTFOLIO =================
class Portfolio(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    website_url = models.URLField(help_text="Live website link")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# ================= WHY CHOOSE US =================
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    animation = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# ================= CLIENT REVIEWS =================
class Review(models.Model):
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    message = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.name} ({self.rating}⭐)"


# ================= CONTACT =================
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    service = models.CharField(max_length=120)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
