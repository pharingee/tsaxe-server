'''
Page models
'''
from django.db import models
from django.utils import timezone, text
from django.utils.translation import ugettext_lazy as _

from pages import constants


class LastUpdatedModel(models.Model):
    '''
    Abstract model to track last updated and created onn
    '''
    created_on = models.DateTimeField(
        _('created on'),
        default=timezone.now,
    )
    last_updated = models.DateTimeField(
        _('last updated'),
        auto_now=True,
    )

    class Meta:
        abstract = True


class SlugNameModel(LastUpdatedModel):
    '''
    Abstract model for sluggable models like tags and page types
    '''
    name = models.CharField(
        _('name'),
        max_length=40,
    )
    slug = models.SlugField(
        max_length=50,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):  # pylint: disable=signature-differs
        if not self.slug:
            self.slug = text.slugify(self.name)

        return super(SlugNameModel, self).save(*args, **kwargs)


class PageType(SlugNameModel):
    '''
    Model for separating page types.
    '''
    nav_type = models.CharField(
        _('navigation type'),
        max_length=1,
        choices=constants.NAV_TYPE_CHOICES,
        default=constants.NONE,
    )


class Tag(SlugNameModel):
    '''
    Tag model
    '''
    is_visible = models.BooleanField(
        _('is visible'),
        default=True,
    )


class Page(LastUpdatedModel):
    '''
    A web page. Can be an article or homepage
    '''
    author = models.DateField()
    published_on = models.DateTimeField(
        _('published on'),
        blank=True,
        null=True,
    )
    page_type = models.ForeignKey(
        PageType,
        related_name='pages',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('page type'),
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='pages',
        verbose_name=_('page type'),
    )
