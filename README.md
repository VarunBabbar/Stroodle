 # Stroodle (Oxford Hackathon 2018)

## Inspiration
* The ReadtoMe app that was developed using Amazon’s Transcribe and Comprehend API.
* We felt there was more we could do with the technology on offer.
* We wanted to make storytelling a better experience not just for the person listening but also for the narrator; an interactive experience that could give the narrator feedback and enhance their creativity.
* Narration in itself requires a tremendous amount of creative/ imaginative thought but we felt that people had little understanding of this.
* Our target audience is children below the age of 5 who are learning to communicate. We want to encourage children to have fun whilst learning and use our software to learn to talk actively. 

## What it does
* Our software converts speech into text using AWS Transcribe real time.
* It identifies the keywords in each sentence of the speech using AWS Comprehend based on context, again in real time.
* It performs a smart search for cartoon, non explicit images of the keywords using Bing Web Search.
* It feedbacks the images in real time, in chronological order in the Python module Pygame. 
* It uses AWS Comprehend to assign positive, negative, or neutral emotional values to phrases depending on the context of the sentence, playing appropriate background music and character sounds. 

## How we built it
* We ran the real time speech to text converter in Java, making use of AWS Transcribes most recent release (5 days ago).
* We used Python and its library Pygame to create the backend that would call the different APIs and give the appropriate output in terms of pictures and music.

## Challenges we ran into
* It was difficult to build a multi layer musical theme to our story. We had to run many simulations to perfect the accuracy of the background music and the extra sounds produced by the roaring and thunder audio files interfered with transcription accuracy. In addition, we also wanted to overlap the background music with the extra sounds mentioned above, which took a lot of tweaking of our code.
* Running the AWS Transcribe real time was harder than initially thought. It took a long time for the API to converge, and the results accuracy was often affected by noise. As a result, we tweaked the ML algorithm by adding priors so that the output was collected more efficiently without losing out on accuracy. For instance, we used the fact that children often narrate their stories in a short subject-verb-object structure to shorten the convergence time of the API and we added further restrictions on repetition criteria to gather our data more efficiently.

## Accomplishments that we proud of
* Being able to make a good use of many APIs and services. Considering none of us had any experience of using APIs, we had to overcome several difficulties (such as dependencies) to get the program up and running. And for that, we are extremely grateful of the support of the AWS staff who gave us some invaluable advice.
* Our program achieved, and surpassed the goal we had in mind. We had no idea that we would be able to make such an interactive solution on a combination of Java and Python. It was incredibly satisfying executing the program from the command line and watching our interactive program run on its own. 

## What we learned
* We gained exposure to the wide variety of APIs offered by commercial agents and how they can make it easier to develop programs and applications for resolving real world problems. Most surprising was the fact that we could use these APIs with ease and integrate them into any projects we were working on.
* We experienced the value of OOP in group projects; allowing for modularity meaning we could work on individual components on our own. Although individually, our progress was pretty slow, the interface structure allowed us to bring together our individual effort at the end.

## What's next for Test
* Creating a larger database of sounds and images (apart from the APIs being used) that would bring about a unique theme to our product.
* Use machine learning to bring about a) personalisation to the user in regard to the kind of images and sounds they’d like in their story and b) improve the accuracy of the speech to text converter.
* Maybe extend it to a VR project!
* Extend beyond storytelling to aid classroom teaching, etc. 

## Setting up Stroodle
#### Getting the AWS/Azure API 
1. Go to Amazon's Developer Console https://aws.amazon.com/comprehend/ and create a new project. 
2. Open the project and search for the API in the library. 
3. Enable the API for your project. 
4. Generate your Subscription Key for it. 
### Making an installation folder
1. Clone the repository.
2. Enter your subscription key under the `read_text.py` -

```
subscription_key = "Enter your key here"
assert subscription_key
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
```
