test_data_0700 = {

    # **Guideword:** COMPOUND NOUNS
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** types
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use a range of compound nouns, as one-word, two-word and hyphenated compounds,
    #  formed from verb + noun, noun + noun and adjective + noun combinations.

    'positive': [
        # Can't get oneword compounds without a dictionary
        # 'My bedroom is on the second floor of my house.',
        'I would like to have an ice-cream.',
        # 'My father has never been to the waterfall near my town.',
        'I guess you went to the hair salon yesterday.',
        'My mother wants to buy a new washing machine.',
        'My sister can drive for us because she just got a driving license.',
        'I wanted to be a baseball player when I was young.',
        'My girlfriend is writing about the working conditions of low income students.',
        'You have to go the ticket office first if you want to watch tonight\'s big match.',
        'This woman asked you where the train station is.',
        'I like to go to the swimming pool on the weekend.',
    ],
    'negative': [
        'My house is much bigger than yours.',
        'Your brother doesn\'t go to school because he feels sick.',
        'Those phones are much cheaper than yours.',
        'We went to watch the game which my friends were playing.',
        'My car is beside my house if you want to drive it.',
        'I like to have food at my house.',
        'My father has never been to that restaurant before.',
        'I am about to learn that language at school.',
        'Russians are all nice and love to drink.',
        'Chinese goods are cheap, but they are easily broken.',
        'That beautiful lady has a friend.',
        'My father is one of the most famous singers in Japan.',
        'I prefer a healthy woman.',
        'My website is open today.',
        'There are many important things in your life.',
        'These subjects are quite difficult to understand.',
        'The world is paying attention to you.',
        'I have made lots of mistakes before.',
        'That crazy woman who is dancing there is my friend.',
        'The question was way too hard for me.',
    ],
}

test_data_0701 = { 

      # **Guideword:** '-ING' FORMS, OBJECT
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** types
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use the '-ing' forms of verbs as nouns, in object position, to refer to activities. 
        
  'positive': [
    'I tried skating and found it rather hard.',
    'I enjoy reading this book.',
    'Molly hates sitting still and doing nothing.',
    'He is interested in learning English.',
    'I prefer watching games to playing them.',
    'I like dancing in front of a crowd.',
    'I practised windsurfing and scuba diving.',
    'Mary is fond of going to concerts.',
    'Have you finished watching the movie?',
    'She became a lawyer after going to graduate school.',
    'Carry is good at playing the violin unlike many of her friends.',
    'He could not be discouraged from pursuing his path by anybody.',
    # 'We call that asking for trouble.',
    # that->asking(acl)
    # 'On Arriving home, I discovered they had gone.',
    # home->arriving(compound)
  ],
  'negative': [
    'I went scuba diving with my friends during the last spring break.',
    'The most important thing is to get some sleep.',
    'He will be reading Spanish books this time tomorrow.',
    'Attending the banquet together is a very clever idea.',
    'A lot of cats had gone missing.',
    'Jeff and I sailed together.',
    'My mother used to go skiing with my father when they were young.',
    'Having a surprise birthday party is a great idea.',
    'Watching television for 5 hours is a very boring way to spend your day.',
    'She likes to go swimming with her cousins.',
    'I decorated the living room last year.',
    'She did not know anything about it.',
    'I climbed the mountain with my sister when I was six.',
    'Our computers were being attacked by hackers.',
    'Spencer’s brand new bag was stolen this morning.',
    'We might as well go skating since there’s an ice rink just across the street.',
    'I went hiking to reduce my stress.',
    'I ran as fast as I could since it was raining.',
    'My mom went shopping for Christmas gifts.',
    'Mark is very self-conscious and sometimes that can be annoying.',
    'I usually go bowling with my friends on Friday nights.',
    'It will be snowing when you get to Tokyo.',
    'My sister is selling all her stuffed toys.',
    'Camping with my family is so entertaining.',
    'I go surfing before school starts.',
    'Louis has been doing volunteer work ever since he graduated from high school.',
    'He could not be discouraged from the pursuit of his dreams by anybody.',
  ],
}
test_data_0702 = { 

      # **Guideword:** COMMON NOUNS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** types
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of common nouns. 
        
  'positive': [
    # only pronouns here
    #'I could call her now, if you like.',
    'You could ask your teacher for his advice.',
    'We could meet up at the fair at six tomorrow.',
    'We could visit your parents before it\'s too late.',
    'My sister and her friend plan to ride their bikes to the movies.',
    # English is wrongly parsed as NNP
    #'I wish I could speak English.',
    'I wonder if you could deal with this problem on your own.',
    'When you go to Paris next month, you could stay with Julia.',
    'I could have done the assignment.',
    # Chines, Italian, French are wrongly parsed as JJ
    #'We could go for Chinese, Italian, or French.',
  ],
  'negative': [
    'Let’s go to San Francisco.',
    'I used to live in Tokyo.',
    'Do you think they will win?',
    'Agatha Christie was prolific.',
    'She is working at Google.',
    'I’d like you to meet him.',
    'They have been annoying him.',
    'He never goes anywhere without Sarah.',
    'Those are very important.',
    'I need to visit it. Can we go there?',
    'She moved there to study.',
    'She was Mrs. Gilbert.',
    'Evian is "naive" backwards.',
    'Cleopatra is the cutest ever.',
    'Mr. Bell seems to understand what they need.',
    'We’ll be vacationing there soon.',
    'I’m craving Oreos.',
    'I’m flying  there later.',
    # tonight is wrongly parsed as NN.
    #'I can see it tonight.',
    'Thomas Jefferson was important.',
  ],
}
test_data_0703 = { 

      # **Guideword:** '-ING' FORMS, SUBJECT
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** types
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the '-ing' form of verbs as nouns in subject position.  
        
  'positive': [
    'Having a car opens the doro to a wide range of activities.',
    'Sleeping too much is bad for your health.',
    'Watching too much TV is not good for your eyes.',
    'Reading a magazine is my daily hobby.',
    # 'Seeing is believing.',
    # believing -> is (aux)
    'Having wealth does not always mean being happy.',
    # 'Succeeding in school is a matter of studying a couple of hours a day.',
    # Succeeding -> is (aux)
    'Walking is great for your health.',
    'Speaking only one language can be compared to living in a room with no windows.',
    'Walking in the park is a good way to relax.',
  ],
  'negative': [
    'I’m good at creating websites.',
    'There is no denying this fact.',
    'We enjoyed traveling all over the world.',
    'Asked some questions, she was not able to answer.',
    'I remember seeing him once.',
    'Considering his ability, the result is unsatisfactory.',
    'Walking in the park, he came across his old friend.',
    'I am sure of her winning.',
    'That is a surprising discovery.',
    'My mother is accustomed to getting up early.',
    'He have trouble waking up in the morning.',
    'I’m looking forward to seeing you.',
    'The man standing over there is my father.',
    'The cookies made our team happy.',
    'We cannot understand his criticizing her.',
    'I like walking in the rain.',
    'We spend a long time playing cards.',
    'I remember seeing her 5 years ago.',
    'It is no use worrying about it.',
    'She denied having met him there.',
  ],
}
test_data_0704 = { 

      # **Guideword:** '-ING' FORMS, ABSTRACT NOUNS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** types
      # **Lexical Range:** 2.0
      # **CEFR level:** C1
      # **CAN-DO:** Can use the '-ing' form of verbs as abstract nouns. 
        
  'positive': [
    'Recording consumes a lot of time.',
    'Running is not good if you are tired.',
    'Shopping used to be my only hobby.',
    'Promoting seems like a tiring job.',
    'Suffering is unnecessary in this situation.',
    'Planning is the best part in everything.',
    'Funding is something you should do if you are rich.',
    'Observing kids can be boring sometimes.',
    'Teaching is fun and also satisfying.',
    'I think that playing is a waste of time if you are an adult.',
    'They have many options for funding.',
    'He has a talent for observing.',
  ],
  'negative': [
    'Ethel is taking a religion course this semester.',
    'Tim is drinking wine on the couch.',
    'I like to sing with little children.',
    'I need to find information about Pulitzer Prize winners.',
    'I was feeling so stressed that I ate an entire box of cookies.',
    'He is eating lunch with his grandpa.',
    'He gave me a great deal of advice before my interview.',
    'She is whispering because they are in a movie theater.',
    'Please take good care of your equipment.',
    'Her job is to train the dogs.',
    'There has been a lot of research into the causes of this disease.',
    'My dad is closing his store this summer.',
    'My son is reading a book about anthropology.',
    'You seem to have a high level of intelligence.',
    'I realized that he has little knowledge.',
    'I love to talk to my professors after class.',
    'She was crossing the street when I saw her.',
    'Her family is visiting her this weekend.',
    'There’s a big brown dog running around the neighborhood.',
    'The coach is practicing alone tonight.',
    'Everything is alright.'
  ],
}
test_data_0705 = {

    # **Guideword:** PLURAL '-S'
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** plural
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can form plurals by adding '-s' to common countable nouns.

    'positive': [
        'I have never been to any Korean restaurants before.',
        'This apartment has several rooms inside.',
        'I don\'t know how many baseball games there are in this season.',
        'My friends have traveled around five countries before.',
        'It takes about 10 minutes from here to school.',
        'I gifted some flowers to my girlfriend.',
        'My sister loves to buy new skirts every season.',
        # clothesが常に複数形で使う名詞だからか、lemmaもclothesになっていました。 -Kevin Note: Clothes はいわゆる集合名詞だ。単数形がない。
        # ちなみにcloth（布）の複数形はclothsで、綴りがちょっと違うらしいです。　Kevin Note: Clothsじゃ複数の布の種類のことを意味する。
        'Foreign cars are much more expensive than Japanese ones.',
        'My friend wants to borrow all your cameras for shooting next week.',
        'I used to wear these shoes when I was young.',
        'My teacher didn\'t like the students\' behavior, so she left.',
        'I ate lots of different meats that night.',
        'My father always gives me lots of things to think about.',
    ],
    'negative': [
        'I need one more desk in my office.',
        'A snake is the animal which I hate most.',
        'There is a problem which I can\'t deal with.',
        'I would like to borrow a pencil.',
        'She has a lovely necklace on her neck.',
        'I don\'t have any knowledge about math.',
        'I got a new one this morning.',
        'The weather today is pretty bad.',
        'There is beautiful furniture in your house.',
        'I heard that my younger sister got a lot of money from her boyfriend.',
        'We got plenty of fish from fishing last week.',
        'I saw many sheep in that zoo.',
        'There is only one way to get out from here.',
        'People need to go outside once in a while for exercise.',
        'I\'m not sure leaving your dream job makes sense after a year even if it is for a promotion.',
        'I got a headache after swimming in the river.',
        'Take a step back, and you will know what is happening right now.',
    ],
}

test_data_0706 = { 

      # **Guideword:** PLURAL '-ES'
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** plural
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form plurals by adding '-es' to countable nouns ending in '-o', '-ch', '-s', '-sh', '-x' or '-z'.
        
  'positive': [
    'Heather researched Japanese volcanoes.',
    'There were a lot of boxes under the Christmas tree.',
    'I helped my mom peel the potatoes.',
    'My husband washed the dishes for me.',
    'There are many buses in the morning.',
    'I made turkey sandwiches for lunch.',
    'Be careful of the foxes that come out at night.',
    'Our son had two soccer matches today.',
    # 'I gave all my makeup brushes to my cousin.',
    # brush is determined to be a verb
    'Madeline loves quizzes.',
  ],
  'negative': [
    'Her hobbies are shopping and scuba diving.',
    'My grandmother told me a lot of stories.',
    'This college is famous for its libraries.',
    'Twenty countries are attending the conference.',
    'The babies started crying.',
    'The dog showed me some of his tricks.',
    'I do like playing with animals.',
    'I am discussing the contract with my colleagues.',
    'My mom scolded me because I lost my keys.',
    'I like these photos.',
    'All the parties that Grace has held in the past were successful.',
    'Grandma lives with four cats.',
    'These boys are graduating from middle school next year.',
    'My father’s boats are missing.',
    'I don’t like the idea of living in big cities.',
    'The girls sitting over there are my enemies.',
    'I’m bringing a few skirts to college.',
    'The ladies excused themselves to go to the bathroom.',
    'Her essays are well written.',
    'There are many zoos in Tokyo.',
    'The thief stole my favorite vase.',
    'She put some berries in her yogurt.',
  ],
}
test_data_0707 = { 

      # **Guideword:** PLURAL '-IES'
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** plural
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form plurals of countable nouns ending in a consonant plus '-y', by changing the 'y' to 'I' and adding '-es'.
        
  'positive': [
    'All the parties that Grace has held in the past were successful.',
    'Twenty countries are attending the conference.',
    'Her hobbies are shopping and scuba diving.',
    'My grandmother told me a lot of stories.',
    'The babies started crying.',
    'This college is famous for its libraries.',
    'Ladies and gentlemen, welcome to the annual ball!',
    'The girls sitting over there are my enemies.',
    'She put some berries in her yogurt.',
    'I don’t like big cities.',
  ],
  'negative': [
    'The Kennedys are a famous family in the U.S.',
    'My happy days are now over.',
    'Sonia visits a lot of zoos.',
    'She eats three apples a day.',
    'She hid the knives in the kitchen drawer.',
    'I met Alice three days ago.',
    'I saw a deer in the woods.',
    'My brother will come afterward.',
    'The news is very depressing.',
    'My mom scolded me because I lost my keys.',
    'My daughter wants a pony for her birthday.',
    'Music unites people of different backgrounds.',
    'These boys are graduating from middle school next year.',
    'Those houses all look alike.',
    'If you spend money, you will have less.',
    'There are many ways to convince your parents.',
    'I’m bringing a few skirts to college.',
    'Her essays are well written.',
    'There were a lot of boxes under the Christmas tree.',
    'Amanda plays with Candice all the time.',
    'My husband washed the dishes for me.',
    'I was contemplating on whether to go fishing or not.',
  ],
}
test_data_0708 = { 

      # **Guideword:** IRREGULAR PLURAL NOUNS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** plural
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form some irregular plural nouns.
        
  'positive': [
    # feet
    'My feet got injured so bad.',
    # antennae
    'This insect has two antennae.',
    # Lebanese (単複同型)
    'I don\'t know any Lebanese people.',
    # fish (単複同型)
    'My friends love ate two fish each.',
    # dozen (単複同型)
    'I bought almost two dozen of these glasses.',
    # teeth
    'I have to go to fix my teeth.',
    # mice
    'When I saw many mice running in front of me, I almost passed out.',
    # children
    'I love to play with children.',
    # men
    'There are a lot of men who would help you.',
    # shrimp(単複同型)
    'We got 4 shrimp each yesterday.',
    # phenomena
    'We call these phenomena break-downs.',
  ],
  'negative': [
    'My friends love to eat a raw fish.',
    'My friends love to eat one raw fish.',
    'Everybody is invited to the party.',
    'He has ten watches.',
    'I have two books.',
    'Bananas are yellow.',
    'How many friends do you have?',
    'She has three dogs.',
    'The bus comes every 10 minutes.',
    'My mother makes pancakes.',
    'We must finish these studies.',
    'I own a house.',
    'My son likes playing baseball.',
    'I bought some books at the store.',
    'I would like two books, please.',
    'She bought four knives for cooking.',
    'Each student is reminded to bring his protractor.',
    'Every student passed the test.',
    'Leaves are falling off the trees early this season.',
    'All of the books I have were written by Haruki Murakami.',
    'One man can have several wives in some countries.',
    'The storm was one of the heaviest snows this winter.',
    'Every dish on this menu is delicious.',
    'All of the rooms are full today.',
    'I bought a car yesterday.',
  ],
}
test_data_0709 = { 

      # **Guideword:** NOUNS ONLY USED IN THE PLURAL
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** plural
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use nouns that only have a plural form, with plural agreement. 
        
  'positive': [
    'I brought two pairs of scissors.',
    'I started to wear a pair of glasses since last year.',
    'He wore trousers to work every day.',
    'I don\'t have any means to get there.',
    'My sunglasses are lying on the countertop.',
    'I found the scissors under the desk.',
    'Japanese people use slippers indoors.',
    'Kids hang their Christmas stockings every year.',
    'Your closet is full of clothes.',
    'My gums ache.',
    'How many pairs of jeans do you need to buy?',
    'Please wear some shorts and a shirt.',
    'I washed two pairs of chino pants.',
    'The jeans were expensive, but the other things were very cheap.',
    'I bought them because I feel comfortable when I am wearing these clothes.',
    'These are my favorite pairs of sneakers.',
  ],
  'negative': [
    'Many fish are swimming in the pond.',
    'People are changing their roles.',
    'Every dish on this menu is delicious.',
    'I bought some books at the store.',
    'We must finish these studies.',
    'I own a house.',
    'I would like two books, please.',
    'He has ten watches.',
    'How many friends do you have?',
    'I have two books.',
    'My mother makes pancakes.',
    'Everybody is invited to the party.',
    'She has many kimonos at home.',
    'She bought four knives for cooking.',
    'Each student is reminded to bring his protractor.',
    'Our staff is working hard.',
    'Every student passed the test.',
    'One man can have several wives in some countries.',
    'She has three dogs.',
    'The police are after the thief.',
    # with single agreement
    'The ironworks is on sale.',
    'I played checkers yesterday.',
    'This is a  textbook of physics.',
    'It’s a species of mammals.',
  ],
}
test_data_0710 = { 

      # **Guideword:** COLLECTIVE NOUNS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** plural
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use collective nouns, usually with a singular verb, but also with a plural verb depending on whether the noun is perceived as a single group or collection of individuals.
        
  'positive': [
    'The company is changing its target market.',
    'Our staff are working hard.',
    'The committee is meeting this morning.',
    'My family have all gone back to Australia.',
    'The crew prepare the ship to enter the harbor.',
    'The government plans to raise the sales tax.',
    'His family is large.',
    'The fleet sails west.',
    'The hospital staff is busy all day every day.',
    # pos error: exception
    # 'The police are after the thief.',
    'The team is away this weekend; they have a good chance of winning.',
  ],
  'negative': [
    'I think that’s a planet, not a star.',
    'I’m flying first-class on Emirate Airlines.',
    'My teacher starts work before sunup.',
    'Thomas Jefferson was a president and philosopher.',
    'Let’s go to the city.',
    'He’s always hanging out with his girlfriend.',
    'I need to visit an old castle. Can we visit Warwick Castle?',
    'I’d like to adopt a cat.',
    'Agatha Christie wrote many books.',
    'Cleopatra is the cutest kitten ever.',
    'The boy threw the ball to his dog, Wilson.',
    'I’d like you to meet my friend Jeremy.',
    'I’m craving Oreos.',
    'There are many important documents at The Library of Congress.',
    'There\'s a reason why Evian is "naive" backwards.',
    'We went to Smith’s Furniture and bought a new couch to replace our old one.',
    'My best friend moved to Israel to study.',
    'I want to be a writer.',
    'Would you like a cookie?',
    'He never goes anywhere without Sarah.',
    'There are a lot of important documents in the archives.',
    'When the Titanic sank, the captain went down with the ship.',
  ],
}
test_data_0711 = { 

      # **Guideword:** UNCOUNTABLE NOUNS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of uncountable nouns. 
        
  'positive': [
    'I would like to give you some advice.',
    'Measure 1 cup of water, 300g of flour, and one teaspoon of salt.',
    'We did an hour of work yesterday.',
    'Can you give me some information about uncountable nouns?',
    'How much rice do you want?',
    'I didn\'t make much progress today.',
    'There has been a lot of research into the causes of this disease.',
    'This looks like a lot of trouble to me.',
    'He did not have much sugar left.',
    'He gave me a great deal of advice before my interview.',
  ],
  'negative': [
    'Will you help me carry these boxes?',
    'Every dish on this menu is delicious.',
    'I bought some books at the store.',
    'We must finish these studies.',
    'I own a house.',
    'I would like two books, please.',
    'He has ten watches.',
    'How many friends do you have?',
    'I have two books.',
    'My mother makes pancakes.',
    'Everybody is invited to the party.',
    'I need to do the dishes soon.',
    'He’s growing tomatoes.',
    'Each student is reminded to bring his protractor.',
    'There are six zeros in a million.',
    'I work two jobs.',
    'Every student passed the test.',
    'I have several Japanese dictionaries.',
    'There are 365 days in a year.',
    'She has three dogs.',
  ],
}
test_data_0712 = { 

      # **Guideword:** WITH 'THE'
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use uncountable nouns with 'the' to talk about something specific. 
        
  'positive': [
    'The news made me frustrated.',
    'The experience I got there is priceless.',
    'I got the information about the meeting yesterday.',
    'The wealth he has got is much more than I have got.',
    'I love the furniture which you have in your house.',
    'We can use the knowledge of history to make better decisions today.',
    'The research I did last year is useless now.',
    'The weather is going to be rainy.',
    'The coffee I like best is from Brazil.',
    'The wind is getting stronger and stronger.',
  ],
  'negative': [
    'I’ve heard that it’s good to drink at least eight glasses of water a day.',
    'I’ll have a glass of water, please.',
    'Yesterday I went to the restaurant which we went together last week.',
    'I didn\'t make much progress today.',
    'This looks like a lot of trouble to me.',
    'He did not have much sugar left.',
    'He gave me a great deal of advice before my interview.',
    'I would like to give you some advice.',
    'My glasses are dirty.',
    'Cancer is a cruel disease.',
    'How much rice do you want?',
    'This bottle is made of glass, so it is very fragile.',
    'We did an hour of work yesterday.',
    'Can you give me some information about uncountable nouns?',
    'I bought three sheets of glass at the shop.',
    'Coffee wakes you up',
    'Salt is necessary for cooking.',
    'Measure 1 cup of water, 300g of flour, and 1 teaspoon of salt.',
    'There has been a lot of research into the causes of this disease.',
    'I don’t have a lot of time.',
    'Weather changes every day',
  ],
}
test_data_0713 = { 

      # **Guideword:** WITH DETERMINERS, QUANTITY
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use uncountable nouns with a limited range of quantity words and phrases including 'some', 'any', 'a lot of', 'more'. ► Determiners: quantity
        
  'positive': [
    'Can I have some tea?',
    'I would like to get some water.',
    'You gave me more advice.',
    'I have got some knowledge at the school.',
    'I don\'t have any water.',
    'There is a lot of evidence here.',
    'She did some research about Japan for me.',
    'There is a lot of fish in that river.',
    'I need some money right now.',
    'There has been a lot of research into the causes of this disease.',
    'This looks like a lot of trouble to me.',
  ],
  'negative': [
    'The news made me frustrated.',
    'The experience I got there is priceless.',
    'I got the information about the meeting yesterday.',
    'I’ve heard that it’s good to drink at least eight glasses of water a day.',
    'Salt is necessary for cooking.',
    'Measure 1 cup of water, 300g of flour, and 1 teaspoon of salt.',
    'The wealth he has got is much more than I have got.',
    'We did an hour of work yesterday.',
    'I love the furniture which you have in your house.',
    'The knowledge about history can be used in the future.',
    'The research I did last year is useless now.',
    'The weather is going to be rainy.',
    'I’ll have a glass of water, please.',
    'The cancer I got was cruel.',
    'The wind is getting stronger and stronger.',
    'How much rice do you want?',
    'Yesterday I went to the restaurant which we went together last week.',
    'Coffee wakes you up',
    'The weather changes every day',
    'He gave me a great deal of advice before my interview.',
  ],
}
test_data_0714 = { 

      # **Guideword:** CONTAINERS, QUANTITY EXPRESSIONS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can refer to an individual example or quantity of an uncountable noun using words for containers and countable items. 
        
  'positive': [
    'There are plates of food on the table.',
    'I want to get a bottle of water.',
    'I made two kinds of soup.',
    'I ate two bowls of ice cream.',
    'You should put a spoon of salt on the dish.',
    'I normally give a bowl of rice to the temple every morning.',
    'I’ll have a glass of water, please.',
    'She ate a plate of seafood.',
    'I only need a piece of information about the issue.',
    'My friend loves to drink a cup of tea every morning.',
    'I’ve heard that it’s good to drink at least eight glasses of water a day.',
  ],
  'negative': [
    'I’ve heard that it’s good to drink water every day.',
    'I need more education.',
    'Milk was spilled on the counter.',
    'He is a very wealthy man.',
    'I love to shop for furniture for my house.',
    'Yesterday I went to the restaurant which we went to together last week.',
    'I need some more education.',
    'All the milk was spilled.',
    'The wealth he has got is much more than I have got.',
    'I love the furniture which you have in your house.',
    'Coffee wakes you up.',
    'You gave me good advice.',
    'The weather is going to be rainy.',
    'This is money from Peru.',
    'Freedom is everything for people.',
    'How much rice do you want?',
    'The wind is getting stronger and stronger.',
    'Can you give me red wine?',
    'She did research about Japan for me.',
    'I got information about the meeting yesterday.',
    'Could you play rock music?',
    'Salt is necessary for cooking.',
    'Research needs more funding in this country.',
    'You should put salt on it.',
    'Weather changes every day',
  ],
}
test_data_0715 = {

  # **Guideword:** UNCOUNTABLE NOUNS
  # **Guideword type:** FORM
  # **Super category:** NOUNS
  # **Sub category:** uncountable
  # **Lexical Range:** 2.0
  # **CEFR level:** B1
  # **CAN-DO:** Can use an increasing range of uncountable nouns.

  'positive': [
    'He did not have much sugar left.',
    'There has been a lot of research into the causes of this disease.',
    'I didn\'t make much progress today.',
    'Can you give me some information about uncountable nouns?',
    'He gave me a great deal of advice before my interview.',
    'This looks like a lot of trouble to me.',
    'How much bread should I bring?',
    'How much rice do you want?',
    'Measure 1 cup of water, 300g of flour, and 1 teaspoon of salt.',
    'I would like to give you some advice.',
    #moved from negative, 'confidence' is uncountable, 'uncle' is actually triggering detector
    'Her uncle had an air of confidence.',

  ],
  'negative': [
    'He has been collecting the works of dog.',
    'I’ll have a glass please.',
    'Their computers are expensive.',
    'Many forests are being destroyed by loggers in the world.',
    # 　everything is not countable in some sense and cannot be added "s"
    # 'I can tell you about everything.',
    'I own a house.',
    'How many friends do you have?',
    # room is marked as uncountable
    # 'There was a fire in her living room.',
    # parser wrongly recognized yesterday as noun
    # 'I bought a car yesterday.',
    'He taught me how to write a paper.',
    'I would like two books please.',
    'I bought a new car last week.',
    'She is the person I like.',
    # "game" here is ambiguous
    # 'I love the game of Go.',
    'She has three dogs.',
    'I’ve heard that it’s good to drink at least eight glasses of it a day.',
    'My son likes playing games.',
    'They ordered a few beers.',
    'I ate some snacks.',
  ],
}
test_data_0716 = { 

      # **Guideword:** WITH DETERMINERS, QUANTITY
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use uncountable nouns with an increasing range of quantity words and phrases including 'much', 'a bit of', 'a little bit of', 'enough', 'further', 'plenty of', 'loads of'.  ►  Determiners: quantity
        
  'positive': [
    'I don\'t have enough money.',
    'I\'ve got plenty of money.',
    'I only have a little bit of money left.',
    'I\'d like a bit of time to do that.',
    'There is no further information about him.',
    'I have a bit of time.',
    'He got loads of money when he was young.',
    'There is much water in the pond today.',
    'Much rain has fallen this year.',
    'Do you have a bit of time now?',
  ],
  'negative': [
    'How many friends do you have?',
    'He taught me how to write a paper.',
    'Security is now a high priority.',
    'We will respond properly to requests from customers for disclosure.',
    'This looks like a lot of trouble to me.',
    'The two women had very different opinions about yoga.',
    'There was a fire in her living room.',
    'My son likes playing baseball.',
    'I bought a car yesterday.',
    'I saw many cars.',
    'Their computers are expensive.',
    'I need some advice about my PC.',
    'He gave me a great deal of advice before my interview.',
    'I would like to give you some advice.',
    'Those rules take priority in our team.',
    'There has been a lot of research into the causes of this disease.',
    'Measure 1 cup of water, 300g of flour, and 1 teaspoon of salt.',
    'Can you give me some information about uncountable nouns?',
    'Details will be sent on request.',
    'I ate many cookies today.',
  ],
}
test_data_0717 = { 

      # **Guideword:** NO ARTICLE
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use uncountable nouns without a definite article to refer to an abstract thing in general. 
        
  'positive': [
    'Peace gives us courage.',
    'Gravity is an important force at that scale.',
    'Light travels faster than sound.',
    'Love needs patience.',
    'Research tends to take a lot of time.',
    'History is way too difficult to remember.',
    'Water boils at 212 degrees Fahrenheit.',
    'Politics is not a very interesting subject to me.',
    # 'English is the most used language.',
    # English: NNP
    'Knowledge makes you grow up.',
  ],
  'negative': [
    'This looks like a lot of snow to me.',
    'I don\'t have enough for everybody.',
    'We worked for an hour yesterday.',
    'There was a fire in her living room.',
    'He did not have any cookies left.',
    'He taught me how to write a paper.',
    'His luggage has been stolen.',
    'How much rice do you want?',
    'Her uncle seemed confident.',
    'They researched the causes of this disease.',
    'I would like to give you my car.',
    'Many people live below the poverty line.',
    'I need a new notebook.',
    'Can you give some information about the work?',
    'I didn\'t make any new paintings today.',
    'Measure 1 cup of water, 300g of flour, and 1 teaspoon of salt.',
    'How much bread should I bring?',
    'He gave me a cup of coffee before my interview.',
    'He has been collecting the works of William Shakespeare.',
    'The trees were covered with snow.',
  ],
}
test_data_0718 = { 

      # **Guideword:** UNCOUNTABLE NOUNS
      # **Guideword type:** FORM
      # **Super category:** NOUNS
      # **Sub category:** uncountable
      # **Lexical Range:** 3.0
      # **CEFR level:** C1
      # **CAN-DO:** Can use a wide range of uncountable nouns, particularly referring to abstract concepts. 
        
  'positive': [
    'There has been a lot of work into the causes of this disease.',
    'Let’s get rid of the garbage.',
    'I realized that he has little knowledge.',
    'Please take good care of your equipment.',
    'The research was done by my daughter.',
    'He gave me a great deal of advice before my interview.',
    'I need to find information about Pulitzer Prize winners.',
    'Good information is necessary for making good decisions.',
    'The children fell asleep quickly after a busy day of fun.',
    'You seem to have a high level of intelligence.',
  ],
  'negative': [
    'The parade included fire trucks and police cars.',
    'We would like some large bottles.',
    'I haven’t got many pens today.',
    'How many candles are on that birthday cake?',
    'I love to listen to songs when I work.',
    'I was feeling so stressed that I ate an entire box of cookies.',
    'There are at least twenty Italian restaurants in Little Italy.',
    'You have several paintings to study in the class.',
    'Being accused of the crime, I was in a difficult situation.',
    'Alex also has four rainbow pencils.',
    'I bought a book on the subject.',
    'Being very shy, he couldn\'t bring himself to ask her to go to the movies with him.',
    'I want an orange in my lunch.',
    'I did it many times when I was young.',
    'Michael can play several different musical instruments.',
    'Each chapter covers over five topics.',
    'There’s a big brown dog running around the neighborhood.',
    'Crossing the road alone is dangerous.',
    'Megan took a lot of photographs when she went to the Grand Canyon.',
    'This car contains four seats.',
  ],
}
test_data_0719 = {

    # **Guideword:** AS SUBJECTS
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** noun phrases - grammatical functions
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use nouns and noun phrases as subjects of the clause.

    'positive': [
        'My name is James.',
        'My next baseball game is on this coming Friday.',
        'Your sister is a teacher in elementary school.',
        'A lot of people here are Japanese people who live in Thailand.',
        'I think that my friend James is from China.',
        'My Friend James\'s nickname is Jack.',
        'My father said that he used to be a baseball player.',
        'I think my brother is a hard-working guy.',
        'My girlfriend is the kindest girl in the world.',
        'Life is pretty hard, and there are many unexpected things happens.',
        'My friends are all nice and kind.',
    ],
    'negative': [
        'She is such a traveler.',
        'I like everything in my home.',
        'I have to go to school because I have a quiz today.',
        'We understand what you have been through.',
        'I would like to invite you to my house.',
        'I will buy this photograph because it is beautiful.',
        'If you want to enter that university, you have to study harder.',
        'Even though you are not good at English, you can go anywhere in the world.',
        'He always sings since he was young.',
        'I don\'t go to music class because I don\'t like to play any musical instruments.',
        'When you finish your homework, just let me know.',
        'This is what I really wanted to do when I come to the baseball stadium.',
        'This is why I don\'t want to go to school today.',
        'This is where I always wanted to come for my entire life.',
        'I gave you nice and beautiful flowers for your birthday.',
        'They brought some water for me.',
        'She bought me a nice watch.',
        'She studies history in her school.',
        'He is searching for his job, and it is not going great.',
    ],
}
test_data_0720 = {

    # **Guideword:** AS OBJECTS
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** noun phrases - grammatical functions
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use nouns and noun phrases as objects of the clause.

    'positive': [
        'I play baseball every day.',
        'She lives a life of luxury.',
        'They should stop that absurd fighting.',
        'I can see the vague figures of two people in the distance.',
        'People in Hong Kong speak Cantonese.',
        'My daughter finished the race in first place.',
        'My sister will begin intensive training for the race.',
        'We discussed new ideas at the meeting.',
        'I think you should try other sports.',
        'I want water because I\'m thirsty now.',
    ],
    'negative': [
        'My next baseball game is on this coming Friday.',
        'Your sister is a teacher in elementary school.',
        'A lot of people here are Japanese people who live in Thailand.',
        'My father used to be a baseball player.',
        'I think my brother is a hard-working guy.',
        'My girlfriend is the kindest girl in the world.',
        # 'I am getting a little tired of all this rain.',
        # getからlittleにdobj dependencyがあるらしく、positive判定が出る。
        # ブラウザのStandard Core NLPだとそうはならないんですけど……
        # ちなみにa litteをなくするとちゃんとnegative判定が出ます。
        # TODO: resolve the conflict between the brawser and API vers of Stanford Core NLP
        'Unless business improves, we will go bankrupt.',
        'I went shopping for flowers in the morning.',
        'Your plan sounds good to me.',
        'I\'ve been feeling exhausted recently.',
        'I fell asleep on the flight.',
        'My neck hurts.',
        'My brother is doing well at school.',
        'This train stops at every station.',
        'I live in a small apartment.',
        'Camels can live without water for several days.',
        'The two sisters walked home together.',
        'Children learn quickly.',
        'The concert just ended.',
    ],
}
test_data_0721 = {

    # **Guideword:** AS COMPLEMENT OF PREPOSITIONS
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** noun phrases - grammatical functions
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use nouns and noun phrases as complements of prepositions in prepositional phrases.

    'positive': [
        'My brother studied English after dinner.',
        'I go to school by bike every day.',
        'My parents went to Kyoto during the summer vacation.',
        'This pen is a present for your father.',
        'He lives near the hospital where I went three days ago for the first time.',
        'There is a book on the desk.',
        'My younger sister walks to school.',
        'I want to go there with my friend.',
        'I saw your boyfriend at the station.',
        'The greater part of this theorem is to illustrate the complicated fact clearly.',
        'People in Cambodia speak Khmer.',
        # in Cambodia
    ],
    'negative': [
        'Your sister is an engineer.',
        'My friend is a Chinese who lives around here.',
        'My mother used to be a teacher five years ago.',
        'I think my brother is quite a lazy boy.',
        'My girlfriend is the most beautiful woman who I\'ve ever met.',
        'You have been feeling tired recently.',
        'My neck hurts.',
        'My brother is doing well recently.',
        'The two sisters walked home together.',
        'Children learn quickly.',
        'The food event just ended.',
        'I play baseball every day.',
        'She generally lives around here.',
        'They should stop that absurd fighting.',
        'You should try other sports.',
        'I want water because I\'m thirsty now.',
        'The students misbehave.',
        'Dogs bark.',
        'Birds are chirping.',
    ],
}
test_data_0722 = {

    # **Guideword:** AS COMPLEMENT OF 'BE'
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** noun phrases - grammatical functions
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use nouns and noun phrases as complements of the verb 'be'.

    'positive': [
        'Your sister is a teacher in elementary school.',
        'My friends are Japanese people who live in Thailand.',
        'I think my sister is such a lazy woman.',
        'My girlfriend is the kindest girl in the world.',
        'We emphasize the fact that the function is a finite measure.',
        'This is an interesting book.',
        'You are a good football player.',
        'Traditional Japan is wonderful.',
        'My mother is quite busy right now.',
        'The formula is easily the longest one I\'ve ever seen.',
    ],
    'negative': [
        'My younger sister is by the window.',
        # 'My next baseball game is on this coming Friday.',
        # is comingで進行形判定される
        'Unless business improves, we will go bankrupt.',
        'I went shopping for clothes in the morning.',
        'Your plan sounds crazy to me.',
        'I\'ve been feeling excited recently.',
        'My back hurts.',
        'I live in a huge apartment.',
        'Camels can live without water for a couple of days.',
        'We walked home together.',
        'Children learn quickly.',
        'The concert just ended.',
        'She lives a life of luxury.',
        'They should stop that absurd fighting.',
        'I can see the vague figures of two people in the distance.',
        'People in Hong Kong speak Cantonese.',
        'My daughter finished the race in first place.',
        'We discussed new ideas at the meeting.',
        'You should try to hang out with new people.',
        'I want to go home as soon as possible.',
        'My friends love to eat Korean foods.',
        'You can talk to me anytime if you need to.',
    ],
}
test_data_0723 = {

    # **Guideword:** AS ADJUNCTS
    # **Guideword type:** FORM
    # **Super category:** NOUNS
    # **Sub category:** noun phrases - grammatical functions
    # **Lexical Range:** None
    # **CEFR level:** A1
    # **CAN-DO:** Can use nouns and noun phrases as adjuncts in some time expressions.

    'positive': [
        'You can visit me tomorrow if you want.',
        'It was rainy yesterday.',
        'I don\'t feel like doing anything today.',
        'We have a one week vacation next week.',
        'She cut her hair last week.',
        'I went to see my grandmother last month.',
        'I shall be back early next month.',
        'I\'ll be seventeen next year.',
        'My dog died last year.',
        'My sister might go to school tomorrow morning.',
        'It was my first time trying scuba diving.',
        'Last time when I saw you you were at the airport.',
        #'Would it be possible for you to check this paper by the next conference?', although semantically denoting a particular time, this example doesn't include a time expression.
        'Would it be possible for you to check this paper by next month?'
        # 形容詞を許容しないと拾えない例を追加しました。
        'My parents went to Kyoto during the summer vacation.',
    ],
    'negative': [
        'I must go to school to take an exam.',
        'I can go anywhere if you let me.',
        'When my brother came into my room, I was sleeping.',
        'Just let me know when you get ready.',
        'What I wanted to do with you was to play a video game together.',
        # 'Time is money.',
        # このtimeは時間表現ではないと思いますが、区別が難しくてできませんでした。
        # 'A year has twelve months.
        # 類似の問題を抱える例文を追加しました。これも区別できませんでした。
        'You can go anywhere after having lunch.',
        'Do homework before hanging out with your friends.',
        'I think my brother is quite a lazy boy.',
        'My brother is doing well recently.',
        'The two sisters walked home together.',
        'I want water because I\'m thirsty now.',
        'The students misbehave.',
        'My brother studied English after dinner.',
        'My younger sister walks to school.',
        'I want to go there with you.',
        'I saw your boyfriend at the station.',
    ],
}
test_data_0724 = { 

      # **Guideword:** WITH 'BY' TO ADD INFORMATION
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the passive with 'by' to add information about something already known.
        
  'positive': [
    'The letters were delivered by an owl.',
    'The best movie has been chosen by the committee.',
    'The bank was robbed by two dumb kids.',
    'My muffin has been eaten by an unknown person.',
    'The dogs were fed by the children.',
    'Taxes are going to be raised by next year.',
    'The dogs were not being fed by anyone.',
    'The fire had been put out by the neighbors.',
    'The bread is baked by my father.',
    # 'You will be fined for littering by the government.',
    # littering->goverment(nmod:by)
    'The camera was bought by a man named Charles.',
  ],
  'negative': [
    # parser error
    # raised -> year (nmod:agent)
    # 'Taxes are going to be raised by next year.',
    'Lisa has recorded a song for her fiancé.',
    'I want an answer by tomorrow morning.',
    'He broke a chair by accident.',
    'Someone has stolen my sweater.',
    'He delivered the flowers to my mother.',
    'Martin handed her a coupon.',
    'Jack had the kindness to give me a present.',
    'My daughter was standing by the door.',
    'Let’s begin by reviewing the last lesson.',
    'He had spent all his money by the time Christmas came.',
    'Alice could speak Chinese at the age of five.',
    'She passed the examination by studying hard.',
    'Mona grew up by the ocean.',
    'I have finished my work for today.',
    'Alex wrote an essay about Asian politics.',
    'He goes by the name of Daniel.',
    'I wrote a letter by hand.',
    'I don’t have a smartphone.',
    'He picked up the photo by one corner.',
    'Some boys were helping the old man.',
    'I could lend you my dictionary.',
    'I am baking a cake with the chef.',
    'I\'m wondering if the sloth sleeps by day.',
    'I remember there was a tree by my house.',
  ],
}
test_data_0725 = { 

      # **Guideword:** PAST SIMPLE, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the past simple passive affirmative after a singular subject. 
        
  'positive': [
    'This door was painted by John.',
    'The apple was eaten by Lauren.',
    'The wallet was given to him by Nick.',
    'The road was closed by the police so they could deal with the accident.',
    'A song was sung by Maddie.',
    'The area was designed to appeal to young people.',
    'The furniture was bought at a local market.',
    'The mistake was corrected by the teacher.',
    'The Internet was invented during the 1950s.',
    'My father was called just after midnight.',
    'I remember that the song was sung by Maria.',
  ],
  'negative': [
    'These mistakes were corrected by the teacher.',
    'I was not listened to by you.',
    'They didn’t make their beds.',
    'A thief stole a bag from my car.',
    'John loved his friends very much.',
    'The audience didn’t cheer for the actor.',
    'She didn’t win the prize.',
    'She did not write a story.',
    'Scientists found a large number of chemicals in the river.',
    'I decorated the living room last year.',
    'She did not know anything about it.',
    'Our computers were being attacked by hackers.',
    'Our computer was being attacked by hackers.',
    'This country was not invaded in that war.',
    'I did not tell them about my father’s death.',
    'The teacher gave the parents a tour of the school.',
    'He is taken to school by his mom.',
    'Ben wrote to the council about the noisy neighbors.',
    'English is spoken here.',
    'The house is being painted.',
    'I took the exam last year.',
    'The company exported their products all over the world.',
    'My friends didn’t let him go.',
    'At school, the professors teach the students.',
    'Many products were assembled in this factory.',
    'Was this pen bought by John?',
    'Has John been told?',
    'Arrangements will be made to send them to other locations.',
    'He could not be discouraged from pursuing his path by anybody.',
  ],
}
test_data_0726 = { 

  # **Guideword:** PRESENT SIMPLE, AFFIRMATIVE
  # **Guideword type:** FORM
  # **Super category:** PASSIVES
  # **Sub category:** passives: form
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use the present simple passive affirmative with a singular subject.
    
  'positive': [
    'It is made from wood and has a natural feel.',
    'They think the cat is taken care of by him, which is not true.',
    'My professor is regarded as an associate professor in the faculty.',
    'Charlie is followed by multiple detectives whom I hired.',
    'How can it happen that he is still regarded as a criminal although he has been in jail for more than ten years?',
    'It is made evident by the fact that she does not work there anymore.',
    'The whole group of students is called prospective students.',
    'He is known for his prowess as a battle commander.',
    'He can be counted among one of the best players of all time.',
    # cannot be regarded
  ],
  'negative': [
    # 分詞の形容詞化
    # TODO: 必要ならばpositiveにして作ること
    'What could I have done so that I am more satisfied with my life?',
    # satisfied: JJ
    'They are concerned that more severe storms might come in the next couple of days.',
    # concerned: JJ
    'My professor was regarded as an associate professor in the faculty.',
    'How surprised was she when she first heard the news?',
    'Charlie was seen by multiple detectives last night.',
    'I was surprised by the fact that she did not work there anymore.',
    'What could I have done to be more satisfied with my life?',
    'They did not buy anything today, and they don\'t know if it is okay.',
    'It happened more than five times that the fire alarm in this dorm went off.',
    'Can you get more ice for this room?',
    'Where should I go after I finished all my assignments?',
    'How can it be possible that they do not want to participate?',
    'I find it interesting to get involved in club activities on campus.',
    'Where do you think they found the last clue?',
    'What happened does not matter to me because it is none of my business.',
    'Charlie went to Toronto to make it possible to have more friends.',
    'I was not surprised by the fact that she passed the exam.',
    'How can you not be satisfied with this much food?',
    'It can be true that they wanted to participate in that.',
    'Where will you be heading next Saturday?',
    'Is it okay for you to come to the meeting tomorrow?',
    'There is not much stuff going on today on campus.',
    'Why does everyone think he is not smart?',
    'They had my hat frozen for more than 48 hours.',
    'Charlie never asked me if I enjoy my research.',
    'Toronto is a huge city with more than 7 million people residing there.',
    'How did you manage to get to that role in the company?',
    # 以下追加
    'This theorem will be proved in the following sections.',
    'Noby is going to be beaten by big G.',
    'The coating seems to have worn off.',
  ],
}
test_data_0727 = { 

      # **Guideword:** WITH 'BY' IN A RELATIVE CLAUSE|
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the passive with 'by' in a relative clause, often to add more information.
        
  'positive': [
    'She has never met the lecturer who is hated by every student.',
    'I enjoyed the concert that we were all invited to by our friends last night.',
    'We saw the new play that was written by Tom Stoppard at the Old Vic.',
    'I love to stay in my new room which was designed by my brother.',
    'It has 760 windows, which are cleaned by her mother every six weeks.',
    'This is the dog that was taken by him.',
    'I went to the house where I was attacked by that man last month.',
    'The book comes from the library that is liked by everyone.',
    'I can’t find my notebook that was taken by someone at that old bookstore.',
    'This is the house where I was raised by my parents.',
  ],
  'negative': [
    'The book was written by a famous writer.',
    'The machine was invented in Kyoto.',
    'The mouse was chased by the cat.',
    'The singer is known to people in the world.',
    'I am interested in foreign cultures.',
    'The city hall is being rebuilt.',
    'These pictures were taken in New York.',
    'This place will be visited by many people.',
    'The door is made of wood.',
    'We were surprised at the news.',
    'That building was broken last year.',
    'The TV show has been watched by many people.',
    'These songs are loved by young people.',
    'The newspapers are delivered around 5 a.m.',
    'The Statue of Liberty was built in 1886.',
    'The door is opened by him.',
    'English is used in Canada.',
    'The house was built by my grandfather.',
    'The church was built in 1882.',
    'It was said that Japanese food is healthy.',
  ],
}
test_data_0728 = { 

      # **Guideword:** INFINITIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use the passive infinitive after a limited number of forms including 'going to', 'have to', 'need to', 'want to'. 
        
  'positive': [
    'That faucet needs to be fixed.',
    'I want to be loved by her.',
    'I don\'t want to be hit by my father.',
    'The ceiling needs to be painted.',
    'I\'m going to be helped by John.',
    'She wants to be recognized by everyone.',
    'He is going to be sent home in a week.',
    'They have to be paid more attention.',
    'My hair needs to be cut.',
    'A driver’s license has to be earned in order to drive a car.',
  ],
  'negative': [
    'The house was built by my grandfather.',
    'The document was being printed when my client arrived.',
    'The machine was invented in Kyoto.',
    'The gate is locked at 10 o’clock every night.',
    'The church was built in 1882.',
    'This place will be visited by many people.',
    'My son was killed with a knife.',
    'I love to stay in my new room which was designed by my brother.',
    'The city hall is being rebuilt.',
    'These pictures were taken in New York.',
    'The TV show has been watched by many people.',
    'The door is opened by him.',
    'This court will be used by the school team.',
    'The window was broken by John.',
    'I am interested in foreign cultures.',
    'The newspapers are delivered around 5 a.m.',
    'The research can be done today.',
    'The book was written by a famous writer.',
    'Their roof was blown off in the storm.',
    'Jim\'s car was stolen.',
  ],
}
test_data_0729 = { 

      # **Guideword:** PAST SIMPLE, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past simple passive affirmative with a range of pronoun and noun subjects both singular and plural.
        
  'positive': [
    'Coffee was drunk by all of the guests.',
    'Their roof was blown off in the storm.',
    'My son was killed with a knife.',
    'The church was built in 1882.',
    'Jim\'s cars were stolen.',
    'These pictures were taken in New York.',
    'The machine was invented in Kyoto.',
    'The book was written by a famous writer.',
    'The windows were broken by John.',
    'The house was built by my grandfather.',
  ],
  'negative': [
    'I am interested in foreign cultures.',
    'This place will be visited by many people.',
    'The ceiling needs to be painted.',
    'The research can be done today.',
    'My hair needs to be cut.',
    'A driver’s license has to be earned in order to drive a car.',
    'He is being scolded by his father.',
    'He will have been scolded by his mother for 10 hours straight.',
    'The gate is locked at 10 o’clock every night.',
    'Until his father came back he had been scolded by his mother.',
    'A full moon will be seen this evening.',
    'I have been helped very often by Bill.',
    'She is highly praised in New York.',
    'This court will be used by the school team.',
    'The city hall is being rebuilt.',
    'They have to be paid more attention.',
    'The TV show has been watched by many people.',
    'I want to be loved by her.',
    'This conversation was being recorded last night.',
    'The newspapers are delivered around 5 a.m.',
  ],
}
test_data_0730 = { 

      # **Guideword:** PRESENT CONTINUOUS, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use the present continuous passive affirmative with a limited range of verbs.
        
  'positive': [
    'The gate is being painted.',
    'The computer is being used by my husband.',
    'My phone is being repaired now.',
    'He is being scolded by his father.',
    'A patient is being transported by an ambulance team.',
    'The book is being written by my favorite author.',
    'He is being watched by many people now.',
    'The city hall is being rebuilt.',
    'It is being made by her.',
    'Our house is being built.',
  ],
  'negative': [
    'I want to be loved by her.',
    'The novel can be borrowed from the library.',
    'Wine is made from grape.',
    'The ceiling needs to be painted.',
    'The temple had been visited by many people until it was broken.',
    'The book was written by a famous writer.',
    'The house was built by my grandfather.',
    'Until his father came back he had been scolded by his mother.',
    'I have been moved by him recently.',
    'The girl was looked after by my parents.',
    'They have to be paid more attention.',
    'The newspapers are delivered around 5 a.m.',
    'This conversation was being recorded last night.',
    'The bridge has been repaired.',
    'I had been praised by my mother till I was 20 years old.',
    'A driver’s license has to be earned in order to drive a car.',
    'The book has been read by a lot of people.',
    'This place will be visited by many people.',
    'These pictures were taken in New York.',
    'I have been obliged to keep secrets.',
  ],
}
test_data_0731 = { 

      # **Guideword:** PRESENT SIMPLE, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the present simple passive affirmative with a range of pronoun and noun subjects.
        
  'positive': [
    'Her new song is widely sung all over the world.',
    'This song is known by every student in America.',
    'The newspapers are delivered around 5 a.m.',
    'Rice is eaten all over the world.',
    'Wine is made from grapes.',
    'The cakes are baked by my family every year.',
    'Spanish is spoken in Spain.',
    'Flowers are sold at a flower shop.',
    'English is understood around the world.',
    'It is said that young people should study hard.',
  ],
  'negative': [
    'These pictures were taken by her.',
    'The story was written by him ten years ago.',
    'I wasn\'t scolded by my mother.',
    'The gate is being painted.',
    'She will be sent a New Year\'s card by him.',
    'His mother was given a carnation by him.',
    'I was taught English by her.',
    'The girl was looked after by my parents.',
    'My son was kicked by his classmate.',
    'A new building will be built here.',
    'The book has been read by a lot of people.',
    'He is being watched by many people now.',
    'The computer is being used by my husband.',
    'That window was broken.',
    'My bicycle was broken last night.',
    'My room was cleaned up by my mother.',
    'A letter was being written by him last night.',
    'She was showed my friend\'s picture by me.',
    'This meeting room is being cleaned by newcomers.',
    'A patient is being transported by an ambulance team.',
  ],
}
test_data_0732 = { 

      # **Guideword:** PRESENT SIMPLE, NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the present simple passive negative with a range of pronoun and noun subjects.
        
  'positive': [
    'These pets aren’t kept by him.',
    'The car isn\'t bought by him.',
    'This question is not solved by everyone.',
    'Those flowers are not sold at that flower shop.',
    'This room is not cleaned regularly.',
    'The box isn’t cleaned by my father.',
    'Rice is not eaten all over the world.',
    'Japanese is not spoken all over the world.',
    'You are not loved by her.',
    'The door is not closed by him.',
  ],
  'negative': [
    'Spanish is spoken in Spain.',
    'Her new song is widely sung all over the world.',
    'The car was bought by Ken.',
    'My room was cleaned up by my mother.',
    'The apples were eaten by him.',
    'These pictures were taken by her.',
    'Cakes are being baked by my mother.',
    'The castle wasn’t built in 1700.',
    'A new building will be built here.',
    'The story was written by him ten years ago.',
    'Wine is made from grape.',
    'The newspapers are delivered around 5 a.m.',
    'He is being watched by many people now.',
    'She was shown my friend\'s picture.',
    'A patient is being transported by an ambulance team.',
    'She will be sent a New Year\'s card by him.',
    'His mother was given a carnation by him.',
    'English is spoken around the world.',
    'This song is sung by every student in America.',
    'The box is opened by her.',
  ],
}
test_data_0733 = { 

      # **Guideword:** WITH VERBS TAKING TWO OBJECTS.
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past simple passive with a limited range of verbs needing two objects, putting the indirect object in subject position. 
        
  'positive': [
    'I was given this pen by him.',
    'Susan was bought a nice jacket by Jack.',
    'I was given a bat by my father.',
    'She was sent a New Year\'s card by him.',
    'His mother was given a carnation by him.',
    'We were given the permission by our manager.',
    'I was given this pocket watch by my uncle.',
    'His child was called Ann by him.',
    'She was shown my friend\'s picture by her father.',
    'My dog was named Boss by me.',
  ],
  'negative': [
    'Japanese is not spoken all over the world.',
    'The newspapers are delivered around 5 a.m.',
    'I have been told a lie by my best friend once.',
    'Wine is made from grapes.',
    'Spanish is spoken in Spain.',
    'This question is not solved by everyone.',
    'This room is not cleaned regularly.',
    'The door is not closed by him.',
    'The car was bought by Ken.',
    'These pictures were taken by her.',
    'The box is opened by her.',
    'Those flowers are not sold at that flower shop.',
    'The castle wasn’t built in 1700.',
    'I have been praised by my mother since I was a child.',
    'The car isn\'t bought by him.',
    'The book will have been read one hundred times if he reads it.',
    'Rice is not eaten all over the world.',
    'My room was cleaned up by my mother.',
    'The story was written by him ten years ago.',
    'Dinner is cooked by her.',
  ],
}
test_data_0734 = { 

      # **Guideword:** GIVING FOCUS WITH 'BY'
      # **Guideword type:** USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the passive with 'by' to give focus.
        
  'positive': [
    'The story was written by him ten years ago.',
    'Dinner is cooked by her.',
    'We were given permission by our manager.',
    'She was sent a New Year\'s card by him.',
    'My room was cleaned up by my mother.',
    'The door is not closed by him.',
    'The car isn\'t bought by him.',
    'The box is opened by her.',
    'His child was called Ann by him.',
    'This question was not solved by everyone.',
  ],
  'negative': [
    'This store is opened at ten.',
    'She was killed in the traffic accident.',
    'The castle wasn’t built in 1700.',
    'I have been praised since I was a child.',
    'Wine is made from grapes.',
    'The stockholders elected him the next president.',
    'He is known to everyone as a professional golfer.',
    'Those flowers are not sold at that flower shop.',
    'Spanish is spoken in Spain.',
    'The young man was promised a new position in the company.',
    'The top of the mountain is covered with snow.',
    'Japanese is not spoken all over the world.',
    'He offered me a bilateral contract.',
    'Rice is not eaten all over the world.',
    'This room is not cleaned regularly.',
    'The book will have been read one hundred times if he reads it.',
    'He was never seen to slow down in his work.',
    'We were caught in a heavy storm in Okinawa.',
    'The newspapers are delivered around 5 a.m.',
    'The hospital was built in 1979.',
  ],
}
test_data_0735 = { 

      # **Guideword:** PRESENT CONTINUOUS, FUTURE REFERENCE
      # **Guideword type:** USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the present continuous passive to refer to the future.
        
  'positive': [
    'Our house is being built.',
    'The door is being opened by him now.',
    'This rooms are being cleaned.',
    'I am being attacked.',
    'My laptop is being repaired.',
    'The book is being read by me.',
    'It is being made by her.',
    'He is being scolded by his father.',
    'My phone is being repaired now.',
    'A patient is being transported by an ambulance team.',
  ],
  'negative': [
    'Toyota cars are exported from Japan.',
    'The young man was promised a new position in the company.',
    'Wine is made from grapes.',
    'He offered me a bilateral contract.',
    'English has been spoken there since 1977.',
    'Spanish is spoken in Spain.',
    'This room is cleaned everyday.',
    'This conversation was being recorded last night.',
    'The story used to be told in my country.',
    'My car has been broken.',
    'The stockholders elected him the next president.',
    'The box is opened by her.',
    'They will be holding a party at this time tomorrow.',
    'The picture was drawn by her.',
    'The mountain will soon be covered with snow.',
    'Japanese is not spoken all over the world.',
    'The car isn\'t bought by him.',
    'The castle wasn’t built in 1700.',
    'Many soldiers had been killed before the war ended.',
    'This room is not cleaned regularly.',
  ],
}
test_data_0736 = {

      # **Guideword:** INFINITIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the passive infinitive affirmative and negative forms after an increasing range of main verbs, modal verbs, adjectives and nouns, in impersonal constructions. 
        
  'positive': [
    'I want to be loved.',
    'All our merchandise must be sold.',
    'More access to education will help them not to be forced to go hungry.',
    'This cake should not to be baked yet.',
    'The principal decided that those supplies are to be used.',
    'Some students were supposed to be made to clean the classroom.',
    'I was asked to be interviewed.',
    'The fruits should not be cut before dinner.',
    'The box must not be opened.',
    'The dinner is not to be held tomorrow.',
    'I was very glad to be invited by them.',
    'I don\'t want to be hit by my father.',
    'I like to be praised by everyone.',
    'It should be done by them immediately.',
    'He did something to be praised by everyone.',
    'The ground is starting to be covered by snow.',
  ],
  'negative': [
    'This story is too long to read in an hour.',
    'There is no time to lose.',
    'They have given a prize to him.',
    'The window was broken by John.',
    'They should speak to each other.',
    'I want you to return these books by tomorrow.',
    'This machine was not broken by him.',
    'John was killed by burglars last night.',
    'There is nothing to see.',
    'The book was written by her.',
    'Jim was proud to have been chosen captain of the team by his friends.',
    'He has a lot of books to read.',
    'I want her to love me.',
    'English is spoken by me.',
  ],
}
test_data_0737 = { 

      # **Guideword:** MODAL PERFECT
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present perfect simple affirmative and negative forms with modal verbs to refer to the past.
        
  'positive': [
    'Without your advice, I would have been robbed of my bag.',
    'I would have been shot.',
    'He should have been scolded.',
    'These policies should have been labeled as failures.',
    'The accident could have been avoided by the exercise of reasonable care.',
    'He sang so well that even a professional singer would have been put to shame.',
    'If the doctor had come sooner, the injured would have been saved.',
    'Had it not been for your courage, we would have been killed.',
    'If he had been a little more careful, the accident might have been avoided.',
    'They might have been killed if the car had gone over the cliff.',
  ],
  'negative': [
    'You cannot have played this guitar.',
    'That would have been difficult for his old self.',
    'He may have read my diary already.',
    'I wish he could have been alive to this day.',
    'Nothing could have been better.',
    'I may have read this book.',
    'She may have forgotten about it.',
    'It must have been important.',
    'He should have studied English.',
    # 'It would have been better left unsaid.',
    # left -> better (advmod)
    'It would have been good to be able to speak with you before he came.',
    'You need not have known this.',
    'I ought to have trusted him.',
    'I might have read this book.',
    'I wish you could have been there.',
    'It would have been better if I\'d been able to speak English.',
    'This would have been easy on a clear road throughout.',
    'You should not have trusted him.',
    'I would have been happier if I was with you.',
    'It would have been cheap at twice the price.',
  ],
}
test_data_0738 = { 

      # **Guideword:** PAST CONTINUOUS AFFIRMATIVE.
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past continuous passive affirmative. 
        
  'positive': [
    'This man was being held in a prison because he did something very bad.',
    'A novel was being written by her.',
    'Pancakes were being made in the kitchen.',
    'Flowers were being grown in this garden.',
    'The room was being measured by Harry Potter.',
    'The stones were being thrown by the boy.',
    'She was being hugged by her brother.',
    'The book was being read by the boy.',
    'The team was being congratulated by the coach.',
    'The mail was being delivered by the postman.',
  ],
  'negative': [
    'A lecture had been given.',
    'Such difficulty had never been experienced by me.',
    'Is a letter being written by her?',
    'The TV wasn\'t being watched.',
    'Why was the child being beaten by her?',
    'What was being written by him on the desk?',
    'Was the desk being built by her?',
    'Had they been invited by her?',
    'The letter had been written by a supporter.',
    'My work had been finished.',
    'Dinner was not being prepared by her.',
    'Are the gifts being bought by them?',
    'For what was such a noise being made by you?',
    'A speech was not being made by him.',
    'Were you being attacked by the suspect?',
    'Had the lecture been given by him?',
    'Why was I being cheated by you?',
    'He was not being listened to.',
    'Which book was being read by you?',
    'Whose bicycle was being repaired?',
    'Had dinner been prepared by her?',
  ],
}
test_data_0739 = { 

      # **Guideword:** PAST PERFECT SIMPLE, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect passive affirmative form.
        
  'positive': [
    'Football had been played by them.',
    'The problems had been solved by Dorothy.',
    'My work had been finished by me.',
    'The city had been defended by the brave men.',
    'Five banks had been robbed by those prisoners.',
    'The enemies had been repelled by them.',
    'The letter had been written by me.',
    'English had been spoken in that country before the wave of nationalism.',
    'The window had been broken by the little girl.',
    'The lecture had been given by him.',
  ],
  'negative': [
    'Why was the child being beaten by her?',
    'Had a lecture been given by him?',
    'Why was such a noise being made by you?',
    'We had taken medicine.',
    'She had killed the mosquitoes.',
    'It had installed windows.',
    'A novel was being written by her.',
    'This man was being held in a prison because he did something very bad.',
    'He had earned money.',
    'Had dinner been prepared by her?',
    'The stone was being thrown by the boy.',
    'The team was being congratulated by the coach.',
    'Which book was being read by you?',
    'The TV wasn\'t being watched.',
    'Dinner was not being prepared by her.',
    'Had a desk been built by her?',
    'They had recorded the voices.',
    'We had celebrated independence Day.',
    'She was being hugged by her brother.',
    'He had cooked biryani.',
  ],
}
test_data_0740 = { 

      # **Guideword:** PAST PERFECT SIMPLE, NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect passive negative form.
        
  'positive': [
    'The spectators hadn\'t been bored by the slow hockey game.',
    'His clothes hadn\'t been donated by him willingly.',
    'Many people had not been made guilty by the system.',
    'The drinking water also had not been infected by terrorists.',
    'He hadn\'t been made a scapegoat by the corrupt officers.',
    'Good traditions had not been established by my father in my family.',
    'The environment had not been completely changed by the Chairman\'s entry.',
    'He hadn\'t been listened to by me.',
    'My work hadn\'t been finished.',
    'A number of the child laborers had not been rescued by police.',
  ],
  'negative': [
    'In my family, good traditions had been established by my father.',
    'A novel was being written by her.',
    'They had recorded our voices.',
    'His shoes are not polished by him.',
    'Why was such a noise being made by you?',
    'That new shirt was not bought by you.',
    'The team was being congratulated by the coach.',
    'We had celebrated independence Day.',
    'Had dinner been prepared by her?',
    'The city had been defended by the brave men.',
    'The TV wasn\'t being watched.',
    'Had passengers been robbed on the train?',
    'Had they been chosen by the president?',
    'The window had been broken by the little girl.',
    'English had been learnt.',
    'Had the problems been solved by Dorothy.',
    'Had the truth been uncovered by him?',
    'Is the book being read by her?',
    'Enemies had been fought by them.',
    'She had killed the mosquitoes.',
  ],
}
test_data_0741 = { 

      # **Guideword:** PAST SIMPLE NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use past simple passive negative. 
        
  'positive': [
    'That building was not broken into last year.',
    'We were not surprised at the news.',
    'The book was not written by her.',
    'This machine was not broken by him.',
    'I was not asked to go out with him.',
    'The TV wasn\'t watched.',
    'The window was not broken by John.',
    'Japanese was not used in this country.',
    'English wasn\'t spoken by the delegates at the meeting.',
    'Milk wasn\'t sold at this store.',
  ],
  'negative': [
    'His clothes had not been donated by him willingly.',
    'The environment had not been completely changed by the Chairman\'s entry.',
    'His shoes are not polished by him.',
    'Enemies had been fought by them.',
    'Good traditions had not been established by my father in my family.',
    'This pencil was used by many people.',
    'The novel was being written by her.',
    'The team was being congratulated by the coach.',
    'The drinking water also had not been infected by terrorists.',
    'She had killed the mosquitoes.',
    'The windows were closed by the students.',
    'The car was used by him.',
    'Tom is known to all the students.',
    'The new shirt is not being worn by you.',
    'The spectators had not been bored by the slow hockey game.',
    'Had in running train passengers been robbed by robbers?',
    'The city had been defended by the brave men.',
    'Is the book being read by her?',
    'They had recorded our voices.',
    'She is liked by everyone.',
  ],
}
test_data_0742 = { 

      # **Guideword:** PRESENT CONTINUOUS, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present continuous passive affirmative with an increasing range of verbs.
        
  'positive': [
    'The computer is being used by my husband.',
    'The book is being read by me.',
    'He is being watched by many people now.',
    'This conversation is being recorded.',
    'It is being made by her.',
    'The book is being read by the man.',
    'I am being kissed by my neighbor\'s wife right now.',
    'My phone is being repaired now.',
    'The cake is being cut by him now.',
    'He is being scolded by his father.',
  ],
  'negative': [
    'The mountain will be getting covered with snow.',
    'Our house was still being built.',
    'I thought this computer was being made in Japan.',
    'The windows were closed by the students.',
    'The drinking water also had not been infected by the terrorists.',
    'English wasn\'t spoken by the members at the conference.',
    'She had killed mosquitoes.',
    'A party will be being held at this time tomorrow.',
    'The spectators had not been bored by the slow hockey game.',
    'Is the book being read by her?',
    'The book was not written by her.',
    'The house will be getting demolished by them tomorrow morning.',
    'She is liked by everyone.',
    'They had recorded our voices.',
    'The dishes were being washed by her at 7 p.m. yesterday.',
    'The car was used by him.',
    'The city had been defended by the brave men.',
    'That building was not demolished last year.',
    'A new shirt is not worn by you.',
    'The window was not broken by John.',
  ],
}
test_data_0743 = { 

      # **Guideword:** PRESENT CONTINUOUS, NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present continuous passive negative.
        
  'positive': [
    'I am not being kissed by my neighbor\'s wife.',
    'That movie isn\'t being watched by anyone.',
    'It is not being made by her.',
    'He isn\'t being scolded by his father.',
    'This conversation isn\'t being recorded.',
    'The book isn\'t being read at all.',
    'The cake isn\'t being cut by him.',
    'He is not being watched by many people.',
    'The computer is not being used by my family.',
    'It is not being decided by the government.',
  ],
  'negative': [
    'The mountain will be being covered with snow.',
    'The meeting will be being held at this time tomorrow.',
    'The window was not broken by John.',
    'They had recorded voice.',
    'The drinking water also had not been infected by terrorists.',
    'The book was not written by her.',
    'She had killed mosquitoes.',
    'The book is being read.',
    'Rock festival is being held by them.',
    'She is being watched by everyone.',
    'The spectators had not been bored by the slow hockey game.',
    'He is being fooled by her.',
    'My phone is being repaired now.',
    'English wasn\'t spoken by the students.',
    'The windows were closed by students.',
    'The city had been defended by the brave men.',
    'The spacecraft was being readied for launch.',
    'I thought this computer was being manufactured in Japan.',
    'The shop is being closed.',
    'A party will be being held at this time tomorrow.',
  ],
}
test_data_0744 = { 

      # **Guideword:** PRESENT PERFECT SIMPLE, AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present perfect passive affirmative form (often in the context of reporting).  ► reported speech
        
  'positive': [
    'I have been praised by my mother since I was a child.',
    'I have been obliged to keep secrets.',
    'We have been ordered to abstain from wine.',
    'They have been slapped by him recently.',
    'I have been drawn in by this band\'s music lately.',
    'I have been helped very often by Bill.',
    'The concert has been canceled.',
    'I have been told a lie by my best friend once.',
    'Dinner has been cooked by her.',
    'This song has been sung by a lot of singers.',
    #moved into positive test cases
    'Have you ever been bitten by a dog?',

  ],
  'negative': [
    'He is not being invited to come with us.',
    'He is not being scolded by his father.',
    'The meeting will be being held at this time tomorrow.',
    'I had been called Tom by everyone until I was twenty.',
    'English wasn\'t spoken by the students.',
    'Until his father came back he had been scolded by his mother.',
    'I had found my glasses, but I lost again.',
    'I am not being kissed by my neighbor\'s wife.',
    'They had recorded our voices.',
    'The spacecraft was being readied for launch.',
    'The shop is being closed.',
    'The rock festival is being held by them.',
    'The thief had already been arrested when we arrived there.',
    'He will have been scolded by his mother ever since he moved back.',
    'He is being fooled by her.',
    'This conversation is not being recorded.',
    'I had seen the bird.',
    'The computer is not being used by my family.',
    'The windows were closed by students.',
  ],
}
test_data_0745 = { 

      # **Guideword:** PRESENT PERFECT SIMPLE, NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present perfect passive negative form (often in the context of reporting). ► reported speech
        
  'positive': [
    'My bag hasn\'t been washed for a while.',
    'That movie hasn\'t been showed yet.',
    'My room has not been cleaned by my mother yet.',
    'My homework hasn\'t been finished yet.',
    'Your house hasn\'t been built yet.',
    'This wallet hasn\'t been used by my mother for a while.',
    'This shirt has not been worn for a month.',
    'This pen has not been bought for a long time.',
    'This cap hasn\'t been used for a week.',
    'I have not been scolded by anyone before.',
    'Hasn\'t the work been done yet?',
  ],
  'negative': [
    'I am not being kissed by my neighbor\'s wife.',
    'This conversation is not being recorded.',
    'The windows were closed by students.',
    'He is not being scolded by his father.',
    'Rock festival is being held by them.',
    'The thief had already been arrested when we arrived there.',
    'I have been praised by my mother since I was a child.',
    'I have studied English for three years.',
    'I have been to London three times.',
    'This song has been sung by a lot of singers.',
    'The computer is not being used by my family.',
    'He is not being invited to stay with us.',
    'Have you ever been bitten by a dog?',
    'They had recorded our voices.',
    'She hasn’t eaten anything since this morning.',
    'I have been helped very often by Bill.',
    'He is being fooled by her.',
    'English wasn\'t spoken among the other students.',
    'I have known Kenji for a long time.',
    'I haven’t played baseball for a week.',
  ],
}
test_data_0746 = { 

      # **Guideword:** WITH MODAL VERBS
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the passive with modal verbs in a range of contexts, with a variety of subjects.
        
  'positive': [
    'The house will be bought by Ken.',
    'It\'s my view that guns should be banned.',
    'The car must be bought by him.',
    'I think that it should be considered more.',
    'Students should be evaluated based on their actual skill.',
    'The fruits must be cut by him before dessert.',
    'The box may be opened by him.',
    'Good traditions should be preserved.',
    'Breakable articles should be packed carefully.',
    'Drunken driving should be severely punished.',
    'Should the house really be renovated right now?',
  ],
  'negative': [
    'They had recorded our voices.',
    'This wallet hasn\'t been used by my mother for a while.',
    'I have been helped very often by Bill.',
    'My father could run 50 meters in 6 seconds when he was a student.',
    'Susan can be lazy.',
    'Your house hasn\'t been built yet.',
    'I could practice more.',
    'Could you close the window?',
    'He is not being invited to stay with us.',
    'This song has been sung by a lot of singers.',
    'You can’t use your cellphone here.',
    'This shirt has not been worn for a month.',
    'Olivia can dance ballet very well.',
    'You can choose anything you like.',
    'The Giants can win this season.',
    'I could practice more but I didn’t.',
    'My older sister can’t swim.',
    'The computer is not being used by my family.',
    'My homework hasn\'t been finished yet.',
    'That movie hasn\'t been shown yet.',
  ],
}
test_data_0747 = { 

      # **Guideword:** WITH VERBS TAKING TWO OBJECTS, , WITH PREPOSITIONAL PHRASE
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the passive with a range of tenses and verbs needing two objects (e.g. give, offer, sell) with the direct object in subject position and the indirect object in a prepositional phrase. 
        
  'positive': [
    'A new job was offered to my sister by that company.',
    'This pocket watch was given to me by my uncle.',
    'The permission was given to us by our manager.',
    'The watch was sold to you by my son.',
    'The information was given to the police by the witness.',
    'A book was given to her by her students.',
    'This designer bag is sold to wealthy people at that shop.',
    'A carnation was given to his mother by him',
    'This expensive pen was sold to that boy by the swindler.',
    'Flowers are offered to the guests by the local flower shop.',
    'A letter was written to me by Mary.',
  ],
  'negative': [
    'Good traditions should be preserved.',
    'They had recorded voice.',
    'She\'s said to sing songs every morning.',
    'My homework hasn\'t been finished yet.',
    'That movie hasn\'t been shown yet.',
    'Students should be required to take an examination.',
    'A nice jacket was bought for Susan.',
    'A beautiful dress was made for me by my mother.',
    'It\'s my view that guns should be banned.',
    'Your house hasn\'t been built yet.',
    'You can choose anything you like.',
    'He was envied for his vast fortune.',
    'This wallet hasn\'t been used by my mother for a while.',
    'Breakable articles should be packed carefully.',
    'A book was bought for her by her students.',
    'You can’t use your cellphone here.',
    'The box may be opened by him only.',
    'This shirt has not been worn for a month.',
    'The child was called Tom by everyone.',
  ],
}
test_data_0748 = {

      # **Guideword:** WITH VERBS TAKING TWO OBJECTS.
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the passive with a wide range of verbs needing two objects, putting the indirect object in subject position. 
        
  'positive': [
    'She was offered a book by the publisher.',
    'He was given his fortune by his grandfather after his death.',
    'He was given the name Tom by everyone.',
    'I was offered a beautiful dress by my mother.',
    'The boy was sold this expensive pen.',
    'The police were given the information by the witness.',
    'I was offered the position by the lead engineer.',
    'Jack was awarded the title by the committee.',
    'His mother was given a carnation.',
    'The guests were sold flowers.',
  ],
  'negative': [
    'This wallet hasn\'t been used by my mother for a while.',
    'He was asked to use his pen by me.',
    'Your house hasn\'t been built yet.',
    'Breakable articles should be packed carefully.',
    'This shirt has not been worn for a month.',
    'English is spoken in Australia.',
    'You can’t use your cellphone here.',
    'The story was written by him ten years ago.',
    'That window was broken.',
    'That movie hasn\'t been shown yet.',
    'My homework hasn\'t been finished yet.',
    'You can choose anything you like.',
    'I was told not to lie.',
    'I was made to clean my room by my father.',
    'They had recorded our voices.',
    'The desk was made by my father.',
    'A new building will be built here.',
    'This story was not written by him.',
    'I saw her go into the building.',
    'This book is read by many people.',
  ],
}
test_data_0749 = {

      # **Guideword:** SUMMARIES AND EVALUATIONS
      # **Guideword type:** USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the passive with modal verbs to evaluate or summarise.
        
  'positive': [
    'To sum up, it could be seen on the chart.',
    'To conclude, the data must be corrected.',
    'In short, they should be organized better.',
    'To conclude, they must be done within a month.',
    'In conclusion, the investigation should be done by the government.',
    'In conclusion, it should be heard by everyone.',
    'To sum up, they must be calculated correctly.',
    'To sum up, they could be heard anytime.',
    'In conclusion, this can be all done by him.',
    'To conclude, it might be seen anywhere.',
    # moved to positive
    'This expensive pen will be sold to that boy.',
    'A new building will be built here.',


  ],
  'negative': [
    'She was amused at his joke.',
    'That window was broken.',
    'He was praised by the teacher.',
    'A beautiful dress was made for me by my mother.',
    'That movie hasn\'t been shown yet.',
    'My homework hasn\'t been finished yet.',
    'He was laughed at by everyone.',
    'The baby was amused with the new toy.',
    'We were surprised at the news.',
    'This story was not written by him.',
    'The story was written by him ten years ago.',
    'A book was bought for her by me.',
    'This material is used for his studies.',
    'Breakable objects are to be packed carefully.',
    'You can choose anything you like.',
    'A letter was written to me by Mary.',
    'He was envied for his vast fortune.',
    'I was told not to lie.',
  ],
}
test_data_0750 = { 

      # **Guideword:** WITH 'WILL', FUTURE REFERENCE
      # **Guideword type:** USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the passive with 'will' to talk about the future.
        
  'positive': [
    'You will be captured.',
    'The ground will be covered with snow in the winter.',
    'Dinner will be cooked by her tomorrow.',
    'This place will be visited by many people.',
    'This bed will be broken soon.',
    'The house will be bought by Ken.',
    'This house will be sold soon.',
    'We don\'t know on exactly which day the baby will be born.',
    'That bike will be brought to the park by him.',
    'A full moon will be seen this evening.',
  ],
  'negative': [
    'The newest building was built over there last month.',
    'My new book is brought by him.',
    'You may be disappointed.',
    'Breakable articles should be packed carefully.',
    'He was envied for his vast fortune.',
    'The story was written by him ten years ago.',
    'You have to be tested on your English grammar.',
    'He was laughed at by everyone.',
    'He was praised by the teacher.',
    'She was amused at his joke.',
    'We were surprised at the news.',
    'The baby was amused with the new toy.',
    'I expect to be surprised on my birthday.',
    'A letter was written to me by Mary.',
    'She wants to be invited to the party.',
    'The car can be bought by him.',
    'She was rescued by him.',
    'This story was not written by him.',
    'This material is used for his study.',
    'John might be promoted next year.',
  ],
}
test_data_0751 = { 

      # **Guideword:** NON-FINITE CLAUSES
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use a passive non-finite '-ing' form as a subordinate clause or a noun clause to give explanatory background information.
        
  'positive': [
    'Being swamped with work, I stayed at home.',
    'Being cursed with bad looks, I need to study hard.',
    'Being accused of the crime, I was in a difficult situation.',
    'Being awed by their charisma, the young man followed their direction.',
    'Being rewarded for my hard work, I was able to take a long vacation.',
    'Being informed aboutwhat and how much we eat is essential to good health.',
    'Being taken by surprise by the offer, we graciously accepted.',
    'Being stressed, he couldn\'t bring himself to ask her to go to the movies with him.',
    'Being charged by the forward, the keeper was injured.',
    # pos error
    # 'Being interested in pasta, I flew to Italy.',
  ],
  'negative': [
    'Evan is being invited by Dolly to visit Paige.',
    'Jack is not being taught how to use chopsticks',
    'You need to paint the whole cupboard, starting from the bottom.',
    'Pancakes are being made in the kitchen.',
    'Flowers are being grown in this garden.',
    'Messing with the teacher is a very bad idea.',
    'Closing this case was very difficult.',
    'Crossing the road alone is dangerous.',
    'This man is not being kept in prison because he did something very bad.',
    'She’s not being hugged by her brother.',
    'The bridge isn’t being painted by the workers.',
    'My sister is having her finger tested at the hospital.',
    'English is being learnt by him with the help of his teacher.',
    'Millie was not being heard at the court.',
    'Jumping around the room is an immature thing to do.',
    'The table is not being repaired by the carpenter.',
    'Tonight’s meeting is not being held in my office.',
    'Allowing her to take responsibility is probably a good idea.',
    'Are his teachers being shown great respect by Ethan?',
    'Penguins living in the Antarctic are being threatened by climate change.',
  ],
}
test_data_0752 = { 

      # **Guideword:** PRESENT CONTINUOUS NEGATIVE
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use the present continuous passive negative form to refer to ongoing situations in the present.
        
  'positive': [
    'The stories are not being written by her.',
    'She’s not being hugged by her brother.',
    'The song is not being sung by Louisa.',
    'Tonight’s meetings aren\'t being held in my office.',
    'The letter isn’t being written by my dad.',
    'Her brother isn’t being kept in the house.',
    'This man is not being kept in prison because he did something very bad.',
    'The table is not being repaired by the carpenter.',
    'The new book isn’t being torn by the cat.',
    'The bridge isn’t being painted by the workers.',
  ],
  'negative': [
    'Evan is being invited by Dolly to visit Paige.',
    'She is not counseling her son.',
    'To conclude, it had been a pleasure working with all of you.',
    'His autobiography is being written by him.',
    'Penguins living in the Antarctic are being threatened by climate change.',
    'He is being chosen their leader by the people.',
    'My bike is being repaired right now.',
    'In addition, it has been proven that infants cry for a reason.',
    'The German book is being read by the boy.',
    'All the books are being bought by her from his school.',
    'Ultimately, it can be mentioned that black is every generation’s favorite color.',
    'A cup of tea is being offered by Paul to Olive.',
    'Her father is being disturbed by Anna.',
    'Flowers are being grown in this garden.',
    'English is being learnt by him with the help of his teacher.',
    'Is your job being done by him right now?',
    'Are his teachers being shown great respect by Ethan?',
    'Pancakes are being made in the kitchen.',
    'We made it a rule to stay away from the garden.',
    'My sister is having her finger tested at the hospital.',
  ],
}
test_data_0753 = { 

      # **Guideword:** SUMMARISING, EVALUATING WITH 'IT'.
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** passives: form
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use the passive with 'it' as a dummy subject, to summarise or evaluate in discussions, usually in formal or academic writing.
        
  'positive': [
    'As a result, it has been shown that you can be fluent in multiple languages.',
    'To sum up, it was decided that it\'s alright to use a taxi every now and then.',
    'Moreover, it is strongly recommended that students not steal school property.',
    'Ultimately, it can be mentioned that black is every generation’s favorite color.',
    'Moreover, it had been suggested that there was already an underlying precedent for the revolution.',
    'In conclusion, it can be said that students prefer to use trains and buses.',
    'In addition, it has been proven that infants cry for a reason.',
    'As shown above, it is encouraged for young people to shop at a thrift store.',
    'To summarize, it is recommended that elderly people consult their doctor before riding the rollercoaster.',
    'In summary, it has been reported that young Japanese people are increasingly taking trips to Korea.',
  ],
  'negative': [
    'We need to get it fixed before the play starts.',
    'To conclude my presentation, I would like to play a short video.',
    'As a result, Liz and Tasha had to leave school early.',
    'It was your idea to go to Mexico.',
    'In addition, my mother was a doctor when she young.',
    'The cat took it away from me.',
    'My mother made a big deal out of it.',
    'Kate’s sister got sick from playing outside while it was snowing.',
    'Finally, the professor agreed to enroll me in his class.',
    'Her sister took it to the post office.',
    'Jack had it hidden in his bag pack.',
    'In conclusion, her initial plan proved to be a disaster.',
    'My father and I talked about it in depth.',
    'In summary, the elephants must be saved at all costs.',
    'At the end, the success of the play depends on good performance.',
    'Furthermore, the employees are not satisfied with their current working environment.',
    'Ultimately, there’s not much difference between these words.',
    'I got it done way before the deadline.',
    'We made it a rule to stay away from the garden.',
    'Moreover, I would like to thank you for your assistance.',
  ],
}
test_data_0754 = {

    # **Guideword:** NON-FINITE PERFECT CLAUSES
    # **Guideword type:** FORM/USE
    # **Super category:** PASSIVES
    # **Sub category:** passives: form
    # **Lexical Range:** None
    # **CEFR level:** C2
    # **CAN-DO:** Can use passive non-finite '-ing' perfect forms in subordinate clauses to give explanatory background information.

  'positive': [
    'Not having been stopped completely, the train continued past the platform.',
    'Having been robbed and destroyed by force and violence, I need a bodyguard.',
    'Having been demonstrated or verified beyond doubt, it should work perfectly.',
    'I myself, having been sent to jail, would never want to go back there.',
    'Having been infected with the flu, he rested at home.',
    'Having been inundated with money from a young age, she spends it freely.',
    'Having been warmed up, I started preparing for dinner.',
    'Having been frequently used, the microwave was broken.',
    'Having been swamped with homework, I wasn\'t able to go out.',
    #satisfied tagged as adjective
    # 'Not having been satisfied, she played the game again.',

    'I myself, having been educated the hard way, would specifically insist on them getting the best possible school education.',
    'Having been taught the difference betwen right and the wrong, we had an idea about everything.',
    'Not having been given precise orders from the top, as usual he decided to work on his own initiative.',
    'Having been shown blatantly practicing deception and hypocrisy, his word is now 100% worthless. ',
    'It really made me smile, having been married recently.',
    'Having been recognised for his services to rugby as part of the 2003 RWC winning team, no doubt it would be for his charity work.',
    'This story is well known, having been told before, in numerous sources relating to the Falklands War. ',
    'Having been told what he looks like, I should be able to track him down. ',
    'Having been told that the Mercedes has been impounded, the trio is released when they unknowingly volunteer to be targets for a taser demonstration. ',
    'Having been told this is rape, she then accused the man and he was arrested. ',
  ],
  'negative': [
    'He\'s been having trouble with back pain for years.',
    'I consider the object as having been attained.',
    'I’ve been having lunch with Mr. Smith.',
    'The bed bore no traces of having been slept in.',
    'There are signs of his having been strangled.',
    'We’ve been having good weather.',
    'I have been having a headache since this morning.',
    'Undoubtedly, she is hiding something.',
    'I have been having dreams about kissing you.',
    'He swore to having been there then.',
    'This tableware shows no signs of having been used.',
    'There are signs of the seal having been tampered with.',
    'I am having a hard time memorizing all the terms.',
    'She acknowledged having been defeated.',
    'He has been having dizzy spells for 3 weeks.',
    'There is no sign of the house having been broken into.',
    'Amanda is definitely running late.',
    'He definitely left the house this morning.',
    'He regretted having been idle.',
    'I\'ve been having some late nights recently.',

    'I have been working.',
    'I haven\'t decided yet.',
    'There has been a party this evening.',
    'Have you finished yet?',
    'I would have to finish that.',
    'But yet my tears unbidden fall.',
    'He has not come down yet.',
    'The driver has drunk a lot.',
    'I would not have been here.',
    'The exhibits are as yet incomplete.',
    'The evil is not yet suppressed.',
    'The money is not yet accounted for.',
    'Things have not yet been set right.',
    'He is not yet quite dead.',
    'You should have worked here.',
    'Why do you have to leave now.',
    'No news is currently traveling outside of that area.',
    'The time is not yet ripe.',
    'You could have changed your lifestype.',
    'The matter is not yet settled.',
    'He is not yet fifty.',
    'The particulars are not yet clear.',
  ],
}
test_data_0755 = {

  # **Guideword:** NON-FINITE PERFECT COMPLEMENTS
  # **Guideword type:** FORM
  # **Super category:** PASSIVES
  # **Sub category:** passives: form
  # **Lexical Range:** None
  # **CEFR level:** C2
  # **CAN-DO:** Can use non-finite '-ing' perfect forms of the passive as the complement of prepositions.

  'positive': [
    'The seal shows signs of having been tampered with.',
    'This tableware shows no signs of having been used.',
    'They were relieved after having been kept silent for so long.',
    'The bill was passed after having been debated at the plenary session.',
    'He has had his expenses stopped as punishment for having been caught breaking the law.',
    'The scene shows no trace of having been broken into.',
    'A fire broke out in the hut where there was no sign of having been started at any particular point.',
    'The bed bore no traces of having been slept in.',
    'He swore to having been attacked there then.',
    'This is a book printed after having been revised.',

    'They are expected to give the couple expensive presents as a reward for having been invited.',
    'We caught the bus as if we were escaping from Saigon, and with the sensation of having been rewarded with one of the funniest holiday evenings of our lives.',
    'Miss Kenton has just been employed as a housekeeper when she knocks on Stevens\' pantry door and comes in without having been bidden to do so, bringing a vase of flowers',
    'You should not come here without having been notified.',
    'One could consider Nagito\'s death as kind of unfair to us, without having been told previously that this could happen.',
    'But it is a very delicate social problem, and the US has avoided it by having been made an experienced immigrant country. ',
    'My point is less about this specific individual case and more about the general distrust they have earned by having been caught in bold faced lies. ',
    'I\'d say you\'re unlucky for having been robbed of one of the best fights in the game. ',
    'I really admire her for having been exposed in front of the public.',
    'For having been considered so sick, she\'s looks amazing. ',
  ],
  'negative': [
    'He denied having been involved in the affair.',
    'I\'ve been too upset to have written you a reply.',
    'Having done my homework, I went out.',
    'Having been convicted of murder, he was sentenced to life imprisonment.',
    'I\'ve been having some late nights recently.',
    'He regretted having been idle instead of working hard.',
    'I have been having dreams about kissing you.',
    'I have been having a headache since this morning.',
    'Having a lot of money, she spends it freely.',
    'She acknowledged having been defeated.',
    'I’ve been having lunch with Mr.Smith.',
    'I’ve been having terrifying dreams.',
    'His homework having been finished early, Tom went to bed.',
    'Having been written in haste, his letter was hard to read.',
    'We’ve been having good weather.',
    'She regrets having never been there.',
    'Having fallen ill, he rested at home.',
    'Not having been satisfied, she played the game again.',
    'He\'s been having trouble with back pain for years.',
    'Having been robbed and destroyed by force and violence, I need a bodyguard.',

    'Having been told this is rape, she then accused the man and he was arrested.',
    'I have been working.',
    'I haven\'t decided yet.',
    'There has been a party this evening.',
    'Have you finished yet?',
    'I would have to finish that.',
    'But yet my tears unbidden fall.',
    'He has not come down yet.',
    'The driver has drunk a lot.',
    'I would not have been here.',
    'The exhibits are as yet incomplete.',
    'The evil is not yet suppressed.',
    'The money is not yet accounted for.',
    'Things have not yet set right.',
    'He is not yet quite dead.',
    'You should have worked here.',
    'Why do you have to leave now.',
    'No news is held at hand.',
    'The time is not yet ripe.',
    'You could have changed lifestype.',
    'The matter is not yet settled.',
    'He is not yet fifty.',
    'The particulars are not yet at hand.',
  ],
}
test_data_0756 = {

      # **Guideword:** 'GET' + '-ED'
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can form the 'get'-passive with a range of forms of 'get' + past participles.
        
  'positive': [
    'We got lost in the woods.',
    'Our belongings almost got stolen.',
    'I always got lost at this street.',
    'I didn’t want any of them to get hurt.',
    'It got cracked somehow or other.',
    'The clock that got broken must be repaired right away.',
    'Because I left that on the floor, it got broken by my pet.',
    'I want to get started on this right away.',
    'The door got broken.',
    # parser cannot recognize married as verb correctly
    #'We’re getting married next month.',
  ],
  'negative': [
    'I\'ve got plenty of friends.',
    'The engineer got the car running again.',
    'Let’s get together at six.',
    'It’s getting dark.',
    'I got the engine run by solar energy.',
    'Once you get him going, he can talk for hours.',
    'We talked a lot but got nowhere in deciding what to do.',
    'We’d better get going before dark.',
    'You had better get ready.',
    'They can\'t get on together',
    'He can\'t get on with them.',
    'I hope you will get better soon.',
    'You have got to be kidding me.',
    'I got my parents to mind my dog while I was away.',
    'I will get my wife to pick me up at the station.',
    'We’ve been trying to get in touch with you.',
    'I will get older.',
    'I am going to get fat.',
    'If you want to get ahead, you must work harder.',
    'He got the machine working.',
  ],
}
test_data_0757 = { 

      # **Guideword:** 'GET' + REFLEXIVE PRONOUN + '-ED'
      # **Guideword type:** FORM
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use a reflexive pronoun with the 'get'-passive. 
        
  'positive': [
    'It was a long time before she could get herself attended to.',
    'He got himself committed because of his actions.',
    'She has never gotten herself noticed for her work.',
    'I wonder how I can get myself motivated again.',
    'He managed to get himself promoted last week.',
    'He contrived to get himself disliked.',
    'I\'d get myself checked by a doctor.',
    'Her other son, Masamura, did not get himself involved in the incident.',
    'They could get themselves killed if they try that again.',
    'His luck finally ran out and he got himself arrested.',
  ],
  'negative': [
    'I can\'t get myself to do anything today because I\'m tired.',
    'He got himself a car.',
    'She got herself a cup of coffee.',
    'She got herself up the mountain.',
    'I am tired, so I can\'t get myself up early in the morning.',
    'You should get yourself a new car now.',
    'He got himself into the university through hard work.',
    'We often get ourselves into trouble when we are determined to have our own way.',
    'Feel free to get yourself a drink if you are thirsty.',
    'He couldn\'t get himself up the stairs.',
    'She got herself a nice dress.',
    'He got himself a new bag.',
    'How did you get yourself into this mess?',
    'Why don\'t you get yourself a decent house?',
    'She get herself up too early in the morning.',
    'He dressed himself up as Santa Claus.',
    'I still cannot get my feelings back under control.',
    'You got yourself a nice guy.',
    'He got himself into trouble.',
    'You got yourself into this mess.',
  ],
}
test_data_0758 = { 

      # **Guideword:** 'HAVE' + OBJ + '-ED', PROACTIVE PASSIVE
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use have + object + -ed to talk about something where the speaker is in a pro-active or a passive role.
        
  'positive': [
    'I had my manuscripts typed.',
    'I just had my hair permed.',
    'I must have the wall fixed before it snows.',
    'I need to have the document verified by the government.',
    'I will have a new dress tailored for my birthday party.',
    'We have our office cleaned every weekend.',
    'I had my car washed.',
    'I had a wallet stolen in the subway.',
    'I had my hair cut yesterday.',
  ],
  'negative': [
    'I tried my best to make myself understood in Japanese.',
    'The baby had everyone in the room laughing.',
    'I won\'t have him saying such things about her.',
    'I can’t have you dating this terrible man.',
    'The word made me sad.',
    'You make me happy.',
    'The teacher had us clean up the classroom.',
    'Peter had his wife take care of him.',
    'My mother had me clean my hands.',
    'She had the doctor check her leg.',
    'We had him report to the general.',
    'I had my brother paint the wall.',
    'We had him report.',
    'He had the doctor look at his arm.',
    'Because I had a cold, I had my mother take me to the hospital.',
    'My boss had me work overtime again.',
    'Her mother had her playing the piano.',
    'Do you want to make me mad?',
    'My teacher had me repeating the phrase until I mastered it.',
    'The widow had two husbands die.',
    'Misa had the engineer repair her car.',
  ],
}
test_data_0759 = { 

      # **Guideword:** 'GET' + OBJECT + 'TO'-INFINITIVE
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'get' + object + 'to'-infinitive to talk about causing someone to do something. 
        
  'positive': [
    'How did you get Tom to clean his room?',
    'I got my friend to cook dinner for us.',
    'Joan got her husband to buy her a big diamond ring.',
    'I got her to stop smoking.',
    'I got him to help me with my homework.',
    'How did you get him to pose for this picture?',
    'We got the doctor to come.',
    'I got him to do the work.',
    'She got me to mow the lawn.',
    'We couldn\'t get him to sign the agreement.',
  ],
  'negative': [
    'I got this letter translated into English.',
    'I got my shoes polished.',
    'I must have the wall fixed before it snows.',
    'I tried my best to make myself understood in Japanese.',
    'Please get the job done as soon as possible.',
    'Don’t get me wrong.',
    'Because I had a cold, I had my mother take me to the hospital.',
    'We have to get the contract signed today.',
    'I need to get my air conditioner fixed.',
    'Her mother had her playing the piano.',
    'I got my left leg broken while I was skiing.',
    'I\'ll get everything done.',
    'The teacher had us clean up the classroom.',
    'My boss had me work overtime again.',
    'We had him report to the general.',
    'I must get my room cleaned before Mom gets home.',
    'I won\'t have him saying such things about her.',
    'The widow had two husbands die.',
    'I just had my hair permed.',
    'The accident got Kevin fired.',
  ],
}
test_data_0760 = { 

      # **Guideword:** 'GET' + OBJECT + '-ED'
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'get' + object + '-ed' to talk about causing or instructing something to happen or to be done by somebody else, often informally. 
        
  'positive': [
    'Melissa got it examined by a doctor.',
    'We need to get it fixed before the play starts.',
    'She got her shoes cleaned by my father.',
    'I got it done way before the deadline.',
    'He got his phone repaired at the mall.',
    'She got her hair cut by her mom.',
    'They had gotten their daughter transferred to a new school.',
    'She got them finished while her mother was in the shower.',
    'She was getting her boots delivered to her on time.',
    'They got their throats tested at the health center.',
  ],
  'negative': [
    'She caught them fishing by the lower lake.',
    'The music got the students dancing in the classroom.',
    'My cat got stuck between the walls.',
    'He got me into horse riding last summer.',
    'I can’t get that child to go to bed.',
    'The cook got burnt in the kitchen.',
    'Once we got the heater going the car started to warm up.',
    'My daughter’s letter got me crying so hard.',
    'Our guide suggested waiting until the storm was over.',
    'The fire got the staffs running around the building.',
    'I opened the storeroom and found that we had mice running around the cabinets.',
    'Get Penny to help us if she can.',
    'Everyone denied seeing the accident.',
    'My father had gotten stuck in the traffic.',
    'Kate’s sister got sick from playing outside while it was snowing.',
    'My umbrella got caught in the mud.',
    'Our mother gets tired of cleaning the house every day.',
    'We got expelled for playing with fire.',
    'For one moment, he got me believing that he had aced his thesis.',
    'I got a call from one of my colleagues.',
  ],
}
test_data_0761 = { 

      # **Guideword:** 'GET' + OBJECT + '-ING'
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'get' + object + '-ing' to talk about causing someone or something to do something.
        
  'positive': [
    # I am not sure if the dependencies is right.
    # 'Don’t get him talking about his illness.',
    # dependencies error
    # 'Once we got the heater going the car started to warm up.',
    'The accident got me thinking about my grandmother.',
    'The lecture got me sleeping and snoring.',
    'For one moment, he got me believing that he had aced his thesis.',
    'The fire got the staff running around the building.',
    'The beer got me feeling crazy.',
    'Olivia got me thinking about my niece in Paris.',
    'The music got the students dancing in the classroom.',
    'My daughter’s letter got me crying so hard.',
  ],
  'negative': [
    'I need to get that dog to stay in his bed.',
    'Do you mind me being here while you’re working?',
    'I can’t get that child to go to bed.',
    'He got me interested in horse riding last summer.',
    'I won’t have you smoking in my presence.',
    'The teacher had the bro recite the poem.',
    'Now that the winter is over, it is lovely to have kids playing in the garden again.',
    'We have never had customers complain about the quality of our products.',
    'Our guide suggested waiting until the storm was over.',
    'Get Penny to help us if she can.',
    'Everyone denied seeing the accident.',
    'I opened the storeroom and found that we had mice running around the cabinets.',
    'I can hear people talking in the background.',
    'Had we been told you were leaving, we would have help a farewell party.',
    'I don’t want to risk him losing his job.',
    'See if you can get the car to start.',
    'She won’t have him telling her what she should do.',
    'He had me washing his car.',
    'I wouldn’t mind having some fish and chips.',
    'Emily and Emanuel had us literally crying with joy.',
  ],
}
test_data_0762 = { 

      # **Guideword:** 'HAVE' + OBJECT + INFINITIVE
      # **Guideword type:** FORM/USE
      # **Super category:** PASSIVES
      # **Sub category:** get and have
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'have' + object + infinitive without 'to' to talk about asking or causing someone to do something, often in formal contexts.
        
  'positive': [
    'I could have him talk about his research in Switzerland.',
    'I must have them introduce themselves first.',
    'We must have them bring their own shoes.',
    'I should have them do all the work for me.',
    'We had her play the piano in the play.',
    'I will have him ride the bus.',
    'I must have her send us the cover letter.',
    'The teacher will have her go home early because of her illness.',
    'You shouldn’t have her wait outside.',
    'You should have her give the speech in Korean.',
    #moved from negatives
    #'I want to have her and Sophia meet sometime.',

  ],
  'negative': [
    'Why have you gone to the store without me?',
    'Have you done what I asked you to do?',
    'Her labor pains have quickened.',
    'We got them to celebrate my birthday.',
    'I need him to bake me some brownies.',
    'I got them to recite a piece for me.',
    'They got her to fix their computer.',
    'I need them to practice at least twice a week.',
    'They need him to calculate the numbers.',
    'I have sent her home to rest and enjoy time with families.',
    'She needs to let them take a break.',
    'Hanako is set to have her baby next month.',
    'Let her have everything her own way.',
    'I want to have her go.',
    'I have always wanted a hamster as a pet.',
    'She cannot have her own way out of regard for her mother-in-law.',
    'I have never met anyone more beautiful.',
    'All her hopes have vanished.',
    'I have no recollection of meeting her.',
    'I have persuaded her to get married.',
    'I still have some feelings for her.',
    'I always had a good time when I was with Gregor.',
  ],
}
test_data_0763 = { 

      # **Guideword:** AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the affirmative form. 
        
  'positive': [
    'The children were doing their homework when I got home.',
    'My head was aching when I was at school.',
    'My hair was going grey.',
    'Caroline was skiing when she broke her leg.',
    'When the fire started, I was watching television.',
    'They were meeting secretly after school.',
    'The sun was shining every day that summer.',
    'They were waiting for the bus when the accident happened.',
    'When we arrived, he was having a bath.',
    'The children were growing up quickly.',
    'It wasn’t snowing while we were playing tennis this morning.',
  ],
  'negative': [
    'They were not having a good time at the party when they decided to go home.',
    'She wasn’t listening to her teacher when he asked a question.',
    'Twenty countries are attending the conference.',
    'We should buy a wedding gift for our teacher.',
    'We were not carrying an umbrella when it started to rain.',
    'She wasn’t attending class properly in those days.',
    'Jim wasn’t playing the trumpet last night.',
    'It wasn’t snowing while we played tennis this morning.',
    'Harry wasn’t watching television at 8 o’clock last night.',
    'I wasn’t making dinner when she arrived.',
    'You weren’t playing cards when he rang.',
    'You shouldn’t play with your fingers while talking to an adult.',
    'Jill wasn’t wearing her uniform at work yesterday.',
    'Brian should take more risks in order to succeed.',
    'Jake and Amy were not eating rice.',
    'He shouldn’t be able to solve that math problem.',
    'I am discussing the contract with my colleagues.',
    'They were not watching a film during class.',
    'The girls sitting over there are my enemies.',
    'Anna wasn’t eating lunch when we called her.',
  ],
}
test_data_0764 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use the past continuous with a limited range of adverbs in the normal mid position. 
        
  'positive': [
    'They were just reading books.',
    # parser recognizes this sentence as a copula.
    # 'They were weekly reading books.',
    'I was probably studying at that time.',
    'I was often watching TV while I was in my room.',
    'He was constantly doing his homework.',
    'He was always playing baseball when I saw him.',
    'You were occasionally studying English when my friends visited you.',
    'We were just eating dinner at that time.',
    'You were always complaining about others.',
    'She was often running when I went to the park.',
    'They were only getting back home when I arrived.',
    'He was always walking to school.',
  ],
  'negative': [
    'What were you doing at 9 AM today?',
    'He was reading when he got an e-mail.',
    'I was sleeping at 11 PM last night.',
    'I was watching TV when the telephone rang.',
    'I was reading a book on the plane.',
    'Who were you talking to when I saw you?',
    'It was raining when I left school.',
    'He is always watching football matches.',
    'What book were you reading when she got home?',
    'Were you listening to music when I got home?',
    'I was playing basketball last night.',
    'He was driving a car.',
    'I was helping my mother.',
    'I was wondering about that the whole time.',
    'I was watching TV around noon.',
    'She was waiting for him.',
    'I was playing the piano then.',
    'They were not listening to me at all when I spoke.',
    'He was not watching me when I looked at him.',
    'Was she working at 10 AM yesterday?',
  ],
}
test_data_0765 = { 

      # **Guideword:** BACKGROUND EVENTS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the past continuous to show that an event was happening in the background to the main event.
        
  'positive': [
    'She was studying when I left home this morning.',
    'She was dating another guy when we saw her.',
    'Mike arrived here while we were watching the show.',
    'When we were out, my parents were cooking them.',
    'Were you listening to music when I got home?',
    'You were reading a book when I went shopping.',
    'He was studying when I entered the room.',
    'When you were in the park, we were practicing with the hoop.',
    'She fell asleep while she was reading a book.',
    'He was playing baseball when I asked him to go out.',
    # 'They were not listening to me at all when I spoke.',
    # listening->spoke(dep)
    'I was sleeping when you called me.',
    'He was not watching me when I looked at him.',
  ],
  'negative': [
    'She was not studying English.',
    'I\'m watching the TV show.',
    'You were carrying this bag.',
    'I\'m going to the school.',
    'You were studying English.',
    'It was raining outside.',
    'I was calling my friend.',
    'You were walking in the park.',
    'You were going somewhere else.',
    'He was doing his homework.',
    'I was playing basketball last night.',
    'What are you writing?',
    'I was doing my homework then.',
    'He was playing baseball.',
    'You were reading a book then.',
    'I was watching TV around noon.',
    'We were listening to music.',
    'She was visiting Britain.',
    'I was watching TV.',
    'I was studying at the library.',
  ],
}
test_data_0766 = { 

      # **Guideword:** EVENTS IN PROGRESS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the past continuous to talk about actions and states in progress around a particular time in the past.
        
  'positive': [
    'Mike arrived here when we were watching the show.',
    'While you were in the office, she was eating Japanese foods.',
    'When we were out, my parents were cooking them.',
    'It was raining while I was in the school.',
    'I was living aboard a boat in 1995, when the economy was better.',
    'Were you listening to music when I got home?',
    'While you were sick, I was reading a book.',
    'I was going shopping while you were at my house.',
    'When I was in my room, my friends were going shopping.',
    'When you were in the park, we were practicing with the hoop.',
    'You were reading a book when I went shopping.',
    'She fell asleep while she was reading a book.',
    'He was studying when I entered the room.',
    # 'They were not listening to me at all when I spoke.',
    # parser: listening->spoke(dep)
    'I was sleeping when you called me.',
    'When I was in the hospital, they were playing baseball.',
    'She was playing baseball while I was outside.',
    'He was not watching me when I looked at him.',
    'I was living aboard in 1995.',
    'I was watching TV around noon.',
    'I was playing basketball last night.',
  ],
  'negative': [
    'She was not studying English.',
    'You were carrying this bag.',
    'John is taking a nap.',
    'You were studying English.',
    'It was raining outside.',
    'I was watching TV.',
    'He\'s always asking silly questions.',
    'I was calling my friend.',
    'I am reading Shakespeare.',
    'You were going somewhere else.',
    'I walked eastward for two hours.',
    'He was doing his homework.',
    'You were reading a book.',
    'I was doing my homework.',
    'He was playing baseball.',
    'When I was young, I used to go to the park.',
    'I went to work by bus.',
    'I was studying at the library.',
  ],
}
test_data_0767 = { 

      # **Guideword:** NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the negative form.
        
  'positive': [
    'You weren’t reading a book then.',
    'I wasn\'t using the computer.',
    'She was not studying English.',
    'He was not cutting paper.',
    'I was not studying at that time.',
    'Yumi was not studying then.',
    'Kumi and I weren\'t watching TV then.',
    'We were not playing baseball then.',
    'Yui wasn\'t singing a song then.',
    'I was not eating a sandwich.',
  ],
  'negative': [
    'I was doing my homework then.',
    'You were studying English.',
    'What were you doing at ten last night?',
    'They were studying English then.',
    'Was he eating breakfast at that time?',
    'Won\'t you be cooking in the kitchen then?',
    'Who is playing the piano?',
    'What were you doing?',
    'Were you reading a book then?',
    'They were playing soccer then.',
    'I was watching TV around noon.',
    'She was reading a letter.',
    'Were you walking in the park?',
    'Where were they playing tennis then?',
    'He was playing baseball.',
    # should be positive since this is a negtive sentence
    #'She is not visiting Britain.',
    'He was running then.',
    'It was raining when I left school.',
    'I was playing basketball last night.',
    'What were you studying?',
  ],
}
test_data_0768 = { 

      # **Guideword:** QUESTIONS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the question form.
        
  'positive': [
    'Was she working at 10AM yesterday?',
    'What were you doing at ten last night?',
    'Were you listening to music when I got home?',
    'What book were you reading when she got home?',
    'Was he eating breakfast at that time?',
    'Where were they playing tennis last week?',
    'Were you walking in the park?',
    'Were you reading a book then?',
    'Who were you talking to when I saw you?',
    'Were you cooking in the kitchen then?',
  ],
  'negative': [
    'You were studying English.',
    'Kumi and I weren\'t watching TV then.',
    'She was reading a letter.',
    'He wasn\'t washing his car.',
    'We weren\'t waiting for the bus.',
    'Yumi was not studying then.',
    'I was sleeping at 11PM last night.',
    'They were not listening to me at all when I spoke.',
    'He was playing baseball.',
    'They weren\'t studying history.',
    'I wasn\'t watching TV yesterday.',
    'He was not watching me when I looked at him.',
    'She was visiting Britain.',
    'He was not cutting paper.',
    'The girl wasn\'t running in the park yesterday morning.',
    'I was not eating a sandwich.',
    'I was not studying at that time.',
    'He was not enjoying the club activity.',
    'I was doing my homework then.',
    'She fell asleep while she was reading a book.',
  ],
}
test_data_0769 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past continuous with an increasing range of adverbs in the normal mid position. 
        
  'positive': [
    'The girl wasn\'t seriously running in the park yesterday morning.',
    'He was still playing baseball at that time.',
    'I was surely sleeping at 11PM last night.',
    'I was not obviously eating a sandwich when you arrived.',
    'He was not still enjoying the club activity at that moment.',
    'I was actually doing my homework then.',
    'She was probably reading a letter last night.',
    'I wasn\'t exactly watching TV yesterday.',
    'She was possibly visiting Britain then.',
    'You were often studying English before, what happened?',
  ],
  'negative': [
    'Was she working at 10AM yesterday?',
    'At 6:00 last night, we were having dinner with our close friend.',
    'Who were you talking to when I saw you?',
    'Were you sleeping when I called you last night?',
    'Yumi was not studying then.',
    'My son told me that he saw a jelly fish while he was walking on the beach.',
    'He was not watching me when I looked at him.',
    'Who were you talking to on the phone?',
    'He was not cutting paper.',
    'Why were they having dinner without their children last night?',
    'I was talking to my mom.',
    'Was she all right when you arrived home this morning?',
    'What book were you reading when she got home?',
    'What was Ken doing at the outside at 7 last night?',
    'She fell asleep while she was reading a book.',
    'I was reading a book when you called me last night.',
    'I was not studying at that time.',
    'They were not listening to me at all when I spoke.',
    'They weren\'t studying history.',
    'Kumi and I weren\'t watching TV then.',
  ],
}
test_data_0770 = { 

      # **Guideword:** REASON
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past continuous to give a reason for something, often with 'because'.
        
  'positive': [
    'She was not there because she was shopping.',
    'I could not go to play baseball since I was taking care of my mother.',
    'Since she was taking exams, she was not here at that time.',
    'Since she was talking with her boyfriend, my friend got sad.',
    'My mother was busy because she was talking with my teacher.',
    'You could not be here since you were doing your own business.',
    'I was not busy at that time because I was playing a video game.',
    'I didn\'t like them because they were always complaining.',
    'He could not talk with you since you were speaking with someone.',
    'Because I was doing my homework, I could not go to the party.',
  ],
  'negative': [
    'I was surely sleeping at 11PM last night.',
    'Yesterday at this time, I was sitting at my desk at work.',
    'I wasn\'t necessarily watching TV yesterday.',
    'The girl wasn\'t seriously running in the park yesterday morning.',
    'What were you doing when you broke your leg?',
    'He was not still enjoying the club activity at that moment.',
    'Was she all right when you arrived home this morning?',
    'When the accident happened, I was also in town.',
    'They weren\'t studying history.',
    'I hoped you had a job.',
    'Paul was waiting for us when we got off the plane.',
    'I was not obviously eating a sandwich when you arrived.',
    'I was studying when Anna called.',
    'My girlfriend was making dinner while I was studying.',
    'They were eating dinner, gossiping, and having a good time.',
    'Yumi was not studying then.',
    'What was Ken doing at the outside at 7 last night?',
    'She fell asleep while she was reading a book.',
    'When the phone rang, I was in the middle of cooking.',
    'While Mary was sleeping last night, someone stole her car.',
  ],
}
test_data_0771 = { 

      # **Guideword:** REPEATED EVENTS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past continuous to talk about ongoing repeated events in the past, often with 'always'.
        
  'positive': [
    'He was always watching TV.',
    'She was always talking with Kumi at school.',
    'You were always complaining about others.',
    'Ken was always crying when he was a child.',
    'He was always making careless mistakes.',
    'He was always studying before, but now he is watching TV all the time.',
    'We were always running along the river in those days.',
    'I was always eating too much.',
    'My sister was always playing outside when he was a kid.',
    'She was always eating when she was a kid.',
  ],
  'negative': [
    'I’ve always wanted to go to Machu Picchu.',
    'He is always doing a good turn for someone.',
    'We were buying a new PC last week.',
    'I always have cash on me.',
    'The baby is just learning to walk and she\'s always tumbling over.',
    'My mother always gets up at six.',
    'He\'s always asking silly questions.',
    'He is always drinking too much.',
    'I\'m always doing my best.',
    'My husband is always losing his phone.',
    'My mom\'s always telling me to scrub my hands.',
    'You’re always playing computer games.',
    'She’s always complaining about her job.',
    'I always walk to work.',
    'I was watching TV when my mother came home.',
    'He is always sleeping in the class.',
    'I’ll always love you.',
    'Mr. Kato was talking on the phone a little while ago.',
    'I was reading a book all day long yesterday.',
    'I always play computer games when I have free time.',
  ],
}
test_data_0772 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** 3.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past continuous with a wide range of adverbs in the normal mid position.
        
  'positive': [
    'You weren\'t actually truly being serious, right?',
    'I was personally expecting more people over there since that movie is so popular.',
    'We were obviously studying for an exam.',
    'It was certainly raining outside.',
    'I was probably reading a book when you called me last night.',
    'I was maybe doing my homework then.',
    'I was luckily playing basketball last night.',
    'Mike was possibly cooking in the kitchen.',
    'It was unfortunately raining when I left school.',
    'He was perhaps studying when I entered the room.',
    'You were seriously studying English.',
    'I was personally expecting more people over there since that movie is so popular.',

  ],
  'negative': [
    'You weren’t reading a book then.',
    'At 6:00 last night, we were having dinner with our close friend.',
    'They were not studying English at that time.',
    'They were running in the park then.',
    'Was he sleeping at that time?',
    'We were listening to music.',
    'Who was playing the piano?',
    'I was playing the guitar then.',
    'She was visiting Britain.',
    'Where was Yumi going?',
    'He was playing baseball.',
    'I was watching TV then.',
    'They were studying English then.',
    'You were walking in the park.',
    'What were you studying?',
    'She was talking on the phone.',
    'I was playing very well.',
    'Were you watching TV then?',
    'My son told me that he saw a jelly fish while he was walking on the beach.',
  ],
}
test_data_0773 = { 

      # **Guideword:** POLITENESS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past continuous to make a request or suggestions more polite or less direct.
        
  'positive': [
    'I was wondering if you could give me a lift.',
    'I was thinking that you could stay with us.',
    'I was wondering if you\'d like to join me for dinner tomorrow.',
    'I was thinking that you could do it for me.',
    'I was thinking that you could play baseball with us.',
    'I was wondering if you could do me a favor.',
    'I was thinking that you could go to the party with me.',
    'I was wondering if you\'d like to come with us.',
    'I was wondering if you could help us.',
    'I was thinking that you could drink as much as you want.',
    'I was hoping you could do it for me.',
    'I was hoping to borrow the car.',
  ],
  'negative': [
    'I wonder what happened.',
    'I wonder what\'s wrong.',
    'I wonder if I\'m going to die.',
    'He was perhaps studying when I entered the room.',
    'They were studying English then.',
    'I was luckily playing basketball last night.',
    'They were running in the park then.',
    'Who was playing the piano?',
    'I was playing the guitar then.',
    'He wondered who would show up at his party.',
    'She was talking on the phone.',
    'I was watching TV then.',
    'Mike was possibly cooking in the kitchen.',
    # very slightly ambiguous
    # 'I was personally expecting more people over there since that movie is so popular.',
    'You were seriously studying English.',
    'I wonder if it is true.',
    'What were you studying?',
    'Where was Yumi going?',
    'At 6:00 last night, we were having dinner with our close friend.',
    'I wonder if this book will sell.',
  ],
}
test_data_0774 = { 

      # **Guideword:** UNDESIRED EVENTS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past continuous
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use the past continuous with 'always' or 'constantly' to talk about repeated events which are undesired or uncontrolled. 
        
  'positive': [
    'I was always reading books with my mother.',
    'She wasn’t always listening to music.',
    'I was always having a good time when I was with Gregor.',
    'He wasn’t always using his phone at the table.',
    'I was constantly dreaming about food.',
    'They were constantly asking my dad questions.',
    'I was always playing the piano when I was young.',
    'I was constantly relaxing in high school.',
    'I wasn’t constantly playing with boys!',
    'We were constantly playing video games in his room.',
  ],
  'negative': [
    'I will always be there for you when you need me.',
    'I am constantly dealing with the urge to drink coffee.',
    'Why am I constantly stressed out?',
    'I have always wanted a hamster as a pet.',
    'There had been a bank here for as long as I can remember.',
    'What had they been looking for?',
    'The issue is constantly on the Prime Minister\'s mind.',
    'You had better start writing your application form.',
    'Where had she been this autumn?',
    'Why do you constantly text with your friends?',
    'She had been in rehabilitation for a long time.',
    'He\'s constantly being asked to make speeches.',
    'Kate is always talking bad about other people.',
    'She is always trying to do her best.',
    'What had Liz been doing to keep her mind off the accident?',
    'She is constantly changing her mind.',
    'Why had George been showering for an hour?',
    'We are always willing to help with your art project.',
    'She always complains about the food at the cafeteria.',
    'Why has he been watching movies all day when he has a test tomorrow?',
  ],
}
test_data_0775 = { 

      # **Guideword:** AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the affirmative form. 
        
  'positive': [
    'I had been enjoying a cup of coffee in the coffee shop for two hours when she appeared.',
    'His illness had been worsening for a week before he consulted the doctor.',
    'I recognized him at once, as I had been seeing him in my dreams for years.',
    'We had been dating for years before we decided to get married.',
    'He had been working as a politician for thirty-five years when he decided to retire.',
    'I had been living abroad before I moved back to start a business.',
    'I had been loving what the singer produced before the big label hired her.',
    'She had been receiving marriage proposals regularly for weeks before she turned twenty.',
    'We had been living there for many years till we moved to Kyoto.',
    'Before the age of 25, she had been traveling all over the world.',
  ],
  'negative': [
    'She has already read the book.',
    'He has visited Sydney once before.',
    'I have just finished my homework.',
    'Tom has not been outside of Canada.',
    'He has recently returned from Tokyo.',
    'She has already left home.',
    'Kate has watched that DVD many times.',
    'He has been awarded prizes more than ten times.',
    'I have lost my way in the woods before.',
    'She has just stopped crying.',
    'I haven’t checked the train schedule yet.',
    'The Hollywood star has never disappointed me as an actor.',
    'Has Akiko had a dog before?',
    'We haven’t cleaned the bathroom yet.',
    'I have met him before.',
    'The train has just arrived at the station.',
    'I have lost the watch.',
    'He has recently published a book.',
    'Have you boiled some broccoli yet?',
    'Have you ever written a poem?',
  ],
}
test_data_0776 = { 

      # **Guideword:** BACKGROUND EVENTS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past perfect continuous talk about a background action or event which began before a point in the past and was still continuing up to a point in the past when the main event happened. 
        
  'positive': [
    'I had been leaving my books on top of my desk, until I changed my habits after my coworker spilled coffee on them.',
    'Before he abruptly left, he had been talking my ear off.',
    'I had been earning much less money before switching to this job.',
    'Roy had been working for hours when Bob flung open the door.',
    'I had been using the eraser I bought the day before constantly until I lost it somewhere.',
    'I had been reading this book for the past couple weeks, until I left it somewhere.',
    'I lost the contact lenses I had been using up until then.',
    'I had been searching everywhere for the eraser I lost yesterday until I finally found it this morning.',
    'My uncle had been using that watch that I gave him, until somebody stole it.',
    'I had been drinking my coffee leisurely, before she showed up and ruined everything.',
  ],
  'negative': [
    'My grandfather has been dead for two years.',
    'Kate has been watching that DVD since she was a child.',
    'Has Akiko had a dog before?',
    'He has recently published a book.',
    'He had been awarded prizes more than ten times.',
    'They’ve been dating for five years.',
    'She has just stopped crying.',
    'The Hollywood star has never disappointed me as an actor.',
    'My brother has been having a toothache for three days.',
    'I haven’t checked the train schedule yet.',
    'Tom has not been outside of Canada.',
    'They have lived here for seven years.',
    'My father has been working at the bank since 2000.',
    'I haven’t smoked for over two years.',
    'I have been busy since this morning.',
    'She hasn’t had a bite of bread since yesterday.',
    'The train had just arrived at the station.',
    'The boy has been wanting a dog for a long time.',
    'I’ve known her since she was just a kid.',
    'Have you boiled some broccoli yet?',
  ],
}
test_data_0777 = { 

      # **Guideword:** CONTINUING EVENTS IN THE PAST
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past perfect continuous to talk about an action or event which began before a point in the past and was still continuing up to that point, often with 'for' or 'since', to give background information. 
        
  'positive': [
    'Professor Collins had been acting as chairperson of the department for ten years before he went to France.',
    'He had been serving as a politician for thirty-five years when he decided to retire.',
    'They had been seeing each other for ten years when they got married.',
    'I had been dating him for 3 years when we got married.',
    'I had been staying in England for a year before I came to Japan.',
    'I had been living in Japan for two years before I went to America.',
    'He hadn’t been eating anything for three days, but he looked strong and healthy.',
    'I had been working in the coffee shop for two hours when she appeared.',
    'She had been living in Tokyo for two years when I first met her.',
    'He had been feeling ill for a week when he consulted the doctor.',
  ],
  'negative': [
    'I lost my eraser I had bought the day before.',
    'The Hollywood star had never disappointed me as an actor until now.',
    'She had been getting marriage proposals before she turned twenty.',
    'I lost the contact lenses I had been using.',
    'Until I ate Russian food at the party, I had never tried it before.',
    'I have been traveling abroad since I was twenty.',
    'Before the age of 25, she had been living in five different countries.',
    'He had never tried natto before he came to Japan.',
    'She hasn’t had a bite of bread since yesterday.',
    'I spent more money than I had expected.',
    'He showed me the pictures that he had taken there.',
    'I had never spoken to a foreigner before I entered college.',
    'They’ve been married for five years.',
    'He had been awarded prizes more than ten times.',
    'I had never talked with her before that time.',
    'I recognized him at once, as I had seen him before.',
    'She had never seen snow till she visited Hokkaido.',
    'Tom has not been outside of Canada.',
    'I haven’t smoked for over two years.',
    'Kate will have watched that DVD for 10 years.',
  ],
}
test_data_0778 = { 

      # **Guideword:** BACKGROUND INFORMATION WITH RELATIVE CLAUSE
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect continuous in a relative clause to give background information.  ► relative clauses
        
  'positive': [
    'The fire dealt a serious blow to the townspeople who had been supporting the economy in Kyoto.',
    'The chair was still warm from the person who had been sitting there before me.',
    'Chogen, who had been soliciting contributions during the Bunji era, faced new problems.',
    'It was the Fudai Daimyo, who had been serving the Tokugawa clan before the Battle of Sekigahara.',
    'At that time, he captured Ekei Ankokuji who had been hiding in Kyoto.',
    'The brothers who had been fighting over their inheritance finally made peace.',
    'The duke, who had been walking slowly, stood quite still.',
    'The criminal fooled the detective who had been watching his apartment.',
    'Tokihiro Yamana, who had been serving the bakufu, entered the battle with 50 cavalrymen.',
    'Tom, who had been working all day, wanted to have a rest.',
  ],
  'negative': [
    'Moreover, it got Tatsuya Masushima, who had been on loan, as a permanent empolyee.',
    'Today I met someone who had been my boss until last year.',
    'The ones who had been sent were from the Pharisees.',
    'The fishing boat had been drifting for five days when it was found.',
    'I hadn\'t been reading this book till my teacher told me to.',
    'They had believed her till she told a lie.',
    'My brother had been living only on water when the search party found him.',
    'I had lived in Japan for two years before I went to America.',
    'There was someone who had been bullied in my group of friends.',
    'He had been playing in the park till it got dark.',
    'I had been studying English for two hours before he came to my house.',
    'Had he been playing in the park until it got dark?',
    'They had been planning their escape for months.',
    'There were Japanese children who had been separated from their families and had been left in China.',
    'It originated with the potters who had been brought back to Japan by Terumoto Mori.',
    'On July 29, the head of Hirotsuna, who had been captured, was executed.',
    'Ken hadn\'t stopped studying until he solved the question.',
    'He had been playing soccer for six years on the team when he was replaced.',
    'Mr. Tanaka had been looking for this file before I arrived.',
    'She searched for her granddaughter who had been taken away.',
  ],
}
test_data_0779 = { 

      # **Guideword:** BACKGROUND INFORMATION WITH TIME CONJUNCTION
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect continuous after a time conjunction to give background information.
        
  'positive': [
    'After he had been thinking about the issue for some time, I decided to give up.',
    'After I had been wondering about where to go next, I gave up.',
    'After I had been walking, I arrived nowhere.',
    'After she had been waiting for hours outside, she got a cold and went home.',
    'After he had been watching the movie for 10 minutes, he decided to be an actor.',
    'After your friends had been talking about you, I thought you were a bad person.',
    'After I had been doing this job for 5 years, I felt exhausted.',
    'After I had been thinking, I decided to stay here.',
    'While he had been doing his job, she slept.',
    'After she had been searching, she thought she had better gave up.',
    'I arrived nowhere, after I had already been walking for hours.',
  ],
  'negative': [
    'Hiro had been looking for this data before I arrived.',
    'Japanese children who had been separated from their families and had been left in China.',
    'I have been reading books for three hours.',
    'I had been studying English for ten years before I went to Hawaii.',
    'They had believed her till she told a lie.',
    'Had you been reading books for three hours?',
    'Mr. Tanaka had been looking for this file before I arrived.',
    'Have you been reading books for three hours?',
    'Moreover, it got Tatsuya Masushima, who had been on loan, as a permanent employee.',
    'I hadn\'t been reading this book until my teacher came and told me to.',
    'I have been waiting for this news for a long time.',
    'Tom, who had been working all day, wanted to have a rest.',
    'My computer had been working fine until yesterday.',
    'They had been planning their escape for months.',
    'The chair was still warm from the person who had been sitting there before me.',
    'The brothers who had been fighting over their inheritance finally made peace.',
    'Ken hadn\'t stopped studying till he solved the question.',
    'He had been playing soccer for six years on the team.',
    'The criminal fooled the detective who had been watching his apartment.',
    'They had been sitting for hours, before they decided to take a walk.',
  ],
}
test_data_0780 = { 

      # **Guideword:** NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** 1.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the negative form. 
        
  'positive': [
    'The program that was terminated had not been working well since 1945.',
    'Ken hadn\'t been studying till he solved the question.',
    'I hadn\'t been working out regularly until my friend started going with me.',
    'Martha had not been walking three miles a day before she broke her leg.',
    'He had not been drinking milk out the carton when Mom walked into the kitchen.',
    'I had not been waiting for this news for a long time.',
    'I hadn\'t been reading this book till my teacher came.',
    'I had not been studying English for at least two hours before he came to my house.',
    'I had not been working at the company for five years when I got the promotion.',
    'She had not been waiting here for three hours.',
    'She had not been constantly worrying about the outcome before you said that.',
  ],
  'negative': [
    'Kenta admired the way the light glinted off his silver medal.',
    'I had known nothing about it until you told me.',
    'I had lived in the U.S. for five years.',
    'I had believed that my cat could recover for three years before she passed.',
    'After your friends had been talking about you, I thought you were bad.',
    'He had been playing soccer for six years on the team.',
    'We were relieved that Kenta had used washable paint.',
    'Moreover, it got Tatsuya Masushima, who had been on loan, on a permanent deal.',
    'He had been studying English for five years before he went to Canada.',
    'The criminal fooled the detective who had been watching his apartment.',
    'Kenta was proud of his hula hoop victory.',
    'I had been studying English for ten years before I went to Hawaii.',
    'When I came home, my brother had just finished his homework.',
    'Mr. Tanaka had been looking for this file before I arrived.',
    'I had been playing the guitar for ten years since I was a child.',
    'Kenta entered a hula hoop contest.',
    'After He had been thinking about the issue, I decided to give up.',
    'He won the silver medal.',
    'The chair was still warm from the person who had been sitting there before me.',
    'I have eaten nothing since this morning.',
  ],
}
test_data_0781 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect continuous with adverbs in the normal mid position. 
        
  'positive': [
    'Ayumi gained weight because she had constantly been eating.',
    'Sarah had perhaps been working at that company for three years.',
    'It had obviously been raining and the ground was still wet.',
    'My brother had probably been living in Christchurch for three years when the earthquake happened.',
    'Your girlfriend had surely been waiting for you at that time.',
    'She had almost been waiting for three hours when you came.',
    'Tom had possibly been teaching at the college for five years.',
    'I had certainly been studying all night long.',
    'We had maybe been playing golf for an hour when it started to rain.',
    'He had seriously been training really hard for this race.',
  ],
  'negative': [
    'She had smoked before she was twenty years old.',
    'She had not been waiting here for three hours.',
    'I had known nothing about it until you told it to me.',
    'I had been waiting for her for 30 minutes when she showed up.',
    'He had not been drinking milk out the carton when Mom walked into the kitchen.',
    'He had been playing soccer for six years on the team.',
    'My father had been drinking beer for long, when I ordered the next one.',
    'I have eaten nothing since this morning.',
    'When I came home, my brother had just finished his homework.',
    'After your friends had been talking about you, I thought you were bad.',
    'My daughter had been talking with her boyfriend on the phone for three hours before I told her to stop.',
    'I had been studying English for ten years before I went to Hawaii.',
    'They had been standing for many hours before they got a chance to sit down.',
    'I had been working at the company for five years when I got the promotion.',
    'She has been teaching English for three years.',
    'Before she was a high school student, she had been playing the piano for ten years.',
    'The criminal fooled the detective who had been watching his apartment.',
    'I hadn\'t been reading this book till my teacher came.',
    'My father had been repairing the car when I arrived home.',
    'Ken hadn\'t been studying till he solved the question.',
  ],
}
test_data_0782 = { 

      # **Guideword:** RESULTS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect continuous to talk about events which started before a time in the past and which finished, but where the effects or results were still important at a point in the past. 
        
  'positive': [
    'I had been reading a book when my brother came home.',
    'My father had been drinking beer for a long time when I ordered the next one.',
    'Before she was a high school student, she had been playing the piano for ten years.',
    'I had been reading this book till my teacher came and took it out of my hands.',
    'John had been watching TV when I came home.',
    'He had been drinking milk out the carton when Mom walked into the kitchen and scolded him.',
    'My father had been repairing the car when I arrived home.',
    'I had been working at the company for five years when I got the promotion.',
    'Ken had been studying till he solved the last question.',
    'Mary had been looking for this book before I arrived.',
  ],
  'negative': [
    'He had lived in Osaka for three years when I moved to Nagoya.',
    'He had already gone out before I called him.',
    'She found her key she had lost the day before.',
    'I had known him before he became a famous singer.',
    'When I arrived at the airport, the plane had taken off.',
    'I gave her the watch that I had bought at a department store.',
    'When she arrived at the airport, she was told to wait for Ann.',
    'We had just finished dinner when he got home.',
    'I had lived in Tokyo for two years when I moved to Chiba.',
    'She has been reading a book.',
    'She had smoked before she was twenty years old.',
    'She has been playing the piano for thirty years.',
    'When I came home, my brother had just finished his homework.',
    'I have lived here for two years.',
    'He had never seen Hiroshi before that time.',
    'I had known nothing about it until you told it to me.',
    'The train had already left before I got to the station.',
    'She had been abroad many times before she studied abroad.',
    'She was crying until then.',
    'It was raining when I woke this morning.',
  ],
}
test_data_0783 = { 

      # **Guideword:** QUESTIONS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use the question form. 
        
  'positive': [
    'What had they been looking for?',
    'Why had she been hiding in the closet?',
    'Who had she been talking to?',
    'Why had George been showering for an hour?',
    'Why had he been watching movies all day when he has a test tomorrow?',
    'How had he been managing all that work?',
    'What had they been doing this morning?',
    'What had Liz been doing to keep her mind off the accident?',
    'Who had Robert been living with?',
    'Where had she been working all day?',
  ],
  'negative': [
    'The surgeon had been operating for 36 hours.',
    'If only I had a map, I could show you the way.',
    'Have you decided which room to rent?',
    'Had we been traveling to Rome, we would have been affected by the accident.',
    'If only she had been home when I called yesterday.',
    'If it were not for electricity, our civilized life would be impossible.',
    'If only I had known the answer yesterday.',
    'Had we listened to her advice, our life would be messed up now.',
    'Where has your sister gone to?',
    'If only I had married another man.',
    'If it hadn’t been for his wife, he would not have changed his job.',
    'If it hadn’t been for your raincoat, I should have been drenched to the skin.',
    'If it were not for sports, how dull school life would be!',
    'If only I had studied more English conversation.',
    'How did she write a book by herself?',
    'Had it not been for her endeavors, adopting this would have been harder.',
    'Have you been to any foreign countries?',
    'Why were you listening to country music?',
    'If only I had a dog, I wouldn\'t be so lonely.',
    'If only I had gone to Italy with Rebekah.',
  ],
}
test_data_0784 = { 

      # **Guideword:** AFTER 'IF' CLAUSES
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past perfect simple in 'if'-clauses to talk about imagined situations in the past, often with regret. ► 'if'-clauses
        
  'positive': [
    'If you hadn’t saved me then, I would have died.',
    'You could have been on time if you had caught the bus.',
    'If you had given me your e-mail, I would have written to you.',
    'If I\'d known you were in hospital, I\'d have visited you.',
    'If you had worked harder, you would have passed your exam.',
    'I would have bought you a present if I had known it was your birthday.',
    'If she had started a little earlier, she might have been in time for the train.',
    'If it had rained, you would have gotten wet.',
    'If I had worked harder I might have passed the exam.',
    'If you hadn\'t lied to me before, I would have believed you.',
  ],
  'negative': [
    'If I were 20, I would travel the world.',
    'If I learned Spanish, I could talk to her.',
    'If I were you, I would give up smoking.',
    'If I were a cat, I could sleep all day.',
    'If I had the money, I could buy the latest iPhone.',
    'If I were a bird, I would fly around the world.',
    'If you really loved me, you would buy me a diamond ring.',
    'If you didn’t save me then, I would have died.',
    'We might buy a larger house when we get more money.',
    'If I were not sick, I would make a trip around the world.',
    'If I were rich, I would buy a large house with a pool.',
    'If I knew where she lived, I would go and see her.',
    'If I were taller, I would buy this dress.',
    'If I were a plant, I would love the rain.',
    'If it were nice out today, they would play baseball.',
    'If she were to fall, she would hurt herself.',
    'If the weather wasn\'t so bad, we would go to the park.',
    'If you went to bed earlier you wouldn\'t be so tired.',
    'If it rained, you would get wet.',
    'If it was sunny today, I would have taken my dog for a walk.',
  ],
}
test_data_0785 = { 

      # **Guideword:** AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the affirmative form.
        
  'positive': [
    'The train had left before I reached the station.',
    'I recognized him at once, as I had seen him before.',
    'When she came to see him, he had already gone out.',
    'Before the age of 25, she had lived in five different countries.',
    'The writer had finished writing the book before he left Japan.',
    'I had been abroad three times before I was twenty.',
    'We had already finished dinner when our father came home.',
    'We all felt comfortable because the living room had been cleaned.',
    'The plane had already taken off before they got to the airport.',
    'When we got to the football ground, the game had already started.',
    'I had not seen him but my brother had seen him.',
  ],
  'negative': [
    'How many times had you been to England before you were 10 years old?',
    'I hadn\'t been there before I became a university student.',
    'How many times had you visited America before you were 20 years old?',
    'He was very tired because he hadn\'t slept well.',
    'Hadn\'t he studied english yet?',
    'I hadn’t bought that comic.',
    'Had he seen her?',
    'I had not intended to go abroad.',
    'She had not smoked before she was twenty years old.',
    'I had not finished the homework when my friend got to my house.',
    'When I arrived at the airport, the plane had not arrived.',
    'I had not finished my homework when my father came home.',
    'He hadn\'t read the book before he returned it.',
    'He hadn\'t finished his homework by the time that he left home for the party.',
    'Had she finished her homework when her mother came home?',
    'He hadn’t eaten for three days, but he looked strong and healthy.',
    'Had you been there by then?',
    'He had not intended to order it.',
    'He had not left before you got there.',
    'How long had Ken lived in England before he came to Japan?',
  ],
}
test_data_0786 = { 

      # **Guideword:** NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use negative forms.
        
  'positive': [
    'I had not finished the homework when my friend got to my house.',
    'When I arrived at the airport, the plane had not arrived.',
    'He had not left before you got there.',
    'He was very tired because he hadn\'t slept well.',
    'She had not smoked before she was twenty years old.',
    'He had not intended to order it.',
    'He hadn\'t finished his homework by the time that he left home for the party.',
    'I hadn\'t been there before I became a university student.',
    'He hadn\'t read the book before he returned it.',
    'I had not finished my homework when my father came home.',
  ],
  'negative': [
    'How many times had you visited America before you were 20 years old?',
    'He had been ill for a week when he consulted the doctor.',
    'I had been in the coffee shop for two hours when she appeared.',
    'How many times had you been to England before you were 10 years old?',
    'Until then he had known nothing about the accident.',
    'Had he seen her?',
    'I had meant to call on you.',
    'We had lived there till we moved to Kyoto.',
    'Before the age of 25, she had lived in five different countries.',
    'I had been abroad three times before I was twenty.',
    'I had known the singer before she became famous.',
    'I had hoped that the rain would stop soon.',
    'Had she finished her homework when her mother came home?',
    'They had known each other for ten years when they got married.',
    'Had you been there by then?',
    'If it were to rain, i would have to cancel my plans.',
    'How long had Ken lived in England before he came to Japan?',
    'The train had left before I reached the station.',
    'When she came to see him, he had already gone out.',
    'If I had just come a little earlier, I could have made it on time.',
  ],
}
test_data_0787 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past perfect simple with a limited range of adverbs (including 'never', 'ever', 'just', 'always', 'already') in the normal mid-position. ► adverbs
        
  'positive': [
    'That was the first time I had ever talked to a foreigner.',
    'I had always hoped to meet my favorite author, but he died young.',
    'We had already finished dinner when our father came home.',
    'The plane had already taken off before they got to the airport.',
    'She had never seen snow till she visited Hokkaido.',
    'She had just finished her paper, when she walked in the door.',
    'I did not recognize him, for I had never seen him before.',
    'I went back to the store, but someone had just bought the last camera.',
    'Until I ate Russian food at the party, I had never tried it before.',
    'That was the most beautiful sunrise I had ever seen.',
  ],
  'negative': [
    'I had finished my homework before the bell was rung as always.',
    'Before the age of 25, she had lived in five different countries.',
    'He showed me the picture that he had taken there.',
    'I had hoped that the rain would stop soon.',
    'How long had Ken lived in England before he came to Japan?',
    'He had not left before you got there.',
    'When I arrived at the airport, the plane had not arrived.',
    'The fishing boat had been drifting for five days when it was found.',
    'She had not smoked before she was twenty years old.',
    'I had not finished my homework when my father came home.',
    'He hadn\'t read the book before he returned it.',
    'It came out that she had been embezzling money from her company.',
    'I had been abroad three times before I was twenty.',
    'I spent more money than I had expected.',
    'Had he seen her?',
    'My brother had been living only on water when the search party found him.',
    'He was very tired because he hadn\'t slept well.',
    'Had you been there by then?',
    'I had not finished the homework when my friend got to my house.',
    'Mr. Tanaka had been looking for this file before I arrived.',
    'They had been planning their escape for months.',
  ],
}
test_data_0788 = { 

      # **Guideword:** TIME UP TO THEN
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the past perfect simple to talk about a time before another time in the past.
        
  'positive': [
    'I found the eraser I had lost the day before yesterday.',
    'I noticed that I had left my textbook in my desk.',
    'I lost my eraser I had bought the day before.',
    'He showed me the picture that he had taken there.',
    'She did not speak to me until I had finished my coffee.',
    'I lost the book which I had borrowed from him two weeks before.',
    'After he had turned off the TV, Roy set to work.',
    'I lost the contact lenses I had bought the day before.',
    'He said Mary had bought a diamond ring.',
    'I lost the watch which my uncle had given me.',
  ],
  'negative': [
    'I had been talking with him for years before that time.',
    'I intended to go abroad.',
    'I hoped you would come to the party.',
    'I had been meaning to call on you.',
    'I had been hoping that he would win.',
    'He had been feeling sick for a week.',
    'She had long been expecting to finish the next chapter by yesterday.',
    'I have studied French for ten years.',
    'I hoped that the rain would stop.',
    'She has had the car for over 10 years.',
    'I never went to Hawaii.',
    'I have just finished my homework.',
    'I had still been hoping to finish my work.',
    'I have never talked with her.',
    'I was intending to become a teacher.',
    'I had been traveling to Alaska every year before 2000.',
    'I have been living in Kyoto.',
    'She has lived in five different countries.',
    'She had been living in Tokyo for two years.',
    'He intended to order it.',
  ],
}
test_data_0789 = { 

      # **Guideword:** AFTER 'BECAUSE', EXPLANATIONS
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect simple after 'because' to give explanatory information.
        
  'positive': [
    'Because she had finished the exam, she felt very happy.',
    'He was very tired because he hadn\'t slept well.',
    'I did not have any money because I had lost my wallet.',
    'She only understood the movie because she had read the book.',
    'Tony knew Istanbul so well because he had visited the city several times.',
    'she decided to go shopping, because she had finished the exam.',
    'They felt bad about selling the house because they had owned it for more than forty years.',
    'They lost many of the games because they had not practiced enough.',
    'We were not able to get a hotel room because we had not booked in advance.',
    'She stayed up all night because she had received bad news.',
  ],
  'negative': [
    'I had just put the washing out when it started to rain.',
    'The usher asked if we had purchased our tickets.',
    'Kristine had never been to an opera before last night.',
    'The boss had said it would be a long meeting.',
    'She had never seen a bear before she moved to Alaska.',
    'The train had just left when I arrived at the station.',
    'She had just left the room when the police arrived.',
    'She had established her company before 2008.',
    'They had gotten engaged before last year.',
    'We had had that car for ten years before it broke down.',
    'She had visited her Japanese relatives once in 1993 before she moved in with them in 1996.',
    'Anthony had met Ryan before you introduced him to us at the party.',
    'My neighbor asked if we had seen her dog.',
    'You had studied English before you moved to New York.',
    'You had studied Italian before you moved to Rome.',
    'George had repaired many cars before he received his mechanic\'s license.',
    'I had fallen asleep before eight o\'clock.',
    'By the time Alex finished his studies, he had been in London for over eight years.',
    'He had never played football until last week.',
    'The teacher asked if we had studied for the exam.',
  ],
}
test_data_0790 = { 

      # **Guideword:** AFTER 'IF ONLY' AND 'WISH', IMAGINED PAST
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the affirmative form after 'if only', and the affirmative and negative forms after 'wish' to talk about regret.
        
  'positive': [
    'If only I had gone there.',
    'If only I had married another man.',
    'I wish I had not bought it.',
    'I wish I hadn\'t been born stupid.',
    'If only I had come five minutes earlier, I could have caught the train.',
    'If only I had studied more English conversation.',
    'If only I had known the answer yesterday.',
    'I wish I had not been there',
    'I wish I had not seen the film.',
    'I wish I had seen him.',
  ],
  'negative': [
    'I wish I had a better memory.',
    'If only I get a chance to see him.',
    'I wish I had more money.',
    'You had studied English before you moved to New York.',
    'If only I had a dog, I wouldn\'t be so lonely.',
    'He had never played football until last week.',
    'They had gotten engaged before last year.',
    'They felt bad about selling the house because they had owned it for more than forty years.',
    'My neighbor asked if we had seen her dog.',
    'I wish I had a car.',
    'If only I had a doctor like him.',
    'She had established her company before 2008.',
    'We were not able to get a hotel room because we had not booked in advance.',
    'If only I had money.',
    'I wish I had a house of my own.',
    'I wish I had wings.',
    'She only understood the movie because she had read the book.',
    'You had studied Italian before you moved to Rome.',
    'The boss had said it would be a long meeting.',
    'If only I could speak French.',
  ],
}
test_data_0791 = { 

      # **Guideword:** INVERSION WITH 'NEVER (BEFORE)'
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can invert the subject and auxiliary verb after 'never (before)' to talk about a unique event, often in formal contexts.
        
  'positive': [
    'Never had the crew seen so jolly and dexterous a fellow.',
    'Never had I found in the greenhouses of the North such satisfying roses.',
    'Never had my mother said something like that.',
    'Never had she met somebody as interesting as him.',
    'Never had I visited such a beautiful place.',
    'Never Had I gone there at that time.',
    'Never had he talked with such an engaging woman.',
    'Never had I seen something like that.',
    'Never had I heard jazz like this.',
    'Never had I realized my ignorance more keenly than I did then.',
  ],
  'negative': [
    'If only I had married another man.',
    'He had never played football until last week.',
    'I wish I had been there',
    'I never had such an experience in my life.',
    'If only I had known the answer yesterday.',
    'She never had a child.',
    'The boss had said it would be a long meeting.',
    'I never had my photograph taken in my life.',
    'I have never had vegetarian cooking before.',
    'I wish I had seen him.',
    'They had gotten engaged before last year.',
    'You had studied Italian before you moved to Rome.',
    'I have never had any financial dealings with him.',
    'You had studied English before you moved to New York.',
    'I had never been here.',
    'I have never had doughnuts for breakfast.',
    'My neighbor asked if we had seen her dog.',
    'She had established her company before 2008.',
    'I wish I had bought it.',
    'He never had conversations with any one.',
  ],
}
test_data_0792 = { 

      # **Guideword:** INVERSION WITH 'NO SOONER ... THAN'
      # **Guideword type:** FORM/USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can invert the subject and auxiliary verb with 'no sooner ... than' to talk about something that happened immediately before something else, often in formal contexts.
        
  'positive': [
    'No sooner had she read the letter than she started crying.',
    'No sooner had they completed the work than they demanded the wages.',
    'No sooner had I closed my eyes than I fell asleep.',
    'No sooner had I arrived at the station than the train came.',
    'No sooner had I stepped out than it started raining.',
    'No sooner had she finished one project than she started working on the next.',
    'No sooner had I eaten the fish than I started feeling sick.',
    'No sooner had I gotten my bags unpacked than I realized that my camera was missing.',
    'No sooner had we heard the noise than we rushed to the spot.',
    'No sooner had I received her call than I left for her place.',
  ],
  'negative': [
    'Hardly had I started working on the computer when the electricity went out.',
    'No sooner did I arrive at the station than the train came.',
    'No sooner did she read the telegram than she fainted.',
    'Hardly had Ben entered the room when his phone started ringing.',
    'Scarcely had I reached the station when the train arrived.',
    'No sooner did the driver see the signal than he applied the brake.',
    'As soon as she finished one project, she started working on the next.',
    'No sooner did I take a dose of medicine than I started feeling better.',
    'No sooner did I go to bed than I fell asleep.',
    'Aric had barely started the speech when Andrew started questioning.',
    'No sooner did the child start crying than his mother lifted him up.',
    'No sooner did he reach the bus station than the bus came.',
    'Hardly had I reached the station when the train came.',
    'Hardly had I seen the thief when he started running.',
    'As soon as I arrived at the station, the train came.',
    'Scarcely had the police seen the culprit when he started fleeing away.',
    'No sooner did we hear the noise than we rushed to the spot.',
    'No sooner did the thieves see the police than they ran away.',
    'Hardly had Alice seen her mother when she started crying.',
    'As soon as the teacher entered the classroom than the students stood up.',
  ],
}
test_data_0793 = { 

      # **Guideword:** ELLIPSIS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can leave out the subject before the past perfect simple where it is understood from the previous clause.
        
  'positive': [
    'My mother was rich and had bought so many things.',
    'She was happy and had gone abroad for a while.',
    # pos error: drunk (JJ)
    # 'She drunk water and had been thirsty.',
    'He was famous singer and had sung a lot.',
    'It was cool and had been rainy for ten days.',
    'I was a baseball player and had practiced everyday.',
    'I was busy and had lost my wallet.',
    'He took exam and had prepared for a week.',
    'She was busy and had lost 10kg.',
    'She felt tired and had slept for a while.',
  ],
  'negative': [
    'The boss had said it would be a long meeting.',
    'She only understood the movie because she had read the book.',
    'The usher asked if we had purchased our tickets.',
    'The train had just left when I arrived at the station.',
    'Anthony had met Ryan before you introduced him to us at the party.',
    'I lost the watch I had bought the day before.',
    'I had taken many photos when it started to rain.',
    'My neighbor asked if we had seen her dog.',
    'I had just put the washing out when it started to rain.',
    'Mr. Green had been the head of the NGO before he went to China.',
    'I had already had a dinner.',
    'They felt bad about selling the house because they had owned it for more than forty years.',
    'You had studied Italian before you moved to Rome.',
    'You had studied English before you moved to New York.',
    'We were not able to get a hotel room because we had not booked in advance.',
    'She had just left the room when the police arrived.',
    'Tony knew Istanbul so well because he had visited the city several times.',
    'The teacher asked if we had studied for the exam.',
    'The train had already departed before they got to the station.',
    'I had been there when I was a university student.',
  ],
}
test_data_0794 = { 

      # **Guideword:** QUESTIONS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use question forms.
        
  'positive': [
    'What had they said that made him so angry?',
    'Had you spoken to him before you met each other?',
    'When had he arrived?',
    'Why had you eaten?',
    'Why had he agreed to work for that salary?',
    'Had you cleaned up the mess by the time they came home?',
    'Where had she gone?',
    'Had you tried sushi before today?',
    'Had Adam ever spoken to the CEO before he was fired?',
    'How much had he drunk before you got to him?',
  ],
  'negative': [
    'She had lived here many years before moving here again.',
    'She drunk water and had been thirsty.',
    'I\'d started the computer.',
    'She\'d lived here for 20 years.',
    'Tony knew Istanbul so well because he had visited the city several times.',
    'She had just left the room when the police arrived.',
    'The boss had said it would be a long meeting.',
    'I had not eaten at that restaurant before today.',
    'Samantha hadn’t had time to explain her side of the story.',
    'They had complained about this two times before.',
    'The train had just left when I arrived at the station.',
    'I had started the computer but it took so long to boot up I used my iPad.',
    'He took exam and had prepared for a week.',
    'My friends had never gone to the USA either.',
    'I was busy and had lost my wallet.',
    'My neighbor asked if we had seen her dog.',
    'She felt tired and had slept for a while.',
    'They hadn\'t complained about this before.',
    'My friends hadn’t ever gone to France.',
    'I had been there when I was a university student.',
  ],
}
test_data_0795 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** 3.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect simple with a wide range of adverbs (including 'finally', 'recently', 'simply') in the normal mid-position.  ► adverbs
        
  'positive': [
    'He had simply abused her hospitality.',
    'She had simply just left the room when the police arrived.',
    'They had recently complained about this two times before.',
    'He had simply taken advantage of Polly\'s youth and inexperience.',
    'I had simply got home safely.',
    # pos error: it seems hard to detect.
    # 'I\'d recently started the computer.',
    'I had recently started the computer.'
    'He had finally convinced several customers of the advantages of his product.',
    # 'She\'d finally lived here for 20 years.',
    'She had finally lived here for 20 years.'
    'She had finally gotten a new boyfriend.',
    'She had finally met her match in Helen.',
  ],
  'negative': [
    'Finally my father compromised.',
    'I don\'t have enough money recently.',
    'I had been there when I was a university student.',
    'I had not eaten at that restaurant before today.',
    'My friends had never gone to the USA either.',
    'I will explain it simply.',
    'She drunk water and had been thirsty.',
    'They hadn\'t complained about this before.',
    'I finally noticed that.',
    'Tony knew Istanbul so well because he had visited the city several times.',
    'It was simply an oversight.',
    'My friends hadn’t ever gone to France.',
    'The train had just left when I arrived at the station.',
    'That is simply violence.',
    'Samantha hadn’t had time to explain her side of the story.',
    'I\'ve bought this recently.',
    'The time will finally come.',
    'The boss had said it would be a long meeting.',
    'I could finally meet John.',
    'There\'s been a lot of rain recently.',
  ],
}
test_data_0796 = { 

      # **Guideword:** BACKGROUND INFORMATION, RELATIVE CLAUSE
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect simple in relative clauses to give background information.    ► relative clauses
        
  'positive': [
    'Ken talked about the movie which he had watched two weeks before.',
    'I lost my book that my father had bought for me the day before.',
    'My brother gave me the dictionary he had used for a year.',
    'I went to the park where I had seen a suspicious person.',
    'I found my bag which I had lost the day before.',
    'I lost the pen that I had borrowed from you.',
    'I lost the contact lenses I had bought the day before.',
    'I lost my pen which I had bought.',
    'He showed me the picture that he had taken there.',
    'He met the man who I had met the day before.',
  ],
  'negative': [
    'He had simply abused her hospitality.',
    'She had finally met her match in Helen.',
    'It was easier than I had expected.',
    'There is a boy who is running in the park.',
    'They hadn\'t complained about this before.',
    'She\'d finally lived here for 20 years.',
    'I had been there when I was a university student.',
    'He said Mary had bought a diamond ring.',
    'After he had turned off the TV, Roy set to work.',
    'She is a girl whose father is a doctor.',
    'She is a girl whom I invited to the party.',
    'Samantha hadn’t had time to explain her side of the story.',
    'He has sons who are married.',
    'She is a girl who came to my house last week.',
    'She had just left the room when the police arrived.',
    'He had finally convinced several customers of the advantages of his product.',
    'I noticed that I had left my textbook in my desk.',
    'I had not eaten at that restaurant before today.',
    'She drank water and had been thirsty.',
    'She did not speak to me until I had finished my coffee.',
  ],
}
test_data_0797 = { 

      # **Guideword:** CHANGE OF SITUATION
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect simple to talk about situations which changed. 
        
  'positive': [
    'I had planned to drink beer, but I drank water instead.',
    'I had planned to go to Japan, but I changed my mind.',
    'I had wanted to go to Japan, but I went to China instead.',
    'He had thought to go out to eat dinner, but he cooked himself.',
    'I had planned to stay here, but I left.',
    'She had thought to go to school, but the school was closed.',
    'She had wanted to get new shoes, but she wanted to get new cap more.',
    'She had wanted to buy new books, but she changed her mind.',
    'He had wanted to stay here, but he went there instead.',
    'She had planned to travel, but she stayed here.',
  ],
  'negative': [
    'She had just left the room when the police arrived.',
    'They hadn\'t complained about this before.',
    'It was nothing but a joke.',
    'He said Mary had bought a diamond ring.',
    'He had simply abused her hospitality.',
    'Ken talked about the movie which he had watched two weeks before.',
    'She drank water and had been thirsty.',
    'It was easier than I had expected.',
    'She had finally met her match in Helen.',
    'He had finally convinced several customers of the advantages of his product.',
    'There was no one left but me.',
    'He met the man who I had met the day before.',
    'I would go abroad but I am poor.',
    'I lost the contact lenses I had bought the day before.',
    'He is not such a fool but he knows it.',
    'I lost the pen that I had borrowed from you.',
    'I had been there when I was a university student.',
    'Excuse me, but could you tell me the way to the museum?',
    'She\'d finally lived here for 20 years.',
    'He showed me the picture that he had taken there.',
  ],
}
test_data_0798 = { 

      # **Guideword:** REPORTS OF QUESTIONS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect simple to report questions, where the main verb in the reporting clause is in the past simple.  ► reported speech
        
  'positive': [
    'She asked me how I had escaped.',
    'I asked you when you had gotten your hair cut.',
    'He asked me where I had been.',
    'He asked you what you had eaten for breakfast.',
    'You asked me when she had arrived at my house.',
    'She asked me how I had been.',
    'She asked me what had happened to me.',
    'I asked you when you had left my house.',
    'I asked you what you had bought.',
    'She asked me where I had gone to.',
  ],
  'negative': [
    'She had wanted to buy new books, but she changed her mind.',
    'Let me know how he did it.',
    'This is the way she opened the box.',
    'He met the man who I had met the day before.',
    'Mary had bought a diamond ring.',
    'He wants to know the reason why she said farewell.',
    'She came to see the university on the day when it was demolished.',
    'I lost the pen that I had borrowed from you.',
    'They hadn\'t complained about this before.',
    'Don\'t forget the time when we first met.',
    'The reason why he was late is unknown.',
    'It rained on the night when we broke up.',
    'She had thought to go to school, but the school was closed.',
    'This is the town where I was born.',
    'We went to the church where we had our wedding.',
    'I had had been to Japan, but I went again.',
    'I had planned to stay here, but I left.',
    'We are looking for the restaurant where we ate dinner last week.',
    'There is no reason why I should wait.',
    'Ken talked about the movie.',
  ],
}
test_data_0799 = { 

      # **Guideword:** REPORTS OF STATEMENTS
      # **Guideword type:** USE
      # **Super category:** PAST
      # **Sub category:** past perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the past perfect simple to report statements, where the main verb in the reporting clause is in the past simple.  ► reported speech
        
  'positive': [
    'She said she had bought so many things for herself.',
    'She said that you had gone abroad.',
    'You explained what had happened at that time.',
    'The newspaper said that my mother had stolen money from the bank.',
    'He told me what had happened between you and her.',
    'She explained what had made her do it.',
    'She told me that she had escaped from her mother.',
    'I told them that I had been abroad so many times.',
    'She told me that she had been sick last few week.',
    'He said that he had slept over at your place.',
  ],
  'negative': [
    'She had just left the room when the police arrived.',
    'She had wanted to buy new books, but she changed her mind.',
    'Before I went to the school, I had had a car accident.',
    'I\'d eaten dinner so I wasn\'t hungry.',
    'It had snowed in the night, so the bus didn\'t arrive.',
    'I had planned to stay here, but I left.',
    'I asked you when you got your hair cut.',
    'She asked me how I escaped.',
    'By the time he came here, I already had finished my dinner.',
    'The train had just left when I arrived at the station.',
    'She had thought to go to school, but the school was closed.',
    'They hadn\'t complained about this before.',
    'I asked you when you left my house.',
    'Ken had watched the movie two weeks before.',
    'I had just put the washing out when it started to rain.',
    'He asked you what you had eaten for breakfast.',
    'He met the man who I had met the day before.',
    'I had been to Japan once, but I went again.',
    'After I had finished my homework, I went to the Internet cafe.',
    'She asked me where I was from.',
  ],
}
