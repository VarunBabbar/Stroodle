import time
import boto3
import json
import requests
import json
from PIL import Image
import sound_stuff
import io
import pygame as pg
import time
from urllib.request import urlopen

filename = "story.txt"

file = open(filename, 'r')

subscription_key = "*Insert you Subscription Key here*"
assert subscription_key
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"


def phrase_to_image(search_term, x, y):
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    #    search_urls=search_results["value"][0]["thumbnailUrl"]
    image_url=search_results["value"][0]["thumbnailUrl"]
    #    image_data = requests.get(search_urls)
    #    image_data.raise_for_status()
    #    image = Image.open(BytesIO(image_data.content))
    #    image.show()
    image_str = urlopen(image_url).read()
    # create a file object (stream)
    image_file = io.BytesIO(image_str)
    # load the image from a file or stream
    image = pg.image.load(image_file)
    image = image.convert()
    pg.transform.scale(image, (300, 300))
    # draw image, position the image ulc at x=20, y=20
    screen.blit(image, (x, y))
    # nothing gets displayed until one updates the screen
    pg.display.flip()
    # time.sleep(5)
    # screen.fill(pg.Color("white"))
    # pg.display.flip()



def text_analyse(text):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    #    print('Calling DetectKeyPhrases')
    a=json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    b=json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    
    aa=json.loads(a)
    bb=json.loads(b)
    #    print(aa)
    try:
        aaa=aa["KeyPhrases"][0]["Text"]
        aaa=sound_stuff.remove_unwanted_words(aaa)
        ccc=max(zip(bb['SentimentScore'].values(),bb['SentimentScore'].keys()))
        print("Keyword: " + aaa)
        print("Max_Sentiment: " + ccc[1])
        #    print(sentiment_analysis["Negative"])
        return([aaa,ccc])#fo
    except:
        pass



if __name__ == "__main__":
    
    count=0
    x=10
    y=10
    pg.init()
    white = (255, 255, 255)
    screen = pg.display.set_mode((1600, 1200), pg.RESIZABLE)
    screen.fill(white)
    
    previous_text = ""
    previous_search_term = ""
    
    # initialise the sentiment
    previous_sentiment = (0.9, 'Negative')
    
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit

        
        text = file.readline()
        
        if text=="":
            print(
                  "Waiting")
            time.sleep(1)
    
    
    
        else:
            """
            if "time" in text:
                print("found")
                text = text.replace("time", "")
            
            if "One day" in text:
                print("found")
                text = text.replace("One day", "")
        """

        
            print("Phrase to be analyzed: " + text)
            
            try:
                print("Text before " + text)
                text = text.replace(previous_text[:-2], "")
                text = text.replace(previous_text[:-5], "")
                text = text.replace(previous_text[:-10], "")
                print("Text to be excluded " + previous_text)
                print("Text after " + text)
                previous_text = text
                search_term = text_analyse(text)[0]

                sentiment = text_analyse(text)[1]

                if search_term == previous_search_term:
                    pass

                else:
                    previous_search_term = search_term
                    phrase_to_image(search_term + " cartoon", x, y)
                    x = x + 400
                    if x == 1210:
                        x = 10
                        y = y + 300

                    # SOUND STUFF

                    pg.mixer.init()

                    if count==0:
                        audio_background = sound_stuff.which_background_audio(previous_sentiment)
                        pg.mixer.Channel(0).stop()
                        #pygame.mixer.music.load(audio_background)
                        pg.mixer.Channel(0).play(pg.mixer.Sound(audio_background))
                        count = count + 1
                    #  checking if there is a change in sentiment forr the background music
#                    if (text_analyse(text)[1][1] == "Neutral") or (previous_sentiment[1] == "Neutral"):
#                        pass
                    if (text_analyse(text)[1][1] == "Positive"):
                        if count == 1:
                            print(sentiment[1])
                            audio_background = sound_stuff.which_background_audio(sentiment)
                            print(audio_background)
                            pg.mixer.Channel(0).stop()
                    #pygame.mixer.music.load(audio_background)
                            pg.mixer.Channel(0).play(pg.mixer.Sound(audio_background))
                            count = count + 1
                        else:
                            pass
#                    pygame.mixer.music.play(1)

                    
#                    previous_sentiment = sentiment

                   # sound effects checked every time
                    audio_sound_effects = sound_stuff.which_sound_effect(search_term)
                    print(audio_sound_effects)
                    if (audio_sound_effects != ' '):
                        pg.mixer.Channel(1).stop()
                        #pygame.mixer.music.load(audio_sound_effects)
                        pg.mixer.Channel(1).play(pg.mixer.Sound(audio_sound_effects))
                    """
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(audio_sound_effects)
                        pygame.mixer.music.play(1)
                    """

            except:
                pass







#ーーーーーーーーーーーーーーーー
#if __name__ == "__main__":
#
#    count = 0
#
#    while True:
#
##        list = ""
#
#        text = file.readline()
#
#        if text=="":
#            print("Waiting")
#            time.sleep(1)
#
#        else:
##            list = list + text
##            list = list.replace('\n', ' ')
#            count = count + 1
#            print(count)
#            if (count == 10):
#
#                print("Phrase to be analyzed: " + text)
#
#                try:
#                    print(text)
#                    search_term = text_analyse(text)
#                    phrase_to_image(search_term + " cartoon")
#                except:
#                    pass
#                count = 0
#
#            else:
#
#                pass
