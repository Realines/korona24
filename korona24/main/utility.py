import pytils.translit
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.template import loader
from django.core.mail import send_mail, BadHeaderError 

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

def compress(image):
    if(image is None):
        return image
    im = Image.open(image)
    im = im.convert('RGB')
    filename = image.name.replace('png','jpg')
    # create a BytesIO object
    im_io = BytesIO()  
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70)  
    # create a django-friendly Files object
    new_image = File(im_io, filename) 
    return new_image



def application_send_mail(message ,email): 
    subject = 'Новая заявка с вашего сайта!' 
    html_message = loader.render_to_string('main/email.html',{
                'subject':   subject,
                'message':   message
            }
        ) 
    print(send_mail(subject, message,'info@adrenaline-krsk.ru', [email],fail_silently=True,html_message=html_message))