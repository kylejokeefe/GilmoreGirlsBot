# Commented out the imports until I am on a machine that I can load Twython onto
#from twython import Twython
import random

# Where keys will go when/if I get approved for API access
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# setting up the api
#api = Twython(
#    consumer_key, 
#    consumer_secret, 
#    access_token, 
#    access_token_secret
#)

#initializing a list of different quotes
quotes = ["RORY: You've got such a great brain!", 
          "RORY: Because I love you, you idiot!!", 
          "RORY: I live in two worlds, one is a world of books",
          "RORY: Not in front of the books, Lane!",
          "RORY: My books look sad. Can books look sad?",
          "RORY: You jump, I jump jack.",
          "RORY: I really do hate everyone today, including myself.",
          "RORY: Butt-faced miscreant!",
          "RORY: Thanks for the concept of lunch.",
          "RORY: Nothing excites me before 11:00",
          "RORY: Dean,  I promise, the only way you could be more important to me is if you had a Kit-Kat  bar growing out of your head.",
          "RORY: I can set my crack pipe aside for a night and do that.",
          "RORY: Come here, You’ve got some dirt on your forehead. I’m sorry. It’s the sign of the devil. My mistake.",
          "RORY: Every relationship is just a big honking leap of faith.",
          "RORY: A little nervous breakdown can work wonders for a girl.",
          "RORY: I just take a book with me everywhere. It's a habit.",
          "LORELAI: I'm not broken. Maybe just a little chipped.",
          "LORELAI: I smell snow.",
          "LORELAI: Do hookers charge to let you talk to them?",
          "LORELAI: I even cleaned the table using something other than the sleeve of my sweater and spit.",
          "LORELAI: I’m going to make out in the coatroom. Don’t eat my chicken.",
          "LOERLAI: Life's short, talk fast.",
          "LORELAI: Oh, I can’t stop drinking the coffee. I stop drinking the coffee, and I stop doing the standing, walking, and words putting into sentence doing.",
          "LORELAI: Because my brain is a wild jungle of scary gibberish… Bicycle. Unicycle. Unitard. Hockey puck. Rattlesnake. Monkey, monkey, underpants.",
          "LORELAI: You have so many years and screw-ups ahead of you.",
          "LORELAI: You’re full of hate and loathing, and I gotta tell you– I love it!",
          "LORELAI: I don't like Mondays, but unfortunately they come around, eventually.", 
          "LORELAI: Give me a burger, onion rings, and a list of people who killed their parents and got away with it. I need some heroes.",
          "LORELAI: Reality has no place in our world.",
          "LORELAI: There’s plenty to do tonight that we can be mortified about tomorrow.",
          "LORELAI: Oh yes, it was beautiful in there. We should commemorate it with an oil painting or a severed head or something.",
          "LORELAI: Well, you know my babbling capabilities are infinite.",
          "LORELAI: Hey, I have a New Year’s Resolution for you: Become more cynical and self-absorbed.",
          "LORELAI: If you're going to throw your life away, he better have a motorcycle!!",
          "LORELAI: And if eating cake is wrong, I don't want to be right.",
          "LORELAI: Yes, I left behind a glass slipper and a business card… just in case the prince is really dumb.",
          "LORELAI: I'm afraid once your heart is involved, it all comes out in moron.", 
          "LORELAI: I hate when I'm an idiot and don't know it. I like being aware of my idiocy", 
          "LORELAI: Hey, I have a huge dilemma that I need your opinion on. Am I more beautiful today than yesterday?", 
          "LORELAI: Oy with the poodles already!",
          "LORELAI: Relationships need verbs.",
          "LORELAI: Coffee, please, and a shot of cynicism.",
          "LORELAI: I'll help you shower when I become a superhero",
          "LORELAI: I'm attracted to pie. It doesn't mean I feel the need to date pie.", 
          "LUKE: I had a meeting at the bank earlier, they like callers.", 
          "LUKE: Yeah, I'm fine. I'm great. It's a big, fat, happy sunshine day for me.", 
          "LUKE: God, that's terrible. It's like drinking a My Little Pony.",
          "LUKE: You gotta realize the only way out is in a body bag.",
          "LUKE: I also enjoyed the Garfield stationary. That’s one funny cat."
          "LUKE: Violent pencil-tossing usually signals a need for pie.",
          "LUKE: Don't add stuff from yur to do list to my to do list.",
          "LUKE: He’s systematically buying up the town. He’s gonna turn it into Taylorville, where everyone will have to wear cardigans and have the same grass height!",
          "LUKE: Call me if anyone sane walks in.",
          "LUKE: Lorelei, this think we're doing here, me, you. I just wanted you to know I'm in. I am all in.",
          "BABETTE: Gnome kicking says a lot about a man's character", 
          "BABETTE: Oh God, I hope nothing's happened to him. You get so attached to their little faces, sometimes you can hear them talk to you at night",
          "MISS PATTY: It’s times like these you realize what is ‘truly’ important in your life. I’m so glad I had all that sex.",
          "PARIS: No, it's National Baptism Day. Ties your tubes, idiot!",
          "PARIS: No men. Just lots and lots of Chinese food.",
          "PARIS: I made a list of enemies, which I've narrowed down from 26 to 5.",
          "PARIS: I want to live my life so I can read an in-depth biography about myself in later years.",
          "FINN: Rory Gilmore, you should be ashamed of yourself, toying with these boys like this. They used to have pride. They used to have dignity. They used to have balls. Damn it, Gilmore! Give them back their balls!",
          "LOGAN: It's club soda, ace.", 
          "LOGAN: You have to tell me why we're committing a felony before we do it.", 
          "LOGAN: People can live a hundred years without really living for a minute.", 
          "MICHEL: People ar eparticularly stupid today, I can't talk to any more of them.", 
          "MICHEL: Excuse me. There is a phone call for you and if I'm to fetch you like a dog then I'd like a cookie and a raise.", 
          "MICHEL: Every day that you breathe, you make my life harder.",
          "MICHEL: There's a phone call for you and if I'm to fetch you like a dog, I'd like a cookie and a raise.",
          "EMILY: Well, if you expect that muffin to fly back to the kitchen by itself you better go get it a cape.", 
          "RICHARD: Oh, people die, we pay. People crash a car, we pay. People lose a foot, we pay.", 
          "EMILY: Then give me a boa and drive me to rino because I'm open for business.", 
          "EMILY: You can use your mother's old golf clubs. They're upstairs, gathering dust, with the rest of her potential",
          "EMILY: It’s always best to tell each other major life events, so there’s no awkwardness.",
          "RICHARD: Well, I'll bring dick up on the internet and see what comes up.", 
          "RICHARD: Cranking Metallica. Is that some sort of drug reference? It's not funny.", 
          "RICHARD: Really? You can see the driveway with your head way up in the air like that?",
          "JESS: Tell her I gotta take another crack at that closet. I think I hung my Tool t-shirt next to my Metallica t-shirt and they don't really get along.",
          "JESS: I gotta tell you, out of all the nutty barn-raising shindigs this town can cook up, this one wasn't half bad.",
          "JESS: Well geez, Ms. Gilmore, why would anyone not want to be in Stars Hollow? That just sounds plumb crazy.",
          "JESS: Oh yeah, I've got gold stars plastered all over my forehead.",
          "JESS: Man, she’s not shipping off to ‘Nam.",
          "JESS: My mother told me never to go through a lady's bag, at least not until you're a couple blocks away.",
          "JESS: Think how dull your life would be without me.",
          "JESS: I wanna be good, life’s just not letting me.",
          "JESS: I don't want to talk to anybody else. I don't like anybody else.",
          "JESS: It's getting a little West Side Story here, and my dancing skills are not up to snuff.",
          "CHRISTOPHER: This town is like one big outpatient mental institution.",
          "LANE: This adult stuff is hard, isn't it?",
          "DEAN: We could go to a bookstore, I’ll watch you browse for six or seven hours.",
          "SOOKIE: Crying a little, but not blubbering. That's what we meant when we said no crying. No blubbering.",
          "SOOKIE: You were a good cake, Clyde. I never should have named you."
          "SOOKIE: It’s my responsibility as your best friend to make sure you do exciting things, even when you don’t want to.",
          "KIRK: I'm so damn lonely not even Animal Planet does it for me anymore.",
          "KIRK: One day it occurred to me: cows never wrinkle",
          "KIRK: I had an imaginary girlfriend for a while when I was young, but she left me.",
          "KIRK: My girlfriend's the whore!!",
          "KIRK: Well, whimsy goes with everything.",
          "KIRK: This is the suit they buried my dad in.",
          "KIRK: Just don't touch my bottom or I'll think you have a machete.",
          "KIRK: I befriend really old women.",
          "KIRK: Yes, I have some balls.",
          "KIRK: Basically, I freak out at beddy-bye",
          "KIRK: I want to get the healthy glow of someone who consistently goes to the gym without actually having to go, of course."]

# Selecting a random quote to be tweeted
quote = random.choice(quotes)

# Placeholder comment for when I eventually integrate adding pictures to the post
image = None

if "RORY" in quote:
    image = open("Gilmore_Girl_Characters\Rory.jpg", 'rb')
elif "LORELAI" in quote:
    image = open("Gilmore_Girl_Characters\Lorelai.jpg", 'rb')
elif "LUKE" in quote:
    image = open("Gilmore_Girl_Characters\Luke.jpg", 'rb')
elif "BABETTE" in quote:
    image = open("Gilmore_Girl_Characters\Luke.jpg", 'rb')
elif "MISS PATTY" in quote:
    image = open("Gilmore_Girl_Characters\Miss_Patty.jpg", "rb")
elif "PARIS" in quote:
    image = open("Gilmore_Girl_Characters\Paris.jpg", 'rb')
elif "LOGAN" in quote:
    image = open("Gilmore_Girl_Characters\Logan.jpg", 'rb')
elif "MICHEL" in quote:
    image = open("Gilmore_Girl_Characters\Michel.jpg", 'rb')
elif "EMILY" in quote:
    image = open("Gilmore_Girl_Characters\Emily.jpeg", 'rb')
elif "RICHARD" in quote:
    image = open("Gilmore_Girl_Characters\Richard.jpg", 'rb')
elif "JESS" in quote:
    image = open("Gilmore_Girl_Characters\Jess.jpg", 'rb')
elif "CHRISTOPHER" in quote:
    image = open("Gilmore_Girl_Characters\Christopher.jpg", 'rb')
elif "LANE" in quote:
    image = open("Gilmore_Girl_Characters\Lane.jpg", 'rb')
elif "DEAN" in quote:
    image = open("Gilmore_Girl_Characters\Dean.jpg", 'rb')
elif "SOOKIE" in quote:
    image = open("Gilmore_Girl_Characters\Sookie.jpg", 'rb')
elif "KIRK" in quote:
    image = open("Gilmore_Girl_Characters\Kirk.jpg", 'rb')

#Validating an image loaded
if image != None:
    print("Image Loaded!")
else:
    print("No image found!")

# Loading image into tweet. Will uncomment once twython is loaded
#response = twitter.upload_media(media=image)
#media_id = [response['media_id']]
#twitter.update_status(status=quote, media_ids=media_id)

# Print to terminal to validate code is working
print("Tweet: " + quote)