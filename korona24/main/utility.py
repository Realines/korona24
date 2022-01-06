import pytils.translit
from io import BytesIO
from PIL import Image
from django.core.files import File

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
    print(filename)
    print(new_image )
    return new_image