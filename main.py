from src.SeleniumMode import SeleniumMode

print('''
    ###########################################################
    #               Anderson Nunes de Lima                    #
    #                                                         #
    #                                                         #
    # Requisitos: Python3.7, Chrome Browser                   #
    #                                                         #
    #                                                         #
    # Dependencia: realize a instalacao das dependencias      #
    # necessarias atravez do comando:                         #
    # python3.7 -m pip install -r requiriments.txt            #
    #                                                         #
    # Execucao: python3.7 main.py                             #
    #                                                         #
    ###########################################################
''')

seleniumExc = SeleniumMode()
seleniumExc.getAmazon('iphone')
