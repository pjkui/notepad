from django import forms
from note.models import Note
class AddForm(forms.Form):
	# """docstring for AddNote"""
	title = forms.CharField(max_length=40)
	color = forms.CharField(max_length=10)
	# author_id = forms.IntegerField()
	# noteType = forms.IntegerField()
	# createTime = forms.DateTimeField()
	# publish = forms.DateTimeField()
	# content_text = forms.CharField(widget=forms.Textarea())
	# class Meta:
	# 	model = Note
	# 	fields = ('title','color','author_id','noteType','content')
	# 	widgets = {
	# 		'name': Textarea(attrs={'cols': 80, 'rows': 20}),
	# 	}
class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title','color','noteType','content']
		widgets={
			'content':forms.Textarea(),
		}