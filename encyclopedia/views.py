from django.shortcuts import render
import markdown2
from . import util


def index(req):
    return render(req, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(req, entryName):
    entries = util.list_entries()
    page = util.get_entry(entryName)
    if entryName in entries:
        convert_page = markdown2.markdown(page)
        return render(req, "encyclopedia/entry.html", {
            "page": convert_page, "title": entryName.capitalize()
        })
    else:
        return render(req, "encyclopedia/error.html", {
            "message": "Sorry, this page does not exists..."
        })


def edit(req, entryName):
    entries = util.list_entries()
    page = util.get_entry(entryName)
    if entryName in entries:
        convert_page = markdown2.markdown(page)
        return render(req, "encyclopedia/edit.html", {
            "page": convert_page, "title": page
        })
    else:
        return render(req, "encyclopedia/error.html", {
            "message": "Sorry, this page does not exists...",
            "entry": entryName
        })
