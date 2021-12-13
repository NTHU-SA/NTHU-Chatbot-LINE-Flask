from API import DataAPI, PhoneAPI

def data_loader(category):
    result = []

    data = DataAPI()

    result, err = data.getQA(category)
    if err:
        print(err)
        return
    
    return result

def phone_list_loader():
    result = []

    phone = PhoneAPI()

    result, err = phone.getPhonelist()
    if err:
        print(err)
        return
    
    return result
