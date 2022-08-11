from django.forms import ModelForm, ValidationError
from django.utils.safestring import mark_safe
from PIL import Image
from product.models import Product
from django.utils.translation import gettext_lazy as _


class ImageAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].help_text = mark_safe(
            _('<span style="color:red; font-size:15px;"> Please upload an image with a resolution greater than {}x{} but less than {}x{}</span>').format(
                *Product.MIN_RESOLUTION_FOR_IMAGE, *Product.MAX_RESOLUTION_FOR_IMAGE)
        )

    def clean_image(self):
        image = self.cleaned_data['photo']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION_FOR_IMAGE
        max_height, max_width = Product.MAX_RESOLUTION_FOR_IMAGE
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError(_('File size too large. Your file size {} maximum file size{}').format(image.size,
                                                                                                         Product.MAX_IMAGE_SIZE))
        if img.height < min_height or img.width < min_width:
            raise ValidationError(
                _('<span style="color:red; font-size:15px;">Image resolution is less than minimum!'
                  'Your image size {}x{} minimum resolution {}x{}</span>').format(img.height, img.width,
                                                                                  min_height, min_width))
        if img.height > max_height or img.width > max_width:
            raise ValidationError(
                _('<span style="color:red; font-size:15px;">Image resolution is less than minimum!'
                  'Your image size {}x{} minimum resolution {}x{}</span>').format(img.height, img.width,
                                                                                  min_height, min_width))
        return image
