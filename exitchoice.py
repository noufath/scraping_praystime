from choice import choice


class ExitChoice(choice):
    '''
        Class Menu Exit
    '''

    def on_selection(self,menu,index):
        print('Bye')
        raise SystemExit