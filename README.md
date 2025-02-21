Django Signals Execution: Synchronous or Asynchronous?

Django provides a built-in signals framework that allows different parts of an application to communicate. However, an important question is whether Django signals execute synchronously or asynchronously by default. Django Signals are Executed Synchronously.
By default, Django signals are executed synchronously. This means that when a signal is sent, Django waits for the corresponding signal handler to complete before executing the next line of code.

Proof with a Code Snippet
The following code snippet demonstrates this behavior:

from django.shortcuts import render
from django.http import HttpResponse
from django.dispatch import Signal, receiver

# Create a custom signal
my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler is running")

# View to send the signal
def send_signal(request):
    print("Sending signal...")
    my_signal.send(sender=None)
    print("Signal sent!")
    return HttpResponse("Check your console for signal output")

Expected Console Output:

If signals were asynchronous, we would expect the "Signal sent!" message to appear before the "Signal handler is running" message. However, the actual output is:

Sending signal...
Signal handler is running
Signal sent!

This confirms that the signal handler runs before the execution of the next line, proving that Django signals are synchronous by default

Conclusion:
Django signals are executed synchronously by default, meaning that Django waits for the signal handler to complete before proceeding. 
To make them asynchronous, you need to run them in a separate thread or a task queue.
