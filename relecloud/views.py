from django.shortcuts import render, HttpResponse
from . import models
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from email.message import EmailMessage
import ssl
import smtplib

#Añadimos el path de las static files
STATIC_URL = settings.STATIC_URL
STATICFILES_DIRS = settings.STATICFILES_DIRS


def index(request):
    #Devolvemos el template con las reviews
    reviews = models.Review.objects.all()
    return render (request, 'index.html', {'reviews':reviews})

def about(request):
    #Obtenemos los destinations de la base de datos
    destinations = models.Destination.objects.all()
    #Añadimos a todos los destinations la url de las static files que es el name .jpg
    for destination in destinations:
        destination.image = 'images/' + destination.name + '.jpg'
    return render (request, 'about.html', {'destinations':destinations})

def reviews(request):
    #Devolvemos el template con los destinations
    reviews = models.Review.objects.all()
    return render (request, 'resenas.html', {'reviews':reviews})


def new_review(request):
    #Obtenemos del post los datos del formulario nombre y review
    name = request.POST['name']
    email = request.POST['email']
    review_txt = request.POST['review']
    #Creamos el objeto review para guardarlo en la base de datos
    review = models.Review(name=name, review=review_txt, email=email)
    review.save()
    review = models.Review.objects.all()

    email_sender = 'relecloud40@gmail.com'
    email_password = 'ydxt vwnk kdun vfgz'
    email_receiver = email

    subject = 'Gracias por tu review ' + name
    body = 'Gracias por tu review ' + name + '.\n\n' + 'Tu review es: ' + review_txt + '.\n\n' + 'Un saludo.'


    # Setting up the email message
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)  # Assuming plain text. Change or add HTML here if needed

    # Sending the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(email_sender, email_password)
        server.send_message(em)  # Corrected to pass only the EmailMessage object

    return redirect('reviews')


def info(request, destination_id):
    #Obtenemos el destination de la base de datos
    destination = models.Destination.objects.get(id=destination_id)
    #Añadimos a todos los destinations la url de las static files que es el name .jpg
    destination.image = 'images/' + destination.name + '.jpg'
   
    return render (request, 'info.html', {'destination':destination,destination.image:destination.image, destination.name:destination.name, destination.description:destination.description, destination.id : destination.id})
