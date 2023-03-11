from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from .forms import ArticleForm

def liste_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'liste_articles.html', context)




def detail_article(request, id_article):
    article = get_object_or_404(Article, id=id_article)
    context = {
        'article': article
    }
    return render(request, 'detail_article.html', context)



def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'ajouter_article.html', {'form': form})


def modifier_article(request, id_article):
    article = Article.objects.get(id=id_article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('detail_article', id_article=id_article)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'modifier_article.html', {'form': form, 'article': article})


def supprimer_article(request, id_article):
    article = get_object_or_404(Article, id=id_article)
    article.delete()
    return redirect('liste_articles')
