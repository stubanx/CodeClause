from pyshorteners import Shortener
url = input("Enter the real URL:=- ")
s_url = Shortener().tinyurl.short(url)
print()
print(s_url)