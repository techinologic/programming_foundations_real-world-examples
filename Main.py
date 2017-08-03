s = 'shirt'
print(s)

class Jeans:
    def __init__(self, waist, length, color, ):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True
    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False

# create new jeans
myJeans = Jeans(32, 30, 'black')

myJeans.put_on()

print(myJeans.wearing)

myJeans.take_off()
print(myJeans.wearing)
