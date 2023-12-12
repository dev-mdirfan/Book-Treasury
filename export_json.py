from django.core import serializers
from books.models import Book
from contacts.models import Contact
from sellers.models import Seller

# Exporting all data into json format   
data = serializers.serialize("json", Book.objects.all())
data = serializers.serialize("json", Contact.objects.all())
data = serializers.serialize("json", Seller.objects.all())

# Now you can write data into a file
out = open("data.json", "w")
out.write(data)
out.close()

