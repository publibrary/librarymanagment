from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


bookstatus=(
    ('newbook','newbook'),
    ('trending','trending'),
    ('latestbook','latestbook'),
    ('comingsoon','comingsoon'),
    ('available','available'),
    ('out of stock','out of stock'),
)

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    Mobileno=models.IntegerField()
    message=models.TextField()
    class Meta:
        db_table="contact"

class service(models.Model):
    photo=models.ImageField(upload_to='service/')
    name=models.CharField(max_length=100)
    description=models.TextField()
    class Meta:
        db_table="service"
    def __str__(self):
        return self.name

class blog(models.Model):
    photo=models.ImageField(upload_to='blog/')
    title=models.CharField(max_length=100)
    description=HTMLField()
    postby=models.CharField(max_length=100)
    poston=models.DateField()
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.title

class author(models.Model):
    photo=models.ImageField(upload_to='author/')
    name=models.CharField(max_length=100)
    description=models.TextField()
    class Meta:
        db_table="author"
    def __str__(self):
        return self.name


class subscribe(models.Model):
    Email=models.CharField(max_length=100)
    class Meta:
        db_table="subscribe"
    def __str__(self):
        return self.Email
    
class category(models.Model):
    photo=models.ImageField(upload_to='category/', default='')
    name=models.CharField(max_length=100)
    class Meta:
        db_table="category"
    def __str__(self):
        return self.name 

class book(models.Model):
    coverphoto=models.ImageField(upload_to='book/')
    booktitle=models.CharField(max_length=100)
    authorid=models.ForeignKey(author,on_delete=models.CASCADE)
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE)
    ISBN=models.CharField(max_length=50)
    description=models.TextField(max_length=3000)
    rating=models.FloatField()
    bookstatus=models.CharField(max_length=50, choices=bookstatus)
    pdfupload=models.FileField(upload_to='pdfs/',default="")
    class Meta:
        db_table="books"
    def __str__(self):
        return self.booktitle

class faq(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="faq"
    def __str__(self):
        return self.question


class issuebook(models.Model):
    STATUS=(
        ('Issued','Issued'),
        ('Returned','Returned'),
    )
    enrollment_no=models.CharField(max_length=20)
    username=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    bookid=models.ForeignKey(book,on_delete=models.CASCADE)
    issuedate=models.DateField()
    returndate=models.DateField()
    fine=models.IntegerField()
    status=models.CharField(max_length=100,default="Issued",choices=STATUS)
    class Meta:
        db_table="issuebook"
    def __str__(self):
        return f"{self.enrollment_no}-{self.username}"

class Ordernow(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )
    issueid=models.ForeignKey(issuebook,on_delete=models.CASCADE,blank=True,null=True,related_name="issues")

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"

