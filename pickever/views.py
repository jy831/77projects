from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Music
from .forms import MusicForm

def index(request):
    music_list = Music.objects.order_by('create_date')
    context = {'music_list': music_list}
    return render(request, 'pickever/music_list.html', context)

def music_create(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            music.create_date = timezone.now()
            music.save()
            return redirect('pickever:index')
    else:
        form = MusicForm()
    context = {'form': form}
    return render(request, 'pickever/music_form.html', context)