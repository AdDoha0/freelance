from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

import logging


from .models import *
from .serializers import *


# Создаем логгер
logger = logging.getLogger(__name__)

class IsExecutor(permissions.BasePermission):
    '''
    проверяется, является ли владелец объекта (obj.owner) тем же пользователем,
    который делает запрос (request.user). Если это так, метод возвращает True,
    что означает, что пользователь имеет доступ к этому объекту.
    Если нет, метод возвращает False, и доступ к объекту будет запрещен.
    '''

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        # это константа, которая используется для обозначения кода состояния HTTP 200 (OK).
        return Response(status=status.HTTP_200_OK)


# --------------------executor------------------------

class ExecutorRetrieveView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class ExecutorUpdateView(generics.UpdateAPIView):
    # queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = (IsExecutor, )


    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Executor.objects.filter(user=user)

        raise PermissionDenied


class ExecutorCreateView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer



class ExecutorListView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer





# --------------------cutomer------------------------

class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly




class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer



class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# --------------------service------------------------

class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ServiceListView(generics.ListAPIView):
    # queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()

        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        executor = params.get('executor', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        return queryset



# ---------------------Order------------------------

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class OrderListView(generics.ListAPIView):

    serializer_class = OrderSerializer


    def get_queryset(self):
        queryset = Order.objects.all()

        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        customer = params.get('customer', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        return queryset



# ----------------Tag--------------------------


class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



# ----------------Ordering------------------------


class OrderingRetrieveView(generics.RetrieveAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingUpdateView(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class OrderingCreateView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class OrderingListView(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


# ----------------Message------------------------

class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()
        params = self.request.query_params

        customer = params.get('customer', None)
        executor = params.get('executor', None)
        from_date = params.get('to_date', None)
        to_date = params.get('to_date', None)


        if executor:
            queryset = queryset.filter(executor_id=executor)

        if customer:
            queryset = queryset.filter(customer_id=customer)

        if from_date:
            queryset = queryset.filter(msg_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(msg_date__lte=to_date)

        return queryset





# ----------------Ticket------------------------

class TicketRetrieveView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer



# ----------------Review------------------------


class ReviewRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ReviewListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = ReviewSerializer


# ----------------Authoring------------------------


class AuthoringRetrieveView(generics.RetrieveAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


class AuthoringUpdateView(generics.UpdateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class AuthoringCreateView(generics.CreateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class AuthoringListView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer
