
from math import floor
class Paperboy:

    # Each paperboy should have several attributes:
    #
    # Name
    # Experience (the number of papers they've delivered)
    # Earnings (amount of money they've earned)
    def __init__(self,name,exp=0,earnings=0):
        self.name = name
        self.experience = exp
        self.earnings = earnings

    # Every day, each paperboy is given a house number to start at and a house number to finish at. They get paid $0.25 for every paper they deliver and $0.50
    #for every paper over their quota. If at the end of the day they haven't met their quota, they lose $2.
    #
    # The minimum number of papers to deliver is 50. The quota is calculated as half of your experience added to the minimum. So the first time a paperboy
    #makes a delivery, the quota is 50. The next time, the quote is 50 plus half the number of papers that the paperboy has delivered in the past. In this way
    #the quota should increase after every delivery the paperboy makes.
    #
    # Each paperboy should have at least these methods:
    #
    # __str__
    def __str__(self):
        return "This paperboy is named {}. He has delivered {} papers and earned ${:.2f}.".format(self.name,self.experience,self.earnings)

    # quota
    # This method should calculate and return the paperboy's quota for his next delivery
    def quota(self):
        return floor(self.experience * 0.5 + 50)

    # deliver(self, start_address, end_address)
    # This method will take two house numbers and return the amount of money earned on this delivery as a floating point number. It should also update the
    #paperboy's experience! Let's assume that the start_address is always a smaller number than the end_address
    # As a stretch exercise you can figure out how to ensure it still works if the above assumption isn't met!
    def deliver(self,start_address,end_address):
        #Added the following lines to ensure that it works even if the start address is larger than the end address
        start = min(start_address,end_address)                                  #Find the smaller value
        end = max(start_address,end_address)                                    #Find the larger value
        total_houses = end - start + 1                                          #Total number of houses is the difference between them, plus one
        curr_quota = self.quota()                                               #Define a local variable for the current quota
        if total_houses == curr_quota:                                          #If the number of houses is the same as the quota,
            earned = (0.25 * total_houses)                                      #The total earned is $0.25 per house
        elif total_houses < curr_quota:                                         #If the number of houses is less than the current quota,
            earned = (0.25 * total_houses) - 2                                  #Calculate how much they earned, then subtract $2.00
        elif total_houses > curr_quota:                                         #If the number of houses is larger than the current quota,
            earned = (0.25 * curr_quota) + (0.50 * (total_houses-curr_quota))   #Earn $0.25 per paper up to the quota, as well as $0.50 for each additional paper
        self.experience += total_houses                                         #Add the number of houses to the experience
        self.earnings += earned                                                 #Add today's earnings to the total earnings
        return earned                                                           #Finally, return the earnings

    # report
    # This method should return a string about the paperboy's performance
    # e.g. "I'm Tommy, I've delivered 90 papers and I've earned $38.25 so far!"
    def report(self):
        return "Look at me! I'm {} and I've delivered {} papers so far. They've paid me ${:.2f} for this, can you believe it?!".format(self.name,self.experience,self.earnings)

# jeff = Paperboy('Jeff',3,4)
# print(jeff)
# print(jeff.quota())
# print(jeff.deliver(1,49))
# print(jeff.deliver(1,56))
# print(jeff)
# print(jeff.report())
# print(jeff.deliver(1,100))
# print(jeff.report())
#

tommy = Paperboy("Tommy")

print(tommy.quota()) #  50
print(tommy.deliver(160, 101)) # 17.5
print(tommy.earnings) # 17.5
print(tommy.report()) # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"

print(tommy.quota()) # 80
print(tommy.deliver(1, 75)) # 16.75
print(tommy.earnings) # 34.25
print(tommy.report()) # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"
