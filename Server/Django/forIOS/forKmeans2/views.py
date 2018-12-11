from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .features import get_feature

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            #print(get_feature(request.FILES['file']))
            print("******extract get_feature succeed 1.0******")
            return HttpResponseRedirect('/forKmeans/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
