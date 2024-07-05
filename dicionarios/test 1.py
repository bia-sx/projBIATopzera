serhumano={'nome':'kerolin','idade':17,'cidade':'amapa'}

#pdp
(print(serhumano('nome')))
(print(serhumano('cidade')))
(print(serhumano('idade')))


#ou


print(serhumano.keys())
print(serhumano.values())

#ou 




for item in serhumano.keys():
    print(serhumano[item])

#ou

    print(serhumano['cidade'])
    serhumano['cidade']="new york"
    serhumano['idade']=32
    print(serhumano['cidade'])
    print(serhumano['idade'])