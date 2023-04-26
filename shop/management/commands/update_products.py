import logging

import requests

from django.core.management.base import BaseCommand
from django.db.models import F
from django_rq import job

from shop.models import Product

logger = logging.getLogger(__name__)


@job
def update_products():
    response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
    result = response.json()
    item = None
    for item in result:
        if item["Cur_Abbreviation"] == "USD":
            break

    if item is not None:
        for product in Product.objects.all():
            product.price_usd = (int((product.price / item["Cur_OfficialRate"])*100))/100
            product.save()

        # Product.objects.update(
        #     price_usd=F("price") * item["Cur_OfficialRate"]
        # )


class Command(BaseCommand):
    help = "Update products"

    def handle(self, *args, **options):
        update_products()
