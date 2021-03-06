# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

from django.views.generic.list import ListView

# import the add note form

from note.forms import AddForm, NoteForm, NOTETYPE_PRIVATE, NOTETYPE_PUBLIC
from note.models import Note, Tag
from django.http import HttpResponseRedirect


def NoteListView(request):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


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
                tags = form.cleaned_data["tags"]
                # TODO: not support chinese character
                tags = tags.replace(",", '|').replace(
                    ";", '|').replace(" ", "").replace("||", "|")
                tagArr = tags.split("|")
                # 下面虽然实现了tags的插入，但是效率不高
                # for tag in tagArr:
                #     tag_record=Tag(tagName=tag,noteID=note.id)
                #     tag_record.save()
                # Optimizaition way
                insert_list = []
                for tag in tagArr:
                    # 此处逻辑不严，如果tag为空，还会插入的，这样没有意义
                    if tag != "":
                        insert_list.append(Tag(tagName=tag, noteID=note))
                # print insert_list
                Tag.objects.bulk_create(insert_list)

                return HttpResponseRedirect('/view?id=' + str(note.id))

            except Exception, e:
                # return HttpResponseRedirect('/view?id='+str(note.id
                return HttpResponse("data is valid and we store it in the database failed. ")
            finally:
                pass
            return HttpResponse("data is valid.")
        else:
            return render(request, 'create.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'create.html', {'form': form})


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

    # 查找这篇笔记所有的标签
    # get all tags of note
    tags = Tag.objects.filter(noteID=note)

    toc = request.GET.get('toc', 'true')
    if toc == 'false':
        # if toc equal  false , then render to view.html
        return render(request, 'view.html', {'note': note, 'tags': tags})
    # default set render to viewTOC template
    return render(request, 'viewTOC.html', {'note': note, 'tags': tags})


def update(request):
    # 现在这个是要进行更新文章的入口
    # 主要的逻辑处理都在这个里面
    # OK
    id = request.GET.get('id', '1')

    note = Note.objects.get(pk=id)
    # 获得本文的所有的标签，因为无论是用户GET还是POST请求都会用到它，所以把它放到前面
    tags = Tag.objects.filter(noteID=note)

    if(request.method == 'POST'):
        # 如果用户要保存数据
        # note = Note()
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # if note get the authorID then set the ID is -1. because at the
            # first step. we didn't hava build UC system.

            # if user forget to set note's type. we set it as default value 0
            if note.noteType == None:
                note.noteType = 0

            if note.color == None:
                note.color = "#000000"

            # set createtime
            note.createTime = timezone.now()

            try:
                note.save()
                # 获得用户提交的新标签
                newTags = form.cleaned_data["tags"]
                # TODO: not support chinese character
                newTags = newTags.replace(",", '|').replace(
                    ";", '|').replace(" ", "").replace("||", "|")
                newTags = newTags.split("|")

                oldTags = []
                for _tag in tags:
                    oldTags.append(_tag.tagName)

                # 如果想让一片文章所有的标签tags都变成最新的。需要先求一次
                # oldTags与newTags的差集，然后删除差集中的所有元素
                # 这样就可以删除所有旧的标签
                # 第二步：newTags 和oldTags进行求差集。然后把这些集合插入到数据库
                # 这样两步就可以实现了标签的更改。
                # Start！
                # first step
                print oldTags 
                print newTags
                print 156
                oldDiff = list(set(oldTags).difference(set(newTags)))  # oldTags中有而newTags中没有的
                # 批量删除
                # TODO 可能有删除性能瓶颈，查查批量删除
                for tag in oldDiff:
                    tagRecorder=Tag.objects.get(tagName=tag,noteID=note)
                    tagRecorder.delete()

                print 165
                print newTags 
                print oldTags

                newDiff=list(set(newTags).difference(set(oldTags)))  # newTags中有而oldTags中没有的
                print 169
                # 批量插入操作
                insert_list = []
                for tag in newDiff:
                    # 此处逻辑不严，如果tag为空，还会插入的，这样没有意义
                    if tag != "":
                        insert_list.append(Tag(tagName=tag, noteID=note))
                # print insert_list
                Tag.objects.bulk_create(insert_list)
                print 178

                # return redirect(reverse('note.views.view',
                # args=['id',note.id]))
                return HttpResponseRedirect('/view?id=' + str(note.id))
                # return HttpResponse(note.content)
                # return HttpResponse("data is valid and we store it in the
                # database. The id of this note is:"+str(note.id))
            except Exception, e:
                # return HttpResponseRedirect('/view?id='+str(note.id
                return HttpResponse("data is valid and we store it in the database failed. %s " %e)
            finally:
                pass
            return HttpResponse("data is valid.")
        else:
            return HttpResponse("data is valid.")
    else:
        # 首先要获得更新文章的id，这个id要传进来的。
        form = NoteForm(instance=note)

        tags_str = ""
        for tag in tags:
            tags_str += "|" + tag.tagName
        # set the tag's value then show it in update view
        # form.cleaned_data['tags'] = tags_str
        form.fields["tags"].initial = tags_str[1:]

        return render(request, 'update.html', {'form': form, 'id': note.id, 'tags_str': tags_str})
    # 这个时候 基本上实现了update的进入操作，但是更新完文章，要保存。下一步要实现保存

# 删除一篇文章


def delete(request):
    id = request.GET.get('id', '0')
    note = get_object_or_404(Note, pk=id)
    try:

        note.delete()
        return HttpResponse("删除成功！")
    except:
        return HttpResponse("删除失败！")
