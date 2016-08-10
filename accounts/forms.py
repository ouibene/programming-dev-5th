from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationFrom):
    #email만 받고싶을 때. Unique의 여부는 알아서 체크해준다.
    username = fomrs.EmailField(label="Email")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = user.username
        if commit:
            user.save()
        return user