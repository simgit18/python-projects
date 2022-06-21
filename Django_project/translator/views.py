from django.shortcuts import render
from django.views import generic
from googletrans import Translator



def TranslatorView(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output=Translator()
        output = output.translate(original_text, dest='de').text
        return render(request, 'translator.html', {'output_text': output, 'original_text':original_text})
    
    else:
        return render(request, 'translator.html')
