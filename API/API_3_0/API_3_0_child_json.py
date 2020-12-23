from lxml import etree
from time import sleep
import base64
import requests
import json
import codecs
from lxml import html
from bs4 import BeautifulSoup

main_url = 'http://vips2:3877'
Login = 'demo'
Password = 'demo'
Type = 'VX'
RNs = {}

headers = {
    'content-type': 'application/json'
}

FL_Service = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Exp"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',

    #/* Доп. параметры для сервиса "ЦККИ" */
    "IssueDate": '11.02.2000',

    #/* Доп. параметры для сервиса "Фактор риска" */
    "PlaceOfBirth": 'Москва',

    #/* Доп. параметры для сервиса "СВИ" */
    "InfoType": '1',

    #/* Доп. параметры для сервиса "Экспертиза" */
    "Address": { #/* адрес постоянной регистрации */

      "Region": '40',
      "City": 'САНКТ ПЕТЕРБУРГ',
      "Street": 'ВОЗНЕСЕНСКИЙ',
      "noStreet": False,
      "House": '34',
      "noHouse": False,
      "Build": '1',
      "Building": '',
      "Flat": '123',
      "noFlat": False
   },
    "AddressTmp": { #/* адрес временной регистрации */
       #... /* структура как у объекта с адресом пост. регистрации */
   },
    "WorkUL": { #/* данные работодателя - ЮЛ */
      "OGRNOrg": '1157746058931', #/* задается либо OGRNOrg, либо INNOrg */
      "INNOrg" : '7713390123',
      "NameOrg": 'МЕЖРЕГИОНАЛЬНОЕ БЮРО КОММЕРЧЕСКОЙ ИНФОРМАЦИИ',
      "Address": { #/* адрес места нахождения ЮЛ */
         "Region": '77',
         "City": 'Москва',
         "Street": 'Приорова',
         "House": '30',
         "Build": '',
         "Building": '',
         "Flat": ''
      },
    "Phone": '+7 (495) 276-12-11'
   },
    "WorkIP": { #/* данные работодателя - ИП */
      "OGRNIP": '312774618000575', #/* задается либо OGRNIP, либо INN */
      "INN": '770404319004',
      "FIO": 'ХРОМОВ АЛЕКСАНДР ВАЛЕРИАНОВИЧ',
      "Address": { #/* адрес регистрации ИП */
         #... /* структура как у объекта с адресом ЮЛ */
      },
      "Phone": '4956950322'
   },
    "Phone": '',
    "PersonArch": { #/* архивные данные ФЛ */
      "SurName": '',
      "FirstName": '',
      "MiddleName": '',
      "SeriaNumber": ''
   }
}

}
IP_Service = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": [""],

    "Params": {
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "OGRNIP": '1027700272148',
    "SeriaNumber": '4004946593',

    #/* адрес места нахождения ЮЛ */
    "Address": {
        "Region": '77',
        "City": 'МОСКВА',
        "Street": 'ЛЕНИНГРАДСКОЕ',
        "House": '71Г',
        "Build": '',
        "Building": '',
        "Flat": ''
                },
    "Phone": '',

}
}
UL_Service = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": [""],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',

    #/* Доп. параметры. Используются только сервисом "Проверка работодателя" */
    "NameOrg": '',

    #/* адрес места нахождения ЮЛ */
    "Address": {
        "Region": '77',
        "City": 'МОСКВА',
        "Street": 'ЛЕНИНГРАДСКОЕ',
        "House": '71Г',
        "Build": '',
        "Building": '',
        "Flat": ''
                },
    "Phone": '',

    #/* данные руководителя */
    "Head": {
        "SurName": 'ШУМАХЕР',
        "FirstName": 'МАРТИН',
        "MiddleName": 'АРНОЛЬД БЕНЕДИКТ'
   }

}


}

FL_BS = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["BSFL"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_IDFL = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["IDFL"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "OGRNOrg": '1056900010375',
    "OGRNIP": '',

    #/* Доп. параметры для сервиса "Экспертиза" */
    "Address": { #/* адрес постоянной регистрации */

      "Region": '40',
      "City": 'САНКТ ПЕТЕРБУРГ',
      "Street": 'ВОЗНЕСЕНСКИЙ',
      "noStreet": False,
      "House": '34',
      "noHouse": False,
      "Build": '1',
      "Building": '',
      "Flat": '14',
      "noFlat": False
   },

    "Phone": '8123106658'

   }

}
FL_CASBO = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["CASBO"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',

}

}
FL_CASBR = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["CASBR"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',

}

}
FL_Exp = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Exp"],
    "Params": {
        "SurName": "ПОНОМАРЕВА",
        "FirstName": "Ирина",
        "MiddleName": "Юрьевна",
        "noMiddleName": False,
        "DateOfBirth": "11.01.1966",
        "SeriaNumber": "4004946593",
        "Address": {
            "Region": "40",
            "City": "САНКТ ПЕТЕРБУРГ",
            "Street": "ВОЗНЕСЕНСКИЙ",
            "noStreet": False,
            "House": "34",
            "noHouse": False,
            "Build": '1',
            "Building": '',
            "Flat": "123",
            "noFlat": False
        },
        "WorkUL": {
            "OGRNOrg": "1157746058931",
            "INNOrg" : "7713390123",
            "NameOrg": "МЕЖРЕГИОНАЛЬНОЕ БЮРО КОММЕРЧЕСКОЙ ИНФОРМАЦИИ",
            "Address": {
                "Region": "77",
                "City": "Москва",
                "Street": "Приорова",
                "House": "30"
            },
            "Phone": "+7 (495) 276-12-11"
        }
    }
}
FL_AFF = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["AFF"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_EXTSOURCE = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["ExtSource"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_FR = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["FR"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',
    "PlaceOfBirth": 'Москва'

}

}
FL_CKKI = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["CKKI"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_Raiting = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Raiting"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '2.5.1983',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_Raiting_2 = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Raiting_2"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_RaitingR = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["RaitingR"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_Raiting_2R = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Raiting_2R"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_Raiting_3R = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Raiting_3R"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    #"INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_Raiting_4R = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["Raiting_4R"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',
    "Address": {
                "Region": "40",
                "City": "САНКТ ПЕТЕРБУРГ",
                "Street": "ВОЗНЕСЕНСКИЙ",
                "noStreet": False,
                "House": "34",
                "noHouse": False,
                "Build": '1',
                "Building": '',
                "Flat": "123",
                "noFlat": False
            }

}

}
FL_FLAUTORF = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["FLAUTORF"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',

}

}
FL_SVI = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "FL",
    "Services": ["SVI"],
    "Params": {

    #/* Основные поисковые параметры */
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "SeriaNumber": '4004946593',
    "IssueDate": '11.02.2000',
    "InfoType": '1'

}

}

UL_BSUL = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["BSUL"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_BSPD = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["BSPD"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_BSR = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["BSR"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_IDUL = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["IDUL"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',

    #/* Доп. параметры. Используются только сервисом "Проверка работодателя" */
    "NameOrg": 'МЕТРО КЭШ ЭНД КЕРРИ',

    #/* адрес места нахождения ЮЛ */
    "Address": {
        "Region": '77',
        "City": 'МОСКВА',
        "Street": 'ЛЕНИНГРАДСКОЕ',
        "House": '71Г',
        "Build": '',
        "Building": '',
        "Flat": ''
                },
    "Phone": '',

    #/* данные руководителя */
    "Head": {
        "SurName": 'ШУМАХЕР',
        "FirstName": 'МАРТИН',
        "MiddleName": 'АРНОЛЬД БЕНЕДИКТ'
   }

}

}
UL_FNSA = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["BSR"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_FNST = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["BSR"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_AFF = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["AFF"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_Benef = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["Benef"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_Balans = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["Balans"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_ExtSource = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["ExtSource"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_Raiting = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["Raiting"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_ULAUTORF = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["ULAUTORF"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_SVI = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["SVI"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}
UL_Employer = {

    "UserName": Login,
    "Password": Password,
    "SubSystem": "UL",
    "Services": ["Employer"],

    "Params": {

    #/* Основные поисковые параметры задается либо OGRNOrg, либо INNOrg */
    "OGRNOrg": '1027700272148',
    #"INNOrg" : '7704218694',
    }
}

IP_BIP = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["BIP"],

    "Params": {
    "SurName": 'ПОНОМАРЕВА',
    "FirstName": 'Ирина',
    "MiddleName": 'Юрьевна',
    "noMiddleName": False,
    "DateOfBirth": '11.01.1966',
    "INN": '782619098267',
    "OGRNIP": '310203231300140',
    "SeriaNumber": '4004946593',

    #/* адрес места нахождения ЮЛ */
    "Address": {
        "Region": '77',
        "City": 'МОСКВА',
        "Street": 'ЛЕНИНГРАДСКОЕ',
        "House": '71Г',
        "Build": '',
        "Building": '',
        "Flat": ''
                },
    "Phone": '',

}
}
IP_ExtendedIP = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["ExtendedIP"],

    "Params": {
    "INN": '782619098267',
    #"OGRNIP": '305183800111906',
    }
}
IP_IDIP = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["IDIP"],

    "Params": {
    "INN": '782619098267',
    #"OGRNIP": '305183800111906',
    }
}
IP_IPA = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["IPA"],

    "Params": {
    "INN": '782619098267',
    #"OGRNIP": '305183800111906',
    }
}
IP_IPT = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["IPT"],

    "Params": {
    "INN": '782619098267',
    #"OGRNIP": '305183800111906',
    }
}
IP_ExtSource = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["ExtSource"],

    "Params": {
    "INN": '782619098267',
    #"OGRNIP": '305183800111906',
    }
}
IP_SVI = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["SVI"],

    "Params": {
    "INN": '782619098267',
    #"OGRNIP": '305183800111906',
    }
}
IP_Employer = {
    "UserName": Login,
    "Password": Password,
    "SubSystem": "IP",
    "Services": ["Employer"],

    "Params": {
    "INN": '200509725407',
    #"OGRNIP": '305183800111906',
    }
}

SERVICES = [
FL_BS,
FL_IDFL,
FL_CASBO,
FL_CASBR,
FL_Exp,
FL_AFF,
FL_EXTSOURCE,
#FL_FR,
FL_CKKI,
FL_Raiting,
FL_Raiting_2,
FL_RaitingR,
FL_Raiting_2R,
FL_Raiting_3R,
FL_Raiting_4R,
#FL_FLAUTORF,
FL_SVI,

UL_BSUL,
UL_BSPD,
UL_BSR,
UL_IDUL,
UL_FNSA,
UL_FNST,
UL_AFF,
UL_Benef,
UL_Balans,
UL_ExtSource,
UL_Raiting,
#UL_ULAUTORF,
UL_SVI,
UL_Employer,

IP_BIP,
IP_ExtendedIP,
IP_IDIP,
IP_IPA,
IP_IPT,
IP_ExtSource,
#IP_SVI,
IP_Employer
]

def request(data):
    url = main_url + '/request'
    r = requests.post(url=url, headers=headers, json=data)
    print(str(data['Services']) + r.text)
    try:
        print(str(data['Services']) + ' ' + r.json()['RequestNumber'])
        RNs[data['Services'][0]] = r.json()['RequestNumber']
        return str(r.json()['RequestNumber'])
    except Exception as e:
        print(e)
        print(str(data['Services']) + r.text)

def response(RN):
    status,  = '3'
    tryes = 30
    data = {
        "UserName": Login,
        "Password": Password,
        "Type": Type,
        "RequestNumber": RN
    }
    url = main_url + '/response'

    r = requests.post(url=url, headers=headers, json=data)
    while (status == '3' and tryes > 0):
        try:
            status = r.json()['Status']
            tryes -= 1
            print('tryes ' + str(tryes))
            sleep(3)
        except:
            print(r.text)
            break
    # strResponce = base64.b64decode(r.json()['Content'][0]['Body']) # здесь лежит номальный ответ
    # soup = BeautifulSoup(strResponce, 'lxml')                      # здесь лежит номальный ответ
    try:
        return  r.json()['Status']
    except:
        return r.text

def balance():
    url = main_url + '/balance'
    data = {
        "UserName": Login,
        "Password": Password
    }
    r = requests.post(url=url, headers=headers, json=data)
    print(r.json())
    return r.json()


for service in SERVICES:
    request(service)
for  service, RN in RNs.items():
    print(service + ' ' + response(RN))
balance()


# response(request(FL_Exp))