# POP bu elemnetni sug;urib oladi
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
copy= bozorlik.pop(1)
print(copy)


# sort() bu elementlarni alifbo shaklida joylashtiradi

bozorlik.sort()
print(bozorlik)

#.sort(reverse=True) bu elementlani teskari shaklda joylashtiradi

bozorlik.sort(reverse=True)
print(bozorlik)

# reverse teskariga aylantirish

sonlar=[8,-6,3,7,99,1,2,-5,5,5]
print(sorted(sonlar, reverse=True))

# len uzunlikni o'lchaydi

print(len(sonlar))

# range

son=list(range(0, 10))
print(son)

toq_sonlar=list(range(1,20, 2))
print(toq_sonlar)

#Nusxa olish


cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
my_cars=cars[:]
print(my_cars)
my_cars.remove('gm')
print(my_cars)
print(cars)

#tuple- o'zgarmas ro'yxat

toys=('bus', 'car', 'dino', 'snake', 'lizard')
# error beradi  chunki tuplega qowib bo'lmaydi
#toys[0] = "teddy"

print(toys)

# faqat uni listga ugurish mumkin

toys=list(toys)
toys[0]="teddy"
print(toys)


