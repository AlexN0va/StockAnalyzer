import time
import replit



delay = 1

def delay_clear(delay):
  time.sleep(delay)
  replit.clear()


print("this program be taken lightly. There are a lot more factors to take into account, although this is a good starting point to choose whether a stock is profitable for average investors. ")

delay_clear(delay=5)



class Preformance:
  def __init__(self, buyCost, sellCost, numShare, exitPoint):
    self.buyCost = buyCost
    self.sellCost = sellCost
    self.numShare = numShare
    self.dollar_return = 0
    self.exitPoint = exitPoint
    

  def profit_per(self):
    prof_per =(self.sellCost - self.buyCost) / self.buyCost
    
    print ("{:.0%}".format(prof_per) + " Return Rate")
  def dollar_rturn(self):
    self.dollar_return =  self.sellCost - self.buyCost

    print ("{:.2}$".format(self.dollar_return) + " Dollar Return Rate")
  def R_margin(self):
    R_R = (self.buyCost - self.exitPoint) / (self.sellCost - self.buyCost)
    
    print ("{:.2}".format(R_R) + " Risk / Reward value \n ")

    ques =  Ratio?(y/n): ")
    if ques.lower().strip() == ("y"):   
      print("If the ratio is great than 1.0, the potential risk is greater than the potential reward on the trade. If the ratio is less than 1.0, the potential profit is greater than the potential loss.")
    elif ques.lower().strip() == ("n"): 
      print("Alright")
    else:
      print("something went wrong. Restarting... ")
      delay_clear()
      exit()

  
    
bCost = float(input("What is your buy Cost: "))
delay_clear(delay)

sCost = float(input("What is your expected sell price: "))
delay_clear(delay)

nShare = float(input("How many shares will you buy: "))
delay_clear(delay)

Exit = float(input("What is your exit point: "))
delay_clear(delay)





p1 = Preformance(bCost, sCost, nShare, Exit)

p1.dollar_rturn()

p1.profit_per()

p1.R_margin()


