from django.db import models
from django.utils.timezone import now
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

    def set_rank(self):
        SEC_IN_HOUR = float(60*60)
        GRAVITY = 1.2

        delta = now() - self.submitted_on
        item_hour_age = delta.total_seconds() // SEC_IN_HOUR
        votes = self.votes - 1
        self.rank_score = votes / pow((item_hour_age+2), GRAVITY)
        self.save()

    def __str__(self):
        return self.title


class Vote(models.Model):
    link = models.ForeignKey(Link)
    voter = models.ForeignKey(User)

    def __str__(self):
        return '{0} link got voted by {1}'.format(self.link.title, self.voter.get_full_name() or self.voter.email)
