from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .models import Link
from .forms import LinkForm


class LinkListView(ListView):
    model = Link
    paginate_by = 5
    queryset = Link.with_votes.all()
    template_name = 'pages/home.html'


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
