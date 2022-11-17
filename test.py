from decouple import config

name = config("NAME", default="python")
print(name)

pwd = config("PASSWORD", cast=int)
print(type(pwd), pwd)
