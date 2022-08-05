from django.shortcuts import render

# Create your views here.

# 검색창 메인.
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        return render(request, 'search/search.html', {})
    return render(request, 'search/search.html')