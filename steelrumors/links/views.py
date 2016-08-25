import json

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Link, Vote
from .forms import LinkForm, VoteForm


class LinkListView(ListView):
    model = Link
    paginate_by = 5
    queryset = Link.with_votes.all()
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            voted = Vote.objects.filter(voter=self.request.user)
            links_in_page = [link.id for link in context['object_list']]
            voted = voted.filter(link_id__in=links_in_page)
            voted = voted.values_list('link_id', flat=True)
            context['voted'] = voted
        return context


class LinkDetailView(DetailView):
    model = Link


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()
        return super(LinkCreateView, self).form_valid(form)


class LinkUpdateView(LoginRequiredMixin, UpdateView):
    model = Link
    form_class = LinkForm


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('home')


class JSONResposeMixin(object):
    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict), content_type='application/jsom')
        response.status = 200 if valid_form else 500
        return response


class VoteFormBaseView(FormView):
    form_class = VoteForm
    success_url = reverse_lazy('home')

    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict))
        response.status = 200 if valid_form else 500
        return response

    def form_valid(self, form):
        link = get_object_or_404(Link, pk=form.data['link'])
        user = self.request.user
        prev_vote = Vote.objects.filter(voter=user, link=link)
        has_voted = (len(prev_vote) > 0)

        ret = {"success": 1}
        if not has_voted:
            v = Vote.objects.create(voter=user, link=link)
            ret["voteobj"] = v.id
        else:
            prev_vote[0].delete()
            ret['unvoted'] = 1
        return self.create_response(ret, True)

    def form_invalid(self, form):
        ret = {'success': 0, 'form_errors': form.errors}
        return self.create_response(ret, False)

class VoteFormView(JSONResposeMixin, VoteFormBaseView):
    pass
