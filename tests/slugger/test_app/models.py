from django.db import models

from slugger.fields import AutoSlugField


class AutoSlugModel(models.Model):
    title = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='title', max_length=10)


class UniqueAutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)


class UniqueForAutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique_for_date='unique_date',
                         unique_for_month='unique_month',
                         unique_for_year='unique_year')
    unique_date = models.DateField()
    unique_month = models.DateField()
    unique_year = models.DateField()


class UniqueForDateTimeAutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique_for_date='pub_datetime')
    pub_datetime = models.DateTimeField()


class UniqueTogetherAutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    field_1 = models.CharField(max_length=10)
    field_2 = models.CharField(max_length=10)
    field_3 = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('created', 'field_1'),
            ('slug', 'field_1',),
            ('slug', 'field_2', 'field_3'),
        )


class ChildUniqueTogetherAutoSlugModel(UniqueTogetherAutoSlugModel):
    pass


class MixedUniqueAutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique_for_date='unique_date')
    unique_date = models.DateField()
    field_1 = models.CharField(max_length=10)

    class Meta:
        unique_together = ('slug', 'field_1')


def custom_slugify(value):
    return 'custom-%s' % value


class CustomAutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', slugify=custom_slugify)


class SelfReferenceAutoSlugModel(models.Model):
    slug = AutoSlugField(populate_from='slug')


class LambdaAutoSlugModel(models.Model):
    slug = AutoSlugField(populate_from='title', slugify=lambda: 'test')


class Child1Model(UniqueAutoSlugModel):
    pass


class Child2Model(UniqueAutoSlugModel):
    pass
