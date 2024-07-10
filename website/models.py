from django.db import models

# Create a model of category
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = "categories"

# Create a model of art
class Art(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    description = models.CharField(max_length=2500, default='', blank= True, null = True)
    image = models.ImageField(upload_to='uploads/art/') 
    artist = models.CharField(max_length=100)
    date_of_adding = models.DateTimeField(auto_now_add=True)
    date_of_finishing = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.title}'

# Create a model of artist
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100, blank= True, null = True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'