from django.db import models


class LinkVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(LinkVoteCountManager, self).get_queryset().annotate(
                votes=models.Count('vote')).order_by('-rank_score','-votes')
