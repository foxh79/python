def emoji_converter(message):
    words = message.split(" ")

    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("Enter greeting with emoji: ")
print(emoji_converter(message))