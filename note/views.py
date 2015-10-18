# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

# import the add note form

from note.forms import AddForm, NoteForm, NOTETYPE_PRIVATE, NOTETYPE_PUBLIC
from note.models import Note


def index(request):
    if request.method == 'POST':
        # when user post form
        form = AddForm(request.POST)  # when form contain data

        if form.is_valid():
            # when data is valid

            color = form.cleaned_data["color"]
            title = form["title"]
            # author_id = form.author_id
            # noteType = form.noteType
            # createTime = form.createTime
            # publish = form.publish
            # content1 = form.content_text
            return HttpResponse(color)
            # return HttpResponse(form["color"])

        else:
            return HttpResponse("not a valid data form ")
    else:
        # when user just visit , not post data to the site
        form = AddForm()
        return render(request, 'index_bootstrap.html', {'form': form})


def create(request):
    if(request.method == 'POST'):
        note = Note()
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # if note get the authorID then set the ID is -1. because at the
            # first step. we didn't hava build UC system.
            if note.authorID == None:
                note.authorID = 0

            # if user forget to set note's type. we set it as default value 0
            if note.noteType == None:
                note.noteType = 0

            if note.color == None:
                note.color = "#000000"

            # set createtime
            note.createTime = timezone.now()

            try:
                note.save()
                return HttpResponse(note.content)
                # return HttpResponse("data is valid and we store it in the
                # database. The id of this note is:"+str(note.id))
            except Exception, e:
                return HttpResponse("data is valid and we store it in the database failed. ")
            finally:
                pass
            return HttpResponse("data is valid.")
        else:
            return render(request, 'create.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'create.html', {'form': form})


def md(request):
    return render(request, 'md.html')


def view(request):
    # a safe way to get note id
    id = 1
    try:
        id = int(request.GET.get('id', 1))
    except:
        id = 1

    note = get_object_or_404(Note, pk=id)

    # check the user's privilege
    if note.noteType == NOTETYPE_PRIVATE and note.authorID == 0:
        return HttpResponse("你没有权限查看该文章")

    toc = request.GET.get('toc', 'true')
    if toc == 'false':
        # if toc equal  false , then render to view.html
        return render(request, 'view.html', {'note': note})
    # default set render to viewTOC template
    return render(request, 'viewTOC.html', {'note': note})
