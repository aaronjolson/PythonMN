import json
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .forms import SignUpForm


def home(request):

    form = SignUpForm()

    return render(request, "conference/base.html", {'form': form, })


def sponsors(request):

    form = SignUpForm()

    return render(request, "conference/sponsors.html", {'form': form, })


def about(request):

    form = SignUpForm()

    return render(request, "conference/about.html", {'form': form, })


@require_POST
def signup(request):

    form = SignUpForm(request.POST)

    response_data = False

    if form.is_valid():
        form.save()
        response_data = True

    print response_data

    return HttpResponse(json.dumps(response_data), content_type="application/json")