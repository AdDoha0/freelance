from django.db import models
from django.contrib.auth.models import User


# исполнитель
class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.user}, phone: {self.phone}"



# заказчик
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.user}, phone: {self.phone}"


# сервисы с описканием услиги и исполнителями, которые могут выаолнить задачу
class Service(models.Model):
    SERVICE_TYPES = [
        ("1", "Веб разработка"),
        ("2", "Маркетинг"),
        ("3", "Копирайтинг"),
        ("4", "Рерайтинг"),
        ("5", "Переводы"),
        ("6", "Видеомонтаж"),
        ("7", "Фотография"),
    ]
    executor = models.ForeignKey("Executor", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPES, default="1", max_length=1)

    def __str__(self):
        return f"{self.name}, {self.get_service_type_display()}, price: {self.price}"



# заказ
class Order(models.Model):
    SERVICE_TYPES = [
        ("1", "Веб разработка"),
        ("2", "Маркетинг"),
        ("3", "Копирайтинг"),
        ("4", "Рерайтинг"),
        ("5", "Переводы"),
        ("6", "Видеомонтаж"),
        ("7", "Фотография"),
    ]
    executor = models.ForeignKey("Executor", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPES, default="1", max_length=1)

    def __str__(self):
        return f"{self.name}, {self.get_service_type_display()}, price: {self.price}"


# Тэги (похоже на категории)
class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)


# Выполнение заказа
class Ordering(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    executor = models.ForeignKey("Executor", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.order_date} - {self.deadline}, Customer {self.customer}, Executor: {self.executor}"


# коментарии (возможно)
class Message(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    executor = models.ForeignKey("Executor", on_delete=models.CASCADE)
    msq_date = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    desc = models.CharField(max_length=1000)


# техподдержка
class Ticket(models.Model):

    # Важность проблемы
    SEVERITIES = [
            ("1", "Низкая"),
            ("2", "Средняя"),
            ("3", "Высокая"),
        ]
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey("Executor", on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default="1", max_length=1)
    desc = models.CharField(max_length=1000)
    is_resolved = models.BooleanField(default=False) # решена/не решена проблема




# позволяет пользователям оставлять отзывы о выполненных услугах.
class Review(models.Model):
    RAITING_FIELD = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    rating = models.CharField(choices=RAITING_FIELD, default="1", max_length=1)
    desc = models.CharField(max_length=1000)


# связывание отзывов с конкретными пользователями (авторами отзывов),
# а также с заказчиками и исполнителями, которые были вовлечены в процесс выполнения услуги.
class Authoring(models.Model):
    review = models.ForeignKey("Review", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey("Executor", on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return f"{self.author}, {self.review_date}"

