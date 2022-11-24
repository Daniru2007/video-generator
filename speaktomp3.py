from gtts import gTTS


def out_to_mp3(content, file_name):
    all_content = content["title"]
    for comment in content["data"]:
        all_content = f"{all_content}. {comment['body']}"
    mp3file = gTTS(all_content)
    mp3file.save(file_name)


if __name__ == "__main__":
    x = ["'It's been a great pleasure to meet you all in the school' he said.", "Hi.", "sup."]
    out_to_mp3(x, "test.mp3")
