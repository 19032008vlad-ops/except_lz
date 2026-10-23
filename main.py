from exception import Validator

file_name = input('Enter filename which you want except: ')
obj = Validator(file_name)    
obj.check_data()
