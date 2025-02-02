# •	14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        return "Notification sent"
class EmailNotification(Notification):
    def send(self):
        return "Email sent"
class SMSNotification(Notification):
    def send(self):
        return "SMS sent"   
obj = EmailNotification()
print(obj.send())
obj = SMSNotification()
print(obj.send())
