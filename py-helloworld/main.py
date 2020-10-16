from User import User

print ("hello world")

name = 'Cesar'
print(name)

number1 = 1
print(number1)

if 1 < 2:
    print("is minor")
else:
    print("is not mnor")

vector1 = ["joel", "eliud", "ana", "la otra ana", "pancho", "karen", "pablito"]

print(vector1[0])

movies = ["the warriors", "amores perros", "toy story", "rata touille", "robert pattonspn te odio"]

print(movies)

for m in movies:
    m = m + "(clasificacion: R)"
    print(m)



def showName():
    print('nombre perron Jesus')

user1 = User("Pancho", 40, "waifuhunter@gmail.com")
print(user1.name)
user1.getInfo()

showName()