# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
#
# avto1=avto_info("GM" ,"lasety", "oq", "avto", 2015)
# avto2=avto_info("KIA" ,"K5", "qora", "avto", 2020, 45000)
# avtolar=[avto1,avto2]
# # avtolar degan lug'at ichiga joylashtirish
# # print(avtolar[1]['narh'])
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh='Nomalum'
#
#     # print(f"{avto['rang']} {avto['model']}. narhi :{narh}")
#
# def oraliq(min, max, qadam):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# result=oraliq(1, 9, 2)
# print(result)

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

print("mavjud avtolar")
avtolar=[]
while True:
    print("\n Quyidagi malumolarni kiriting:")
    kompaniya=input("ishlabchiruvchi:")
    model=input("modeli: ")
    rang=input("rangi :")
    korobka=input("korobkasi:")
    yil=input("ishlab chiqarilgan yili:")
    narh=input("narhi: ")

    avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))


    javon=input("yana qoshasizmi? yes/no:")

    if javon=="no":
        break
print("bor mashina")
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh="Nomalum"
    print(f"{avto['rang'].title()} {avto['model'].title()} {korobka} korobka . narhi {narh}")

print(avtolar)
