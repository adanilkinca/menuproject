from django.db import models
from unicodedata import name

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=160)

    def __str__(self):
        return self.menu_category_name
    
    class Meta:
        verbose_name = 'Menu Category'
        verbose_name_plural = 'Menu Categories'

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=150)
    cocktail = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name='category_name')

    def __str__(self):
        return f'{self.name} : {self.cocktail}'
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
    
class Customer(models.Model):
    name = models.CharField(max_length=180)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

class Logger(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    time_log = models.TimeField(help_text = 'Enter the exact time')

    def __str__(self):
        return f'{self.last_name}, {self.first_name}, {self.time_log}'

# for shell to populate(Cocktails):
# from menuapp.models import Menu, MenuCategory
# # Create MenuCategory instances
# category_names = [
#     "Longdrink",
#     "Shot",
#     "Sour",
#     "Non-alcoholic"
# ]
# categories = []
# for category_name in category_names:
#     category = MenuCategory.objects.create(menu_category_name=category_name)
#     categories.append(category)
# # Create Menu instances
# menu_data = [
#     {"name": "Margarita", "price": 12, "cocktail": "Longdrink", "category": categories[0]},
#     {"name": "Tequila-boom", "price": 5, "cocktail": "Shot", "category": categories[1]},
#     {"name": "Mojito", "price": 9, "cocktail": "Sour", "category": categories[2]},
#     {"name": "Long Island Ice Tea", "price": 16, "cocktail": "Longdrink", "category": categories[0]},
#     {"name": "Monkey's Brain", "price": 7, "cocktail": "Shot", "category": categories[1]},
#     {"name": "Raul and Fidel", "price": 9, "cocktail": "Shot", "category": categories[1]},
#     {"name": "Pelican", "price": 8, "cocktail": "Non-alcoholic", "category": categories[3]},
# ]
# for data in menu_data:
#     menu = Menu.objects.create(
#         name=data["name"],
#         price=data["price"],
#         cocktail=data["cocktail"],
#         category_id=data["category"]
#     )
#     menu.save()


# # For shell to populate (Customers):
# from menuapp.models import Customer
# # Create customers instances
# menu_data = [
#     {"name": "Charly", "reservation_day": "Tuesday", "seats": 1},
#     {"name": "Robert", "reservation_day": "Sunday", "seats": 10},
#     {"name": "George", "reservation_day": "Saturday", "seats": 12},
#     {"name": "Sandra", "reservation_day": "Tuesday", "seats": 6},
#     {"name": "Keanu", "reservation_day": "Monday", "seats": 47},
#     {"name": "Quentin", "reservation_day": "Saturday", "seats": 8},
#     {"name": "Salma", "reservation_day": "Friday", "seats": 7},
#     {"name": "Leo", "reservation_day": "Wednesday", "seats": 8},
# ]
# # Iterate over the data and create Customer objects:
# for item in menu_data:
#     customer = Customer(name=item["name"], reservation_day=item["reservation_day"], seats=item["seats"])
#     customer.save()
# # Verify that the data is populated by querying the Customer table:
# customers = Customer.objects.all()
# for customer in customers:
#     print(customer)
