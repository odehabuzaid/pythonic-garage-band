from pythonic_garage_band import Band, Bassist, Drummer, Guitarist

if __name__ == '__main__':
    amir = Guitarist('Amir Eid')
    Tamer = Drummer('Tamer Hashem')
    adam = Bassist('Adam El Alfy')
    band = Band('Cairokee', [amir, Tamer, adam])
    
    
    print(band.to_list())
    print('the Leader :',amir)
    print()
    print(amir.play_solo())
    print(amir.get_instrument())
