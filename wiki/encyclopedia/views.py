from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Search, Create_page, Edit_page
import random

from . import util
from markdown2 import Markdown

def index(request):
    # returns a template encyclopedia/index.html
    return render(request, "encyclopedia/index.html", {
        # provides the template with a list of all entries in the encyclopedia from list_entries function from util.py
        "entries": util.list_entries(),
        "input": Search(),
    })

def content(request, title):
    markdowner = Markdown()
    # returns a template encycolpedia/title.html
    try: 
        body = markdowner.convert(util.get_entry(title))
    except TypeError:
        return render(request, "encyclopedia/error.html", {
            "message": "Error! Page does not exist.",
            "input": Search(),
        })
    return render(request, "encyclopedia/title.html", {
        # contents = the content of the html file
        "input": Search(),
        "contents": body,
        "title": title,
    })


def search(request):
    form = Search(request.GET)
    if form.is_valid():
        q = form.cleaned_data["q"]
        if util.get_entry(q):
            return HttpResponseRedirect(reverse("content", kwargs={"title": q}))
        else:
            return render(request, "encyclopedia/search.html", {
                "input": Search(),
                "form": q,
                "entries": util.list_entries()
            })
    return render(request, "encyclopedia/search.html")
    
def create(request):
    if request.method == "POST":
        form = Create_page(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title.lower() in [e.lower() for e in util.list_entries()]:
                return render(request, "encyclopedia/error.html", {
                    "message": "Error! Page already exists",
                    "input": Search(),
                })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("content", kwargs={"title": title}))    
    # default webpage for create_new_page
    return render(request, "encyclopedia/create_new_page.html", {
        "input": Search(),
        "create_page": Create_page(),
    })


def random_pages(request):
    return HttpResponseRedirect(reverse(
        "content", 
        kwargs={"title": random.choice(util.list_entries())}
        ))


def edit(request, title):
    if request.method == "POST":
        form = Edit_page(request.POST)
        if form.is_valid():
            util.save_entry(title, form.cleaned_data["content"])
            return HttpResponseRedirect(reverse("content", kwargs={"title": title}))
        else:
            form = Edit_page(initial={
                "title": title,
                "content": util.get_entry(title),
            })
    
    return render(request, "encyclopedia/edit_page.html", {
        "input": Search(),
        "title": title,
        "edit_page": Edit_page(initial={
            "title": title,
            "content": util.get_entry(title)}),
    })

