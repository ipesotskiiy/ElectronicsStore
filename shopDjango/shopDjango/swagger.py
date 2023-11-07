from django.utils.module_loading import import_module
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from django.conf import settings

from mainapp.views import Registration, EmailVerify, ProfileView
from order.views import BasketView, CheckoutView, AddToBasketView, DeleteFromCartView, ChangeQTYView
from product.views import ProductDetailView, CategoryDetailView

schema = APISpec(
    title=' Electronics Store Swagger',
    version='1.0',
    openapi_version='3.0.2',
    plugins=[MarshmallowPlugin()],
)

schema.path(path='user/registration/', view=Registration.as_view(), operations={
    'get': {
        'description': 'Get the registration page.',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    },
    'post': {
        'description': 'Process user registration.',
        'requestBody': {
            'content': {
                'application/json': {
                    'schema': {'email': 'string',
                               'first_name': 'string',
                               'last_name': 'string',
                               'birth_day': 'date',
                               'password1': 'string',
                               'password2': 'string'}
                }
            }
        },
        'responses': {
            '200': {
                'description': 'Successful response'
            },
            '400': {
                'description': 'Invalid request'
            }
        }
    }
}
            )

schema.path(path='user/confirm_email/', view=EmailVerify.as_view(), operations={
    'get': {
        'description': 'Get the email verify page.',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='user/profile', view=ProfileView.as_view(), operations={
    'get': {
        'description': 'Get profile page.',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='orders/basket', view=BasketView.as_view(), operations={
    'get': {
        'description': 'Get basket page',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='orders/checkout', view=CheckoutView.as_view(), operations={
    'get': {
        'description': 'Get checkout page',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='add-to-basket/<str:ct_model>/<str:slug>/', view=AddToBasketView.as_view(), operations={
    'get': {
        'description': 'Add product to basket',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='remove-from-basket/<str:ct_model>/<str:slug>/', view=DeleteFromCartView.as_view(), operations={
    'get': {
        'description': 'Delete product from basket',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='change-quantity/<str:ct_model>/<str:slug>/', view=ChangeQTYView.as_view(), operations={
    'post': {
        'description': 'Delete product from basket',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='products/<str:ct_model>/<str:slug>/', view=ProductDetailView.as_view(), operations={
    'get': {
        'description': 'Get product page',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})

schema.path(path='category/<str:slug>/', view=CategoryDetailView.as_view(), operations={
    'get': {
        'description': 'Get all products from category',
        'responses': {
            '200': {
                'description': 'Successful response'
            }
        }
    }
})
