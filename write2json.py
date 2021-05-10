import json

person_dict = {

    "file_path": r"C:\Users\rv\Downloads",
    "ext_id": "hdhinadidafjejdhmfkjgnolgimiaplp",
    "urls": [
        "https://www.makemytrip.com/",
        "https://www.amazon.in/",
        "https://www.bankofamerica.com",
        "https://www.jpmorganchase.com",
        "http://aliexpress.com",
        "https://www.rakuten.co.jp/",
        "https://myspace.com/"
    ]

}

# with open(r'C:\Users\rv\Downloads\person.txt', 'w') as json_file:
#     json.dump(person_dict, json_file)

f=open(r'C:\Users\rv\Downloads\configData.txt')
data_dic = json.load(f)
print(data_dic['ext_id'])