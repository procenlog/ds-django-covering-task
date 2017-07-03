from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User

from .models import Book, RequestRecord
from .forms import BookForm
from .viewmixins import LoginRequiredMixin


def logs(request):
    with open("book_store/book_manipulation.log") as f:
        lines = reversed(f.readlines())
    return render(request, 'book_store/logs.html', {'lines': lines})


class RequestsView(generic.ListView):
    template_name = 'book_store/requests.html'
    context_object_name = 'request_list'
    queryset = RequestRecord.requests.last_10()


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('book_store:index')


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_create'
    success_url = reverse_lazy('book_store:index')


def user_test(request):
    username = request.user.username
    if username:
        return HttpResponse("You are logged in as %s." % username)
    else:
        return HttpResponse("You are not logged in.")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):    #Method not incapsulated in model because of form.save incapsulation.
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print request.POST['next']
            return HttpResponseRedirect(request.POST['next'])
        else:
            return HttpResponse('Invalid username or password')
    else:
        if request.GET:
            next = request.GET['next']
        else:
            next = reverse('index')
        return render(request, 'book_store/login.html', {'next' : next})


class IndexView(generic.ListView):
    template_name = 'book_store/index.html'

    def get_queryset(self):
        return Book.objects.order_by('title')