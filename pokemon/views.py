from django.shortcuts import render
from pokemon.models import Pokemon

# Create your views here.

#포켓몬 목록을 보여주고싶어함.  pokemon_list는 '모델명(소문자)_list'
def pokemon_list(request): #url로부터 요청이 들어옴. pokemon_list실행
    qs = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list' : qs,
        }) #template file // pokemon_list는 qs와 같다고 지정한 것 render는 pokemon_list:qs와 함께 pokemon/pokemon_list.html을 완성시키겠다

#render 메서드는 넘겨진 요청(request)과 blog/post_list.html 템플릿 받아 리턴된 내용이 브라우저에 보여지게 됩니다.