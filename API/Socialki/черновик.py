from pyrogram import Client, Filters

app = Client("123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")


@app.on_message(Filters.private)
def hello(client, message):
    message.reply("Hello {}".format(message.from_user.first_name))


app.run()