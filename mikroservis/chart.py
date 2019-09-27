import requests
from PIL import Image


url = 'http://portal14:8064'
data = {
    "width":  500,
    "height": 300,
    "data": [
        ["Год", "Прибыль", "Самооценка", "Количество девушек"],
        ["2004",  1000,      400,  0],
        ["2005",  1170,      460,  20],
        ["2006",  660,       1120, 0],
        ["2007",  1170,      460,  0],
        ["2008",  660,       1120, 400],
        ["2009",  1030,      540,  0]
    ],
    "options": {
        "colors": ["red", "magenta", "#FFAABB"],
        "title": "Кронос Информ",
        "curveType": "function",
        "legend": { "position": "bottom" }
    }
}

r = requests
R = r.post(url=url, json=data)

with open('c:\\img00000.png', 'wb')as file:
    file.write(R.content)

im = Image.open("c:\\img00000.png")
im.show()