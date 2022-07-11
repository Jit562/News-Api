from django.shortcuts import render
import requests

from .models import Exam, Student, School
from django.db.models import Max, Min, Avg , Sum ,Count , Q, F



# Create your views here.

# News Api Inpliment code here

API_KEYS = '46dd51b1fe554e938485ad6f3659e447'

def Home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
        URL = f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={API_KEYS}'
        response = requests.get(URL)
        data = response.json()
        articles = data['articles']

    else:
        URL = f'https://newsapi.org/v2/top-headlines?category={category}&category=business&apiKey={API_KEYS}'
        response = requests.get(URL)
        data = response.json()
        articles = data['articles']

    context = {
        'articles':articles
    }
    return render(request , 'home.html', context)

# News Api Inpliment code end Here    


# Stock Api Inpliment code here

def Index(request):
    # student = Student.objects.all()
    # student = Student.objects.all()[::5]
    # student = Student.objects.all()[0:5]
    
    # student = Student.objects.filter(name='Ramesh')

    # student = Student.objects.exclude(name='Ramesh')

    # student_data = Student.objects.exclude(amount=20000) & Student.objects.exclude(amount = 500)

    # student = Student.objects.order_by('amount') assending order by

    # student_data = Student.objects.order_by('-amount')  dessending order by

    # student_data = Student.objects.order_by('id').reverse()[:2]

    # student_data = Student.objects.order_by('id')[0:3]

    # student = Student.objects.values('name','city')

    # student = Student.objects.values_list('name','amount', named=True)

    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates('pass_date', 'month')

    # student_data = Student.objects.dates('pass_date', 'years')

    # student_data = Student.objects.dates('pass_date', 'days')

    # student = Student.objects.none()

    # qs1 = Student.objects.values_list('id','name','city','amount', named=True)
    # qs2 = School.objects.values_list('id','name','city','salary', named=True)
    # student = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id','name','city', named=True)
    # qs2 = School.objects.values_list('id','name','city', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id','name','city', named=True)
    # qs2 = School.objects.values_list('id','name','city', named=True)
    # student = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id','name','city', named=True)
    # qs2 = School.objects.values_list('id','name','city', named=True)
    # student = qs2.difference(qs1)

    # student = Student.objects.filter(id=1)& Student.objects.filter(city='Delhi')

    # student_data = School.objects.filter(id=1, city='Delhi')

    # student_data = Student.objects.filter(Q(id=1) & Q(city='Delhi'))

    # student = Student.objects.filter(Q(id=2) | Q(city='Delhi'))

    # student_data = Student.objects.get(pk=3)
    # student_data = Exam.objects.all()

    # student = Student.objects.first()
    # student = Student.objects.order_by('name').first()


    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.latest('')

    # Student.objects.filter(city__icontains ="delhi").update(amount=(F('amount')*0.6) + (F('amount')))

    # student = Student.objects.filter(city__icontains='delhi')

    # student = Student.objects.filter(id=2).values()
    # student = Student.objects.filter(id=2).values_list(flat=True)
    # student = Student.objects.values_list()

    # student = Student.objects.filter(city__icontains ="delhi").aggregate(Count('city'))
    student = Student.objects.filter(city__icontains ="delhi").count()

    print(student)

    # student = Student.objects.filter(city__icontains='delhi')
    
    

    # context = {
    #     'student':student,
    #     'student_data':student_data,
    # }
    return render(request, 'index.html' ,{'st':student})

# Stock Api Inpliment end code here


# Search code here
def Search(request):
    query = request.GET['query']
    st = Student.objects.filter(name__icontains=query)
    st1 = Student.objects.filter(city__icontains=query)
    st2 = Student.objects.filter(amount__icontains=query)

    st3 = st.union(st1, st2)
    return render(request, 'search.html', {'student':st3})



