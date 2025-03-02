from django.shortcuts import render
from products.models import Product,Brand,Catageory
from django.db.models import F
from django.http import HttpResponse
from django.template import loader


def display(request,product_P_Id):
    product_details=Product.objects.filter(P_Id=product_P_Id).values()
    
    
    context = {
        "product_details": product_details,
    }
    
    return render(request, "product_details.html", context)

def index(request):
    product_list = Product.objects.all()
    
    context = {
        "product_list": product_list,
    }
    
    return render(request, "products.html", context)

def catageory(request):
    category_list = Catageory.objects.all()
    
    context = {
        "category_list": category_list,
    }
    
    return render(request, "catageory.html", context)

def sub_categeories(request,catageory_Cat_Id):
    sub_categeories=Catageory.objects.filter(Parent__isnull=False,Parent=catageory_Cat_Id).values(
    parent_cat=F('Parent__Cat_name'), 
    sub_cat=F('Cat_name')
)
    
    context = {
        "sub_categeories": sub_categeories,
    }
    
    return render(request, "sub_categeories.html", context)




from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def filter(request):
    all_categories = Product.objects.select_related('Cat_id').values_list('Cat__Cat_name',flat=True).distinct()
    category_filter = request.GET.get('cat_name', 'All')

    categories = Catageory.objects.all()
    products = Product.objects.select_related('Cat').order_by('P_name').all()
    page = request.GET.get('page', 1)

    
    
    if category_filter !='All':
        
        products = products.filter(Cat__Cat_name=category_filter).order_by('P_name')
        
    if category_filter =='All':
        products = Product.objects.select_related('Cat').order_by('P_name').all()
        
    paginator = Paginator(products, 4)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  
   

   

    context = {
        "page":page,
        "products": products,
        "categories": categories,
        "all_categories": all_categories,
        "selected_name": category_filter,
       
    }
    print(category_filter)
    return render(request, "filter.html", context)


