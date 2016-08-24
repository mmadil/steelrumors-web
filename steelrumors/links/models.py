from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .managers import LinkVoteCountManager
from steelrumors.users.models import User


class Link(models.Model):
    title = models.CharField(_('headline'), max_length=100)
    submitter = models.ForeignKey(User)
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField(_('url'), max_length=255, blank=True)
    description = models.TextField(blank=True)

    objects = models.Manager()
    with_votes = LinkVoteCountManager()

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        ordering = ('title',)

    def get_absolute_url(self):
        return reverse('link_detail', kwargs={'pk': str(self.id)})

    def __str__(self):
        return self.title


class Vote(models.Model):
    link = models.ForeignKey(Link)
    voter = models.ForeignKey(User)

    def __str__(self):
        return '{0} link got voted by {1}'.format(self.link.title, self.voter.get_full_name() or self.voter.email)
