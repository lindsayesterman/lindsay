#lesson_5_functions_hw.py
#1

from sense_emu import SenseHat
from time import sleep
from email_module import send_email_message

def clubmember_card(card_value):
  if card_value == 100 or card_value == 200:
    classes = 20
  elif card_value == 300 or card_value == 500:
    classes = 15
    card_value =+ 15
  else:
    classes = 0
  return card_value/classes

 
def main():
  print("Lindsay Esterman")
  print(clubmember_card(100))
  print(clubmember_card(500))
main()


#2
def find_sum(lower_param:int, upper_param:int):
  sum = (lower_param + upper_param)
  return sum
 

def main():
  print(find_sum(5, 10))
main()

#3
def green_pixels(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int, s:SenseHat):
    s.set_pixel(x1, y1, 0, 255, 0)
    s.set_pixel(x2, y2, 0, 255, 0)
    s.set_pixel(x3, y3, 0, 255, 0)

def main():
    s = SenseHat()
    green_pixels(4, 5, 7, 2, 1, 3, s)
main()

#4
def multi_comp(value_one, value_two):
  product = value_one * value_two
  sum = (value_one + value_two)
  exponent = value_one ** value_two

  return product, sum, exponent
 

def main():
  print(multi_comp(5, -2))
  print(multi_comp(3, 4))
main()


#5
def compute_balance(current_balance:float = 1000, payment:float = 20):
  current_balance -= payment
  if current_balance > 0:
    return "balance owed", current_balance
  elif current_balance < 0:
    return "credit", abs(current_balance)
  else:
    return "paid in full", 0


def main():
  print(compute_balance(500))
  print(compute_balance(payment = 1100))
  print(compute_balance(payment = 1000))
main()


#6
def data_center_monitor(min_temp:float, max_temp:float, min_humidity:float, max_humidity:float, email_address:str, s:SenseHat):
    try:
      while True:
          s = SenseHat()
          temp = s.get_temperature()
          sleep(1)
          humidity = s.get_humidity()
          message_sent = False
          if (temp <= min_temp or temp >= max_temp) or ( humidity <= min_humidity or temp >= max_humidity):
              print("sending email")
              if not message_sent:
                  send_email_message(email_address, email_address, email_address, "Propel0!", "Temp or humidity out of range")
                  message_sent = True
    except KeyboardInterrupt:
        print("Exiting...")



def main():
    s = SenseHat()
    data_center_monitor(70,90,40,55, "lindsaypythonacct@gmail.com", s)
main()
