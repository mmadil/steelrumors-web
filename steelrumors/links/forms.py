from django import forms

from .models import Link, Vote


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ('submitter', 'rank_score')


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('voter', 'link')
