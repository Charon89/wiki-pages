from django.shortcuts import render
import markdown2
from . import util

def index(req):
    return render(req, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikiEntry(request, name):
    # calling list of entries
    entries = util.list_entries()
    # also the entry funtion passing in the name of the md file
    page = util.get_entry(name)
    # if name in entries then convert the md using markdown
    if name in entries:
        convert_page = markdown2.markdown(page)
        return render(request, "encyclopedia/wiki.html", {
            "page": convert_page, "title": name.capitalize()
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "Sorry, this page does not exists..."
        })
