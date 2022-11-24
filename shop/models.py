from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
	name = models.CharField('Nomi',max_length=150,)
	slug = models.SlugField('*',max_length=150, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:category_detail', kwargs={'category_slug':self.slug})

class Tag(models.Model):
	name = models.CharField('Nomi',max_length=150,)
	slug = models.SlugField('*',max_length=150, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:tag_detail', kwargs={'tag_slug':self.slug})

class Colors(models.Model):
	COLORS = (
	('white','WHITE'),
	('black','BLACK'),
	('blue','BLUE'),
	('green','GREEN'),
	('yellow','YELLOW'),
	('red','RED'),
	('tomato','TOMATO'),
	('pink','PINK'),
	('teal','TEAL'),
	('brown','BROWN'),
	)
	color = models.CharField('Rang nommi', max_length=50, choices=COLORS)

	def __str__(self):
		return self.color

class Product(models.Model):
	name = models.CharField('Nomi',max_length=250)
	slug = models.SlugField('*',max_length=250,unique=True)
	category = models.ForeignKey(Category,
		on_delete=models.CASCADE,
		related_name='products')
	tag = models.ManyToManyField(Tag, related_name='product_tags')
	image = models.ImageField('Rasmi', upload_to='product_images/')
	color = models.CharField('Rangi',max_length=50)
	other_colors = models.ManyToManyField(Colors, related_name='other_colors')
	price = models.PositiveIntegerField('Narxi',default=0)
	old_price = models.PositiveIntegerField('Avvalgi Narxi',default=0)
	description = models.TextField('Tovar haqida')
	instock = models.BooleanField('Bor / Yok', default=True)
	count = models.PositiveIntegerField('Soni', default=1)

	def __str__(self):
		return f"Tovar - {self.name}"

# Product Images model
class ProductImages(models.Model):
	product = models.ForeignKey(Product,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='product_images')
	image = models.ImageField('Tovar alohida rasmlari',
		upload_to='product_images/',
		blank=True, null=True,)

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Tovar rasmlari'
		verbose_name_plural = 'Tovar rasmlari'

