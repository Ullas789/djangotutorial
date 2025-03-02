from products.models import Product,Brand,Catageory
from django.db.models import F

# list all products
q0=Product.objects.values_list('P_name',flat=True)
print(q0)

# list all products And filter based on cat_id  or given a catgeory id ,list all the products
q1=Product.objects.filter(Cat_id='20').values('P_name','Cat_id')
print(q1)


# list all products and filtrer based on cat_name
q2=Product.objects.filter(Cat__Cat_name='android').all()
for q in q2:
    print(q.P_name)
# list all Catageory
q=Product.objects.select_related('Cat_id').values_list('Cat__Cat_name',flat=True).distinct()
print(q)
# list all category and their products
q3=Product.objects.select_related('Cat_id').values('P_name','Cat__Cat_name').all()
for q in q3:
    print(q)


#list all products and print brand name
q4=Product.objects.select_related('B_id').values('P_name','B__B_name')
print(q4)


# list all sub categories under a category  based on parent_cat_id
q5=Catageory.objects.filter(Parent_id=10).values('Parent','Cat_name')
print(q5)


# list all sub catagories under a list of categories based on id
q6=Catageory.objects.filter(Parent_id=10).values('Cat_Id','Cat_name')
print(q6)


# list all categories and sub_categories name

q7 = Catageory.objects.filter(Parent__isnull=False).values(
    parent_cat=F('Parent__Cat_name'), 
    sub_cat=F('Cat_name')
)

for q in q7:
    print(q)

q8= Catageory.objects.all()
for q in q8:
    print(q.Cat_name)