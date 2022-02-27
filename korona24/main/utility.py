import pytils.translit
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.template import loader
from django.core.mail import send_mail, BadHeaderError 
import json

def translify(text):
    text = pytils.translit.translify(text)
    text = text.replace(' ', '_')
    text = text.replace("'", "")
    text = text.replace(",", "")
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace('.', '')
    text = text.replace(':', '-')
    return text.lower()

def cropping(image,crop, quality=70):
    if(image is None):
        return image
    im = Image.open(image)
    im = im.convert('RGB')
    filename = image.name.replace('png','jpg')
    # create a BytesIO object
    im_io = BytesIO()   
    crop_data = ()
    crop_list = crop.split(',') 
    for num in crop_list: 
        crop_data += (int(num),)
    print(crop_data)
    im = im.crop(crop_data)
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=quality)  
    # create a django-friendly Files object
    new_image = File(im_io, filename) 
    return new_image

def compress(image, quality=70):
    if(image is None):
        return image
    im = Image.open(image)
    im = im.convert('RGB')
    filename = image.name.replace('png','jpg')
    # create a BytesIO object
    im_io = BytesIO()  
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=quality)  
    # create a django-friendly Files object
    new_image = File(im_io, filename) 
    return new_image



def application_send_mail(message ,email,subject = 'Новая заявка с вашего сайта!'):  
    html_message = loader.render_to_string('main/email.html',{
                'subject':   subject,
                'message':   message
            }
        ) 
    print(send_mail(subject, message,'info@adrenaline-krsk.ru', [email],fail_silently=True,html_message=html_message))