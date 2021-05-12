from pytube import YouTube
import os
from django.http import FileResponse
from django.shortcuts import render, redirect
import pafy

def index(request):
    if request.method == 'POST':
        url = request.POST.get('ytlink')
        embedlink = url.replace("watch?v=","embed/")
        video = pafy.new(url)
        print(video.title)
        context = {
            'yobj':video,
            'embedlink':embedlink
        }
        return render(request,'home.html',context)        
    return render(request,'index.html')


# def index(request):
#     return render(request,'index.html')