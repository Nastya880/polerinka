from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    @property
    def likes_count(self):
        return Rating.objects.filter(post=self, type=Rating.LIKE).count()
    @property
    def dislikes_count(self):
        return Rating.objects.filter(post=self, type=Rating.DISLIKE).count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Rating(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"
    TYPE_CHOICES = (
        (LIKE, "нравится"),
        (DISLIKE, "не нравится")
    )
    post = models.ForeignKey(Women,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    type = models.CharField(max_length=80, choices=TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return 'Rating by {} on {}'.format(self.user, self.post)

