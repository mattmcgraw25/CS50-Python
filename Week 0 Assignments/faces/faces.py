#user inputs :) OR :( and converts to emojis

def main():
    feelings = input()
    convert(feelings)
    print(convert(feelings))

def convert(feelings):
    feelings = feelings.replace(":)", "🙂").replace(":(", "🙁")
    return feelings

main()
