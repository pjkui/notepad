# coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#import the add note form

from forms import AddForm

def index(request):
		if request.method == 'POST':
			# when user post form
			form =AddForm(request.POST) # when form contain data

			if form.is_valid() :
				#when data is valid
				
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
			#when user just visit , not post data to the site
			form = AddForm()
			return  render(request,'index_bootstrap.html',{'form':form})

