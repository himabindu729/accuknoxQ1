from django.shortcuts import render
from django.http import HttpResponse
from django.dispatch import Signal,receiver

# Create your views here
my_signal=Signal()

@receiver(my_signal)
def my_signal_handler(sender,**kwargs):
    print("Signal handler is running")

def send_signal(request):
    print("Sending signal...")
    my_signal.send(sender=None)
    print("Signal sent!")
    return HttpResponse("Check your console for signal output")


# By default, Django signals are executed synchronously. 
# This means that when a signal is triggered, Django waits for the signal handler to complete before proceeding with the next line of code.

