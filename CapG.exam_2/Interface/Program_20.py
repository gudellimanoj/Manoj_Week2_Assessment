# •	20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC, abstractmethod
class IUserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(IUserAuthentication):
    def login(self, username, password):
        return f"Google login successful for {username}"
    def logout(self):
        return "Google logout successful"
class FacebookAuth(IUserAuthentication):
    def login(self, username, password):
        return f"Facebook login successful for {username}"
    def logout(self):
        return "Facebook logout successful"
google=GoogleAuth()
print(google.login("manu","123"))
print(google.logout())
facebook=FacebookAuth()
print(facebook.login("manu","123"))
print(facebook.logout())
