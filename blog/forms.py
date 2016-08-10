from django import forms
from blog.models import Comment, Post


class CommentModelForm(forms.ModelForm):
    #form field 추가 가능.
    #e.g) tags = forms.CharField()

    class Meta: #model from은 meta정보가 먼저 진행됨
        model = Comment
        fields = ['author', 'message', 'jjal'] #post의 존재를 모른다.

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'created_at']

class CommentForm(forms.Form):
    author = forms.CharField()
    message = forms.CharField(widget=forms.Textarea) #textfield가 없음. 때문에 위젯을 설정한다.
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None) #좌) 수정할 arguments
        super(CommentForm, self).__init__(*args, **kwargs) #2, 3 문법. *** 이렇게 필드셋업이 끝난 이후에만 각 필드(아래)에 접근 가능하다.

        if self.instance:
            self.fields['message'].initial = self.instance.message
            self.fields['author'].initial = self.instance.author

        else:
            self.instance = Comment()

        #save라는 instance는 존재하지 않기 때문에 save 설정해줌.
        #
    def save(self, commit=True):
        self.instance.author = self.cleaned_data['message']
        self.instance.message = self.cleaned_data['author']
        if commit:
            self.instance.save()
        return self.instance


