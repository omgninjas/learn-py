from django.shortcuts import render, redirect
from collection.forms import QuoteForm
from collection.models import Quote
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404



def create_quote(request):
    form_class = QuoteForm
    
    if request.method == 'POST':
        
        form = form_class(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            
            quote.user = request.user
            quote.slug = slugify(quote.author)
            
            quote.save()
            
            return redirect('quote_detail', slug=quote.slug)
        
        else:
            form = form_class()
            
        return render(request, 'quotes/create_quote.html', {
            'form': form,
            
        })

# Create your views here.
def index(request):
    # defining the variable
    quotes = Quote.objects.all()
    # this is your new view 
    return render(request, 'index.html', {
        'quotes' : quotes,
    })
    
    
def quote_detail(request, slug):
    # grab the object
    quote = Quote.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'quotes/quote_detail.html', {
        'quote': quote,
    })
    
@login_required    
def edit_quote(request, slug):
    quote = Quote.objects.get(slug=slug)
    
    if quote.user != request.user:
        raise Http404
        
    form_class = QuoteForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_detail', slug=quote.slug)
    else:
        form = form_class(instance=quote)
        
    return render(request, 'quotes/edit_quote.html', {
        'quote': quote,
        'form' : form,
        
    })
    
def browse_by_name(request, initial=None):
    if initial:
        quotes = Quote.objects.filter(
            name__istartswith==initial).order_by('name')
    else:
        quotes = Quotes.objects.all().order_by('name')