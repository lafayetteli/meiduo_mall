from goods.models import SKU
from celery_tasks.main import app
from meiduo_mall.utils.categories import get_categories
from meiduo_mall.utils.breadcrumb import get_breadcrumb
import os
from django.shortcuts import render
from django.conf import settings

def generate(sku_id):
    sku = SKU.objects.get(pk = sku_id)
    categories = get_categories()
    breadcrumb = get_breadcrumb(sku.category)
    spu = sku.spu
    specs = sku.specs.order_by('id')
    skus = spu.skus.order_by('id')
    sku_options = {}
    sku_option = []
    for sku1 in skus:
        infos = sku1.specs.order_by('spec_id')
        option_key = []
        for info in infos:
            option_key.append(info.option_id)

            if sku.id == sku1.id:
                sku_option.append(info.option_id)
        sku_options[tuple(option_key)] = sku1.id

    specs_list = []
    for index, spec in enumerate(specs):
        option_list = []
        for option in spec.options.all():

            sku_option_temp = sku_option[:]

            sku_option_temp[index] = option.id

            option.sku_id = sku_options.get(tuple(sku_option_temp), 0)

            option_list.append(option)

        spec.option_list = option_list

        specs_list.append(spec)

    context = {
        'sku': sku,
        'categories': categories,
        'breadcrumb': breadcrumb,
        'category_id': sku.category_id,
        'spu': spu,
        'specs': specs_list
    }
    response = render(None, 'detail.html', context)
    html_str = response.content.decode()

    file_name = os.path.join(settings.BASE_DIR, 'static/detail/%d.html' % sku.id)

    with open(file_name, 'w') as f1:
        f1.write(html_str)
# @app.tasks(name = 'generate_detail_html',bind = True ,retry_backoff = 2)
# def generate_detail_html(self,sku_id):
#     try:
#         generate(sku_id)
#     except Exception as e:
#         self.retry(exc=e,max_retries=3)
@app.task(name='generate_detail_html', bind=True, retry_backoff=2)
def generate_detail_html(self, sku_id):
    try:
        generate(sku_id)
    except Exception as e:
        self.retry(exc=e, max_retries=3)