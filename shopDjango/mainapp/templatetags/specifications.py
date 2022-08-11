from django import template
from django.utils.safestring import mark_safe

from product.models import MobilePhone

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'laptop': {
        'Количество слотов оперативной памяти': 'number_of_ram_slots',
        'Тип видеокарты': 'video_card_type',
        'Видеопроцессор': 'video_processor',
        'Тип памяти': 'memory_storage_type',
        'Частота обновления экрана в герцах': 'screen_refresh_rate_hertz',
        'Размер экрана': 'screen_size',
        'Разрешение экрана': 'screen_resolution',
        'Матрица экрана': 'screen_matrix',
        'Процессор': 'cpu_name',
        'Оперативная память в гигабайтах': 'ram_in_gigabytes',
        'Вес': 'weight',
        'Операционная система': 'operating_system',
        'Ёмкость аккумулятора в миллиамперах': 'battery_capacity_in_milliamps',
        'Встроенная память в гигабайтах': 'built_in_memory_in_gigabytes',
    },
    'mobilephone': {
        'Количество камер': 'number_of_camera',
        'Количество SIM-карт': 'number_of_sim_cards',
        'Частота обновления экрана в герцах': 'screen_refresh_rate_hertz',
        'Размер экрана': 'screen_size',
        'Разрешение экрана': 'screen_resolution',
        'Матрица экрана': 'screen_matrix',
        'Процессор': 'cpu_name',
        'Оперативная память в гигабайтах': 'ram_in_gigabytes',
        'Вес': 'weight',
        'Операционная система': 'operating_system',
        'Ёмкость аккумулятора в миллиамперах': 'battery_capacity_in_milliamps',
        'Встроенная память в гигабайтах': 'built_in_memory_in_gigabytes',
    },
    'freezer': {
        'Общий полезный объем в литрах': 'total_usable_volume_in_liters',
        'Минимальная температура в градусах Цельсия': 'minimum_temperature_in_degrees_Celsius',
        'Уровень шума в децибелах': 'noise_level_in_decibels',
        'общее количество ящиков': 'total_number_of_boxes',
        'Количество ящиков': 'number_of_drawers',
        'Количество ящиков с дверцами': 'number_of_drawers_with_doors',
        'Потребляемая мощность в ваттах': 'power_consumption_in_watts',
        'Хладагент': 'refrigerant'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
