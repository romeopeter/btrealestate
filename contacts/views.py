from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

  # Check if user has made inquiry already
  if request.user.is_authenticated:
    user_id = request.user.id
    has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
    if has_contacted:
      messages.error(request, 'You have already made an enquiry for this listing')
      return redirect('/listings/'+listing_id)


  contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

  contact.save()

  # Email parameters
  subject = 'Property listing Enquiery'
  message = 'There has been an enquiry listing for ' + listing + '. Sign into admin panel for info'
  sender = settings.EMAIL_HOST_USER
  recipient_email = [realtor_email]
  
  # Send email
  send_mail(subject, message, sender, recipient_email)


  messages.success(request, 'Your request has been submitted, a realtor will get back to you.')

  return redirect('/listings/'+listing_id)