from django.http import HttpResponse
from django.template import loader
import datetime
from members.models import Member


# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    mymembers1 = Member.objects.values_list('firstname') #Return specfic column
    mymembers2 = Member.objects.filter(firstname='Kundan').values() # return specific column
    # mydata = Member.objects.filter(lastname='Refsnes', id=2).values() # AND condition
    # mydata1 = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values() # OR condition
    # Member.objects.filter(firstname__startswith='L'); # WHERE firstname LIKE 'L%'; # case sensetive
    # mydata = Member.objects.filter(firstname__istartswith='s').values() # WHERE firstname LIKE 's%'; # case insensetive
    # mydata = Member.objects.filter(firstname__contains='bias').values() # WHERE firstname LIKE '%bias%'; #case sensetive
    # mydata = Member.objects.filter(lastname__icontains='ref').values() # WHERE lastname LIKE '%ref%'; # case insensetive
    # mydata = Member.objects.filter(firstname__endswith='s').values() #WHERE firstname LIKE '%s'; # case sensetive
    # mydata = Member.objects.filter(firstname__iendswith='s').values() #WHERE firstname LIKE '%s'; # case insensetive
    # mydata = Member.objects.filter(firstname__exact='Emil').values() # WHERE firstname = 'Emil'; # case sensetive
    # mydata = Member.objects.filter(firstname__iexact='emil').values() #WHERE firstname = 'emil'; # case insensetive
    # mydata = Member.objects.filter(firstname__in=['Tobias', 'Linus', 'John']).values()  # WHERE firstname IN ('Tobias', 'Linus', 'John'); # case sensetive
    # mydata = Member.objects.filter(id__gt=3).values() # WHERE id > 3;
    # mydata = Member.objects.filter(id__gte=3).values() # WHERE id >= 3;
    # mydata = Member.objects.filter(id__lt=3).values() #  WHERE id < 3;
    # mydata = Member.objects.filter(id__lte=3).values() # WHERE id <= 3;
    # mydata = Member.objects.filter(id__range=(2, 4)).values() # WHERE id BETWEEN 2 AND 4;
    # mydata = Member.objects.filter(firstname__range=('G', 'M')).values() # WHERE id BETWEEN 'G' AND 'M';
    # mydata = Member.objects.all().order_by('firstname').values() # SELECT * FROM members ORDER BY firstname; # ascending order
    # mydata = Member.objects.all().order_by('-firstname').values() # SELECT * FROM members ORDER BY firstname DESC; # descending order
    # mydata = Member.objects.all().order_by('lastname', '-id').values() # SELECT * FROM members ORDER BY lastname ASC, id DESC; # Multiple Order Bys




    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
        'mymembers1': mymembers1,
        'mymembers2': mymembers2,
    }
    print(mymembers)
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return  HttpResponse(template.render())

def testing(request):
    template = loader.get_template("filter_example.html")
    context = {
        'prices': [70, 35, 52],
        'fruits': ['Apple', 'Banana', 'Cherry', 'Kiwi', 'Orange'],
        'vegetables': ['Asparagus', 'Broccoli', 'Carrot'],
        'name': "Capt'n Jack",
        'animal': 'lion',
        'name1': 'Tobias',
        'name2': 'Kundan Kotangale',
        'colors': ['Red', 'Green', 'Blue', '', 'Yellow'],
        'colors1': ['Red', None, 'Blue', '', 'Yellow'],
        'cars': [
            {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
            {'brand': 'Volvo', 'model': 'XC90', 'year': 2022},
            {'brand': 'Volvo', 'model': 'P1800', 'year': 1962},
            {'brand': 'Ford', 'model': 'Focus', 'year': 2004},
        ],
        'totalsum': 40,
        'heading': 'Hello &lt;i>my&lt;/i> World!',
        'var1': 'John\nDoe',
        'size': 26214400,
        'firstname': 'kundan',
        'lastname': 'Refsnes',
        'mynumber': 7.122489,
        'mynumber1': 981358286,
        'mynumber3': 75641,
        'cars1': [
            {'brand': 'Ford', 'model': 'Mustang', 'year': 1964},
        ],
        'mytext': 'Hello\nmy name is Leo.\n\nI am a student.',
        'phone': '555-autmobile',
        'arr': [0, 1, 2],
        'text': 'Hi, my name is Linus',
        'mytext1': '&lt;h1>Welcome to &lt;b>MY&lt;/b> World!&lt;/h1>',
        'mydate': datetime.datetime.now(),
        'mybirthdate': datetime.datetime(1993, 10, 1),
        'date1': datetime.datetime(2022, 6, 8, 9, 30),
        'date2': datetime.datetime(2022, 6, 8, 13, 45),
        'marslanding': datetime.datetime(2050, 5, 17),
        'moonlanding': datetime.datetime(1969, 7, 20),
        'date11': datetime.datetime(2022, 6, 8, 17, 39),
        'date22': datetime.datetime(2022, 6, 8, 8, 13),
        'mytext2': 'Hello my friend, do you like DJANGO',
        'mytext3': '&lt;h1>Hello my friend, do you like DJANGO?&lt;/h1>',
        'food': ['Seafood', ['Fish', 'Lobster'], 'Vegetables', ['Carrots', 'Broccoli']],
    }
    return HttpResponse(template.render(context,request))

def filter_django(request):
    template = loader.get_template("filter_django.html")
    return HttpResponse(template.render())

def django_tags(request):
    template = loader.get_template("django_tags.html")
    context = {
        'x': '',
        'y': 'Ford',
        'z': 'BMW',
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange',"Orange"],
        'mycar': {
            'brand': 'Ford',
            'model': 'Mustang',
            'year': '1964',
        },
        'cars': ['Ford', 'Volvo', 'BMW'],
        'colors': ['Red', 'Green', 'Blue'],
        'myvar': 1,
        'cars1': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Sierra',
                'year': '1981',
            },
            {
                'brand': 'Volvo',
                'model': 'XC90',
                'year': '2016',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }],
        'mylist': [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5],
    }
    return HttpResponse(template.render(context,request))

def template_test(request):
    templates = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(templates.render(context,request))