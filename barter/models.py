from django.db import models
from django.utils import timezone
from user.models import CustomUser
from .utils.random_id import generate_id

# Create your models here.
class Item(models.Model):
    itemId = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
        db_index=True
    )
    
    seller = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=150)
        
    timeCreated = models.DateTimeField(auto_now_add=True)

    deadline = models.DateTimeField()

    # image = models.ImageField(blank=True)
    # tags = models.JSONField(blank=True)

    status = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.itemId:
            while True:
                candidate_id = generate_id()
                if not Item.objects.filter(itemId=candidate_id).exists():
                    self.itemId = candidate_id
                    break
            
        super().save(*args, **kwargs)

    def is_expired(self, *args, **kwargs):
        return timezone.now() > self.deadline

    def barter_status(self):
        if self.is_expired():
            return "expired"
        
        return 'active'


class BarterLogs(models.Model):
    buyer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    buyer_request_time = models.DateTimeField(blank=True, null=True)
    seller_accepted_time = models.DateTimeField(blank=True, null=True)

    def is_requested(self, *args, **kwargs):
        return self.buyer_request_time is not None
        
    def is_accepted(self, *args, **kwargs):
        return self.seller_accepted_time is not None
    
    def buyer_request(self, buyer, *args, **kwargs):
        if self.buyer_request_time is not None:
            raise ValueError("This barter already has a buyer request")
        self.buyer = buyer
        self.buyer_request_time = timezone.now()
        self.save(update_fields=["buyer", "buyer_request_time"])

    def seller_accept(self, seller, *args, **kwargs):
        if self.buyer_request_time is None:
            raise ValueError("This barter has no request!")

        if self.seller_accepted_time is not None:
            raise ValueError("This barter has already been completed!")
        
        self.seller = seller
        self.seller_accepted_time = timezone.now()
        self.save(update_fields=["seller", "seller_accepted_time"])