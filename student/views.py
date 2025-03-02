from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from student.models import Student,Semester,Marks,Subject
from django.db.models import Avg,Sum,FloatField,Count,ExpressionWrapper


# def student(request):
#     return HttpResponse("Hello, world. You're at the student index.")

def display(request,student_id):
    Marks_list=Student.objects.filter(id=student_id).annotate(sem_percentage=ExpressionWrapper((Sum('marks__Marks') / Count('marks__Sub_Id')),output_field=FloatField())).values('marks__Sem_Id','sem_percentage')
    context = {
        "Marks_list": Marks_list,
    }
    
    
    return render(request, "marks.html", context)
  

def index(request):
    student_list = Student.objects.all()
    
    context = {
        "student_list": student_list,
    }
    
    return render(request, "student.html", context)


from django.shortcuts import render, redirect
from .forms import StudentForm

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            usn = form.cleaned_data['usn']
            sem = form.cleaned_data['sem']
            
            # Redirect to next page with query params
            return redirect(f'result/?usn={usn}&sem={sem}')
    else:
        form = StudentForm()
    
    return render(request, 'form.html', {'form': form})

def result(request):
    usn = request.GET.get('usn')
    sem = request.GET.get('sem')
    
    details=Marks.objects.select_related('Student_Id','Sub_Id','Sem_Id').filter(Student_Id__Usn=usn,Sem_Id__Sem=sem).all()
    print(f"hi {details}")
    total_percentage=Marks.objects.filter(Student_Id__Usn=usn, Sem_Id__Sem=sem).aggregate(Avg("Marks", default=0)).values()
    if not details.exists():
        return render(request, 'result.html', {'no_recods':True})
    for d in details:
        
        name=d.Student_Id.Name
        current_sem=d.Student_Id.Current_sem
        
        print(d.Sem_Id.Sem)
    
    

    context={
        'usn': usn, 
        'sem': sem,
        'total_percentage':total_percentage ,
        'details':details,
        'name':name,
        'current_sem':current_sem,
        'no_records':False
        
       

            
    }

    return render(request, 'result.html', context)