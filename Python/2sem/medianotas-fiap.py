notas = []

def mediacp(cp1,cp2,cp3):

    if cp1 <= cp2 and cp1 <= cp3:
        menor = cp1
        mediacp = (cp2+cp3)/2
        return mediacp
    elif cp2 <=cp1 and cp2<=cp3:
        menor = cp2
        mediacp = (cp1+cp3)/2
        return mediacp
    else: 
        menor = cp3
        mediacp = (cp1+cp2)/2
        return mediacp 
        # return (cp1+cp2+cp3-menor)/2

def medisem(sem,gs, mediacp, sp1,sp2=0):
    sem = input('qual semestre ')
    # gs = input('nota da gs: ')
    # sp1 = input('nota sp1: ')

    if sem == 1 :
        sp2 = sp1
        mediasem = gs*0.6 + mediacp*0.2 + (sp1+sp2)/2*0.2
        return mediasem
    else:
        sp2 = input('nota sp2: ')
        mediasem = gs*0.6 + mediacp*0.2 + (sp1+sp2)/2*0.2

def mediaAno(sem1,sem2):
    notaFinal = 0.4*sem1 + 0.6*sem2
    return notaFinal

def ler(sem):
    cp1 = float(input('Nota CP1 '))
    cp2 = float(input('Nota CP2 '))
    cp3 = float(input('Nota CP3 '))
    gs = float(input('GS '))
    sp1 = float(input('SPrint 1 '))

    if sem ==2:
        sp2 = input('nota sp2: ')
        return [cp1,cp2,cp3, gs, sp1, sp2]

    return [cp1,cp2,cp3, gs, sp1]

nsem1 = ler(1) #cp 1 cp2 cp3 gs sprint1
nsem2 = ler(2) # cp1 cp2 cp3 gs sprint1 sprint2

mcp1 = mediacp(nsem1[0], nsem1[1], nsem1[2])
mcp2 = mediacp(nsem2[0], nsem2[1], nsem2[2])

msem1 = medisem(1, nsem1[3], nsem1[4])
msem2 = medisem(1, nsem2[3], nsem2[4], nsem2[5])

mediaano = mediaAno(msem1, msem2)

if mediaano >- 60:
    print(f'Voce foi aprovado com nota{mano}')
elif mediaano >= 40:
    print(f'voce foi para exame {mano}')
else:
    print(f'Tente denovo {mano}')

# def mediacp(cp1, cp2, cp3):
#     if cp1 <= cp2 and cp1 <= cp3:
#         mediacp = (cp2 + cp3) / 2
#         return mediacp
#     elif cp2 <= cp1 and cp2 <= cp3:
#         mediacp = (cp1 + cp3) / 2
#         return mediacp
#     else:
#         mediacp = (cp1 + cp2) / 2
#         return mediacp


# def medisem(sem, gs, mediacp, sp1, sp2=0):
#     if sem == 1:
#         sp2 = sp1
#         mediasem = gs * 0.6 + mediacp * 0.2 + ((sp1 + sp2) / 2) * 0.2
#         return mediasem
#     else:
#         mediasem = gs * 0.6 + mediacp * 0.2 + ((sp1 + sp2) / 2) * 0.2
#         return mediasem


# def mediaAno(sem1, sem2):
#     notaFinal = 0.4 * sem1 + 0.6 * sem2
#     return notaFinal


# def ler(sem):
#     cp1 = float(input('Nota CP1: '))
#     cp2 = float(input('Nota CP2: '))
#     cp3 = float(input('Nota CP3: '))
#     gs = float(input('Nota da GS: '))
#     sp1 = float(input('Nota Sprint 1: '))

#     if sem == 2:
#         sp2 = float(input('Nota Sprint 2: '))
#         return [cp1, cp2, cp3, gs, sp1, sp2]

#     return [cp1, cp2, cp3, gs, sp1]


# nsem1 = ler(1)
# nsem2 = ler(2)

# mcp1 = mediacp(nsem1[0], nsem1[1], nsem1[2])
# mcp2 = mediacp(nsem2[0], nsem2[1], nsem2[2])

# msem1 = medisem(1, nsem1[3], mcp1, nsem1[4])
# msem2 = medisem(2, nsem2[3], mcp2, nsem2[4], nsem2[5])

# madiaano = mediaAno(msem1, msem2)

# if madiaano >= 60:
#     print(f'Você foi aprovado com nota {madiaano:.2f}')
# elif madiaano >= 40:
#     print(f'Você foi para exame com nota {madiaano:.2f}')
# else:
#     print(f'Tente de novo. Sua nota foi {madiaano:.2f}')
