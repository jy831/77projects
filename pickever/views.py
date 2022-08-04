from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Music, Report
from .forms import MusicForm, ReportForm

def index(request):
    music_list = Music.objects.order_by('create_date')
    context = {'music_list': music_list}
    return render(request, 'pickever/music_list.html', context)

@login_required(login_url='common:login')
def music_create(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            music = form.save(commit=False)
            music.author = request.user
            music.create_date = datetime.datetime.now()
            music.save()
            return redirect('pickever:index')
    else:
        request_user_last_music = Music.objects.filter(id=request.user.id)
        if request_user_last_music.exists() == False:
            form = MusicForm()
            context = {'form': form}
            return render(request, 'pickever/music_form.html', context)
        else:
            request_user_last_music = request_user_last_music.order_by('create_date')
            request_user_last_music = request_user_last_music.last()
            last_music_time = request_user_last_music.create_date
            time_diff = datetime.datetime.now() - last_music_time
            if time_diff.seconds >= 600:
                form = MusicForm()
                context = {'form': form}
                return render(request, 'pickever/music_form.html', context)
            else:
                messages.error(request, '10분이 지나야 어쩌구')
                return redirect('pickever:index')


@login_required(login_url='common:login')
def music_vote(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.user == music.author:
        messages.error(request, '본인이 등록한 노래는 추천할수 없습니다')
    else:
        music.voter.add(request.user)
    return redirect('pickever:index')

def music_delete(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.user != music.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', music_id=music.id)
    music.delete()
    return redirect('pickever:index')


@login_required(login_url='common:login')
def report_create(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporting = request.user
            report.reported = music.author
            report.reported_music = music.title
            report.report_date = datetime.datetime.now()
            report.save()
            return redirect('pickever:index')
    else:
        form = ReportForm()
    context = {'form': form}
    return render(request, 'pickever/report_form.html', context)