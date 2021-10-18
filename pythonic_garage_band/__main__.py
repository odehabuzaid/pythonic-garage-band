

if __name__ == '__main__':
    from pythonic_garage_band import Band, Bassist, Drummer, Guitarist
    amir = Guitarist('Amir Eid')
    Tamer = Drummer('Tamer Hashem')
    adam = Bassist('Adam El Alfy')
    
    band = Band('Cairokee', [amir, Tamer, adam])
    print(len(band))
    
    print(band.to_list())
    print('the Leader :',amir)
    print()
    print(amir.play_solos())
    print(amir.get_instrument())
