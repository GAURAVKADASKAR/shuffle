
import random
from django.shortcuts import render
from django import forms

# Define the form to accept rows, columns, and words
class MatrixForm(forms.Form):
    rows = forms.IntegerField(min_value=1)
    columns = forms.IntegerField(min_value=1)

# The view to handle matrix creation
def matrix_view(request):
    if request.method == 'POST':
        form = MatrixForm(request.POST)
        if form.is_valid():
            rows = form.cleaned_data['rows']
            columns = form.cleaned_data['columns']
            matrix = [[None for _ in range(columns)] for _ in range(rows)]

            return render(request, 'index.html', {'form': form, 'matrix': matrix})
    else:
        form = MatrixForm()

    return render(request, 'index.html', {'form': form})

