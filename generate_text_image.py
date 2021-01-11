import random
import argparse
import wordcloud
from wordcloud import WordCloud

def generate_text_image(words, out, layout_color, width, height, step_size, bias):

    '''
    Generate an image of words in a given string using wordcloud module.

    Argument:
        words -- string of words separated by comma
        out -- path to output image
        layout_color -- background color
        width -- width of image
        height -- height of image
        step_size -- difference between freqencies of words
        bias -- lowest initial frequency of a word

    Returns:
        None
    '''

    word_list = words.split(',')[::-1]

    text_list = []
    for i, word in enumerate(word_list):
        for j in range(i*step_size+bias):
            text_list.append(word)
    random.shuffle(text_list)
    text_corpus = " ".join(text_list)

    image = WordCloud(background_color=layout_color, height=height, width=width).generate(text_corpus)
    image.to_file(out)
    print("Image successfully saved to {}".format(out))

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-ws", "--word_string",
                    required=True,
                    help="string of words separated by comma")
    ap.add_argument("-o", "--out",
                    required=True,
                    help="path to output image")
    ap.add_argument("-l", "--layout_color",
                    default='black',
                    help="background color")
    ap.add_argument("-W", "--width",
                    type=int,
                    default=1200,
                    help="width of image")
    ap.add_argument("-H", "--height",
                    type=int,
                    default=800,
                    help="height of image")
    ap.add_argument("-s", "--step_size",
                    type=int,
                    default=50,
                    help="difference between freqencies of words")
    ap.add_argument("-b", "--bias",
                    type=int,
                    default=10,
                    help="lowest initial frequency of a word")

    args = vars(ap.parse_args())

    generate_text_image(args["word_string"], args["out"], args["layout_color"],args["width"], args["height"],
                        args["step_size"], args["bias"])