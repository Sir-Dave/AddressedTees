from django.db import models
from PIL import Image

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Product(models.Model):

    def upload_location(self, filename):
        file_path = "images/{category}/{filename}".format(category=str(self.category),
                                                          filename=filename)

        return file_path

    SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "Extra extra Large"),
    )

    name = models.CharField(max_length=20)
    size = models.CharField(max_length=3, choices=SIZES)
    image = models.ImageField(upload_to=upload_location)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def save(self):
        super().save()
        image = Image.open(self.image.path)
        if image.width > 300 or image.height > 300:
            output_size = (300,300)
            image.thumbnail(output_size)
            image.save(self.image.path)


class Order(models.Model):
    item_color = models.CharField(max_length=20)
    item_size = models.CharField(max_length=20)
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()
    delivery_location = models.TextField()
    item_name = models.CharField(max_length=20)
    order_time = models.DateTimeField(auto_now_add=True)
    design_type = models.CharField(max_length=20)
