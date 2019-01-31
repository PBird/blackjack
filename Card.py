class Card(object):
    shapes =('heart', 'tile', 'clover', 'pike')
    numbers = (
       'A',
       '2',
       '3',
       '4',
       '5',
       '6',
       '7',
       '8',
       '9',
       '10',
       'J',
       'Q',
       'K',
    )
    def __init__(self, number, shape):
        """
            initilize card
            parameters: 
                number[integer],  0-13 
                shape[integer],  0-4
        """
        self.number = number
        self.shape = shape
    def __str__(self):

        return '(%s,%s)'%(Card.shapes[self.shape], Card.numbers[self.number] )

if __name__ == '__main__':
    ace = Card(0,0)
    print(ace)