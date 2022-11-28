from readreddit import read_reddit
from speaktomp3 import out_to_mp3
from takess import take_screenshots
from generatevid import generate_vid
from pprint import pprint


def main(argv):
    content = read_reddit(
        "https://www.reddit.com/r/AskReddit/comments/xrxtcx/raskredit_whats_the_dumbest_rule_in_your_school/")
    out_to_mp3(content, "out.mp3")
    take_screenshots(content)

    # content["path"] = "img/ss.png"
    # for i, data in enumerate(content["data"]):
    #     content["data"][i]["path"] = f"img/ss{i}.png"

    generate_vid(content)


if __name__ == "__main__":
    main(__import__("sys").argv)
