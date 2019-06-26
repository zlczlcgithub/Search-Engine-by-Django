test_data_0022 = {
    # **Guideword:** COMBINING TWO ADJECTIVES WITH 'AND'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** combining
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use 'and' to join a limited range of common adjectives.
    'positive': [
        "The teachers are very nice and friendly.",
        "I like my house because it is big and comfortable.",
        "You can buy Turkish and English products as well.",
        # "It's getting colder and colder.",
        # colder が NN判定される
        "It's getting warmer and warmer.",
        "This book is very interesting and very instructive.",

        "It's quite easy and quick.",
        "That is why American relationships are always so cold and distant.",
        "You must post a clear and direct question.",
        "Many domestic and foreign investors want that in their portfolio.",
        "There were good and bad things that were said.",
        'Bears are gloomy and downbeat!',
    ],
    'negative': [
        "John likes coffee and Mary likes tea.",
        "We're here and out of that bloody place."
        "I really like John and Mary.",
        "It's potato that John likes and Mary hates.",
        "Here's the whiskey which I went to the store and bought.",

        "The bus and the truck collided.",
        "They knocked and knocked.",
        "I woke up and got out of bed.",
        "She was sick and took some medicine.",
        "A pause and then the inspector spoke more truculently.",

        "Another step, and I'll shoot.",
        "It's raining, and you'd better take a taxi.",
        "Mary isn't pretty, and yet people like her.",
        "You doubt his ability, and with reason.",
        "He is a fool, and make no mistake about it.",

        "My friend and adviser is dead.",
        "What I say and do is my own affair.",
        "Her calmness and confidence are astonishing.",
        "Where are Bertha and her baby to sleep at night?",
        "That's mean on his part and I can't stand it any more.",
        "That's very complex.",

        # S and S
        'Storia is expensive and Shirt Circle is inexpensive.',
        'Be honest and be graceful!',
    ],
}

test_data_0023 = {
    # **Guideword:** COMBINING TWO ADJECTIVES WITH 'BUT'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** combining
    # **Lexical Range:** None
    # **CEFR level:** A2
    # **CAN-DO:** Can use 'but' to join a limited range of common adjectives, after 'be'.

    'positive': [
        "The weather was cloudy but fine.",
        "It was cheap but beautiful.",
        "It's expensive but beautiful.",
        "That's weird but nice.",
        "I think it's not bad but good.",
        "The buildings are fancy but old.",
        # pos error for kind (RB)
        # "I know Tom is kind but lazy.",
        "I'm smart but lazy",
        "They were messy but awesome.",
        "It was hard but awesome to read.",
        "The class was so difficult but enjoyable.",
        "Artificer is fun but weird.",
    ],
    'negative': [
        "I don't agree with it, but I do sympathize with them.",
        "I looked everywhere but didn't find it.",
        "To prevent that, you need a special script akin to the one Station Science uses, but Squad didn't implement it for the claw.",
        "Boomer Sooner doesn't give me a headache but when you play it continually it gets annoying as fuck.",
        "So you see that in these examples we have raised revenue but taxed very differently to do so.",
        "It looks good on them, but most of us would not look good in it.",
        "You complain about your situation now but what would be the alternative?",
        # dependency error
        # "Sorry but life is not perfectly fair, you by the way are also not and neither is the tax system.",
        "But really, just comb it out by starting from the bottom and work your way up if it's tangled.",
        "It's not as straightforward as 'wash and let dry', but it'll tangle or frizz like crazy if you don't do anything.",
        "My parents smoked my whole life, but I never knew it until I was in my 20s.",
        "I mean, it's not as bad as last time, but still.",
        "I tried that before, but it just made me angry.",
        "The stars aren't visible here because of the clouds, but the mountains look very beautiful in the moonlight anyway.",
        "I have never played it on a tablet, but I played with my friend who played on tablet.",
        "I'm glad I did it, but there's a whole bunch of other stuff I'd like to do also.",
        "We want to sell our house and move, but not until Google actually comes to the Triangle and lays down cables.",
        "I don't need you do to that, but thank you for all your help.",
        "I'm kind of stuck because we have two kids, but once they're grown up, it's going to be hard for me to find a reason to stick around.",
        "He's hasn't done anything terrible, but he was just a dick to most people.",
        "I don't remember how full my bladder was, but I would have peed too.",
        "You told me what it was, but I still had to see for myself.",
        "I don't know what this is, but it's scary.",
        # S but S
        'That route is faster, but it will be more expensive.',
        'It\'s nice that we can learn French cuisine at Culinary Street Studio, but their classes are only available in the evenings.',
    ],
}
test_data_0024 = { 

      # **Guideword:** BEFORE THE NOUN
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use a comma to combine two adjectives used before the noun, following the usual order of adjective types.
        
  'positive': [
    'In order to get home, we must travel over several narrow, treacherous roads.',
    'In the article we found old, thin paper cutouts we used to play with when we were children.',
    # 'Allen owns several blue, wool sweaters.',
    # blue -> sweaters (appos) ↓これなら通る
    'Allen owns several blue, warm sweaters.',
    'The Tigris River ends near the Persian Gulf in a wide, swampy delta.',
    # 'The poster depicted a brown-haired, blue-eyed child wearing a red denim shirt.',
    # , -> child (root)
    'Timmy was no cute, dumb boy. He was a clever, conniving businessman.',
    'We were prepared for a long, tedious planning session.',
    'The Assyrians employed fierce, brutal tactics against their opponents.',
    'She was a faithful, sincere friend.',
    # 'Smart, funny Jaimie quickly advanced as a class leader.',
    # advanced -> Smart (advmod)
  ],
  'negative': [
    'I found a wallet and I reported it to the police.',
    'If it rains tomorrow, I will not go there.',
    'He has lived in Hokkaido and in Okinawa.',
    'She had a fever, so she was absent from school.',
    'That animal is not a giraffe but a panda.',
    'When I was a child, I often played menko.',
    'Although you are nice, you can\'t be my friend.',
    'If you are free tomorrow, we can meet up.',
    'You, he and I are good friends.',
    'You or I am wrong.',
    'I want pens, notebooks, textbooks and glasses.',
    'Because I couldn’t catch the train, I was late for school.',
    'When he comes, I will give him this present.',
    'I can neither write nor speak French.',
    'Mike or John will be elected chairperson.',
    'As soon as I arrived at school, I kept to the toilet.',
    'Study hard, or you will fail the entrance exam.',
    'You and I are students.',
    'Study hard, and you will pass the entrance exam.',
    'He is very rich, but he is not happy.',
  ],
}
test_data_0025 = { 

      # **Guideword:** COMBINING COMPARATIVE ADJECTIVES WITH 'AND'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'and' to join a limited range of comparative adjectives.► adjectives: comparatives
        
  'positive': [
    'It is getting darker and more dangerous.',
    'Your new phone looks smaller and nicer than the old one.',
    'I can teach you cheaper and better.',
    'As the evening wore on, the wind became stronger and more perilous for the pilots.',
    'This book seems like more interesting and more excited.',
    'This bag is much cheaper and bigger.',
    # 'It is getting colder and colder.',
    # colder: NN
    'The hot-air balloon is going up higher and smaller.',
    # 'He is much taller and cuter than me.',
    # cuter: NN
    'This airplane is much cheaper and faster.',
  ],
  'negative': [
    'You want books more than CDs.',
    'He likes math better than English.',
    'We walked more slowly than a turtle.',
    'It took more time than I\'d expected.',
    'It\'s warmer this year than it was last year.',
    'I like him better than her.',
    'I\'m going earlier than that.',
    'I wanted to tell you sooner.',
    'These beans are more delicious than last year\'s beans.',
    'I am younger than you.',
    'I became more and more nervous as the interview went on.',
    'Sleeping is more important than taking medicine.',
    'Skiing is more difficult than surfing.',
    'There\'s nothing better than a cold beer after exercise.',
    'She\'s better friends with him than I am.',
    'I\'m happier than last time.',
    'I\'m sure we\'ll be able to sing better than the other classes.',
    'That one has a shorter tail.',
    'Japan\'s schools are tougher than the ones in Korea.',
    'The ball drops more slowly than a falling feather.',
    'If they choose to stay longer, they can stay a few hours more and pay 20 dollars,'
    ' or they can stay one day more and pay the full daily rate.',
  ],
}
test_data_0026 = { 

      # **Guideword:** COMBINING MORE THAN TWO ADJECTIVES
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use commas and 'and' to join more than two adjectives, after 'be'.
        
  'positive': [
    'My home is small, dirty and pretty dark.',
    'There is a nice, cozy, and natural cafe over there.',
    'You are intelligent, humble, and generous.',
    'She is cute, beautiful and clean.',
    'He is smart, handsome and rich.',
    'This product is cheap, useful and cool.',
    'My last year was strenuous, hectic, and unlucky.',
    'I am tired, hungry and thirsty.',
    'My grandfather is old, weak and kind.',
    # 'I would say that you are happy, chill, and fun right now.',
    # chill: UH
  ],
  'negative': [
    'Your children are only five and seven years old, so you want to be careful about the information you give them.',
    'The ruby is big and round, and there are twelve diamonds around the edge of the ruby.',
    'You can build operating systems, systems applications, and compilers with C.',
    'Examples of system applications are database systems, word processors, and graphic packages.',
    'You, he and I are good friends.',
    'I went to eat outside and met my friends.',
    'I bought a book and a pencil.',
    'I bought hen\'s eggs, fish and seashells.',
    'I found a wallet and I reported it to the police.',
    'We visited Kyoto, Osaka, and Nara.',
    'I took a train to go home and she took a bus.',
    'He drinks orange juice and I drink mango juice.',
    'I will wear this and go shopping.',
    'She does both simultaneous and consecutive interpreting.',
    'He has lived in Hokkaido and in Okinawa.',
    'Tom and David are good friends.',
    'I want pens, notebooks, textbooks and glasses.',
    'We met and went to see a movie.',
    'He and his friend both passed the entrance exam.',
    'You and I are students.',
    'She was over there and I saw her.',
    'I like apples and oranges.',
    'I have both managerial and operational roles in the company.',
    'Study hard and you will pass the entrance exam.',
  ],
}
test_data_0027 = { 

      # **Guideword:** COMBINING THE SAME COMPARATIVE ADJECTIVE WITH 'AND'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'and' to repeat a comparative adjective to indicate change over time, usually after 'become' or get. ► adjectives: comparatives
        
  'positive': [
    # 'This product is becoming cheaper and cheaper to buy.',
    'She is getting more and more famous.',
    'It is getting colder and colder.',
    'Snow White became more and more beautiful as she grew up.',
    'The weather is getting hotter and hotter.',
    'The days are getting shorter and shorter.',
    'This place is getting more and more popular these days.',
    'My friend gets cuter and cuter.',
    'It is getting darker and darker.',
    'All people are getting older and older day by day.',
  ],
  'negative': [
    'You, he and I are good friends.',
    'She was over there and I saw her.',
    'She does both simultaneous and consecutive interpreting.',
    'He and his friend both passed the entrance exam.',
    'I took a train to go home and she took a bus to go home.',
    'I wanted to tell you sooner.',
    'He has lived in Hokkaido and in Okinawa.',
    'Japan\'s schools are tougher than the ones in Korea.',
    'We visited Kyoto, and Osaka, and Nara.',
    'I want pens, notebooks, textbooks and glasses.',
    'You want books more than CDs.',
    'I\'m sure we\'ll be able to sing better than the other classes.',
    'He likes math better than English.',
    'The ball drops more slowly than a falling feather.',
    'He drinks orange juice and I drink mango juice.',
    'I went to eat outside and met my friends.',
    'Skiing is more difficult than surfing.',
    'These beans are more delicious than last year\'s beans.',
    'It\'s warmer this year than it was last year.',
    'I am younger than you.',
    'She will need the U.S. bank account number and the routing number.',
    'There is a large timer and a small timer.',
    'If they choose to stay longer, they can stay a few hours more and pay 20 dollars, or they can stay one day more and pay the full daily rate.',
  ],
}
test_data_0028 = {

      # **Guideword:** COMPOUND ADJECTIVES
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use a limited range of compound adjectives ('good-looking', 'well-known') 
        
  'positive': [
    'That\'s not well-known in Japan.',
    'A good-looking horse may sometimes break down.',
    'That actor is good looking.',
    'He is well-known as a hen-pecked husband.',
    'The song is well known to everybody.',
    'Kumamon is now well known across the country.',
    'His name is well known to us',
    'That restaurant has many good looking dishes.',
    'He is good-looking and smart.',
    'From my point of view, everyone is good-looking.',
  ],
  'negative': [
    'You look good with a smiley face.',
    'He was popularly known as Shikibu.',
    'I think that cherry blossoms would look good on the Shrine gate.',
    'He is known to everybody.',
    'It will look good on you.',
    'It is not known who his mother was.',
    'That hairstyle doesn\'t look good on you.',
    'You look good in green.',
    'I should have known better.',
    'Nothing certain is known.',
    'Her name is not known.',
    'You look good with short hair.',
    'Do those sunglasses look good on me?',
    'The author is not known',
    'Flowers look good on you.',
    'I think you look good in that dress',
    'It is not known who compiled the text.',
    'The location of her tomb is not known.',
    'Those clothes will definitely look good on my grandchild.',
    # どっちの意味か捉えづらい。
    # 'That was well known.',
  ],
}
test_data_0029 = { 

      # **Guideword:** COMPOUND ADJECTIVES
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use an increasing range of compound adjectives ('up-to-date', 'state-of-the-art')
        
  'positive': [
    'Someone who is tolerant and placid is an easy-going person.',
    'A tablecloth which is very white is a snow-white tablecloth.',
    'A polite child is a well-behaved child.',
    'A train which moves slowly is a slow-moving train.',
    'You can buy the state-of-the-art graphics cards if you\'re rich.',
    'Someone who is more experienced is more likely to have be an open-minded person.',
    'A lamp whose shade is red is an up-to-date decoration in today\'s fashion.',
    'Dresses which are as yellow as a lemon are lemon-yellow dresses.',
    'A mountain on which some snow has fallen down is a snow-covered mountain.',
    'People who don\'t easily see with the ideas of the others are narrow-minded people.',
  ],
  'negative': [
    'Ten young boys are playing soccer.',
    'Indian food is spicy.',
    'I have a lot of friends.',
    'She has much money.',
    'Students listened quietly to her speech.',
    'There are many pencils on the desk.',
    'His suit is nice and blue.',
    'They are walking on the beach slowly.',
    'Music makes people happy.',
    'You have a lot of work.',
    'The painting is beautiful.',
    'They sell old books.',
    'He has a few books.',
    'He has a small bag.',
    'Jack is eating a big steak.',
    'We saw someone strange at the station.',
    'He has a new car.',
    'I want something cold to drink.',
    'This is a beautiful lake.',
    'We had a little rain this summer.',
  ],
}
test_data_0030 = { 

      # **Guideword:** PHRASES MODIFYING NOUNS
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use adjective phrases to modify nouns.
        
  'positive': [
    'This is a big, tall, and expensive house for this neighborhood.',
    'She is a nice and intelligent person.',
    'This is very delicious and extremely expensive pie.',
    'The extremely tired kitten fell asleep by her food dish.',
    'She has a new boyfriend who is a rich, handsome, and talented man.',
    'I got a new, expensive, and functional phone yesterday.',
    'Your apple pie has a very tempting smell.',
    'It was a very pricey but really beautiful outfit.',
    'That complex has quite small but cheap apartments.',
    'It was an unbelievably difficult exam.',
  ],
  'negative': [
    'The house they live in is beautifuls.',
    'We had little rain this summer.',
    'You have to be open-minded about things.',
    'Danny’s dog is well-behaved.',
    'This lake is quite beautiful.',
    'He has few books.',
    'Linda’s hair is gorgeous.',
    'The shoes I lost were my most comfortable.',
    'She has much money.',
    'The shark we saw was a man-eater.',
    'The jacket he just bought is second-hand.',
    'We saw someone strange at the station.',
    'He is more intelligent than this boy.',
    'He has a small bag.',
    'Susan is really clever.',
    'Jack likes his steak well-done.',
    'The doctor is very late.',
    'He writing is meaningless.',
    'There are many pencils on the desk.',
    'Ten boys are playing soccer.',
  ],
}
test_data_0031 = { 

      # **Guideword:** COMPOUND ADJECTIVES
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** combining
      # **Lexical Range:** 3.0
      # **CEFR level:** C1
      # **CAN-DO:** Can use a wide range of compound adjectives ('open-minded', 'above-mentioned', 'well-to-do', 'jaw-dropping') 
        
  'positive': [
    'I want to be more open-minded.',
    'The above-mentioned are the regular teachers.',
    'Buses are available for some of the above-mentioned routes.',
    'He is a well-to-do merchant.',
    'Her parents are well-to-do.',
    'I have become open-minded.',
    'She likes a man who is open-minded.',
    'The view from the mountaintop was truly jaw-dropping.',
    'She seems an open-minded person.',
    'The details of the above-mentioned steps are as follows.',
  ],
  'negative': [
    'You have done well.',
    'The peaches are dropping ripe.',
    'This is something that should be mentioned specially.',
    'Your mind is made up.',
    'Are you out of your mind!?',
    'Were you well today as well?',
    'He mentioned the launch.',
    'Mind your own business.',
    'Nothing comes to mind.',
    'I don\'t mind labour.',
    'The animal ran away dropping blood on his trail.',
    'He is being mentioned as the possible next president.',
    'He mentioned having met me.',
    'I don\'t want my name mentioned.',
    'All account numbers are mentioned.',
    'The men were dropping on every side.',
    'Are you all of a mind?',
    'I\'m doing quite well.',
    'The sun was dropping toward the west.',
    'It is mentioned in that document.',
  ],
}
test_data_0032 = {

    # **Guideword:** COMBINING MULTIPLE ADJECTIVES
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** combining
    # **Lexical Range:** None
    # **CEFR level:** C2
    # **CAN-DO:** Can combine more complex, lengthy strings of adjectives, joining the last two adjectives with 'and'.

    'positive': [
        'Our new homeroom teacher would be nice, cool, smart, and fair.',
        'The beneficial effect of the release of the videogame was significant, far-reaching, and long-lasting.',
        'The angry, irritated, and blushing teacher scolded his pupils for eating chewing gum in his class.',
        'Your father has left a great, fantastic, and wonderful gift for you.',
        'She is sweet, beautiful, and easy to talk to.',
        # friendly -> kind (advmod)
        # 'She is kind, beautiful, and easy to talk to.',
        'The exam you are going to take is said to be long, difficult, and expensive.',
        'The view at the top of the mountain would be so beautiful, spectacular, and unearthly.',
        'The green, white, and blue colour in the national flag of Sierra Leone looks like the signboard of Family Mart.',
        'The earthquake in 2011 caused a serious, widespread, and irreversible damage to the Tohoku region.',
        'This new express train is rapid, comfortable, and not so expensive.',
    ],
    'negative': [
        'Thank you to the six thousand, four hundred and ninety-two people who came here to join us!',
        'She likes grammar and all that.',
        'The houses were a mix of pre- and post-war architecture.',
        'I love going to the beach for the warmth, the sun, and the sea air.',
        'I am so ready for springtime, bluebonnets, thunderstorms and fireflies.',
        'Twenty three and a half gallons of milk have spilt from the pail.',
        'She should go and find another job.',
        'My best friend and my father’s father both come from Wales.',
        'The Australians have won three gold medals and two silvers in the swimming events.',
        'National African American History Month is a celebration of freedom, purpose, and opportunity they have bestowed on future generations.',
        'You are putting false information out and convincing your loyal fans of lies.',
        'I found it hard to follow what the teacher was saying, and eventually I lost my ability to concentrate.',
        'You are a vegetarian and you eat fish?',
        'The meal was very expensive and not very nice.',
        'Please rate and leave comments as well!',
        'She spends hours and hours on the phone.',
        'They knocked down all the houses and they built a car park.',
        'I asked him to go and find my glasses.',
        'Both you and I know what really happened.',
        'Many pupils have extra classes in the evenings and on the weekends.',
    ],
}
test_data_0033 = {

    # **Guideword:** FOCUS
    # **Guideword type:** USE
    # **Super category:** ADJECTIVES
    # **Sub category:** combining
    # **Lexical Range:** None
    # **CEFR level:** C2
    # **CAN-DO:** Can use a list of adjectives in ellipted clauses before and after a noun, to give focus. ► focus

    'positive': [
        "Narrow, winding, and treacherous, we had to travel many roads to get to our destination.",
        "In the attic – dusty and thin – we found our old childhood toys had aged the same as we had.",
        "The poster depicted a child, brown-haired and blue-eyed, who was expounding on the greatness of some sugary cereal.",
        "Tanned and handsome, the old farmer pulled his boots off for the last time.",
        "The latter – thin and wirey – didn't look like much of a contender.",
        "Intelligent and funny, Jaimie quickly advanced as a class leader.",
        "Warm and dense, the fog had settled over the paddies and there was the stillness that precedes rain.",
        "The popular girls – blonde, blue-eyed and wealthy – were the ones who lived on the beach and had suntans.",
        "Insistent and loud, a voice rang out in the hall as she reached the head of the stairs.",
        "Good-natured and friendly, it was only natural that he was so popular among his peers.",
    ],
    'negative': [
        "The big blue football jersey fit the boy just right.",
        "An unmarked police car patrolled the area.",
        "A police car patrolled the desolate, nighttime neighborhood.",
        "Zach rode the wooden roller coaster six times.",
        "The mountainous region offers the best views in the whole country.",
        "Take a look at this bright green spider!",
        "He bought a wonderful old French car.",
        "There is a cute little cottage at the peak.",
        "An attractive young American lady crossed the street.",
        "We have modern Japanese electric cars here.",
        "Yesterday I saw a big square blue box in his house.",
        "Thousand of cheering fans filled the arena.",
        "The game featured several new players.",
        "Our English textbook is boring.",
        "My fifteen interesting young UAE students ask great questions.",
        "I bought a black, wooden table.",
        "Yesterday my sister gave me a blue wool sweater.",
        "I bought an enormous, rectangular Turkish rug on my vacation.",
        "Don’t forget to bring your new striped jacket.",
        "The child was playing with a blue and red plastic robot.",
    ],
}
test_data_0034 = {

    # **Guideword:** + -ER
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** comparatives
    # **Lexical Range:** None
    # **CEFR level:** A2
    # **CAN-DO:** Can form comparative adjectives from adjectives of one syllable by adding '-er'.


    'positive': [
        "I played computer games with my older brother.",
        "The shirt was cheaper than the trousers.",
        "It is easy to use and it is smaller than the old one.",
        "It is greater than nothing.",
        "You are higher than him.",
        "How is the smarter boy of the two?",
        "Which is the harder shell?",
        "What makes it look brighter?",
        "What is on the lower level?",
        "How did you become younger?"
    ],
    'negative': [
        "You look thinner.",
        "I am good.",
        "Why did it seem bigger?",
        # Exception; bett is analyzed as true adjective while it obviously is not an adjective.
        #"It seems better.",
        "Why are you becoming stranger?",
        "What's the reason that makes you such a fat man.",
        "It's better if you do it differently.",
        "Why do you guys fight with each other so strictly?",
        "How good are you?",
        "Is this the best choice for us all?",
        "Who is your best friend?",
        "What is your hobby?",
        "It is a good chance to capture it.",
        "Why did it sound better?",
        "What makes it worse than usual?",
        "Therefore, it's the worst decision I have ever made.",
        "What did you know about her disadvantages?",
        "Why should we go ahead with the worst project?",
        "What is the most interesting?",
        "What is your hobby?",
        "Where are you?",
        "How is it going?",
        "What makes it so special?",
        "What is the most beautiful thing in the world?",
        "Is that the highest mountain you have climbed up?",
        "You seem tired."
        'Tell your friend to use the zoom on her camera to look past you for a closer view.',
    ],
}
test_data_0035 = {

    # **Guideword:** + -IER
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** comparatives
    # **Lexical Range:** None
    # **CEFR level:** A2
    # **CAN-DO:** Can form comparative adjectives with adjectives of two syllables ending in '-y' by changing the 'y' to an 'I' and adding '-er'.

    'positive': [
        "I like it because it's small and easier to use than other phones.",
        "The students were happier and there were lots of stories for their parents.",
        "It's easier for me to get hired.",
        "He is uglier than you.",
        "This environment is noisier than the one before.",
        "Now the burden is heavier.",
        "You are funnier than anyone else here.",
        "Currently, he is busier with his work.",
        "America is drier in this season.",
        "He is sleepier than me.",
    ],
    'negative': [
        "I am good.",
        "It seems better.",
        "Why are you so tired?",
        "What's the reason that makes you such a fat man.",
        "It's better if there's no war.",
        "Why do you guys fight with each other so violently?",
        "How good are you?",
        "Is this the best choice for us all?",
        "Who is your best friend?",
        "What is your hobby?",
        "It is a good chance to capture it.",
        "Why did it sound better?",
        "What makes it worse than usual?",
        "Therefore, it's the worst decision I have ever made.",
        "What did you know about her disadvantages?",
        "Why should we go ahead with the worst project?",
        "What is the most interesting?",
        "What is your hobby?",
        "Where are you?",
        "How is it going?",
        "What makes it so special?",
        "What is the most beautiful thing in the world?",
        "Is that the highest mountain you have climbed up?",
        "You seem tired."
    ],
}
test_data_0036 = {

    # **Guideword:** BEFORE NOUNS
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** comparatives
    # **Lexical Range:** None
    # **CEFR level:** A2
    # **CAN-DO:** Can use comparative adjectives attributively, before nouns.

    'positive': [
        "How did the older people feel about the drama?",
        "We cannot succeed without a better plan.",
        "I have stricter conditions.",
        "Better communication was required at the meeting.",
        "I just watched a cricket match with my younger brother and my father.",
        "I bought the shoes and the t-shirt for my older brother's party.",
        "I want to take this course because I want to know more about computers, so that I can get a better job. ",
        "He is an uglier man than you.",
        "It gradually became a noisier environment.",
        "You should take newer samples.",
        "You are the type of person that can always create a happier environment.",
        "Currently, he has a busier schedule than most of us.",
        "Africa is a drier area in the world.",
        "He is a much wittier person than me.",
    ],
    'negative': [
        "I am good.",
        "It seems better.",
        "Why are you so tired?",
        "What's the reason that makes you such a fat man.",
        "It's better if there's no war.",
        "Why do you guys fight with each other so strictly?",
        "How good are you at basketball?",
        "Is this the best choice for us all?",
        "Who is your best friend?",
        "What is your hobby?",
        "It is a good chance to capture it.",
        "Why did it sound better?",
        "What makes it worse than usual?",
        "Therefore, it's the worst decision I have ever made.",
        "What did you know about her disadvantages?",
        "Why should we go ahead with the worst project?",
        "what is the most interesting?",
        "What is your hobby?",
        "Where are you?",
        "How is it going?",
        "What makes it so special?",
        "What is the most beautiful thing in the world?",
        "Is that the highest mountain you have climbed up?",
        "You seem tired.",
        'Answer the questions so you can find your perfect dress.',
        # before nouns
        'Tell him wine tastes better in a glass.',
    ],
}
test_data_0037 = {
    # **Guideword:** COMPLEMENT OF 'BE'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** comparatives
    # **Lexical Range:** None
    # **CEFR level:** A2
    # **CAN-DO:** Can use comparative adjectives as a complement of 'be'.
    'positive': [
        "Sam, It would be better if you came after 4.30 p.m.",
        "You can come by bus, it's easier.",
        "You need to wear shorts and a t-shirt so you are more comfortable.",
        "He is much uglier than you.",
        "Currently, he is busier than most of us.",
        "Africa is drier than any other continent.",
        "He is much more hard-working than any of you.",
        "I am more interesting than any one else in the party.",
        "Why are you smarter than him?",
        "The competition is much more competitive."
    ],
    'negative': [
        "It gradually became a noisier environment.",
        "You are the type of person that can always create a happier environment.",
        "You should take more responsibility than the rest of the team.",
        "I want to take this course because I want to know more about computers, so that I can get a better job. ",
        "I just watched a cricket match with my younger brother and my father.",
        "I bought the shoes and the t-shirt for my older brother's party.",
        "I am good.",
        "It seems better.",
        "Why are you so tired?",
        "What's the reason that makes you such a fat man.",
        "It's best if there's no war.",
        "Why do you guys fight with each other so strictly?",
        "How good are you at baseball?",
        "Is this the best choice for us all?",
        "Who is your best friend?",
        "What is your hobby?",
        "It is a good chance to capture it.",
        "Why did it sound better?",
        "What makes it worse than usual?",
        "Therefore, it's the worst decision I have ever made.",
        "What did you know about her disadvantages?",
        "Why should we go ahead with the worst project?",
        "what is the most interesting?",
        "What is your hobby?",
        "Where are you?",
        "How is it going?",
        "What makes it so special?",
        "What is the most beautiful thing in the world?",
        "Is that the highest mountain you have climbed up?",
        "You seem tired."
    ],
}
test_data_0038 = {

    # **Guideword:** DOUBLE CONSONANT + '-ER'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** comparatives
    # **Lexical Range:** None
    # **CEFR level:** A2
    # **CAN-DO:** Can form comparative adjectives with adjectives of one syllable with a short vowel, by doubling the final consonant and adding '-er'

    'positive': [
        "The rooms are all very beautiful, but I prefer my room because it's bigger.",
        "I bought lots of T-shirts because the weather is getting hotter.",
        "You look thinner wearing these clothes.",
        # The parser could not analyze wetter as "JJR" correctly, instead as "NN".
        #"Putting this bottle of water in the room, the environment would become wetter",
        "You can become slimmer by exercizing.",
        "Tom is a fatter person than any of us.",
        "This hat is redder than most of the others.",
        "Watching the news, the boy becomes sadder.",
        "A bigger tool is required.",
        "The hotter the weather becomes, the more accidents there will be."
    ],
    'negative': [
        "Sam, It would be better if you came after 4.30 p.m.",
        "You can come by bus, it's easier.",
        "You need to wear shorts and a t-shirt so you are more comfortable.",
        "He is an uglier man than you.",
        "Currently, he is busier than most of us.",
        "Africa is a drier area in the world.",
        "He is much more hard-working than any of you.",
        "I am a more interesting man.",
        "Why are you smarter than him?",
        "It is a much more competitive competation.",
        "It gradually becomes a noisier environment.",
        "It seems brighter.",
        "Is that the highest mountain you have climbed up?",
        "That is kind of the point.",
        "About how many miles are on it?",
        "Trying is better than not trying.",
        "What makes it worse than usual?",
        "I bought the shoes and the t-shirt for my older brother's party.",
        "You are the type of person that can always create a happier work atmosphere.",
        "You should take more responsibility to the public.",
        'You earn $4,200 each month, and you don\'t want to pay more than 25% of your monthly income for the mortgage.',
    ]
}
test_data_0039 = {

  # **Guideword:** ENDING IN '-E' + '-R'
  # **Guideword type:** FORM
  # **Super category:** ADJECTIVES
  # **Sub category:** comparatives
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can form comparative adjectives with adjectives of one syllable ending in 'e', by adding '-r'.
    
  'positive': [
    'I think it will be nicer.',
    'You can come by boat, but I prefer to come by aeroplane because it is safer.',
    'This crack is going to be wider as time goes by.',
    #'This will become finer over the coming weeks.',
    #"finer" marked NN
    'This city is even larger than Tokyo.',
    'She is an abler woman than I thought.',
    # later is analyzed as "RB" instead of "JJR"
    #'The meeting was later than we expected.',
    # braver is analyzed as "RB" instead of "JJR"
    #'How did he change himself to a braver man in such a short period',
    # TODO: parser has troubles in accuracy of recognizing adjectives.
    'This is a nicer environment for us employees.',
    'You will become safer once you finish your martial arts training.'
  ],
  'negative': [
    "Sam, It would be better if you came after 4.30 p.m.",
    "You can come by bus, it's easier.",
    "You need to wear shorts and a t-shirt so you are more comfortable.",
    "He is an uglier man than you.",
    "Currently, he is a busier man than most of us.",
    "Africa is a drier area in the world.",
    "He is much more hard-working than any of you.",
    "I am a more interesting man.",
    "Why are you smarter than him?",
    "It is a much more competitive competition.",
    "It gradually became a noisier environment.",
    "It seems brighter in here.",
    "Is that the highest mountain you have climbed up?",
    "That is kind of the point.",
    "About how many miles are on it?",
    "Trying is better than not trying.",
    "What makes it worse than usual?",
    "I bought the shoes and the t-shirt for my older brother's party.",
    "You are the type of person that can always create a happier work environment.",
    "You should take more responsibility for the crisis."
    'You guess that taking the first bite will make you grow taller.',
  ],
}
test_data_0040 = { 

      # **Guideword:** IRREGULAR
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form irregular comparative adjectives.
        
  'positive': [
    'That is getting to be a worse day than yesterday.',
    'I feel like Tokyo has better weather than Osaka.',
    'I have two elder sisters.',
    'I have more friends than last year.',
    'We are expecting further details.',
    'I need more money to buy this computer.',
    'It\'s better to commit less fraud.',
    'There was a farther road we could have taken.',
    'The latter expression is the more important one.',
    'We think that there should be no more wars.',
    'Naomi is the elder of the two.',
    'They had a better economy before the war.',
    'If you wish to lose weight, eat less meat.',
    'Mary is a better dancer than Beth.',
    'This product is worse than I thought.',
    'I have less cash than you.',
    'She sings worse songs than I do.',
    'You have a better pitching arm than me.',
    'We\'ll look further if you want to buy a better wrist watch.',
    'I went farther north in Norway.',
    'I can\'t walk to one further store, this is the last one for today.',
    'Osaka has a worse summer than before.',
    'The more money one has, the more money one wants.',
    'The less milk in the soup the better.',
    'I feel like going to one further meeting.',
    'Of these two plans, I prefer the latter to the former.',
    'You should respect your elder brother.',
  ],
  'negative': [
    'It\'s faster than the bus.',
    'This brown table is three times bigger than that black one.',
    'I have found a nicer hotel.',
    'I can\'t walk any more.',
    'I wanted to tell you sooner.',
    'It’s even hotter than yesterday.',
    'He worked three hours longer than I did yesterday.',
    'I\'m happier than last time.',
    'They worked harder than me.',
    'Computers are getting cheaper and cheaper.',
    'It was easier than the practice test.',
    'The downtown library is bigger than the school library.',
    'This book is less large than that.',
    'You probably know more about San Francisco than I do.',
    'It\'s warmer this year than it was last year.',
    'The employment rate will go up more.',
    'I\'m going earlier than that.',
    'It\'s harder than I thought.',
    'She can run faster than Wendy.',
    'Japan\'s schools are tougher than the ones in Connecticut.',
    'I got up earlier than usual.',
    'They worked harder.',
    'I will get more frustrated if this goes on.',
    'I was hungrier than you.',
    'John is taller than Rick.',
    'An older gentleman asks if he can help.',
  ],
}
test_data_0041 = { 

      # **Guideword:** WITH 'MORE'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form a range of comparative adjective phrases using 'more' + longer adjectives (usually three or more syllables). 
        
  'positive': [
    'I think it\'s more interesting than a report.',
    'This flower is more beautiful than that one.',
    'Listening is more important than speaking.',
    'They bought more excellent bags than I did.',
    'Sleeping is more important than taking medicine.',
    'That is more common than you thought.',
    'These beans are more delicious than last year\'s beans.',
    'He is more famous than anyone in this town.',
    'This movie is much more important than homework.',
    'My dog is more adorable than others.',
    'This book is more well-known than that one.',
  ],
  'negative': [
    'It\'s faster than the bus.',
    'That is getting worse.',
    'The brown monkey is smaller than the gray one.',
    'You read faster than me,',
    'I have fewer friends than you.',
    'I need something smaller than this.',
    'I can\'t walk any more.',
    'It’s even hotter than yesterday.',
    'I\'m happier than last time.',
    'I need more money to buy this computer.',
    'Computers are getting cheaper and cheaper.',
    'You play baseball better than me.',
    'It was easier than the practice test.',
    'We walked more slowly than a turtle.',
    'The downtown library is bigger than the school library.',
    'You probably know more about San Francisco than I do.',
    'The employment rate will go up more.',
    'It\'s harder than I thought.',
    'We need a little more coffee.',
    'John is taller than Rick.',
    'She can run faster than Wendy.',
    'I got up earlier than usual.',
    'The more one has, the more one wants.',
    'It\'s much quicker and easier to dry short hair.',
    'This product is worse than I thought.',
  ],
}
test_data_0042 = { 

      # **Guideword:** WITH 'THAN'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use a comparative adjective with 'than' to compare two nouns or noun phrases.► comparative clauses
        
  'positive': [
    'I think it\'s more interesting than a report.',
    'It\'s faster than the bus.',
    'This flower is more beautiful than that one.',
    'Listening is more important than speaking.',
    'The brown monkey is smaller than the gray one.',
    'They bought more excellent bags than I did.',
    'Sleeping is more important than taking medicine.',
    'The downtown library is bigger than the school library.',
    'These beans are more delicious than last year\'s beans.',
    'This movie is much more important than homework.',
  ],
  'negative': [
    'You look more beautiful in white.',
    'I like the red one better.',
    'When I was younger, I enjoyed watching Doraemon.',
    'That is getting worse.',
    'I feel better this morning.',
    'The girl became more and more beautiful.',
    'I prefer cats to dogs',
    'It\'s getting colder and colder outside.',
    'Sometimes I feel inferior to my older brother.',
    'I need more money to buy this computer.',
    'Computers are getting cheaper and cheaper.',
    'We walked more slowly than a turtle.',
    'I\'ll call you later.',
    'Your products are superior to all similar items.',
    'You read faster than me.',
    'We need a little more coffee.',
    'You should study harder.',
    'You should run faster.',
    'Walk faster, or you will be late for school.',
    'Please speak more slowly.',
    'It\'s much quicker and easier to dry short hair.',
  ],
}
test_data_0043 = { 

      # **Guideword:** WITH '(SO) MUCH'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use '(so) much' to modify and intensify comparative adjectives used predicatively after a verb, usually 'be'. 
        
  'positive': [
    'My town is so much warmer than this town.',
    'We’re so much happier than when we got married.',
    'I think this pink dress is so much prettier than the blue one.',
    'That actor was so much more popular than this actor.',
    'His brother may be much kinder than him.',
    'He is so much more handsome than my ex.',
    'My sister is much more beautiful than she was 20 years ago.',
    'This car is much more expensive than that one.',
    'Her necklace was much more gorgeous than mine.',
    'This story is much more interesting than that one.',
  ],
  'negative': [
    'It took more time than I\'d expected.',
    'You like books better than CDs.',
    'I\'m going earlier than that.',
    'I wanted to tell you sooner.',
    'He is very tall but his brother is even taller.',
    'She\'s better friends with him than I am.',
    'That one has a shorter tail.',
    'Japan\'s schools are tougher than the ones in Korea.',
    'There\'s nothing better than a cold beer after exercise.',
    'The ball drops more slowly than a falling feather.',
    'Skiing is more difficult than surfing.',
    'She is richer than most people but her mother is even richer.',
    'These beans are more delicious than last year\'s beans.',
    'I became more and more nervous as the interview went on.',
    'I\'m sure we\'ll be able to sing better than the other classes.',
    'We walked more slowly than a turtle.',
    'I\'m happier than last time.',
    'Her score was bad but mine was even worse.',
    'I like him better than her.',
    'Ken is far taller than Tom.',
  ],
}
test_data_0044 = { 

      # **Guideword:** WITH 'A (LITTLE) BIT'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'a (little) bit' to modify comparative adjectives used predicatively after a verb, usually 'be'.
        
  'positive': [
    'My house is a little bit taller than hers.',
    'You are a bit more handsome than my brother.',
    #'Her life is a little bit better than others.',
    'She is a bit more famous than me.',
    #'This bag is a little bit cheaper than that one.',
    'She is a bit taller than me.',
    'This new necklace is a little bit more expensive than the old one.',
    'My phone is a bit older than yours.',
    # 'It\'s a bit colder today than yesterday.',
    # bit -> colder (compound)
    'She is a bit stinkier than my sister.',
    'That is a bit more unfortunate than last time.',
    'I\'m a bit more embarrassed than he was.',
    #'This train is a bit later than yesterday.',
    'You\'re a bit harsher than my previous teacher.',
  ],
  'negative': [
    'We’re much happier than when we got married.',
    'My sister is much more beautiful than she was 20 years ago.',
    'My throat hurts a little bit.',
    'Her necklace was much more gorgeous than mine.',
    'I\'m a bit under pressure now.',
    'That is a bit unfortunate.',
    'This story is much more interesting than that one.',
    'I am in a little bit of a hurry',
    'This car is much more expensive than that one.',
    'I think this pink dress is much prettier than the blue one.',
    'My town is much warmer than this town.',
    'It tastes a bit rich.',
    'His brother may be much kinder than him.',
    'I overcooked the fish a bit.',
    'I have a bit of time.',
    'That actor was much more popular than this actor.',
    'He is much more handsome than my ex.',
  ],
}
test_data_0045 = { 

      # **Guideword:** WITH 'AND'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'and' to repeat a comparative adjective to indicate change over time, usually after 'become' or 'get'.  ► adjectives: comparatives
        
  'positive': [
    'This room is getting warmer and warmer.',
    'This place getting more and more popular these days.',
    'She is getting more and more beautiful.',
    'My friend becomes cuter and cuter.',
    # 'This product is becoming cheaper and cheaper to buy.',
    # becoming -> cheaper (conj:and)
    'My dog is getting bigger and bigger.',
    'My brother becomes taller and taller.',
    'All people are getting older and older day by day.',
    'My friend becomes more and more famous in Japan every day.',
    'The weather is getting hotter and hotter.',
  ],
  'negative': [
    'She was over there and I saw her.',
    'He likes math better than English.',
    'My mother gets up earlier than I do.',
    'It\'s warmer this year than it was last year.',
    'I went to eat outside and met my friends.',
    'The more I know him, the more I love him.',
    'This flower is more beautiful than that one.',
    'He is much taller than his brother.',
    'The sooner, the better.',
    'I wanted to tell you sooner.',
    'The more you have, the more you want.',
    'She does both simultaneous and consecutive interpreting.',
    'This house is bigger than that one.',
    'I am younger than you.',
    'The older we grow, the weaker our memory becomes.',
    'He and his friend both passed the entrance exam.',
    'Skiing is more difficult than surfing.',
    'He is a lot taller than his brother.',
    'The higher we go up, the colder the air becomes.',
    'I took a train to go home and she took a bus to go home.',
  ],
}
test_data_0046 = { 

      # **Guideword:** WITH 'EVEN'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'even' to modify and intensify comparative adjectives used predicatively after a verb, usually 'be' and 'get'.
        
  'positive': [
    'Her score was bad but mine was an even worse score.',
    'Most people love her last movie, but they think the new one is an even better movie.',
    'He is very tall but his brother is an even taller man.',
    'He plays the piano very well, but he plays an even better saxophone.',
    'An even more important point is that the new Internet service is super cheap.',
    'Tatebayashi in Gunma is an even hotter city than this one.',
    'Your exam score is great, but mine is an even better score.',
    'Tomorrow will be an even colder day with snow in Tokyo.',
    'He was an even more popular actor than Orson Welles.',
    'She is richer than most people but her mother is an even richer person.',
  ],
  'negative': [
    'His brother may be much kinder than him.',
    'He is much more handsome than my ex.',
    'Don’t even think of quitting your job.',
    'Even though I called David more than 50 times, he didn’t answer.',
    'Last night’s game between the Reds and the Blues was an even fight.',
    'The color of the walls of this house are an even color.',
    'Steve even helped me.',
    'This story is much more interesting than that one.',
    'He has even tried bungee jumping.',
    'You honestly shouldn’t have said that to her, even if everyone was thinking it.',
    'This car is much more expensive than that one.',
    'I think this pink dress is much prettier than the blue one.',
    'I’m too tired to do anything. I don’t even want to watch TV.',
    'I am younger than you.',
    'Two, four, and six are even numbers.',
    'I wanted to tell you sooner.',
    'He likes math better than English.',
    'My town is much warmer than this town.',
    'Her necklace was much more gorgeous than mine.',
    'Most American people have even teeth.',
  ],
}
test_data_0047 = { 

      # **Guideword:** WITH 'A LOT'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'a lot' to modify and intensify comparative adjectives used predicatively after a verb, usually 'be'. 
        
  'positive': [
    'I am a lot more handsome than you.',
    'His TV is a lot bigger than mine.',
    'I will be a lot more famous in the future.',
    'This wallet is a lot bigger and more expensive than the old one.',
    'It would be a lot easier if you help me.',
    'It would be a lot more convenient than before.',
    'It would be a lot better if you gave me a hand.',
    'This new phone would be a lot more convenient than the old one.',
    'You should be a lot more careful in choosing who you spend your time with.',
    'It’s a lot hotter than yesterday.',
  ],
  'negative': [
    'I think soccer is more exciting than baseball.',
    'Tatsuo is the tallest in the classroom.',
    'You\'re driving worse today than yesterday.',
    'A lot of people came to this event.',
    'Could you sing more quietly please?',
    'She arrived at the restaurant the earliest of the six people.',
    'There are a lot of friends around here.',
    'Jim works harder than his brother.',
    'The little boy ran farther than his friends.',
    'A lot of my cousins live abroad.',
    'He arrived there earlier than Jack.',
    'I like cats a lot.',
    'Her sister is more selfish than her.',
    'Everyone in the race ran fast, but John ran the fastest of all.',
    'My friend speaks English better than me.',
    'He has done the best in the team.',
    'She likes to eat a lot.',
    'We’re even happier than when we got married.',
    'The teacher spoke more slowly to help us to understand.',
    'My sister is even more beautiful than she was 20 years ago.',
  ],
}
test_data_0048 = { 

      # **Guideword:** WITH 'MUCH' + NOUN
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'much' to modify and intensify comparative adjectives used attributively before countable and uncountable nouns. 
        
  'positive': [
    'He bought a much more expensive watch than mine.',
    'I have much more handsome friends than you.',
    'They held a much more interesting event than last time.',
    'He has much more exciting toys than me.',
    'This one is a much more interesting movie than that one.',
    'I brought much heavier bags than last time.',
    'She has much longer hair than me.',
    'She has a much smaller cat than mine.',
    'She has a much taller brother than me.',
    'He knows much more talented actors than she does.',
  ],
  'negative': [
    'She arrived at the restaurant the earliest of the six people.',
    'It’s a lot hotter than yesterday.',
    'It would be a lot easier if you help me.',
    'My sister is even more beautiful than she was 20 years ago.',
    'This wallet is a lot bigger and more expensive than old one.',
    'His TV is a lot bigger than mine.',
    'He arrived there earlier than Jack.',
    'The teacher spoke more slowly to help us understand.',
    'The little boy ran farther than his friends.',
    'Her sister is more selfish than her.',
    'Everyone in the race ran fast, but John ran the fastest of all.',
    'I think soccer is more exciting than baseball.',
    'You\'re driving worse today than yesterday.',
    'He has done the best in the team.',
    'My friend speaks English better than me.',
    'Tatsuo is the tallest in the classroom.',
    'We’re even happier than when we got married.',
    'Could you sing more quietly please?',
    'Jim works harder than his brother.',
    'This new phone would be a lot more convenient than the old one.',
  ],
}
test_data_0049 = { 

      # **Guideword:** WITH 'SLIGHTLY'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'slightly' to modify comparative adjectives to a small degree.
        
  'positive': [
    'They are similar to Japanese Cormorants but slightly smaller.',
    'Please speak slightly louder.',
    'Please show me a slightly larger bag.',
    'He talked slightly slower.',
    'It is getting slightly worse than before.',
    'He seems to be slightly better today.',
    'I want to stay in a slightly cheaper hotel.',
    'It\'s slightly colder than last week.',
    'It\'s slightly larger than Hokkaido.',
    'I\'ll quote that slightly lower.',
  ],
  'negative': [
    'We’re even happier than when we got married.',
    'I think our arrival will be slightly delayed.',
    'My sister is even more beautiful than she was 20 years ago.',
    'My friend\'s house is in a slightly inconvenient place.',
    'The weather there was slightly different from what I\'m used to.',
    'Tatsuo is the tallest in the classroom.',
    'This new phone would be a lot more convenient than the old one.',
    'He knows much more talented actors than she does.',
    'His score had fallen slightly under his goal.',
    'The crystals were slightly crushed.',
    'They held a much more interesting event than last time.',
    'Please set a slightly challenging goal for yourself.',
    'He has much more exciting toys than me.',
    'I am slightly interested in that country\'s culture.',
    'I was slightly embarrassed.',
    'She has much longer hair than me.',
    'This wine has a slightly sour flavor.',
    'His TV is a lot bigger than mine.',
    'I have much more handsome friends than you.',
    'That is slightly complicated.',
  ],
}
test_data_0050 = { 

      # **Guideword:** WITH 'NO' OR 'NOT ANY'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'no' / 'not any' with comparative adjectives to limit the scale of comparison. ► comparative clauses
        
  'positive': [
    'This smartphone is no bigger than my hand.',
    'If the rain is no worse than last week, we can still go swimming.',
    'Working too much is no healthier than sleeping too much.',
    'She\'s no less beautiful than her sister.',
    'His songs are not any better than mine.',
    'You are no happier than you were a year ago.',
    'This laptop is not any cheaper than here.',
    'It is not any more expensive to rent a car than to buy one at these prices.',
    'This route not any faster than that one.',
    'If we do that, we are no better than our enemies.',
  ],
  'negative': [
    'No one can book orders from customers better than Roy.',
    'This magazine is very popular with the younger generation.',
    'As time went on, things got worse and worse.',
    'This machine runs more quietly than the old one.',
    'Your apartment has a little less space than ours.',
    'International relationships became more and more strained.',
    'Your company is larger than ours.',
    'You have a right to your property, and still more to your life.',
    'This car is easy to drive, but that one is much easier.',
    'He became more obstinate, the older he grew.',
    'Here are two roads; I wonder which is the shortest.',
    'The Asian market is much more active than the European one.',
    'This is far better than that.',
    'The older he grew, the more obstinate he became.',
    'We are now living a more comfortable life than we did before.',
    'We respect him all the more for his diligence.',
    'He is in better health now than he was when he was staying with us.',
    'His heartbeat was growing weaker and weaker.',
    'Nothing could be further from the truth.',
    'Iron and copper are metals. Iron is the more useful of the two.',
  ],
}
test_data_0051 = { 

      # **Guideword:** WITH 'NOT THAT MUCH'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** comparatives
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'not that much' to modify comparative adjectives to a small degree. ► comparative clauses
        
  'positive': [
    'Our new house isn\'t that much farther from the station than our old one.',
    'This explanation is not that much clearer in comparison to other more technical ones,',
    # parser mistakenly parsed colder as noun
    # 'It isn\'t that much colder here even in winter.',
    'Although this laptop is not that much more expensive, one can do so much with it.',
    'This problem isn\'t that much more serious than it was last week.',
    'They\'re not that much more expensive than just tiling the roof.',
    'He is not that much more intelligent, but thorough intensive effort, he finally got first prize in the previous exam.',
    'The folk tradition of people huddling together at a shrine on a specific day is not that much more popular nowadays.',
    'In places like Silicon Valley, the situation is not that much better.',
    'For most Japanese people, the Chinese language is not that much more difficult than other foreign languages.',
  ],
  'negative': [
    'I went shopping and spent a lot of money.',
    'I would much rather have my baby at home than in hospital.',
    'It was pouring with rain but there wasn’t much wind.',
    'The repairs to our car cost much more than we were expecting.',
    'There\'s nothing much to do around here.',
    'Is there much unemployment in that area?',
    'There is much concern about drug addiction in the US.',
    'I haven\'t got much change, I\'ve only got a ten euro note.',
    'Do you think many people will come?',
    'I\'ll say this much for Kay, she always agrees to help whenever we ask her.',
    'He had heard many stories about Yanto and he knew he was trouble.',
    'There aren’t many women who are priests.',
    'I\'d very much like to try skydiving someday.',
    'Are there many campsites near you?',
    'I know this isn\'t much, but it\'s the best I can do.',
    'My car isn\'t much to look at, but it\'s fast.',
    'I\'d very much like to visit them sometime.',
    'How many eggs are in this cake?',
    'That wasn\'t much of a lecture.',
    'I\'m not much of a photographer.',
  ],
}
test_data_0052 = {
    # **Guideword:** WITH 'VERY'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** modifying
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use 'very' with a limited range of common gradable adjectives.
    'positive': [
        "I like Croydon because it's very quiet and very nice.",
        "My neighbours are very friendly.",
        "That's very complex.",
        "It is very high. ",
        "It's seriously very easy.",

        "It's not very hard to find at all.",
        "I make it very clear when I'm not sure of a price, and am open to suggestions.",
        # "I am suddenly very nervous about tomorrow.",
        "I am very nervous about tomorrow.",
        "my situation is very similar.",
        "This is the very best butter.",

        "I also find it very hard to communicate with my parents.",
        "She was very quiet at her desk.",
        "It was not very cold.",
    ],
    'negative': [
        "I love it, and it suits you very well.",
        "It was like the very end of the episode of the story.",
        "I had the very same conversation with a barista just before Christmas.",
        "I try very hard to change this",
        "That's so complex.",

        "It is so high. ",
        "It's seriously so easy.",
        "I don't like him very much.",
        "Do you like him much?",
        "We much appreciate your offer.",

        "We appreciate your offer very much.",
        "She spoke very quickly.",
        "He's very much admired by his students.",
        "Very soon I could see nothing but snow.",
        "I'm able to do it very quickly now.",

        "She sat so silently",
        "He is the very man I was seeking.",
        "It was not so cold.",
        "He did it simply because he wanted to.",
        "Very rarely do you find the ideal partner.",
    ],
}

test_data_0053 = { 

  # **Guideword:** WITH DEGREE ADVERBS
  # **Guideword type:** FORM
  # **Super category:** ADJECTIVES
  # **Sub category:** modifying
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use adverbs of degree ('really', 'so', 'quite') with an increasing range of common gradable adjectives.
    
  'positive': [
    'It was really hot when I was in Japan last month.',
    'My friend looks really happy.',
    'You are really lovely.',
    'This chocolate is so sweet that I can\'t eat all of it.',
    'Your face is so big.',
    'The clothes that you wear are all so expensive.',
    'The curry rice that you cook for me is so good.',
    'My cat is so small and always sleeping.',
    'My mother was quite sad because you didn\'t come to my house yesterday.',
    'This camera looks quite cheap but can take excellent photos.',
  ],
  'negative': [
    'My house is not that big.',
    'Your cell phone is useful and easy to use.',
    'My sister is popular among students.',
    'This ocean is too deep to swim in.',
    'You are kind of different from others.',
    'My friends run fast so I can\'t catch up.',
    'It is essential for me to study abroad.',
    'My father is angry, so I have to go home now.',
    'It was hard for me to find you.',
    'I\'m a little bit busy right now.',
    'You are such a crazy person.',
    'I got fat.',
    'This cave was dark, and I couldn\'t see anything.',
    'This is my favorite color.',
    'You look tired.',
    'I\'m not afraid of anything.',
    'It is common sense so you had better know that.',
    'You are such a brave man.',
    'Your food is delicious and tasty.',
    'You can take this because it is free.',
    'They may ask you about your love of music, so be sure to tell them that you write songs and play guitar!',
  ],
}
test_data_0054 = {

      # **Guideword:** WITH PREPOSITIONAL PHRASE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form adjective phrases with a very limited range of adjectives + a prepositional phrase. 
        
  'positive': [
    'You are fond of playing baseball.',
    'I am happy for you.',
    'I was aware of your friends.',
    'She is afraid of getting to class late.',
    'It is totally different from yours.',
    'I am familiar with what you just said.',
    'I will be late for the class.',
    'She was absent from the lecture.',
    'You are responsible for this event.',
    'She was anxious about you so much.',
    'The house was full of people, my family and friends.'
  ],
  'negative': [
    'He keeps the room warm.',
    'Tom is the boy with blue eyes.',
    'He has a friend to play tennis with every Sunday.',
    'That building is tall.',
    'The cat under the chair is mine.',
    'This is a beautiful lake.',
    'My father stayed at home.',
    'I want something to eat.',
    'One of the men pitching on the ground is John’s father.',
    'I want something cold to drink.',
    'They sell old books.',
    'The woman in the red dress is my aunt.',
    'We saw someone strange at the station.',
    'This book is interesting.',
    'My sister is under the tree.',
    'I found the book interesting.',
    'I saw him at the station.',
    'He lives in Japan.',
    'I bought a dress to wear to the party.',
    'Your shoes are on the floor.',
  ],
}
test_data_0055 = { 

      # **Guideword:** WITH 'TOO'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'too' with common gradable adjectives. 
        
  'positive': [
    'It is too expensive for me.',
    'That\'s too bad.',
    'It\'s too kind of you.',
    'The rice is too moist.',
    'It is too deep to wade across.',
    'By the time he got home, he was too tired to think.',
    'Don\'t drink too much beer.',
    'It\'s much too cold for swimming.',
    'She is too serious to joke around with.',
    'Isn\'t it too close?',
    'Don\'t be too sure of yourself!',
    'There is too much salt in it.',
  ],
  'negative': [
    'We have a cat, and a puppy, too.',
    'I study English at that school too.',
    'We finished preparing the party, and very quickly too.',
    'Higashino Keigo is my favorite author too.',
    'He is coming too.',
    'Can I come too?',
    'We had one at my elementary school too.',
    'I\'m going to quit too.',
    'I am sleepy too.',
    'Nice to meet you too.',
    'Are there battledores with our faces too?',
    'Do you like smart men too?',
    'I think so too.',
    'Not only do I have to buy groceries, but I also have to cook too?',
    'I’m currently working from Monday to Friday, and sometimes Weekends too.',
    'She is smart, funny and beautiful too.',
    'Our customers are frustrated, but we too have our own problems to solve.',
    'I have a slight cold too.',
    'I sometimes do that too.',
    'Is he coming too?',
  ],
}
test_data_0056 = { 

      # **Guideword:** WITH 'TOO' + PREPOSITIONAL PHRASE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'too' + adjective + prepositional phrase
        
  'positive': [
    'Japan is too large for me to travel completely.',
    'That\'s too bad for you.',
    'He\'s way too young for this problem.',
    'This phone is way too old for us to use right now.',
    'This watch is way too small for me.',
    'It is too deep for him to swim in.',
    'This problem is way too big for me to solve.',
    # 'It is too kind of you.',
    # 古いannotator順ならテストに通る
    # なお新しいとkindが副詞、古いと名詞で判定される（つまりどっちも間違い）
    'It is too dreadful for my friends.',
    'You\'re too good for playing baseball.',
    'Don\'t be too sure of yourself!',
  ],
  'negative': [
    'It is way too hard to understand Japanese.',
    'This snack is too sweet to eat.',
    'My company has too many people.',
    'He is coming too.',
    'Our customers are frustrated, but we too have our own problems to solve.',
    'It is way too easy to solve.',
    'We finished preparing the party, and very quickly too.',
    'The work is way too much.',
    'Nice to meet you too.',
    'I think so too.',
    'This chair is way too expensive.',
    'This water is way too sweet.',
    'She is smart, funny and beautiful too.',
    'Can I come too?',
    'This medicine is way too strong to drink.',
    'Your English is way too good.',
    'Do you like smart men too?',
    'It is too difficult to play.',
    'Not only do I have to buy groceries, but I also have to cook too?',
    'I’m currently working from Monday to Friday, and sometimes on weekends too.',
    'Is he coming too?',
  ],
}
test_data_0057 = { 

      # **Guideword:** ADJECTIVE PHRASE + NOUN
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use adjective phrases attributively, before a noun.
        
  'positive': [
    'It was a really big event yesterday.',
    'I got a very important call from your parents this morning.',
    # 'My friend has really nice parents.',
    # nice -> parents (dobj)
    'This is our really old house.',
    'My mother bought a very big, red box for me.',
    'There is a pretty nice woman over there.',
    'This is really hard question for all of us.',
    'There is a very huge lake near the town.',
    'I saw a very small cat outside of my house.',
    'He is a rather old baseball player.',
  ],
  'negative': [
    'I’m tired of his complaints.',
    'It is easy for me to read three books a day.',
    'She was rude to him for no reason.',
    'She wants to go somewhere nice.',
    'I want something cold to drink.',
    'We saw someone strange at the station.',
    'The book is boring.',
    'I am interested in economics.',
    'It was rude of her to leave so suddenly.',
    'I am 180 centimeters tall.',
    'He was bored with the lecture.',
    'I’m so tired.',
    'I am bored with football.',
    'I am good at baseball.',
    'My son is 10 months old.',
    'I found something interesting.',
    'The wall is about 16 inches thick.',
    'This is the problem involved in the plan.',
    'How do you train somebody new?',
    'I am afraid to go home.',
  ],
}
test_data_0058 = { 

      # **Guideword:** WITH 'ENOUGH'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'enough' to modify adjectives. 
        
  'positive': [
    'You don\'t try hard enough.',
    'You aren\'t fit enough.',
    'I still am not happy enough.',
    'I\'m not rich enough.',
    'We are smart enough to overcome anything.',
    'The bath is not hot enough.',
    'I\'m still not tired enough to sleep.',
    'It is not sweet enough.',
    'I didn\'t feel well enough.',
    'It is good enough for me.',
  ],
  'negative': [
    'They had sufficient evidence for a conviction.',
    'Please rest well and get plenty of sleep',
    'There is plenty of food.',
    'I\'ve got plenty of money.',
    'I believe that this can achieve a sufficient speed.',
    'We\'d like to insure sufficient time for that.',
    'There\'s sufficient food to support the people.',
    'I have plenty of time tomorrow.',
    'My explanation was not sufficient.',
    'He has plenty of fight in him.',
    'She makes a sufficient salary.',
    'They all have sufficient equipment.',
    'I believe there are sufficient results for that.',
    'Sufficient evidence has been secured.',
    'There\'s plenty of room for improvement .',
    'There are plenty of fish in the sea.',
    'The pension is not sufficient for living expenses.',
    'His speech had plenty of punch.',
    'You\'ve got plenty of time.',
    'There is plenty of mold growing on the wall.',
  ],
}
test_data_0059 = { 

      # **Guideword:** WITH 'QUITE A'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can form adjective phrases with 'quite a' + adjective.
        
  'positive': [
    'I had quite a busy day today.',
    'His wife is quite a talented woman.',
    'That\'s quite a good effort.',
    'The mayor is quite a difficult man to manage.',
    'He sat there for quite a long time.',
    'She is quite a clever girl.',
    'That is quite a good place.',
    'That is something from quite a long time ago.',
    'It is really quite a good story.',
    'It is quite a nice school.',
  ],
  'negative': [
    'His English is quite good.',
    'I am quite satisfied with it.',
    'It may be done quite cheap.',
    'You are quite skillful.',
    'She is quite a child.',
    'It happened quite recently.',
    'I am not quite so strong as you are.',
    'It\'s quite out of the question.',
    'I do not quite understand.',
    'It\'s getting quite cold.',
    'I am quite short tempered.',
    'She has quite recovered from her illness.',
    'I quite appreciate it.',
    'He loses his temper quite easily.',
    'He passed away quite suddenly.',
    'I quite agree with you.',
    'This book is quite useless.',
    'That is quite effective.',
    'That\'s quite unnecessary to add.',
    'He is quite indifferent to the matter.',
  ],
}
test_data_0060 = { 

      # **Guideword:** WITH 'TOO' + 'TO'-INFINITIVE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'too' before adjectives followed by 'to'-infinitive.
        
  'positive': [
    'This box is too heavy to lift.',
    'It\'s too early to go home.',
    'The Japanese government takes too long to decide.',
    'It is never too late to learn.',
    'We are too busy to attend to such details.',
    'You are too ready to believe.',
    'He is too proud to acknowledge his defeat.',
    'I am too busy to have enough time to spare.',
    'You are too lazy to get up.',
    'The news is too good to be true.',
  ],
  'negative': [
    'Chinese is interesting to me too.',
    'I want to buy another book too.',
    'I want to talk with you tomorrow too.',
    'We are going to go to Geneva too.',
    'I am going to become strong too.',
    'I\'m looking forward to it, too.',
    'Is it time for you to sleep too?',
    'I want to be happy too.',
    'You want to go, too, I suppose?',
    'I have to work on Sunday too.',
    'I want these to be sold in Japan too.',
    'I want to see you too.',
    'I want to do fireworks next year too.',
    'I\'m looking forward to the trip to India too.',
    'I want to go there too.',
    'I have been saying that too.',
    'Tell him not to drink too much.',
    'You should come to Japan, too.',
    'I went to the club the next day too.',
    'I want to try to go to Cambodia too.',
  ],
}
test_data_0061 = { 

      # **Guideword:** WITH 'ENOUGH' + 'TO'-INFINITIVE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'enough' after adjectives followed by 'to'-infinitive 
        
  'positive': [
    'His voice was loud enough to be heard.',
    'He was foolish enough to trust her.',
    'She is old enough to work.',
    'She\'s wise enough to know that.',
    'She is old enough to marry.',
    'I\'m rich enough to buy a house.',
    'You are healthy enough to leave the hospital.',
    'The stairs are tall enough to tire me out.',
    # parser could not parse kind as adjective correctly
    #'He was kind enough to show me the way',
    'It is cold enough to make me shiver.',
  ],
  'negative': [
    'I can not cry enough.',
    'I can never thank you enough.',
    'That is enough with this information.',
    'Please drink enough water.',
    'I don\'t get enough exercise.',
    'You aren\'t putting enough effort in.',
    'I didn\'t get enough sleep today.',
    'We have had enough of rain.',
    'You don\'t have enough push.',
    'You\'ve done more than enough.',
    'I have not eaten enough.',
    'I\'ve had enough of drinking alcohol.',
    'There\'s not enough water for them.',
    'I didn\'t explain well enough.',
    'I don\'t have enough free time.',
    'That was not washed well enough.',
    'It is boiled just enough.',
    'I have a feeling that there isn\'t enough light.',
    'The money is not enough.',
    'You don\'t try hard enough.',
  ],
}
test_data_0062 = { 

      # **Guideword:** WITH 'RATHER A'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can form adjective phrases with 'rather a' + adjective, often in formal contexts. 
        
  'positive': [
    'It\'s rather a curious situation.',
    'That\'s rather a tall order for anyone.',
    'To tell the truth, he was rather a shy boy.',
    'I have rather a busy afternoon in front of me.',
    'It\'s rather a good idea.',
    'That\'s rather a cynical remark.',
    'She was always rather a strange girl.',
    'She is rather a pretty girl.',
    'I made rather a good amount of money invested in a gold watch.',
    'It was rather a good performance.',
  ],
  'negative': [
    'It\'s rather cold today.',
    'The rice is boiled rather hard.',
    'I hear he has become rather prosperous.',
    'His greeting was rather ceremonious.',
    'You are rather tall, aren\'t you?',
    'It\'s snowing rather more than usual this year.',
    'I would have rather gone to Tokyo.',
    'I\'d rather have fish instead of meat.',
    'I found the movie rather entertaining.',
    'She sings rather unmusically.',
    'I\'d rather not say where we went.',
    'His business methods are rather conservative.',
    'I\'m rather proud of it.',
    'I\'m rather an optimist.',
    'I want to love rather than be loved.',
    'I feel rather depressed this morning.',
    'My room is rather small.',
    'His treatment is rather rough.',
    'I would rather take the train.',
    'I should rather think so.',
    'She is rather smartly dressed.',
  ],
}
test_data_0063 = { 

      # **Guideword:** WITH EXTREME ADVERBS
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can modify gradable adjectives with extreme adverbs of degree ('absolutely', 'extremely', 'incredibly', 'totally') to intensify their meaning. 
        
  'positive': [
    'She\'s absolutely stunning.',
    'I am extremely glad to hear the news.',
    'You are absolutely right.',
    'That was incredibly fascinating.',
    'You are totally useless.',
    'He is totally safe.',
    'It\'s absolutely impossible for me.',
    'The interactive exhibit is extremely fun for people of all ages.',
    'I am incredibly grateful for your cooperation.',
    'I am extremely tired.',
  ],
  'negative': [
    'You will absolutely enjoy it.',
    'I totally agree with your explanation.',
    'Absolutely, do not go anywhere.',
    'His father totally disagreed with his becoming a painter.',
    'She has totally changed her character.',
    'The country\'s foreign trade totally depends on this port.',
    'I\'ve been so busy I totally forgot that.',
    'I absolutely will go on Friday next week.',
    'I extremely resent that.',
    'I absolutely will win a medal.',
    'I totally don\'t get what\'s so good about her.',
    'I don\'t totally understand the reason.',
    'I\'m totally looking forward to it.',
    'I totally understand how that feels.',
    'That is something I totally cannot imitate.',
    'I totally know what you mean.',
    'I extremely love black tea.',
    'That book will absolutely sell.',
    'We absolutely welcome him.',
    'The emperor said that this totally lacked justice.',
  ],
}
test_data_0064 = { 

      # **Guideword:** COMPARISON
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** modifying
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use adjectives in 'as … as' and 'so … that' in comparative structures. ► comparative clauses
        
  'positive': [
    'I got up so early that I was ablet to spend time drinking coffee.',
    'His speech was so fast that nobody could follow it.',
    'It was so cold that children stopped playing.',
    'The London tube system is not as efficient as the Tokyo subway.',
    'The new equipment does not have as large a price tag as fixing the old ones.',
    'The weather was not as nice as it could be.',
    'Takeshi is not as tall as Ken.',
    'It\'s not as expensive as meat.',
    'I can not run as fast as he.',
    'He is as great a statesman as any one who ever lived.',
    'Her essays are often as long as books.',
  ],
  'negative': [
    'As long as you\'re going too, I\'m satisfied.',
    'We would not mind to prepare anything so that you may have plenty of time.',
    'The roof had fallen in, so that the cottage was not habitable.',
    'They met on Sunday so that they would go to the theme park.',
    'He has so imprudent as to fall in love.',
    'He got up early so as to catch the first train.',
    'We did it without you so that you could rest.',
    'The number of page views on my website in April is twice as large this month.',
    'I worked overnight, so that I couldn’t join the party.',
    'Switch the light on so that we can see what it is.',
    'The journey was not so much hard as it was exciting.',
    'Jeff works harder than me.',
    'This watch is just as expensive a gift.',
    'You should get coins so that you can use the vending machine.',
    'The sun was obscured by the clouds as I opened the window.',
    'He talked to the shy girl so that she would not feel left out.',
    'She wears high-heeled shoes so that she can look taller.',
    'I overslept, so that I missed the train.',
    'You should prequalify people so as to not waste anybody\'s time.',
    'I\'ll get there to rescue you as quickly as possible!',
    'The professor went so far as to deny the existence of the moon landing.',
  ],
}
test_data_0065 = {
    # **Guideword:** ATTRIBUTIVE (WITH NOUNS)
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** position
    # **Lexical Range:** 1
    # **CEFR level:** A1
    # **CAN-DO:** Can use a limited range of adjectives attributively, before a noun. ► noun phrases
    'positive': [
        "We have a big garden and a small swimming pool.",
        "I am your new neighbour.",
        "I like my home because I have a nice park next to my house."
        "This is good fish.",
        "John is a clever boy.",

        "He is in good health.",
        "Sally is a pretty girl.",
        "Sally is a cute girl.",
        "He is an old man.",
        "She married a rich businessman.",
        "I love to drink hot coffee.",
    ],
    'negative': [
        "John is clever.",
        "I am very fond of Mary in some ways.",
        "He was aware of the danger.",
        "John left the room angry.",
        "This flower is beautiful.",

        "She seems clever.",
        "Whether he will resign is uncertain.",
        "She sat silent.",
        "John came home drunk.",
        "He married young.",

        "I found the book very interesting.",
        "I consider what he did foolish.",
        "He pushed the door shut.",
        "The gardener watered the tulips flat.",
        "The chef cooked the food black.",

        "John ate the meat raw.",
        "I love to drink coffee hot.",
        "I can't drink coffee",
        "I know a man suitable for the job.",
        "This is a custom peculiar to Japan.",
    ],
}
test_data_0066 = {
    # **guideword:** predicative, with 'be'
    # **guideword type:** form
    # **super category:** adjectives
    # **sub category:** position
    # **lexical range:** 1
    # **cefr level:** a1
    # **can-do:** can use a limited range of adjectives predicatively, after 'be'.
    'positive': [
        "I like my home because my bedroom is big.",
        "This place is lovely.",
        "My kitchen is nice.",
        "This place is beautiful.",
        "John is clever.",

        "It turns out to be clear.",
        "A carbuncle is more valuable than a rock.",
        "I am happy in some ways.",
        "He was worried.",
        "The box is large.",
    ],
    'negative': [
        "This is good fish.",
        "I am finding it easy.",
        "She seems clever.",
        "John is a clever boy.",
        "Who comes nearest him in wit?",

        "He had nothing to eat.",
        "Sally is a cute girl.",
        "He is an old man.",
        "She sat in silence",
        "John left the room angry.",

        "John came home drunk.",
        "I found the book very interesting.",
        "I consider what he did foolish.",
        "He died young.",
        "The joggers ran their Nikes ragged.",

        "There is something comical about him.",
        "Is are anywhere good where I can go?",
        "There is no way out.",
        "The meeting was held yesterday.",
        "He keeps aloof from the outer world.",
    ],
}

test_data_0067 = { 

      # **Guideword:** LIMITING ADJECTIVES
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of adjectives ('main', 'only') that limit the noun that they go before.
        
  'positive': [
    'The main purpose is to get along with each other.',
    'The main thing I will do today is baseball.',
    'The only thing that he gave me was money.',
    'The main problem is how to settle it down.',
    'The main course is sauteed fish.',
    'The only place he would go is the park near his house.',
    'The only thing that I have heard is that she went somewhere else.',
    'The only person who knows about this issue is you.',
    'The main reason is that he doesn\'t like me at all.',
    'The only thing I came up with was to run away.',
  ],
  'negative': [
    'Only if she goes, will I go too?',
    'God only knows.',
    'She not only didn\'t come, but she also didn\'t call.',
    'I read that article only yesterday.',
    'You will only regret your harsh words to me.',
    'He went skiing only to sprain his ankle.',
    'Only to see the waning moon.',
    'I only have you.',
    'I only wanted to ask you the time.',
    'I can only wait.',
    'This information is for your eyes only.',
    'He had only to open his eyes.',
    'I am only too glad to go.',
    'I have only just finished the work.',
    'It is only too likely to happen.',
    'It was only after he entered the room that he realized how cold was.',
    'If only he had told me the whole story.',
    'He is a good man, only he sometimes drinks too much.',
    'He not only speaks French but also German.',
    'If I only knew.',
  ],
}
test_data_0068 = {

    # **Guideword:** PREDICATIVE, WITH 'BE'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** position
    # **Lexical Range:** 2
    # **CEFR level:** A2
    # **CAN-DO:** Can use an increasing range of adjectives predicatively, after 'be'.

    'positive': [
        "Yes, I am free Monday morning.",
        "I love her because she is friendly.",
        "Are there any notably good or bad things that are common on them?",
        "Are you sure you're actually reading my posts?",
        "At first I was mildly annoyed they'd hide that from me, but very quickly I realized I was thankful they did.",
        "This is so awesome!",
        "I think home invaders are lower than child molesters.",
        "The debates were heavy, I can't remember what the final ruling was.",
        "I know people who have thought Onion articles were real.",
        "What if I really am delusional?",
        "Sadly, I am notorious for being confused.",
        "If so, I am sorry that you went through that.",
        "Well if you decide you need to rid yourself of her, I am free.",
        "This would be much more enjoyable if it were slowed down.",
        "What if they were all right about me?",
        "However I turned a profit, so I am content.",
        # TODO: 形容詞化分詞を外した方がいい場合は外す。
        # 分詞の形容詞化
        "You can change the game options in the game if I am not mistaken.",
    ],
    'negative': [
        "That is kind of the point.",
        "About how many miles are on it?",
        "Attempts at doing something are not automatically vindicated just because you failed.",
        "I really hope that Alim is doing most of the legwork.",
        "I had to turn the damn game off because I was getting a headache.",
        "The first paragraph was me disagreeing with you claiming I 'mollycoddled' him. ",
        "That was such bullshit.",
        "This was an old interview.",
        "This is so fucking typical.",
        "There are a billion youtube tutorials to show you where your eye is.",
        "If they were to legitimately honor duplicates, how could they prevent double dipping?",
        "Those were days I loved most.",
        "My worst fears were coming to fruition.",
        "Am I being an apologist by saying this?",
        "I am all for renewables but I feel we are being screwed over.",
        "I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces.",
        "I am in an LDR with someone 1200 miles from my home.",
        "My buddy was having problems with it after he installed the new operating system.",
        "It was complete bullshit, but you can't review it.",
    ],
}
test_data_0069 = { 

      # **Guideword:** PREDICATIVE, WITH LINKING VERBS
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of adjectives predicatively, after linking verbs 'look' and 'feel'.
        
  'positive': [
    'You look busy.',
    'This book looks interesting.',
    'You look wonderful in the jacket.',
    'I would feel disappointed if you said so.',
    'I feel calm when I stay with you.',
    'I feel nauseous when I stand in front of people.',
    'She felt jealous when she saw you guys walking together.',
    # 'Everything looked beautiful outside in the early morning.',
    # parser: looked->outside(dobj)
    'I feel great.',
    'She looks young for her age.',
    'I bought them because I feel comfortable when I am wearing these clothes.'
  ],
  'negative': [
    'We feel like eating Japanese food.',
    'My friends feel like going out today.',
    'I feel like I’ve been here before.',
    'She feels like she is going to have a fever.',
    'I feel that he is interested in her.',
    'Her face looks like a dog\'s.',
    'She is looking for a nice guy.',
    'I can look after you anytime.',
    'I look like I am going to swim.',
    'I feel that it’s going to rain tomorrow.',
    'I know I look like your father.',
    'You look like my friend.',
    'She feels like watching a movie tonight.',
    'I was looking for you for a long time.',
    'She looks like she\'s going home now.',
    'She is looking forward to meeting you.',
    'You feel like having a girlfriend is better than being alone.',
    'You feel like it’s been a long day.',
    'She looks just like my sister.',
    'I feel like I gained some weight.',
  ],
}
test_data_0070 = { 

      # **Guideword:** ADJECTIVES WITH PREFIX 'A-'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use adjectives with the prefix a- ('asleep', 'awake', 'alive', 'alone') predicatively only, after linking verbs. 
        
  'positive': [
    # parser cannot recognize "alone" as adjective
    #'I dislike being alone.',
    'I feel alive.',
    'He is alive and well.',
    'He is alive with enthusiasm.',
    # parser cannot recognize "alone" as adjective
    #'Leave me alone.',
    'You\'re probably asleep.',
    'I will continue to be awake.',
    'I heard that she is still alive.',
    'My companions were all asleep.',
    'You were awake until late last night.',
    'I was awake the whole time.',
  ],
  'negative': [
    'Please wake me up.',
    'You get lonely easily.',
    'You look lonely.',
    'I sometimes wake during the night.',
    'I found it difficult to sleep.',
    'I want to live life in my own way.',
    'I probably won\'t be lonely.',
    'I sometimes wake up at night.',
    'You wake up early.',
    'I want to live in Osaka.',
    'What time did you wake up today?',
    'He doesn\'t have a house to live in.',
    'An asleep bear is less dangerous than an awake one.', 
    'They live together but in different worlds.',
    'I am going to sleep.',
    'Where do you live?',
    'I haven\'t had enough sleep.',
    'I\'m having trouble because I\'m lonely.',
    'Let\'s sleep when we can.',
    'I cannot sleep soundly.',
  ],
}
test_data_0071 = { 

      # **Guideword:** ATTRIBUTIVE (WITH NOUNS)
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of adjectives attributively, before a noun. ► noun phrases
        
  'positive': [
    'They sell old books.',
    'Working at that company is an interesting experience.',
    'There is an excited audience.',
    'She bought a beautiful, pink shirt.',
    'This is a beautiful lake.',
    'He always wears a nice, clean shirt.',
    'He has a small bag.',
    'That was an exciting game.',
    'I bought a large, white plastic bag.',
    'Busy people tend to buy a cheap bento box for lunch',
  ],
  'negative': [
    'I want something cold to drink.',
    'It was rude of her to leave so suddenly.',
    'I’m so tired.',
    'She was rude to him for no reason.',
    'It is easy for me to read three books a day.',
    'I found something interesting.',
    'We saw someone strange at the station.',
    'She wants to go somewhere nice.',
    'I was happy that he was coming.',
    'I am interested in economics.',
    'The wall is about 16 inches think.',
    'This is the problem involved in the plan.',
    'My son is 10 months old.',
    'I am good at baseball.',
    'How do you train somebody new?',
    'This book is boring.',
    'I am bored with football.',
    'I am afraid to go home.',
    'He was bored with the lecture.',
    'I am 180 centimeters tall.',
  ],
}
test_data_0072 = { 

      # **Guideword:** WITH 'MAKE' AS OBJECT COMPLEMENT
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use adjectives as object complement after 'make'.
        
  'positive': [
    'Rumors about her rudeness made her angry.',
    #'That video made her popular among the rest of the students.',
    # parser mistakenly recognized popular as complement of "her" instead of make.
    #'That video made her popular among school.',
    'The new movie makes people emotional.',
    'Don’t make the problem worse than it is.',
    'The news made me happy.',
    'That textbook made him smart.',
    'This smell makes me hungry.',
    'The movie always makes me sad.',
    'The song made her famous.',
    'Your new shirt makes you cool.',
  ],
  'negative': [
    'We had him report.',
    'He doesn\'t let her drive.',
    'I felt my fear rise.',
    'We got the doctor to come.',
    'What made you think so?',
    'I\'ll let him do so.',
    'I had my hair cut.',
    'She helped her mother water the garden.',
    'I had the wall painted.',
    'I saw the girl crossing the street.',
    'I had a suit made.',
    'I broke my left leg while I was skiing.',
    'I made him understand what I meant.',
    'She made her sister clean the room.',
    'I had my brother paint the wall.',
    'I got her to stop smoking.',
    'I\'ll let you know when I get home.',
    'I got my shoes polished.',
    'I heard the bell ring.',
    'I got this letter translated into English.',
  ],
}
test_data_0073 = { 

      # **Guideword:** WITH PRONOUN
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use an adjective or adjective phrase after pronouns like 'something', 'nothing', 'somewhere', 'nowhere'.
        
  'positive': [
    'There is nothing more important than your health.',
    'In those years she and her kids hid somewhere safe and survived the war.',
    'There is nowhere safe.',
    'She knows something special about him.',
    'There\'s nothing wrong with him.',
    'It\'s nice to do something good for the community.',
    'There is nowhere special for my family.',
    'There is nothing better than a home cooked meal.',
    'I want something cold to drink.',
    'I want to go somewhere interesting.',
  ],
  'negative': [
    'She knows everything about him.',
    'It is nothing to me.',
    'She knows anything about him.',
    'Forget everything else about him.',
    'That kind of talk will get you nowhere.',
    'I want something to drink.',
    'He knows something.',
    'Is there somewhere with benches near here?',
    'Let\'s eat somewhere else for a change of pace.',
    'I am also going to go somewhere.',
    'I want somebody to fight with against them.',
    'Do you have anything to do this evening?',
    'I have something to tell you.',
    'Something is wrong.',
    'She needs somewhere to stay, right?',
    'They had nothing to eat then.',
    'I want to camp somewhere with cooler weather.',
    'The missing boat was nowhere to be found.',
    'Do you need anything to read?',
    # not sure whether this should be a positive testcase
    #'The concert hall was nowhere near full.',
  ],
}
test_data_0074 = { 

      # **Guideword:** DEGREE ADJECTIVES BEFORE NOUNS
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** 1.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use a limited range of degree adjectives ('real', 'absolute', 'complete') before a noun to express intensity.
        
  'positive': [
    'This is not a complete edition.',
    'This film is a complete failure.',
    'His real worth was unknown.',
    'He wields absolute power over the school.',
    'She\'s an absolute angel.',
    'I have absolute trust in you.',
    'The real winter has come.',
    'That dam project is a complete waste of money.',
    'He holds absolute power in the company.',
    'I just want real friends who I can trust.',
  ],
  'negative': [
    'That development will be completed soon.',
    'The today was absolutely horrible.',
    'Can you complete this form?',
    'I absolutely will not smoke tobacco.',
    'I absolutely will never be in love with you.',
    'They had absolutely no confidence.',
    'You should complete the procedures.',
    'I will complete all the unfinished work.',
    'I have absolutely no plans to go out.',
    'Is the number complete?',
    'I will absolutely contact you.',
    'I absolutely want to obtain that prize.',
    'Is that registration complete?',
    'That process is still not complete.',
    'It is absolutely impossible.',
    'How long did it take to complete?',
    'Data transmission is complete.',
    'That will be complete soon.',
    'I thought that it was absolutely right.',
    'You are absolutely right.',
  ],
}
test_data_0075 = { 

      # **Guideword:** ATTRIBUTIVE ONLY, TIME ADJECTIVES
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the adjectives 'present', 'future', 'former' before a noun.
        
  'positive': [
    'He is a future doctor.',
    'He treats his former wife civilly.',
    'The present headmaster is the twelfth generation leader in his family.',
    'All engineers are terrible nerds, the present company always excepted.',
    'She is a former professional wrestler.',
    'He has two children by his former wife.',
    'One will always return to one\'s former love.',
    'He is our former principal.',
    'What do you believe you\'ll do in your future life?',
    'We met with our former teacher.',
  ],
  'negative': [
    'His future is dark.',
    'I was present at my father\'s deathbed.',
    'Let\'s leave it like that for the present.',
    'This is a present for you.',
    'They have a promising future.',
    'Thank you for your present.',
    'I am anxious about the future.',
    'I must bring him some present.',
    'I will be more careful in future.',
    'Who can read the future?',
    'You have a long future ahead of you.',
    'I want to sell books in the future.',
    'I will present a case.',
    'I shall stay here for the present.',
    'There is no time like the present.',
    'I am worried about the future.',
    'The members are all present.',
    'I am pessimistic about the future.',
    'They present a united front.',
    'I had the honor of being present.',
  ],
}
test_data_0076 = { 

      # **Guideword:** PAST PARTICPLE AS ADJECTIVE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use the '–ed' form of a verb as an adjective, after a noun.
        
  'positive': [
    # 'The house built on the hill belonged to my grandmother.',
    # built -> house (nsubj)
    'The books left on the shelf are those that nobody wanted.',
    'The spectators marvelled at the paintings displayed.',
    'Each film shown in the festival has already won at least one award.',
    'The families enjoyed watching the floats paraded through the streets.',
    'It\'s becoming harder to meet the high standards required.',
    'The photographers assigned to the story met up to trade tips.',
    # 'The song heard through the door of the practice room was beautiful.',
    # heard -> song (nsubj)
    'Everbody wanted to comment on the improvements made.',
    'I\'ve tried to address the comments made at the meeting.',
  ],
  'negative': [
    'They loved hearing the news.',
    'The child has already played the piano since he was very young.',
    'The scientist researched the effect of the beam on the growth rate of the eggs.',
    'It depends on why they wanted to do it.',
    'She received a huge raise when she was promoted.',
    'The president passed a new law.',
    'They have shown a different movie every night for years.',
    'The boat glided silently across the bay.',
    'He didn\'t keep her secret.',
    'They kept talking to each other even after the breakup.',
    'People have deep concerns about the policy.',
    'There were many problems with the system.',
    'Members received a special discount.',
    'The team was focused on solving the issue.',
    'There were legitimate reasons to do such a thing.',
    'The publicist promoted the new novel.',
    'I have already heard this song.',
    'Geese used to fly over the house every summer.',
    'He was frustrated with the results.',
    'The chef has invented a new dish that he plans to serve to customers this weekend at his restaurant.',
  ],
}
test_data_0077 = { 

      # **Guideword:** DEGREE ADJECTIVES BEFORE NOUNS
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** position
      # **Lexical Range:** 2.0
      # **CEFR level:** C2
      # **CAN-DO:** Can use an increasing range of adjectives before a noun to express intensity.
        
  'positive': [
    'I want to become friends with such an outstanding young girl.',
    'Daniel’s family members are magnificent artists.',
    'Unemployment is a growing, severe problem.',
    'The sad disgraceful thing is that I need to leave town in two days.',
    'The only important thing is for you to go to college.',
    'There shall be torrential rains tomorrow in the south of the country.',
    'This is a subtle, eloquent poem.',
    'He bought me an flashy pink car.',
    'I listened to a magnificent, classic song of hers.',
    'There is a beautiful, blue flower in the vase.',
  ],
  'negative': [
    'The one thing I want is to be rich.',
    'I lent my notebook to Stephanie.',
    'Their bikes are parked near the grocery store.',
    'I need you to get me onions and carrots.',
    'Many are the books that influenced the way I think.',
    'In spite of the fact that our car is broken, I want to go to Las Vegas.',
    'We need some milk if we are to make pancakes.',
    'They read books while waiting for me at the dentist.',
    'I shall never eat at this restaurant again.',
    'The fact speaks for itself.',
    # should be able to be filtered out.
    #'Her calendar has cute puppies on it.',
    'You need to drink some water occasionally.',
    'They shall be friends for as long as they live.',
    'I lost my earphones at the lake.',
    'What they like to eat is smoked salmon.',
    'I dropped my glove while I was shoving the snow.',
    'Jessica shall be a senator very soon.',
    'I need some time to think about the proposal.',
    'The noise was coming from the classroom.',
    #should be true
    'The fact is that she has seven brothers.',
  ],
}
test_data_0078 = {
    # **Guideword:** 'MY BEST FRIEND'
    # **Guideword type:** FORM
    # **Super category:** ADJECTIVES
    # **Sub category:** superlatives
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use the irregular superlative adjective 'best' in the phrase 'my best friend'.
    'positive': [
        "She's my best friend.",
        "Shahin is my best friend.",
        "My best friend drove in to hang out.",
        "My best friend had her first child just before she ended her senior year of high school. ",
        "I started Portal 2 co-op with my best friend.",

        "I had this girl as my best friend.",
        "My best friend is Archana from school.",
        "My best friend is very lovely and is loved by everyone such as my parents and my teacher."
        "The name of my best friend is Jyoti.",
        "I have lots of friends from my childhood but Rushi is my best friend forever.",
    ],
    'negative': [
        "Then one day after a promotion I come home and she is sleeping with one of my friends.",
        "A close friend of mine was deeply attracted to his best friend.",
        "A close friend of mine was deeply attracted to her best friend.",
        "I started Portal 2 co-op with our best friend.",
        "She's my friend.",

        "Vichyssoise is my best food.",
        "She was not our best friend, but a very close one.",
        "I was just having this conversation with my best friends.",
        "His best friend abandoned him.",
        "I found out more about her from another customer of mine who is her best friend.",

        "I do my best to ignore it and push through.",
        "I tried my best to explain this method.",
        "A friend of mine goes to the school.",
        "Sorry to hear about your friend.",
        "I never played it on a tablet, but I played with my friend who played on tablet.",

        "I enjoy visiting with old and new friends.",
        "My friends are the type to do that.",
        "It was my best record.",
        "Some of my friends can whistle songs perfectly.",
        "My best advice is to just shop around.",
    ],
}

test_data_0079 = { 

      # **Guideword:** COMPLEX NOUN PHRASES
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can form a limited range of complex noun phrases with a superlative adjective  + prepositional phrase, to talk about something unique.► noun phrases ►  clauses: comparison
        
  'positive': [
    'She is the most beautiful woman in this town.',
    'That is the longest bridge in my country.',
    'He was the smallest human in the world.',
    'It is the saddest moment of my life.',
    'It was the best moment of my life.',
    'He was the heaviest man in my class.',
    'This is the newest phone in this area.',
    'They are the happiest people in the world.',
    'This is the highest building in Japan.',
    'I was the most popular student in high school.',
  ],
  'negative': [
    'I think it\'s more interesting than a report.',
    'Things aren\'t as bad as you think.',
    'That one has a shorter tail.',
    'Your story is as long as a book.',
    'These beans are more delicious than last year\'s beans.',
    'I wanted to tell you sooner.',
    'This book is as heavy as a rock.',
    'It is the best book ever.',
    'There\'s nothing better than a cold beer after exercise.',
    'I\'m happier than last time.',
    'Computers are getting cheaper and cheaper.',
    'It was easier than the practice test.',
    'Ernie doesn\'t sound as happy as usual.',
    'It\'s warmer this year than it was last year.',
    'I\'m going earlier than that.',
    'These books are the most interesting this library has to offer.',
    'The ball drops more slowly than a falling feather.',
    'She\'s better friends with him than I am.',
    'I became more and more nervous as the interview went on.',
    'Skiing is more difficult than surfing.',
    'The sights are much more impressive when you see them in real life.',
    'Japan\'s schools are tougher than the ones in Korea.',
  ],
}
test_data_0080 = { 

      # **Guideword:** WITH 'IN' + NOUN
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use prepositional phrases with 'in' + singular name of a place after a superlative adjective.
        
  'positive': [
    'She is the most beautiful woman in this town.',
    'It was the most expensive one in this shop.',
    'That is the longest bridge in my country.',
    'He was the smallest human in the world.',
    'This is the most famous school in my town.',
    'He was the heaviest man in my class.',
    'This is the newest phone in this area.',
    'They are the happiest people in the world.',
    'This is the highest building in Japan.',
    'I was the most popular student in high school.',
  ],
  'negative': [
    'Yuri comes to school the earliest ouf of all of us.',
    'I became more and more nervous as the interview went on.',
    'This problem is the most difficult of all.',
    'Human life is the most important of all.',
    'There\'s nothing better than a cold beer after exercise.',
    'Skiing is more difficult than surfing.',
    'It is the saddest moment of my life.',
    'Computers are getting cheaper and cheaper.',
    'That one has a shorter tail.',
    'It was the best moment of my life.',
    'Japan\'s schools are tougher than the ones in Korea.',
    'He can swim the fastest of all students.',
    'The sights are much more impressive when you see them in real life.',
    'This flower is the most beautiful of the five flowers.',
    'Your story is as long as a book.',
    'Summer is the hottest of the four seasons.',
    'He can run the fastest of all.',
    'These beans are more delicious than last year\'s beans.',
    'Ken is the tallest of the five.',
    'Ernie doesn\'t sound as happy as usual.',
  ],
}
test_data_0081 = { 

      # **Guideword:** WITH 'OF' + NOUN
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of prepositional phrases with 'of' after a superlative adjective, to refer to one thing within a set or part of a set.
        
  'positive': [
    'He is the tallest of the five.',
    'Yuri comes to school the third earliest of us.',
    'This problem is the most difficult of all.',
    'The human life is the most important of all.',
    'It is the saddest moment of my life.',
    'It was the best moment of my life.',
    'He can swim the third fastest of all students.',
    'This flower is the most beautiful of the five flowers.',
    'Summer is the hottest of the four seasons.',
    'He can run the fastest of all.',
  ],
  'negative': [
    'I can play the piano the best in my family.',
    'It was the most expensive one in this shop.',
    'She is the very best soccer player in town.',
    'They are the happiest people in the world.',
    'I was the most popular student in high school.',
    'This is the highest building in Japan.',
    'She is the most beautiful woman in this town.',
    'I think this is by far the best song she has ever made.',
    'My house is the largest in our neighborhood.',
    'He is beloved by all.',
    'This is the most famous school in my town.',
    'He was the heaviest man in my class.',
    'This restaurant is the second most popular in Tokyo.',
    'He was the smallest human in the world.',
    'This cake is the most delicious cake in the shop.',
    'This theory is well worth dedicating the rest of my life to.',
    'We had a meeting yesterday, just the two of us.',
    'I got up the earliest in my family.',
    'I can run the fastest in the soccer team.',
    'He was the most famous person in the town.',
    'That is the longest bridge in my country.',
    'This is the newest phone in this area.',
    'This is the best movie that I’ve ever seen.',
  ],
}
test_data_0082 = { 

      # **Guideword:** ELLIPSIS, WITH 'THE'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'the' with a limited range of superlative adjectives without a following noun, when the noun is understood.
        
  'positive': [
    'We have watched many baseball games and this game is the most memorable.',
    'There are many restaurants around here, but this one is the best.',
    'I love my friends, but my family is the best.',
    'I have seen many cute girls but you are the most beautiful.',
    'She has many watches and this one is the most expensive.',
    'This flower is the most beautiful.',
    'I bought a new pencil, but the previous one was the best.',
    'You have met lots of students, but he is the smartest.',
    'Summer is the hottest.',
    'I have been to many countries and Japan is the most beautiful.',
    'This problem is the most difficult of all.',
    'She is the most beautiful in her class.',
    'My house is the largest in our neighborhood.',
    'This restaurant is the second most popular in Tokyo.',
    'He is the youngest in his family.',
  ],
  'negative': [
    'Mt.Everest is the highest mountain in the world.',
    'She is the very best soccer player in town.',
    'They are the happiest people in the world.',
    'I was the most popular student in high school.',
    'This is the highest building in Japan.',
    'She is the most beautiful woman in this town.',
    'I think this is by far the best song she has ever made.',
    'I am the most handsome guy in this class.',
    'This is the most famous school in my town.',
    'He was the smallest human in the world.',
    'He was the most famous person in the town.',
    'That is the longest bridge in my country.',
    'He is the tallest man in this class.',
    'This is the newest phone in this area.',
    'The Nile is the longest river in the world.',
    'This is the best movie that I’ve ever seen.',
  ],
}
test_data_0083 = { 

      # **Guideword:** WITH '-EST'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form superlative adjectives with adjectives of one syllable with a short vowel, by doubling the final consonant and adding '–est'.
        
  'positive': [
    'This year is the hottest in ten years.',
    'She is the fattest person in her class.',
    'This moment was the gladdest moment for me.',
    'I used to be the fattest in my family before.',
    'The truth that I could see you is the gladdest thing in my life.',
    'She is the hottest woman in my class.',
    'August is the hottest month in Japan.',
    'This box is the biggest box in my house.',
    'This park is the biggest in this town.',
    'I am your biggest fan.',
  ],
  'negative': [
    'This is the newest phone in this area.',
    'This is the highest building in Japan.',
    'I think this is by far the best song she has ever made.',
    'My house is the largest in our neighborhood.',
    'This problem is the most difficult of all.',
    'This restaurant is the second most popular in Tokyo.',
    'This flower is the most beautiful.',
    'I love my friends, but my family is the best.',
    'She has the longest hair in my class.',
    'She is the most beautiful woman in this town.',
    'That is the longest bridge in my country.',
    'This is the best movie that I’ve ever seen.',
    'I have seen many cute girls but you are the most beautiful.',
    'This is the most famous school in my town.',
    'She is the very best soccer player in town.',
    'My friend\'s home is the highest in my province.',
    'He was the most famous person in the town.',
    'My friends are the most popular group in my school.',
    'I was the most popular student in high school.',
    'I bought a new pencil, but the previous one was the best.',
  ],
}
test_data_0084 = { 

      # **Guideword:** WITH '-EST'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form superlative adjectives by adding the suffix '-est', to adjectives of one syllable.
        
  'positive': [
    'He was the smallest human in the world.',
    'She is the fastest person in her class.',
    'This moment was the longest for me.',
    'She has the shortest hair in my class.',
    'He is the tallest of the five.',
    'He has the fewest monitors in the office.',
    'I could be the fastest runner in the soccer team if I wanted to.',
    'My friend\'s home is the highest in my province.',
    'This park is the biggest in this town.',
    'Summer is the hottest of the four seasons.',
  ],
  'negative': [
    'The human life is the most important of all.',
    'What you have done is the worst.',
    'This problem is the most difficult of all.',
    'I can play the piano the best in my family.',
    'I got up the earliest in my family.',
    'That baseball game last week was the most exciting.',
    'Yuri comes to school the third earliest of us.',
    'She is the most beautiful woman in this town.',
    'This is the best movie that I’ve ever seen.',
    'This flower is the most beautiful of the five flowers.',
    'This cake is the most delicious cake in the shop.',
    'This is the most famous school in my town.',
    'This movie is the most interesting one for me.',
    'It was the best moment of my life.',
    'He was the most famous person in the town.',
    'It was the most expensive one in this shop.',
    'This TV program is the most popular in this country.',
    'I know that this bag is the most expensive in this shop.',
    'They are the happiest people in the world.',
    'I was the most popular student in high school.',
  ],
}
test_data_0085 = { 

      # **Guideword:** WITH '-EST'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form superlative adjectives using the '-est' suffix, with adjectives of one syllable, and with two-syllable adjectives ending in -y.
        
  'positive': [
    'This process is the easiest of all.',
    'My mother was the prettiest near here before.',
    'She was always the third earliest student to arrive.',
    'He was the heaviest man in my class.',
    'This week is the busiest of this year.',
    'They are the happiest people in the world.',
    # 'She is the funniest man in the class.',
    # parser: funniest is noun
    'He has the loveliest personality in this class.',
    'What happened to you is the sorriest thing of this week.',
    'I got up the earliest in my family.',
    'This is the longest road in the western USA.',
    'The new Ferrari is the fastest luxury car in existence'
  ],
  'negative': [
    'The Nile is a long river in Egypt.',
    'That is one bridge in my part of the country.',
    'This is one of the taller buildings in Japan.',
    'You have met lots of students, but he is smarter than all of them.',
    'My house is one of the larger ones in our neighborhood.',
    'I was popular in high school.',
    'I have seen many cute girls but you are truly beautiful.',
    'This is a famous school in my town.',
    'She is a very good soccer player in town.',
    'Mt. Everest is an extremely tall mountain.',
    'I think this is by far the best song she has ever made.',
    'He was the most famous person in the town.',
    'We have watched many baseball games and this game is the most memorable.',
    'She has many watches and this one is the most expensive.',
    'There are many restaurants around here, but this one is the best.',
    'This is the best movie that I’ve ever seen.',
    'This restaurant is the second most popular in Tokyo.',
    'This is the worst phone you can buy.',
    'He is the eldest of all his siblings.',
    'I have been to many countries and Japan is the most beautiful.',
  ],
}
test_data_0086 = { 

      # **Guideword:** WITH 'MY' OR 'YOUR'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form a noun phrase with 'my' or 'your' + superlative adjective + noun, with a limited range of nouns and contexts. ► noun phrases
        
  'positive': [
    'I would like to buy your newest bag.',
    'Please show me your oldest glasses.',
    'She can bring her cutest cat.',
    'I will take my oldest sister to the party.',
    'He is my best friend.',
    # parser could not parse funniest correctly
    #'I can take my funniest friend tomorrow.',
    'Can you show me your most important thing?',
    'This is my newest car.',
    'I know you can bring your best friend to the party.',
    'You should come with your nicest shoes.',
    'She knows my most important secrets.',
  ],
  'negative': [
    'She is the smallest in this office.',
    'I can tell this is the cheapest stuff in this shop.',
    'My friend is the kindest person.',
    'This is the tallest building in the world.',
    'I was the best baseball player in the school.',
    'This school is the oldest near here.',
    'I can tell this is the worst timing.',
    'The best thing is that you came to the class.',
    'This is the happiest moment of my life.',
    'This is the most expensive one in the world.',
    'You walk the slowest.',
    'This flower is the most beautiful.',
    'He is the smartest guy in the class.',
    'She is the best person for this issue.',
    'This car can run fastest.',
    'This is the heaviest rain in this year.',
    'This laptop is the best.',
    'This park is the largest in this town.',
    'That car is the coolest car I have ever seen.',
    'I know this way is the safest.',
  ],
}
test_data_0087 = { 

      # **Guideword:** WITH '-ST'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form superlative adjectives using the suffix '-st' to adjectives ending in '–e'.
        
  'positive': [
    'You are the nicest person I have ever met.',
    'She is the cutest in the office.',
    'Your house is the finest in this area.',
    'This country is the freest in the world.',
    'This shopping mall is the largest in my country.',
    'This is the cutest thing I have ever seen.',
    'The nicest cafe near here would be here.',
    'This place is the safest right now.',
    'This football field is the largest in my town.',
    'I love to watch the latest movies.',
  ],
  'negative': [
    'This park is the biggest in this town.',
    'That baseball game last week was the most exciting.',
    'I can play the piano the best in my family.',
    'This flower is the most beautiful of the five flowers.',
    'She is the fattest person in her class.',
    'It was the most expensive one in this shop.',
    'I got up the earliest in my family.',
    'I was the most popular student in high school.',
    'This moment was the gladdest moment for me.',
    'This TV program is the most popular in this country.',
    'This movie is the most interesting one for me.',
    'This is the most famous school in my town.',
    'This cake is the most delicious cake in the shop.',
    'He was the most famous person in the town.',
    'This is the best movie that I’ve ever seen.',
    'What you have done is the worst.',
    'I know that this bag is the most expensive in this shop.',
    'Yuri comes to school the third earliest of us.',
    'Human life is the most important of all.',
    'This problem is the most difficult of all.',
  ],
}
test_data_0088 = { 

      # **Guideword:** WITH 'THE'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form a noun phrase with 'the' + superlative adjective + noun. ► noun phrases
        
  'positive': [
    'This is the biggest box in my house.',
    'That is the longest bridge in my country.',
    'She is the hottest woman in my class.',
    'This is the tallest building in Japan.',
    'She is the fattest person in her class.',
    'I was the most popular student in high school.',
    'She has the longest hair in my class.',
    'It was the loveliest flower in the garden.',
    'August is the hottest month in Japan.',
    'This is the biggest park in this town.',
  ],
  'negative': [
    'I am your biggest fan.',
    'This park is the biggest in this town.',
    'That baseball game last week was the most exciting.',
    'I can play the piano the best in my family.',
    'This flower is the most beautiful of the five flowers.',
    'My house is the largest in our neighborhood.',
    'I bought a new pencil, but the previous one was the best.',
    'I love my friends, but my family is the best.',
    'I love my school the most.',
    'I have seen many cute girls but you are the most beautiful.',
    'I got up the earliest in my family.',
    'This TV program is the most popular in this country.',
    'This flower is the most beautiful.',
    'I know that this bag is the most expensive in this shop.',
    'My friend\'s home is the highest in my province.',
    'What you have done is the worst.',
    'This restaurant is the second most popular in Tokyo.',
    'Yuri comes to school the third earliest of us.',
    'Human life is the most important of all.',
    'This problem is the most difficult of all.',
  ],
}
test_data_0089 = { 

      # **Guideword:** WITH 'THE MOST'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form superlative adjective phrases using 'the most', with longer adjectives of two or more syllables. 
        
  'positive': [
    'This flower is the most beautiful of the five flowers.',
    'It was the most expensive one in this shop.',
    'This TV program is the most popular in this country.',
    'I was the most popular student in high school.',
    'This movie is the most interesting one for me.',
    'This is the most famous school in my town.',
    'The baseball game aired yesterday was the most exciting ever.',
    'He was the most famous person in the town.',
    'I know my painting is the most beautiful in the world.',
    'This problem is the most difficult of all.',
  ],
  'negative': [
    'She is the cutest in the office.',
    'He was the heaviest man in my class.',
    'They are the happiest people in the world.',
    'I love to watch the latest movies.',
    'This week is the busiest in this year.',
    'You are the nicest person I have ever met.',
    'She comes to school the third earliest of us.',
    'This shopping mall is the largest in my country.',
    'I got up the earliest in my family.',
    'Your house is the finest in this area.',
    'At most, the medicine might be effective as a pain reliever.',
    'This is the cutest thing I have ever seen.',
    'Most of the papers are written in English.',
    'She is the funniest in the class.',
    'This process is the easiest of all.',
    'The nicest cafe near here would be that one.',
    'My mother was the prettiest near here before.',
    'What happened to you is the sorriest thing in this week.',
    'This place is the safest right now.',
    'This football field is the largest in my town.',
    'This country is the freest in the world.',
  ],
}
test_data_0090 = { 

      # **Guideword:** COMPLEX NOUN PHRASES
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can form an increasing range of complex noun phrases with a superlative adjective + prepositional phrase, to talk about something unique. ► noun phrases
        
  'positive': [
    'This is the oldest building in the town.',
    'Saito Yuki is the most popular player of the Nippon-Ham Fighters.',
    'Mt. Fuji is the largest mountain in Japan.',
    'This is the most expensive component in the equipment.',
    'This is the most useful dictionary of all of the options by far.',
    'Tokyo Sky Tree is the tallest tower in the world.',
    'She is the cleverest girl in our class.',
    'The best movie of 2011 is the Social Network.',
    'He is the most famous singer in the town.',
    'The Shinano is the longest river in Japan.',
  ],
  'negative': [
    'I am not in the least afraid to die of cancer.',
    'Out of all of us, I am the youngest.',
    'He studied the hardest of the three.',
    'The lake is deepest at this point.',
    'Tom can swim the fastest.',
    'In the shop, this car is the most expensive.',
    'She is most famous in Japan.',
    'She sings songs the best in the class.',
    'You must sleep at least seven hours a day.',
    'Among all the students, he is the brightest.',
    'John runs fastest of the four.',
    'Out of everyone, she is the tallest.',
    'This is a second-rate company at best.',
    'Which season do you like the best?',
    'I am the tallest, not you.',
    'In the school, he can run the fastest.',
    'This book is by far the most interesting.',
    'He is happiest when he is left alone.',
    'The strongest man cannot stop the laws of nature.',
    'This chocolate is the sweetest I have ever eaten!',
  ],
}
test_data_0091 = { 

      # **Guideword:** 'THE BEST' WITH NOUN AND PRESENT PERFECT
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'the best' before a noun + present perfect to talk about a unique experience.
        
  'positive': [
    'This is the best day I have ever spent in this town.',
    'It\'s probably the best place I\'ve surfed.',
    'That\'s the best news I have ever heard.',
    # 'That may have been the best day of fishing I\'ve ever had.',
    # fishing -> had (acl:relcl)
    'Ichiro is the best hitter Japan has ever produced.',
    'This is the best shopping mall I have ever visited.',
    'Japan is the best country I have ever been.',
    'It was the best decision I have ever made.',
    'This shirt is the best thing I have ever bought.',
    'This is the best ice cream I\'ve ever had.',
  ],
  'negative': [
    'Our boss brings out the best in people.',
    'This is the best place to see the fireworks.',
    'I think it\'s the best way.',
    'Wherever you live is the best place.',
    'This restaurant is considered the best in the city.',
    'I think the best place is in the corner, by the front window.',
    'The best way is to save quarters.',
    'We\'re known for that and it\'s the best tour to do here in the city.',
    'I would like to pick your brain on how best to make this presentation.',
    'I was just wishing the best for Chris.',
    'He has been my best friend ever since.',
    'Then what\'s your assessment for the best course of action?',
    'What\'s the best way to cook this?',
    'It\'s the best skiing you can get.',
    'Grandma is the best person to help you.',
    'Today is the best day to visit a shrine.',
    'What\'s the best way to get there?',
    'Hope it\'s the best one yet!',
    'What\'s the best way to improve one\'s spoken English?',
    'Some say yoga is the best way to release stress.',
  ],
}
test_data_0092 = { 

      # **Guideword:** 'ONE OF THE'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'one of the' before a superlative adjective, followed by a plural noun. ► noun phrases
        
  'positive': [
    'She is one of the brightest students.',
    'Emerald is one of the most valuable gems.',
    'Mt. Yari is one of the highest mountains in Japan.',
    'That is one of the longest rivers in the world.',
    'Recycling is one of the best ways to reduce environmental pollution.',
    'Luxembourg is one of the smallest countries in Europe.',
    'He is one of the richest men in the world.',
    'This picture is one of the most famous pictures in Japan.',
    'Picasso is one of the greatest painters in the world.',
    'Flying is one of the safest forms of travel.',
  ],
  'negative': [
    'America has the second most people in the world.',
    'He is by far the wisest in my class.',
    'He runs the fastest of the students.',
    'This is the most tasty white wine in this region.',
    'Tokyo is the biggest city in Japan.',
    'Most of the most valuable land in the area is owned by Mr. Lancaster',
    'He is happiest when he is driving his car.',
    'Osaka is the second largest city in Japan.',
    'This is the second highest building in this city.',
    'He is the least trustworthy man I\'ve ever known.',
    'He is the tallest boy of all the boys in the class.',
    'She is the youngest member in this circle.',
    'Working and parenting are two of the most valued areas of our lives.',
    'Osaka is the second smallest prefecture in Japan.',
    'Mt. Everest is the highest mountain.',
    'Iron is the most useful metal of all metals.',
    'He runs fastest in the class.',
    'This is the tastiest wine of all the wines I\'ve ever tried.',
    'She is the third tallest student in the class.',
    'She studied hardest in her class.',
  ],
}
test_data_0093 = { 

      # **Guideword:** 'THE BEST' WITH NOUN AND  'TO-' INFINITIVE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'the best' before a noun + 'to'-infinitive.  ► clauses: comparative
        
  'positive': [
    'Today is the best day to visit a shrine.',
    'This is the best place to see the fireworks.',
    'Making foreigner friends is the best way to study English.',
    'Some say yoga is the best way to release stress.',
    'We\'re known for that and it\'s the best tour to do here in the city.',
    'Now is the best time to see cherry blossoms.',
    'Grandma is the best person to help you.',
    'The best thing to do now is to run away.',
    'Japan is the best country to live in.',
    'The best seasons to eat whale meat is spring.',
  ],
  'negative': [
    'That may have been the best day of fishing I\'ve ever had.',
    'The father is the best judge of the child.',
    'This shirt the best thing I have ever bought.',
    'This is the best shopping mall I have ever visited.',
    'That company is one of the best in the business.',
    'It was the best decision I have ever made.',
    'That\'s the best news I have ever heard.',
    'You\'re the best man for the job.',
    'Japan is the best country under the sun.',
    'Spring is the season I like the best.',
    'This is the best day I have ever spent.',
    'The weather today was the best so far.',
    'This is the best ice cream I\'ve ever had.',
    'Ichiro is the best hitter Japan has ever produced.',
    'Japan is the best country I have ever been.',
    'It\'s probably the best place I\'ve surfed.',
    'She is the best scholar among the teachers.',
    'The best is often the enemy of the good.',
    'The prize went to the best performer.',
    'I did the job to the best of my ability.',
  ],
}
test_data_0094 = { 

      # **Guideword:** WITH DETERMINERS
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can form noun phrases with a range of determiners before a superlative adjective. ► noun phrases
        
  'positive': [
    'You can show us your finest video that you\'ve prepared for us.',
    'My friends talked about their happiest moment of life.',
    'Emi is my best friend.',
    'She came with her tallest sister.',
    'She is my richest friend.',
    'That is my most expensive bag.',
    'This is her lowest point in her life.',
    'You should wear your best clothes for the party.',
    'These are your coolest works.',
    'You are my cutest and most beautiful friend.',
  ],
  'negative': [
    'Wherever you live is the best place.',
    'This restaurant is considered the best in the city.',
    'I think the best place is in the corner, by the front window.',
    'Grandma is the best person to help you.',
    'Recycling is one of the best ways to reduce environmental pollution.',
    'What\'s the best way to improve one\'s spoken English?',
    'He is the least trustworthy man I\'ve ever known.',
    'Emerald is one of the most valuable gems.',
    'The best way is to save quarters.',
    'Osaka is the second largest city in Japan.',
    'Some say yoga is the best way to release stress.',
    'This is the most tasty wine of all wines I\'ve ever tried.',
    'She is the youngest member in this circle.',
    'This is the second highest building in this city.',
    'That is one of the longest rivers in the world.',
    'We\'re known for that and it\'s the best tour to do here in the city.',
    'He has been the earliest to arrive every day.',
    'This is the tastiest white wine in this region.',
    'What\'s the best way to get there?',
    'He is one of the richest men in the world.',
  ],
}
test_data_0095 = { 

      # **Guideword:** WITH 'BY FAR'
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the premodifer 'by far' to make a superlative adjective stronger.
        
  'positive': [
    'The last of these reasons is by far the most important.',
    'She is by far the best singer in her class.',
    'She is by far the best player in that country.',
    'This place is by far the most famous in our city.',
    'He was by far the best student in the class.',
    'She is by far the most popular singer among young people.',
    'He is by far the greatest of all scholars.',
    'She was by far the smartest student.',
    'This is by far the best way.',
    'This dictionary is by far the best.',
  ],
  'negative': [
    'She is the tallest in the class.',
    'Mike is the tallest in our class.',
    'I am the youngest of the five.',
    'I can play the piano the best in my family.',
    'He studied the hardest of the three.',
    'Ken’s house is the largest in our neighborhood.',
    'She is one of the most beautiful women in the world.',
    'I can run the fastest in the soccer team.',
    'Which do you like the best of these cars?',
    'She sings songs the best in the class.',
    'This is the best movie that I’ve ever seen.',
    'I got up the earliest in my family.',
    'Which season do you like the best?',
    'Oliver is the very best soccer player in town.',
    'This cake is the most delicious cake in the shop.',
    'Who is the tallest in the class?',
    'This is the longest rope of the three.',
    'He is the most famous in the town.',
    'This restaurant is the second most popular in Tokyo.',
    'Which is the most expensive of the three cars?',
  ],
}
test_data_0096 = { 

      # **Guideword:** ELLIPSIS, WITH 'THE'
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use '(one of) the' with an increasing range of superlative adjectives without a following noun, when the noun is understood.
        
  'positive': [
    'Russia\'s territory is the largest.',
    'Her cat is the cutest.',
    'Summer is the hottest.',
    'That mountain is the tallest.',
    'Sushi in Tokyo is the best.',
    'You are the best.',
    'He is the coolest.',
    'I got a new phone which is the most expensive.',
    'Drinking beer with good friends at night is the best.',
    'You are the most gifted.',
  ],
  'negative': [
    'My house is the largest one in our neighborhood.',
    'The cheapest ones are have the poorest quality.',
    # the fartest appears without noun so it should be true case
    #'Your dog ran the fastest of any dog in the race.',
    'We all threw our rocks at the same time.',
    'Luxembourg is one of the smallest countries in Europe.',
    'Flying is one of the safest forms of travel.',
    'She is the tallest person in the family.',
    'The best career is the one that makes you happy.',
    'Today is the worst day I\'ve had in a long time.',
    'She’s one of the richest women in America.',
    'Recycling is one of the best ways to reduce environmental pollution.',
    'She is one of the brightest students.',
    'Working and parenting are two of the most valued areas of our lives.',
    'The Amazon is one of the longest rivers on earth.',
    'This is the least expensive sweater in the store.',
    'You play tennis better than I do.',
    'I ran pretty far yesterday, but I ran even farther today.',
    'This sweater is less expensive than that one.',
    'This is the smallest box I\'ve ever seen.',
    'Emerald is one of the most valuable gems.',
  ],
}
test_data_0097 = { 

      # **Guideword:** WITH NOUN AND 'TO-' INFINITIVE
      # **Guideword type:** FORM
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use superlative adjectives before a noun + 'to'-infinitive. ► clauses: comparative
        
  'positive': [
    'I heard that that movie is the best one to help you calm down.',
    'The most amazing way to help others is by volunteering in your local community.',
    'She knows that the fastest way to go home is just to take a taxi.',
    'The most interesting thing to talk about with him is his experience as an ambassador.',
    'The best way to study is to go wherever you can focus.',
    'I know the fastest way to get there.',
    'The best thing to do after dinner is to take a walk.',
    'I can tell you that the best way to relax is to read a book.',
    'Drinking alcohol is the best way to sleep well.',
    'The best way to spend my free time is to listen to music.',
  ],
  'negative': [
    'This sweater is less expensive than that one.',
    'The most amazing thing is to see the sunrise from a mountain top.',
    'She is one of the brightest students.',
    'Sushi in Tokyo is the best.',
    'She bought the cheapest wallet in the shop.',
    'I ran pretty far yesterday, but I ran even farther today.',
    'Luxembourg is one of the smallest countries in Europe.',
    'The best solution is to just wait for it to end.',
    'Her cat is the cutest.',
    'My house is the largest one in our neighborhood.',
    'She likes to play baseball the most.',
    'Flying is one of the safest forms of travel.',
    'You are the best.',
    'This movie is the best for crying.',
    'I want the best wine in this bar.',
    'Russia is the largest.',
    'This is the smallest box I\'ve ever seen.',
    'This is the least expensive sweater in the store.',
    'Your dog ran the fastest of any dog in the race.',
    'She is the tallest in the family.',
  ],
}
test_data_0098 = { 

      # **Guideword:** WITH NOUN AND POSTMODFIER
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use a postmodifier to make the superlative stronger in the structure superlative + postmodifier + noun. 
        
  'positive': [
    'This is probably the most efficient possible measure to keep similar accidents from happening,',
    'Please sell the house at the highest possible price.',
    'I want to give the best possible guidance to each student.',
    'This is the smallest possible quantity.',
    'This is the most beautiful possible view from the mountain according to my father.',
    'High-resolution STEM requires the smallest possible probe with the highest possible current.',
    'Make the most effective possible use of men and material.',
    'The radial electric field profile shall be such that its axis has the highest possible extent of verticality.',
    'This makes it possible to perform a refresh mode in the shortest possible time',
    'Use the greatest possible care.',
  ],
  'negative': [
    'He is a possible vice president.',
    'It\'s best to be together as much as possible.',
    'leave as fast as possible.',
    'They fled in all possible directions.',
    'He tried every possible method.',
    'I want to move my body as possible as I can.',
    'I\'ll do my best to deal with that as soon as possible.',
    'Is it possible that I can have mistaken my man?',
    'That would be best as quickly as possible.',
    'I will do so, if possible.',
    'I\'ll do my best to get that response as soon as possible.',
    'That may not be possible.',
    'I began to see that here was one of the best of all possible shipmates.',
    'I\'ll come here as soon as possible.',
    'I shall use the shortest form possible.',
    'I will do my best so that I can help you as much as possible.',
    'I request you will answer as soon as possible.',
    'As a tourist resort, this city has the best of all possible worlds.',
    'We will try our very best as much as possible.',
    'I tried all possible means.',
  ],
}
test_data_0099 = { 

      # **Guideword:** WITH POSTMODFIER AND NOUN
      # **Guideword type:** FORM/USE
      # **Super category:** ADJECTIVES
      # **Sub category:** superlatives
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use a postmodifier to make the superlative stronger, in the structure superlative + noun + postmodifier ('possible', 'ever', 'by far'). 
        
  'positive': [
    'You are the kindest teacher ever.',
    'Japan finished in seventh place, its strongest ranking ever.',
    'That is the third highest total ever.',
    'This is the tastiest escargot dish ever.',
    'That was the most opportune chance ever.',
    'That\'s my highest score ever.',
    # 'This is the most expensive bid ever in the posting system.',
    # system -> ever (advmod)
    'I shall use the shortest form possible.',
    'This is like the worst and best excuse ever.',
    'This is about 2.9 percent of Tokyo\'s population, the largest percentage ever.',
    'The new one being built in China is the longest dam by far.',
    'Her newest concert was her most impressive performance by far.',
  ],
  'negative': [
    'He is by far the best of all scholars.',
    'That would be best to do as quickly as possible.',
    'I request you will answer as soon as possible.',
    'This is by far the best seafood restaurant in this area.',
    'Please sell the house at the best possible price.',
    'I want to give the best possible guidance to each student.',
    'He tried every possible method.',
    'I will do so, if possible.',
    'He suggests the best possible driver class name for the driver.',
    'It\'s best to be together as much as possible.',
    'Leave as fast as possible.',
    'Is it possible that I can have mistaken my man?',
    'You are by far the best swimmer of us all.',
    'It was by far the best summer vacation I\'ve ever had.',
    'Use the greatest possible care.',
    'That may not be possible.',
    'This is the smallest possible quantity.',
    'I\'ll do my best to deal with that as soon as possible.',
    'She is by far the best player in that country.',
    'Make the best possible use of men and material.',
  ],
}
