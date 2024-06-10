from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm
# Create your views here.

def index(request):
    items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in items)
    return render(request, 'index.html', {'items': items, 'total_calories': total_calories})

def add_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodItemForm()
    return render(request, 'add_item.html', {'form': form})

def delete_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    item.delete()
    return redirect('index')

def reset_items(request):
    FoodItem.objects.all().delete()
    return redirect('index')