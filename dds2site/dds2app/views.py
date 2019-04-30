from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AttachmentForm


def index(request):
    return HttpResponse("dds2app index!!!")


def upload_file(request):
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return redirect('index')
    else:
        form = AttachmentForm()
    return render(request, 'dds2app/upload_file.html', {'form': form})
