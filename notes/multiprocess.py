"""2. Multiprocessing Real World Example

Suppose:
You are building:

Video rendering
AI model training
Image processing
Data analytics
Heavy calculations

Example:
Image resize of 10 lakh images.

Single process:

bahut slow

Multiprocessing:

CPU ke multiple cores use honge
"""

from multiprocessing import Process
import time

def process_data(num):
    print(f"Processing {num}")
    time.sleep(2)

p1 = Process(target=process_data, args=(1,))
p2 = Process(target=process_data, args=(2,))
p3 = Process(target=process_data, args=(3,))

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

print("Completed")

"""
Easy Analogy
Threading

Like:

Ek restaurant me same kitchen
Multiple waiters

Shared resources.

Good for:

waiting tasks
Multiprocessing

Like:

Multiple separate kitchens

Each process independent.

Good for:

heavy CPU work
Python Important Point

Python has:

GIL (Global Interpreter Lock)

Isliye:

threading CPU-heavy work me true parallelism nahi deta
multiprocessing deta hai
Which one should you use?
Situation	Use
API calls	Threading
Email sending	Threading
Chat app	Threading
File upload/download	Threading
Web scraping	Threading
Image processing	Multiprocessing
AI/ML training	Multiprocessing
Video rendering	Multiprocessing
Heavy calculations	Multiprocessing
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