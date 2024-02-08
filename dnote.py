"""
django notes.

step.1 ( installation)
pip install django

#####################

step.2 ( creating project / website )
django-admin startproject ap1
check all command --> python manage.py

#####################

step.3 ( running local server )
cd ap1
python manage.py runserver

#####################

step.4 ( creating new application )
cd ap1
django-admin startapp myapp1


#####################

step.5 ( installation new application in our project / website )

project ထဲက setting.py ထဲမှာရှိတဲ့ installed_apps  စာရင်းထဲကို application အမည် ထည့်ရမည်။

new application ၏ အမည်သည် myapp1 ဆိုပါစို့။
myapp1 ဟူ၍ ထည့်ပေးရမည်။

လိုအပ်ချက်အရ အမည် ပြောင်းလဲသည့်အခါ အမှားအယွင်းမဖြစ်စေရန်အတွက် application အမည်ကို အသေမထည့်ပေးသင့်ပါ။

သူ၏ အမည်သည် myapp1.apps.Myapp1Config ထဲတွင်ရှိသည်။

￼
#####################

website တစ်ခုဖြစ်လာတဲ့အခါ user name , password သိမ်းဖို့ database တည်ဆောက်ဖို့လိုအပ်ပါသည်။

#####################

step.6 ( creating database )
python manage.py migrate
( database (username , email, password တွေသိမ်းဖို့ row , column ) အလိုလို တည်ဆောက်ပေး )

#####################

step.7 (  creating super user account ) ( adminster account ) ( စီမံခန့်ခွဲမည့်သူ )
python manage.py createsuperuser
user name = admin
password  = y
email = abcfounder682@gmail.com

#####################

step.8 ( login to admin site ) ( ထိန်းချုပ်ရာနေရာ  )
python manage.py runserver
# /admin
# login ဝင်ကြည့် ( view site , log out, change password )

#####################

django
1. startproject
2. startapp

* project ထဲက setting.py ထဲမှာရှိတဲ့ installed_apps  စာရင်းထဲကို application အမည် ထည့်ရမည်။

manage.py
1. migrate
2. runserver
3. createsuperuser

#####################

step.1 ( creating new environmemnt )
>>py -m venv W

#####################

This will set up a virtual environment, and create a folder named "W" with subfolders and files, like this:
W
  Include
  Lib
  Scripts
  pyvenv.cfg

#####################

step.2 ( activate the environment )
>>W\Scripts\activate.bat

#####################

output

(W) C:\Users\User>

#####################

step.3 ( installation )

py -m pip install django

#####################

step.4 ( checking version )
py --version
django-admin --version

#####################



# step.7

python manage.py runserver

# wsgi.py

from django.http import HttpResponse

def x(request):
    return HttpResponse("Apples")


# urls.py
# use dot to search in same path ( use when same name with original package )

from .wsgi import x

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/", x)
]

### check product
http://127.0.0.1:8000/product/

#####################

1. environment
2. installation
3. W\Scripts\activate.bat
4. cd W
5. django-admin startproject shop
6. cd shop
7. test ( wsgi, urls )

#####################

1. W\Scripts\activate.bat
2. cd W, cd shop
3. database for user name, password ( super user )

4. django-admin startapp product
5. models ( table ---> name, price, stock, image )
object
attribute ( obj, class )
data ( variable ) / method ( fun )

product
data = name, price, stock, image
method = discount(),

6. admin register
7. install application(product)
8. makemigrations ( Create model Products )
9. migrate ( install app )
10. table ( admin site )

11. y function ( p.html )
12. urls link ( "product/" )

#####################

3. database for user name, password ( super user )

python manage.py migrate
python manage.py createsuperuser

user name = abc
email = abcfounder682@gmail.com
password = y

#####################

4. startapp fruitShop
cd W
cd shop
django-admin startapp product

#####################

5. product/models.py
from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=255)


#####################

6. product/admin.py

from django.contrib import admin
from .models import Fruit

admin.site.register(Fruit)


#####################

# 7. shop/setting.py
"product.apps.ProductConfig"

#####################

8. Create model

python manage.py makemigrations

Migrations for 'Fruit':
  product\migrations\0001_initial.py
    - Create model Fruit

#####################

9. install model

python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, product, sessions
Running migrations:
  Applying product.0001_initial... OK

#####################

10. table ( admin site )

from django.contrib import admin
from .models import Fruit

class FruitTable(admin.ModelAdmin):
    list_display = ("name", "price", "stock")

admin.site.register(Fruit, FruitTable)


#####################

11. y function ( p.html )

from .models import Product

def y(request):
    products = Product.objects.all()
    return render(request, "p.html", {"products": products})

#####################

# templates / p.html

<h1> Products </h1>

<ul>
    {% for product in products %}
            <img src={{ product.image }} style="width:50%">
            <li> {{ product.name }} ($ {{ product.price }}) </li>
            <li>stock( {{ product.stock }}  )</li>
    {% endfor %}
</ul>

#####################


<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  width: 40%;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

.container {
  padding: 2px 16px;
}
</style>
</head>

<body>
{% for product in products %}
<h2>{{ product.name }}</h2>
<div class="card">
    <img src={{ product.image }} style="width:100%">
        <div class="container">
            <h4><b>price ( ${{ product.price }} )</b></h4>
            <h4><b>Instock ( {{ product.stock }} )</b></h4>
            <p>About apples ...  ..   .... </p>
                <div class="card-action">
                    <a href="#">Order</a>
               </div>
       </div>
</div>
</body>
</html>
{% endfor %}

#####################

12. urls link
path('product/', x)

#####################

#####################

Extra


1. local server
python manage.py runserver

2. local server link
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/product/

3. ctrl + c
4. cd ---> change directory
5. apple's image link
https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80


#####################

#####################









# do not need
python manage.py makemigrations
python manage.py migrate



python manage.py runserver
http://127.0.0.1:8000/admin/








# templates / p.html

<h1> Products </h1>

<ul>
    {% for product in products %}
            <img src={{ product.image }} style="width:50%">
            <li> {{ product.name }} ($ {{ product.price }}) </li>
            <li>stock( {{ product.stock }}  )</li>
    {% endfor %}
</ul>






















<module 'django' from
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\django\\__init__.py'>















['',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\python310.zip',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\DLLs',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\lib',
'C:\\Users\\User\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\win32',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\win32\\lib',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\Pythonwin',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\lib\\site-packages']

['',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\python310.zip',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\DLLs',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\lib',
'C:\\Users\\User\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\win32',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\win32\\lib',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\Pythonwin',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0',
'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\\lib\\site-packages',
'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages
\\Python310\\site-packages\\django\\__init__.py']

path.append("'C:\\Users\\User\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\django")




"""