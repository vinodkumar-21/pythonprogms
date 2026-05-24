"""
Threading vs Multiprocessing — Real World Example

Simple difference:

Threading → same memory, lightweight, best for waiting tasks (I/O)
Multiprocessing → separate memory, heavy but true parallel CPU work

1. Threading Real World Example
Suppose you build a:

Chat app
Email sender
Notification system
API calls system

Example:
You need to send:

Email
SMS
Push notification

at the same time.

Without threading:

send_email()
send_sms()
send_push()

One by one chalega → slow.

Using threads:
"""

from threading import Thread
import time

def send_email():
    time.sleep(2)
    print("Email sent")

def send_sms():
    time.sleep(1)
    print("SMS sent")

def send_push():
    time.sleep(3)
    print("Push sent")

t1 = Thread(target=send_email)
t2 = Thread(target=send_sms)
t3 = Thread(target=send_push)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All notifications sent")

"""
Real-world use cases of Threading
Django/Flask API calling external APIs
Chat applications
Notification systems
File downloading
Database queries
Web scraping
RabbitMQ consumers
Microservices communication

Because mostly system waiting karta hai:

network
DB
API response
"""





"""
In Django/FastAPI Real Projects

Mostly:

async
threading
Celery
RabbitMQ
Redis queues

used hote hain background tasks ke liye.

Example:
User uploads video:

API immediately response de deti hai
Background worker video process karta hai

Ye real production architecture hota hai.
"""