from django.shortcuts import render

from home.models import Video


def home_view(request):
    # Get your video object however appropriate for your app
    video = Video.objects.first()  # Or some other query

    return render(request, 'home/home.html', {
        'video': video,
    })