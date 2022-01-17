import requests

#get

data=str(input(" Enter Your number: "))

amount=int(input(" Enter Your amount: "))


#api="https://www.okaypia.com/user_signup"


api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"



#for i in range(amount):
    #print(i)

requests.get(api)
