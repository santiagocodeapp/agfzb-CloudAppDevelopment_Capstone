# from django.db import models
# from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data



from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField

# Create your models here.

class User(AbstractUser):
    pass


class Positions(models.Model):
    field_position = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.field_position}"

class Players(models.Model):
    team = models.CharField(max_length=64)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    player_positions = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first} {self.last} Position: {self.player_positions}"


class Report(models.Model):
    CoachName = models.CharField(max_length=64)
    Player = models.ForeignKey('Players', on_delete = models.CASCADE)
    Defense = models.CharField(max_length=1000)
    Hitting = models.CharField(max_length=1000)
    Pitching = models.CharField(max_length=1000)
    Character_Work_Ethic = models.CharField(max_length=1000)

    def __str__(self):
        return f"New Report"


class IMG_Teams(models.Model):
    team = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.team}"