from django.shortcuts import render
import stripe
from accounts.models import Order
from madewithlove import settings
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response 







class PaymentView(APIView):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    permission_classes = (permissions.AllowAny,)
 
    def post(self, request, *args, **kwargs):
        #  order = Order.objects.get(user=self.request.user, ordered=False)
         token = request.data["token"]["id"]
         print(token,'tokeeeeeen')
         a="tok_1I3RymCNmtNvriYQ4O5ZQrKs tokeeeeeen"
         
         stripe.Charge.create(
            amount=200,
            currency="usd",
            source=token,
            description="My First Test Charge (created for API docs)",
            receipt_email= request.data["token"]["email"]

         )
         return Response('ok')
