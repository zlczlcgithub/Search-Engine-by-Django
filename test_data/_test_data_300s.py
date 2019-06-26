test_data_0300 = { 

      # **Guideword:** SIMPLE
      # **Guideword type:** FORM
      # **Super category:** CONJUNCTIONS
      # **Sub category:** subordinating
      # **Lexical Range:** 3.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use a wide range of simple subordinating conjunctions ('once, whereas, unless, except (that) provided (that)'), to introduce a subordinate clause.
        
  'positive': [
    'Unless medical treatment is started soon, you will probably die.',
    'I like Dragon Ball, whereas you like Naruto.',
    'Unless another solution is found, we should stop this project.',
    'Canada is cold, whereas Japan is fairly warm.',
    'Once you\'ve signed, you cannot cancel the contract.',
    'She knows nothing about him except that he is a teacher.',
    'I have money in my pocket, whereas you have candy in your bag.',
    'I\'d do it for you except I know you can do it for yourself.',
    'Provided that you learn how to speak English well, you won\'t ever forget it.',
    'Unless a miracle happens, the company will become bankrupt.',
  ],
  'negative': [
    'All of us will go except you.',
    'Nothing comes into view except for you.',
    'Everybody is busy except me.',
    'The fire was extinguished at once.',
    'No admittance except on business.',
    'He came at once after he heard the news.',
    'I provided for him.',
    'You are only young once.',
    'He doesn\'t do anything except watch TV.',
    'We provide subsidies.',
    'I can\'t speak English except for a little.',
    'I don\'t buy anything except for cheap things.',
    'They provide examples like the one that follows.',
    'He is of no use except as a clerk.',
    'All my family except me left.',
    'Let\'s begin our work at once.',
    'We must always provide against accidents.',
    'Everything happened all at once.',
    'I don\'t have anything except for this much.',
    'Nobody was hungry except me.',
  ],
}
test_data_0301 = { 

      # **Guideword:** COMPLEX
      # **Guideword type:** FORM
      # **Super category:** CONJUNCTIONS
      # **Sub category:** subordinating
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use more complex subordinating conjunctions ('as long as, as soon as, in order that, despite the fact that, due to the fact that, as if, as though') to introduce a subordinate clause. 
        
  'positive': [
    'You\'ll be fine due to the fact that you are so experienced.',
    'I will call you as soon as I know.',
    'I\'ll stay in contact after I move, it will be as though I was right at home with you.',
    'Please close the door in order that we may have some privacy.',
    'As long as you are there, I\'m good.',
    'I will send it as soon as it is completed.',
    'I go on overseas trips despite the fact that I can\'t speak English.',
    'He works hard in order that his family may live in comfort.',
    'I came early in order that I could get a good seat.',
    'It looks as if we\'re going to have a storm.',
  ],
  'negative': [
    'It’s not as bad as I thought.',
    'He is as strong as my brother.',
    'My bonus was not as big as I expected.',
    'She drinks as much water as he does.',
    'Finding what you want on the Web should be as easy as finding a book in the library.',
    'Mt. Fuji isn’t as tall as Mt. Everest.',
    'He is almost as good at skiing as me.',
    'This novel isn’t as interesting as that one.',
    'I don’t think the cheese cake served at the coffee shop is as good as the rumor says.',
    'He is as tall as his father.',
    'You love him as much as you love me.',
    'This computer is as expensive as that one.',
    'My dog runs as fast as yours.',
    'He is as tall as I am.',
    'I can’t play the piano as well as her.',
    'My sister doesn’t drive as carefully as my brother.',
    'He runs as fast as I do.',
    'He doesn’t hate her as much as he used to.',
    'Rick can jump as high as Bill.',
    'Mr. Kagawa isn’t as old as he looks.',
  ],
}
test_data_0302 = { 

      # **Guideword:** FOCUS
      # **Guideword type:** FORM/USE
      # **Super category:** CONJUNCTIONS
      # **Sub category:** subordinating
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'whatever', 'wherever', 'however', etc. as a subordinating conjunction, at the beginning of a sentence, to give focus.
        
  'positive': [
    'Whatever anyone may say, she will not listen to him.',
    'Wherever I went, I ran into the wall of prejudice.',
    'However things seem, they will never be the same as they were.',
    'Whatever I may say, he will not consent.',
    # 'However his style may be, I like him for his ideas.',
    # may -> be (root) ???
    'Whatever you do, try your best.',
    'Wherever we may go, we will get lost.',
    'However things may end up, we have nothing to lose.',
    'Whatever you do, do your best.',
    'Wherever I am, I think of you.',
  ],
  'negative': [
    'He believes whatever I say.',
    'Do whatever you want with me.',
    'She was warmly received wherever she went.',
    'I walked around town wherever my feet led me.',
    'You can swim wherever you like.',
    'He says whatever comes into his head.',
    'You shall have whatever price you want.',
    'You shall do whatever you like.',
    'You may buy whatever you think fit.',
    'She follows her brother wherever he goes.',
    'He is always sloppy whatever he does.',
    'You may sit wherever you like.',
    'He gets lost wherever he goes.',
    'I read whatever interests me.',
    'He says whatever he wants.',
    'He came along with me wherever I went.',
    'His dog follows him wherever he goes.',
    'I know nothing whatsoever about it.',
    'Keep your head whatever happens.',
    'Help yourself to whatever you please.',
  ],
}
test_data_0303 = {

  # **Guideword:** 'IN THAT'
  # **Guideword type:** FORM/USE
  # **Super category:** CONJUNCTIONS
  # **Sub category:** subordinating
  # **Lexical Range:** None
  # **CEFR level:** C2
  # **CAN-DO:** Can use 'in that' as a subordinating conjunction, to give greater in-depth explanation, often in formal contexts.

    'positive': [
      'Nowadays it is widely argued that professional sports are damaging to people\'s health in that they involve gruelling training sessions as an integral part of the occupation.',
      # dependencies error, that -> in (case)
      # 'It\'s often said that nowadays people must be proud of medical advances, in that life is getting considerably longer.',
      'Directive weapons aren\'t all that special in that they can be acquired ingame at any time, whereas special weapons are obtained only under specific conditions.',
      # 'This was a fun game and the master builder mechanic is pretty interesting in that each turn one player gets to set the price for the buildings that will available that round.',
      'I\'m pretty content that the relatively consistent flatness and straight-ahead motion is good in that I\'m not constantly bending and twisting.',
      'He acts just like a monkey in that he is stupid.',
      'The situation is improving in that the average salary is going up every year.',
      'You are even worse in that you prosecute wholly innocent people for crimes they did not commit.',
      'However, we as humans are unique in that we are aware of the suffering of others, and that gives us a responsibility to minimize pain and suffering.',
      # 'I can feel blessed in that I do have room enough to help them.',
      # 'I\'m selfish in that I refuse to die for the sake of a whole planet.',
      'I am rather like a cat in that I hate being wet.',
      'I always though it was refreshing to visit, in that you got to see so many new styles every time.',
    ],
    'negative': [
      'Anything that anyone points to as showing otherwise is merely a symptom of the bigotry prevalent in that culture.',
      'In that regard, I couldn\'t care less what Suh might do.',
      'All I "knew" was that there was a spirit there that protected those boys in that center.',
      'What is anyone in that thread talking about?',
      'I\'ve only seen The Shining a few times, but I\'ve never noticed Stephen King in that photo before.',
      'The performance would be the same as what they mentioned in that step.',
      'Bright headlights in that situation let in more light than you can handle.',
      'This has been a great year, and we should bask in that fact.',
      'We didn\'t really think in that way.',
      'When things are introduced in that way to me, it makes me feel much worse.',
      'VLO raises a big red flag in that area.',
      'If we\'re talking about \'nam and you fought in that war, okay, you can talk about it a bit if it\'s relevant.',
      'Nothing happens in that corner of the screen.',
      'It\'s brought up in that chapter.',
      'I try to pump a little first in that situation to relieve pressure.',
      'Until it\'s you in that same situation, stop throwing stones and go home.',
      'I don\'t think the fight has been so equal that the influence hasn\'t changed in that amount of time.',
      'I\'m extremely interested in that game as well so if that comes out in early February then I\'ll probably get it.',
      'Glass was a bad choice for the inactive sloped blocks in that last video.',
      'In that case, change the configuration file.',
      'It is inferior in that respect.',
      'You cannot use that in that shape.',
      'Is that okay in that place?',
    ],
}
test_data_0304 = {

  # **Guideword:** WITH NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** articles
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use articles 'the', 'a' and 'an' before nouns. ► noun phrases

  'positive': [
    'My mother baked a chocolate cake for dessert.',
    'I went to the supermarket yesterday but they were out of sugar so I can’t bake a cake.',
    'I took the subway to go to school today, but there was an accident and as a result, I didn’t make it in time for the first period.',
    'But for your assistance, I wouldn’t have been able to buy a car.',
    'Although I missed the bus, I was able to catch a taxi.',
    'Crying will make you feel better, though it won’t solve the issue.',
    'The test will be about a past assignment or a topic that was discussed in class.',
    'My sister is getting married in July, so I have to buy her a present.',
    'All the animals had run away.',
  ],
  'negative': [
    'My actions were good or bad.',
    'Molly has lots of friends.',
    'Our dog is smart and more obedient than other dogs.',
    'She wants to have Chinese cuisine for lunch.',
    'His room had many pieces of furniture.',
    'This is my dog and cat.',
    'I am craving cheesecake right now.',
    'We will have meatloaf with some vegetables.',
    'My pet rabbit is fluffy and cuddly.',
    'My big sister is always annoying.',
    'Which is more important, playing or studying?',
    'My grandpa is smart and thoughtful.',
    'I have math class on Monday and Friday.',
    'I prefer to have chicken or fish for lunch.',
    'My hockey stick should be somewhere around here.',
    'I like to eat meat with garlic and salt.',
    'Perhaps you should take some medicine before it gets worse.',
    'I am excited about visiting Bali with my mother this summer.',
    'I went shopping with my classmates last night.',
    'Gorillas are said to be extremely smart.',
    'We made plans to go to church this Wednesday.',
  ],
}
test_data_0305 = {

  # **Guideword:** 'A' + ADJECTIVES
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** articles
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'a' and 'an' before adjectives in a noun phrase. ► adjectives ►  noun phrases

  'positive': [
    'The test will be about a past assignment or a complicated topic.',
    'Whether my actions were good or bad is a huge deal for me.',
    'I am building an intelligent robot for my science project.',
    'A green bag was at the lost and found.',
    'Tokyo is a busy city with a large population.',
    'Going to the festival next week is a fabulous idea.',
    'Jumping up and down is a mundane exercise.',
    'My niece is a sweet girl.',
    'An ambitious friend is something I need in my life right now.',
    'I will wear a red dress to prom this year.',
  ],
  'negative': [
    'Our dog is smart and more obedient than other dogs.',
    'She wants to have French cuisine for dinner.',
    'My mother baked a cake for dessert.',
    'I am craving frozen yogurt right now.',
    'My dad bought me a car for my birthday last month.',
    'We will have lamb chop with some vegetables on the side.',
    'My older brother is always annoying.',
    'Although I missed the final train, I was able to catch a taxi.',
    'An interview is something I am really bad at.',
    'My hockey stick should be in the kitchen.',
    'Perhaps you should take some medicine before your fever gets worse.',
    'My daughter is well known for her artistic talent.',
    'I always put an apple in my smoothie.',
    'My perfect son was chosen to be the valedictorian this year.',
    'I am shocked because I lost my purple sunglasses.',
    'Could you run to the market and buy some eggs?',
    'Could you pass me the hot sauce, please?',
    'That latest movie seems really funny.',
    'Tai chi is good for your mental health.',
    'Where is that fluffy puppy of yours?',
  ],
}
test_data_0306 = {

  # **Guideword:** 'A' + 'VERY' + ADJECTIVES
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** articles
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'a' + 'very' + adjectives in basic noun phrases. ► adverbs ►  noun phrases

  'positive': [
    'My sister’s daughter is a very eloquent girl.',
    'Whether my actions were good or bad is a very big deal for me.',
    'Bangkok is a very crowded city.',
    'Attending the banquet together is a very clever idea.',
    'My nephew is a very shy boy.',
    'Nancy and James are in a very serious relationship.',
    'Christmas is a very busy holiday.',
    'My uncle bought me a very fancy car for my birthday last year.',
    'Getting married is a very important event in life.',
    'Watching television for 5 hours is a very boring way to spend your day.',
  ],
  'negative': [
    'That latest movie seems very funny.',
    'Yoga is very good for your mental health.',
    'Expensive apples are very sweet.',
    'My English literature teacher is very strict with deadlines.',
    'The famous model from France is very skinny.',
    'Having a surprise birthday party is a great idea.',
    'Skipping class to go shopping was an extremely bad idea.',
    'My mom bakes very tasty brownies.',
    'It was very peaceful in the woods.',
    'Candies can be addictive for little children.',
    'Cheryl is a sweet girl who is kind and compassionate to everyone.',
    'Mark is very self-conscious, and sometimes that can be annoying.',
    'We need to give you a special medicine.',
    'My college interview was a complete disaster.',
    'My sister is punctual unlike most of her friends.',
    'It’s very kind of him to buy flowers for my sick daughter.',
    'Steven is a genius who has no sense of fashion.',
    'I was very shocked to hear the news of my professor’s death.',
    'Signing all these papers is very tiring.',
    'Calling your ex-fiancé is a sign that you still love her.',
  ],
}
test_data_0307 = {

  # **Guideword:** PREPOSITION + 'THE' + NOUN
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** articles
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'the' in prepositional phrases relating to time.

  'positive': [
    'I took my iron pill in the morning and tea in the afternoon, that\'s ok.',
    'The only time they do recaps is at the end of the year.',
    'We were all invited, but the 15-year-old is grounded and a 3-month-old doesn\'t need to be at a loud party in the middle of the night.',
    # 'I can\'t speak for the Sunday events but I go to melee every chance I get and it\'s absolutely wonderful!',
    # 'I pretty much started studying in early February for the June exams.',
    'I think the share buttons are a throwback from the days when social media was new.',
    'My brother developed cancer and was told one night after months of chemo and radiotherapy that he would be dead by the morning.',
    'I know the price has increased slightly from last year due to rising production costs over the past year.',
    'Usually, when I\'m at work my mum will feed them around 12 in the afternoon then again just after four.',
    'The police decided to act fast because the guy was planning to kill everyone before the night.',
  ],
  'negative': [
    'Things on the edges of my vision appear one second and are gone the next.',
    'You can have any pokemon you want in the game, including from other Generations if you follow these instructions.',
    'Cancer must be wiped from the world no matter what.',
    'You can\'t play football before the whistle.',
    'Reminded me of cleaning out the toilets the morning before returning from camp.',
    'I just went to my first meetup yesterday and had a blast.',
    'This is the last year I have with just my two kids since I have another one on the way in June.',
    'I will have my birthday party on this Sunday.',
    'He might be able to be here on time.',
    'My father played baseball with me last Friday.',
    'My friends and I will meet up at the coffee shop after the practice.',
    'You think you can get away with saying that shit to me over the Internet?',
    'Under Kansas law, a child under the age of 15 is legally unable to drink alcohol.',
    'Last time I saw a cow in a tornado he was heading somewhere over the rainbow.',
    'I\'ve never watched the show and it was about to start.',
    'I forgot my pencil under the desk in the office.',
    'Now you have to wait 5 minutes until the next teacher arrives.',
    'We are all too young to decide the future.',
    'I\'d start by figuring out why there is a colony on the planet.',
    'My name is Katie and my birthday is the day after tomorrow.',
  ],
}
test_data_0308 = {

  # **Guideword:** PREPOSITION + NO ARTICLE
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** articles
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use no article before a limited range of nouns in some fixed expressions with prepositions.

  'positive': [
    'He doesn\'t like to go to school because he is not good at studying.',
    'I\'ll just need to find a way out to Tokyo so I can get the rest of the way by bus.',
    'My sister baked apple cake for work.',
    'His father is from Thailand, but his mother is from China.',
    'My mother told me that I have to be at home before sunset.',
    'Your young brother is unable to do anything without help.',
    'I have to send this paper by tomorrow; otherwise I can\'t pass this course.',
    'I need to get home by train.',
    'Unlike my family, her family always goes there by bus.',
    'You are pretty smart to go to work early.',
    'I can have anything for dinner at home.',
    'You can park your new car at work.',

  ],
  'negative': [
    'Food can dip below a certain temperature once it\'s cooked.',
    'I\'m not sure leaving your dream job makes sense after a year even if it is for a promotion.',
    'I understand it\'s easy to get excited about a new car.',
    'I met a lot of people along the way home.',
    'There are plenty of delicious foods around the world.',
    'We have to clean up our whole house before the new year.',
    'You have to submit this homework by the end of this month.',
    'I\'m just getting back from an injury.',
    'He got lost inside the airport since it is pretty huge.',
    'You need to think outside the box.',
    'The way you behave is like a small cat.',
    'We don\'t give up on winning the game until the whistle is blown.',
    'You can\'t leave the class without a permission.',
    'He got tanned a lot during the vacation.',
    'My house is opposite to the cake shop.',
    'He can make new friends as much as he wants through the Internet.',
    'You should try calling again and ask to speak to a manager.',
  ],
}

test_data_0309 = { 

  # **Guideword:** NO ARTICLE
  # **Guideword type:** FORM/USE
  # **Super category:** DETERMINERS
  # **Sub category:** articles
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use no article before a limited range of singular, plural and uncountable nouns when referring to things in general.
    
  'positive': [
    'Can horses cross rivers?',
    'Faith will move mountains.',
    'Life is what you make it.',
    'Words have wings.',
    'I played baseball when I was a junior high student.',
    'I intended to go to hospital.',
    'Time flies like an arrow.',
    'Fortune comes in at the merry gate.',
    #parser error 'light' marked as 'JJ'
    #'There is always light behind the clouds.',
    'Life isn’t about finding yourself.',
    'Life is about creating yourself.',
    'Winter has come.',
    "The cloth was so smooth that it seemed to run through her fingers like water.",
    "I like rice.",
  ],
  'negative': [
    # 'The future starts today, not tomorrow.',
    'It always seems impossible until it\'s done.',
    'A goal without a plan is just a wish.',
    # 'A wise man makes more opportunities than he finds.',
    'A quitter never wins, and a winner never quits.',
    'She had left all that remained of her money.',
    'The tasks of hunting out the last remnant of the ruffians were left to them.',
    'Throw it in the air on a breezy day.',
    'The last oaks had been cut down or burned out a hundred years ago.',
    'Every noble house has its words.',
    'The poor man was half mad.',
    'Is it the wildlings?',
    'He saw the dread on her face.',
    'She took her husband\'s hand.',
    'His second father had become a brother as well.',
    'Where the king goes, the realm follows.',
    'The first step is always the hardest.',
    'A word to the wise is sufficient.',
  ],
}
test_data_0310 = { 

      # **Guideword:** 'THE' + ADJECTIVES, SPECIFYING
      # **Guideword type:** FORM/USE
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'the' + adjectives in a noun phrase, to specify. 
        
  'positive': [
    'I saw the new students coming into the dormitory.',
    'You tell me that the old building is covered with blue sheets now.',
    'Did you manage to get out of the boring class?',
    'You let us know what happened to the old television.',
    'Charlie will try to find the better seat in the car.',
    'They were so confused with the new evidence.',
    'There is something left in the new printer in the office.',
    'You found something on the wooden table.',
    'When they left for Toronto, they found some seats left on the unpopular flight.',
    'You bought the new phone yesterday.',
    'What they are expected to do for the next two hours in the airport?',
  ],
  'negative': [
    'How did you know about the news yesterday?',
    'I had no idea what I was supposed to do when I started the job.',
    'I hope you will get better soon.',
    'We could not hear what the professor said clearly.',
    'All the students felt the office hours were too short.',
    'The papers are all sitting in this room.',
    'They do not like it when people use their cars without permission.',
    'Would you mind reminding me which station I need to go?',
    'Where do they usually go to have a nice cup of coffee?',
    'The document is attached that I think you will need for the reservation.',
    'Is he available next Tuesday for the meeting?',
    'What made you want to get involved in this club?',
    'We stayed up all night watching lots of movies.',
    'She knew she was meant to succeed at that point in her life.',
    'What did Charlie tell you to do?',
    'If you have any questions, you may want to go to the office hours.',
    'The witness confused the police with her ambiguous account of the accident.',
    'How did you know about this position?',
    'Sooner or later, he will realize the fact.',
    'That red car over there is being towed.',
  ],
}
test_data_0311 = {
    # **Guideword:** 'THE' + SUPERLATIVES
    # **Guideword type:** form
    # **Super category:** determiners
    # **Sub category:** articles
    # **Lexical Range:** none
    # **CEFR level:** A2
    # **CAN-DO:** Can form a noun phrase with 'the' + superlative adjectives + noun.
    'positive': [
        "The best place is La Baule, which is Europe's biggest beach.",
        "It has the latest technology.",
        "It was the most expensive mobile phone in the shop.",
        "We must also work out the next best policy.",
        "We must also work out the second best policy.",

        "Time is the most important thing of all.",
        "It is the least important thing of all.",
        "Hw is the greatest conductor that ever lived.",
        "This is the best football team.",
        "He is the shyest man alive.",
    ],
    'negative': [
        'Have you been to Tokyo?',
        'Have you gotten sick?',
        "I've just watched a football competition with my family and friends.",
        'Have you watched it?',
        'I left my mobile in your house, have you seen it?',

        "Will you come by bus?",
        "Will you come with any friends?",
        "What will come?",
        "Could you meet me at my home at 7 pm?",
        "Could you look for it?",

        "Would you like to go with me to the U2 concert?",
        "Will you come with me?",
        'I have never tried it.',
        "I bought a beautiful pink skirt and a white top.",
        "Lysiane is taller than me and she has short black hair.",

        "It is a beautiful old city and there is the old wall around the city.",
        "I left my small white bag.",
        "Don't forget to wear old, comfortable clothes.",
        "What have you done?",
        "I like oranges the best.",

        "You should make the best of your time.",
        "I am not the least afraid to die of cancer.",
        "Smoking is a bad habit, to say the least.",
        "That is most kind of you.",
    ],
}

test_data_0312 = { 

      # **Guideword:** 'ANOTHER'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'another' with singular nouns. ► pronouns ► determiners 
        
  'positive': [
    'Some people say that Trump is another Hitler.',
    'I think you should see another doctor.',
    'Can I get another piece of cake, please?',
    'Jasmine and I are having another baby.',
    'You should go to another school.',
    'Let’s try another restaurant.',
    'The traffic is jammed today, so let\'s go another day.',
    'I\'ve decided to stay in San Francisco for another month.',
    'She has been living with another person since she dropped out of high school.',
    'I don\'t think we will see another you in 100 years.',
  ],
  'negative': [
    'Children often call each other names.',
    'Where are the other books?',
    'Do you guys have any other questions?',
    'I wish we had understood each other better.',
    'I think the other one looks better.',
    'Are any other shirts on sale?',
    'He has no other t-shirts than the one he is wearing now.',
    'He always hangs out with some other girls instead of his wife.',
    'I threw away the other books.',
    'I like the other design better.',
    'You look like each other.',
    'I like other colors better than that.',
    'There should be other ways of dealing with this issue.',
    'My daughters don\'t talk to each other.',
    'We can mail each other and video chat anytime.',
    'We have other colors if you want.',
    'They took to each other instantly.',
    'I like the other color better.',
    'Do you have any other questions?',
    'The other three passengers were unhurt and alive.',
    'Do you know each other?',
  ],
}
test_data_0313 = { 

      # **Guideword:** PREPOSITION + NO ARTICLE
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use no article before an increasing range of nouns in some fixed expressions with prepositions. 
        
  'positive': [
    'I can get there by bicycle.',
    'I came home on foot.',
    'Dad goes to work at night.',
    'I know the subject by heart.',
    'The two countries have been at war for nearly 40 years.',
    'I went to school by car.',
    'The criminal went to prison.',
    'I am going to school.',
    'She is in hospital.',
    'The kids went to bed.',
  ],
  'negative': [
    'They go on trips five times a year.',
    'This is a different sky from the one I knew in the past.',
    'There is a young man.',
    'He waited for his friends for an hour.',
    'Please pass me the salt.',
    'I walk home under a dark sky.',
    'The book was interesting.',
    'Can I use the pen?',
    'It was a rather warm day.',
    'He is an Einstein of the 21st century.',
    'I’d like to invite you to a dinner.',
    'What did you think of the hotel?',
    'She takes piano lessons twice a week.',
    'We had a call from a Mr. Brown.',
    'A bird flies in the sky.',
    'Money is a reason why I like him.',
    'I stayed at a hotel in New York.',
    'She goes to the church.',
    'I want a pair of socks.',
    'A boy is standing by the post office.',
  ],
}
test_data_0314 = { 

      # **Guideword:** NO ARTICLE
      # **Guideword type:** FORM/USE
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use no article before an increasing range of singular and plural nouns when referring to things in general. 
        
  'positive': [
    'Vegetables are sold at the far end of the store.',
    'I like summer the best.',
    'Apples are good for you.',
    'Girls are better than boys.',
    'I ate lunch at the restaurant.',
    'We had bacon and eggs for breakfast.',
    'I have breakfast at seven every morning.',
    'Salt is necessary for cooking.',
    'I like apples and oranges.',
    'Cars are usually kept in garages.',
  ],
  'negative': [
    'The moon is revolving around the earth.',
    'He is an Einstein of the 21st century.',
    'What did you think of the hotel?',
    'I stayed at a hotel in New York.',
    'This is a different sky from the one I knew in the past.',
    'I bought an orange in the market.',
    'A child needs a parent\'s love.',
    'Would you open a window?',
    'I can’t afford to buy a Sony.',
    'I bought a bag.',
    'She goes to the church.',
    'I walk to my house home under a dark sky.',
    'A long time ago, there was an old man and an old woman.',
    'I’d like to invite you to a dinner.',
    # 'The old man went into the mountain to cut down trees.',
    'The climate in the Sahara Desert is very hostile.',
    'Do you know the actress from the movie?',
    'There is a young man.',
    'Can I use the pen?',
    'The sun is shining.',
  ],
}
test_data_0315 = { 

      # **Guideword:** ONE MORE (WITH 'ANOTHER')
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'another' to talk about something additional. 
        
  'positive': [
    'Jasmine and I are having another baby.',
    'I got another year older again.',
    'Please lend that to me for another week.',
    'The bad weather continued for another few weeks.',
    'They won\'t be ready for another month.',
    'This weather will probably stay the same for another couple weeks or so.',
    'I object to waiting another year.',
    'I\'ve decided to stay in San Francisco for another six months.',
    'The play was held over for another month.',
    'Can I get another piece of cake, please?',
  ],
  'negative': [
    'I prefer the other color better.',
    'Friends should be faithful to each other.',
    'What are the other people saying about this movie?',
    'The other boys are out now.',
    'My daughters don\'t talk to each other.',
    'I wish we had understood each other better.',
    'There is no other way.',
    'You can bring the others back.',
    'I like other colors better than that.',
    'You look like each other.',
    'We have other colors if you want.',
    'Do you have any other questions?',
    'We are sympathetic to each other\'s problems.',
    'They are on bad terms with each other.',
    'Are any other shirts on sale?',
    'I threw away the other books.',
    'The other three passengers were alive and unhurt.',
    'I’ll check other stores.',
    'One is my younger brother, and the others are my colleagues.',
    'Do you have others like it?',
    'You don\'t understand each other.',
  ],
}
test_data_0316 = { 

      # **Guideword:** DIFFERENT (WITH 'ANOTHER')
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'another' to talk about something different. 
        
  'positive': [
    'We should get another opinion.',
    'I would like to read another book.',
    'Let’s try another restaurant.',
    'I’ll try another color.',
    'Another teacher is coming this week.',
    'Would you like another cup of coffee, or is this one fine?',
    'I have another cellular phone if you don\'t like this one.',
    'I think you should see another doctor.',
    'I drank a cup of coffee, but I think I\'d like to drink another drink next time.',
    'The traffic is jammed today, so let\'s go another day.',
  ],
  'negative': [
    'Do you have any other questions?',
    'The other boys are out now.',
    'You look like each other.',
    'We have other colors if you want.',
    'Are any other shirts on sale?',
    'There were other cars besides my car in the parking lot at that time.',
    'I like the other design better.',
    'One is for her and the other is for him.',
    'Some of the boys were late, but the others were in time for the meeting.',
    'There are other ways to study English.',
    'I think the other one looks better.',
    'My daughters don\'t talk to each other.',
    'Where are the other books?',
    'They took to each other instantly.',
    'I threw away the other books.',
    'Be kind to others.',
    'There is no other way.',
    'I like other colors better than that.',
    'I wish we had understood each other better.',
    'The other three passengers were alive and unhurt.',
  ],
}
test_data_0317 = { 

      # **Guideword:** 'THE OTHER'
      # **Guideword type:** FORM/USE
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'the other' with a singular noun to refer to the second or the opposite of two things, and with a plural noun to refer to one of a set of things. ► pronouns ►  noun phrases
        
  'positive': [
    'This phone is broken, but the other phones are not.',
    'This box is white, but the other box is blue.',
    'Please let us have an answer one way or the other way.',
    'One book is thin, and the other book is thick.',
    'He has two daughters; one is a teacher, and the other daughter is a nurse.',
    'This watch is expensive, and the other watches are cheap.',
    'I can\'t tell one twin from the other twin.',
    'How does my son compare with the other students?',
    'One building was much taller than the other buildings.',
    'Work and play are both necessary to health; the one activity gives us energy and the other activity gives us rest.',
  ],
  'negative': [
    'Can I get another piece of cake, please?',
    'I will try again in different way.',
    'He raised his hands one after the other.',
    'They drove the car one after the other.',
    'I bought this book the other day.',
    'Are any others on sale?',
    'We are in sympathy with each other.',
    'The bad weather continued for another week.',
    'I\'ve decided to stay in San Francisco for another six months.',
    'I received her letter this morning.',
    'Friends should be faithful to each other.',
    'I saw her the other day.',
    'He is the man you met yesterday.',
    'This weather will probably hold for another week.',
    'Otherwise, she would have gone to the cinema with us.',
    'We have this in another color if you want.',
    'They are on bad terms with each other.',
    'I met him on the street the other day.',
    'She looks in another direction.',
    'Jasmine and I are having another baby.',
  ],
}
test_data_0318 = { 

      # **Guideword:** 'THE MORE … THE MORE …'
      # **Guideword type:** FORM/USE
      # **Super category:** DETERMINERS
      # **Sub category:** articles
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the in comparative phrases 'more', 'less', 'worse', 'better … the more', 'less', 'worse …' to talk about one thing that is affected by another. ► comparative clauses 
        
  'positive': [
    'The better you do, the more confident you become.',
    'The more she thought about it, the less she liked it.',
    'The better I get to know her, the more I like her.',
    'The more he talks about soccer, the less I’m interested in it.',
    'The less the singer appeared on TV, the less people were interested.',
    'The more I know him, the more I’m attracted to him.',
    # 'The more I study, the more my confidence level drops.',
    'The more I think about it, the less sure I am.',
    'The more help a man has in his garden, the less it belongs to him.',
    'The worse they do, the worse their morale gets.',
  ],
  'negative': [
    'He likes math better than English.',
    'Turtles live longer than rabbits.',
    'Sleeping is more important than taking medicine when you have a cold.',
    'The teacher spoke more slowly to help us to understand.',
    'Tom runs faster than John.',
    'Which is larger, Tokyo or Hokkaido?',
    'Snakes are more dangerous than rabbits.',
    'You don’t want books more than you want CDs.',
    'I am younger than you.',
    'No other country in the world is smaller than Vatican City.',
    'This chocolate is sweeter than that chocolate.',
    'Japanese is more difficult than English.',
    'My sister is younger than I by three years.',
    'Elephants are bigger than frogs.',
    'Could you sing more quietly please?',
    'This bouquet is better than that one.',
    'The economic growth rate of China is higher than that of Japan.',
    'He is getting taller and taller.',
    'More and more people are texting while walking.',
    'It is becoming more and more important to study English.',
  ],
}
test_data_0319 = {

  # **Guideword:** 'THIS' WITH SINGULAR NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'this' with singular nouns. ► noun phrases ►  pronouns: demonstrative

  'positive': [
    'I don\'t like this weather because it is way too hot.',
    'He might go to Japan this month.',
    'I need more money to pay for this room.',
    'Refs don\'t want this game to be a blowout in the 1st quarter.',
    'This information is not enough to solve our problems.',
    'We will go to the beach this summer.',
    'She is falling in love with this kid because he is so adorable.',
    'When he read this article, he got surprised and went out of the room.',
    'People tend to forget how this country was founded.',
    'She still remembers this song which I sang for her last birthday.',
  ],
  'negative': [
    'This is my first to time to visit Japan.',
    'This is your pen which I borrowed yesterday.',
    'Since this is too hard to understand, I give up on talking with her.',
    'If you still like this, I can give it to you.',
    'Don\'t mess around like this.',
    'You forgot your jacket in his room on that day.',
    'I still remember about that crazy night.',
    'That video was taken by my mother and she loved it.',
    'When my sister was young, she loved to watch these movies.',
    'My skin is getting tanned these days.',
    'These chairs were made in China and they are easily broken.',
    'I hate those who smoke on the road.',
    'Those are my new clothes which I bought last month.',
    'Those books are way too advanced for him since he\'s only about eleven years old.',
    'His brother used to play these card games when he was young.',
    'These Japanese foods are pretty delicious.',
    'It is quite hard for him to understand these problems.',
    'You should consider it more because it might become a serious problem.',
    'These are my special memories in my childhood.',
    'This is my wife and she is such a nice woman.',
  ],
}
test_data_0320 = {

  # **Guideword:** 'THIS', POINTING
  # **Guideword type:** USE
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'this' in a limited range of contexts to refer to places
  # from the speaker's or writer's point of view. ► noun phrases ►  pronouns: demonstrative

  'positive': [
    'I don\'t like this place because many people have seen ghosts at night.',
    'I went to this high school and it was my best memory of my life.',
    'This place is so much fun since there are lots of people walk around.',
    'I always hated the plumbing in this house.',
    'The owner of my company used to own this shop.',
    'I went to school near this park and when I came home to Florida for the holidays, this special place was on my list of must-visit destinations.',
    'It takes about 20 minutes from my house to this station.',
    'Just tell me I don\'t have to stay in this room right now.',
    'When I was young, I often came to this baseball stadium with my father.',
    'He constantly said how much he hated this company and how he would take his business elsewhere.',
  ],
  'negative': [
    'You forgot your jacket in her room on that day.',
    'His college is located near my house.',
    'That convenience store is closed today.',
    'Have you ever been to that cafe before?',
    'That is my dream place to settle down in the future.',
    'I love those kinds of restaurants because they are quite sweet and delicious.',
    'This is the hospital where I was born.',
    'He is pretty sure that this is the place where he lost his cellphone.',
    'These world heritage sites are pretty famous and well-known all over the world.',
    'If you wonder, I can meet you at these cafes before you go to the school.',
    'I would like to ask you where the train station is.',
    'The police station is located close to the bar we went last time.',
    'My sister doesn\'t know which airports she will depart from.',
    'I want to work at that company because there are lots of talented people working together.',
    'My father has never been to that Korean restaurant where we went yesterday.',
    'This is the high school where my wife studied.',
    'Those universities are the best universities in Japan.',
    'There are lots of souvenir shops near the station.',
    'My friend told me that the amusement park in Osaka is much higher than the one in Tokyo.',
    'She might go to her favorite cafe for studying.',
  ],
}
test_data_0321 = {

  # **Guideword:** 'THIS', FUTURE
  # **Guideword type:** USE
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'this' with time and date words to refer to 'the one that's coming'.

  'positive': [
    'I will go to Thailand this summer.',
    'This spring will be perfect if you stay with me.',
    'My sister might have free time this weekend.',
    'My family will be away on this Friday, so you can come over.',
    'His goal this year is to make a new girlfriend.',
    'Her brother might come back to her house this evening.',
    'I will start my new job from this July.',
    'This winter will be colder than last winter.',
    'I have to submit my homework by this weekend.',
    'My father will be pretty busy this summer vacation, so I guess we can\'t hang out together.',
  ],
  'negative': [
    'I still remember that night when you got lost in Thailand.',
    'That summer was one of the best times of my life.',
    'We went swimming in the sea last summer.',
    'My brother got drunk so bad last Friday, that he couldn\'t remember anything.',
    'My mother has been sick for the last few months.',
    'I am learning programing these days.',
    'These last few weeks were quite hard time for me to work.',
    'She might come back to Japan in March.',
    'My baseball team normally practices from Monday to Friday.',
    'My father doesn\'t eat anything in the morning.',
    'I normally eat some snack in the evening to get some energy.',
    'That shop will be closed tonight, so we have to go to other shops to drink.',
    'I couldn\'t be in the class the day before yesterday '
    'My sister was sick and I had to take care of her all day.',
    'She forgot the way to this cafe from her house.',
    'I might be away from Tokyo for the next few days because of my job.',
    'The next decades will be the digital era and lots of new technology will be invented.',
    'My family wants to go to Kyoto on the coming Saturday.',
    'Last Friday party was just amazing and people would love to do it again.',
    'I have nothing to do in the afternoon.',
    'TV show will be on TV next Tuesday\'s night.',
  ],
}

test_data_0322 = { 

      # **Guideword:** 'THIS' WITH UNCOUNTABLE NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** 2.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'this' with uncountable nouns. ► noun phrases ►  pronouns: demonstrative
        
  'positive': [
    'This evidence will keep him safe for a while.',
    'My mother told me that this food is healthy food and good for me. ',
    'Does this tea taste better with sugar?',
    'This rice tastes better than the one I had in the restaurant.',
    'Why does this air feel so humid and dusty at the same time?',
    'Didn\'t they think this love would last forever?',
    'It looks like this water contains something bad.',
    'This knowledge would last in my memory forever.',
    'What did you do to make this money?',
    'It is true that this research will be used for a better future.',
  ],
  'negative': [
    'I can hear many people singing the same song again and again.',
    'This song sounds very good to me.',
    'The rice I had yesterday was so good that I want to recommend everyone to try it at least once.',
    'How did you get to know about this computer?',
    'What did you do to improve this?',
    'We do not own this.',
    'I am listening to this channel and I like it a lot.',
    'What you do not know is written on this page of the book.',
    'This is a nice sheet of paper.',
    'She does not need to use the money to travel to Toronto.',
    'How do they know if this train goes to Toronto?',
    'Have you ever considered applying to this job?',
    'The personality of mine fits into the qualification pretty well.',
    'You could tell what is important and what is not.',
    'We are pretty sure that that book is good for an introduction.',
    'I can tell that that evidence would not work for anything.',
    'They cannot be prouder of their research.',
    'I don\'t think this would work nicely for both of us.',
    'Where did she visit to find that out?',
    'When does he think he could finish everything by?',
  ],
}
test_data_0323 = { 

      # **Guideword:** 'THIS' POINTING
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** 2.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'this' in an increasing range of contexts to refer to places and things from the speaker's or writer's point of view. ► noun phrases ► pronouns: demonstrative
        
  'positive': [
    'How do you know about this place?',
    'Has Charlie been to this area of the town?',
    'Would you like to live in this house?',
    'What did he do to improve this result?',
    'You should not drink this water since the pipe was broken.',
    'Where do you think I can find the same shirt as this one?',
    'Do you know anything about this kid?',
    'We are not sure about this issue.',
    'You can contact me at this email address.',
    'Can they try to hold this door for a while longer?',
  ],
  'negative': [
    'I do not think it is a good idea to get a new car now.',
    'That place seems sketchy and I would avoid going there.',
    'Can you think of any other options?',
    'Don\'t you think this is a good place to take photos of flowers?',
    'The company is doing great this year, which made me happy.',
    'Charlie has never heard of it before.',
    'Would you be open to moving your car to another place?',
    'Why did he resign from that role in the company?',
    'Would you mind telling me what happened to that?',
    'Charlie has not really attended a class before with that professor.',
    'You do not need to go to the school, do you?',
    'I was quite surprised at the fact that they have never been there before.',
    'I need to go shopping this afternoon in order to get some groceries.',
    'Can you hear the voice through the wall?',
    'We went for a walk that night.',
    'Could you please let us know when you will be back?',
    'What seems true may not be actually true.',
    'She wonders that they do not know much about it.',
    'Have you ever heard of it before?',
    'Can you hear me singing in the bathroom?',
  ],
}
test_data_0324 = { 

      # **Guideword:** POINTING
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'this' in an increasing range of contexts to refer to places and things from the speaker's or writer's point of view. ► noun phrases ► pronouns: demonstrative
        
  'positive': [ 
    'They told me that they had heard this song before.',
    'This rule does not apply to me.',
    'Would this plan go very well?',
    'You can use this number to call me anytime.',
    'This place reminds me of my childhood.',
    'In this house, I rule everything.',
    'He would be open to taking over this class.',
    'You knew about this university.',
    'She does not like it when I use this pencil to write something.',
    'I saw this airplane yesterday.',
  ],
  'negative': [
    'Can I get a list of people I need to contact?',
    'They do not think that is the right way to treat people.',
    'They would assign me the task either way.',
    'She just gave up looking up the names of everyone.',
    'Has Charlie started working on the assignment?',
    'She does not think I can carry much water all at once.',
    'Have you ever heard of that place before?',
    'Charlie would not be able to help me with that project.',
    'Did you hear the people surprised at the amount of soda we ordered for the event?',
    'He just bought a new laptop and he is very happy about it.',
    'The new air conditioner is working totally fine.',
    'We can do whatever we want to do here.',
    'We knew there was a new president in the college.',
    'I said I do not want to do that.',
    'That sounds like a feasible idea.',
    'I wish I had more power over them.',
    'Don\'t you ever consider yourself very friendly?',
    'Will you want to take over that task?',
    'What she expected came true, which made her very happy.',
    'They told him they were not a fan of gossips.',
  ],
}
test_data_0325 = { 

      # **Guideword:** 'THIS', ALREADY MENTIONED
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'this' to refer to something with immediate relevance which has already been mentioned. ► noun phrases ►  pronouns: demonstrative
        
  'positive': [
    'There’s a building near the station. My uncle is the owner of this building.',
    'My mom wrote me a letter. This letter makes me cry overtime I read it.',
    'Do you know someone who can clean my room and get this cleaning done by tomorrow?',
    'My father lends me his watch sometimes. I like this watch because the design is delicate.',
    'Lara had a beautiful vase in her living room. She likes this vase very much.',
    'I met the city governor last week. This occasion helped me understand the crisis of my home city.',
    'We are looking for a new waiter. If you are interested in this job, please give me a call.',
    'She gave a beautiful picture to me. I like this picture very much.',
    'I encountered a man I had never seen before. Then I was spoken to by this stranger.',
    'Marry was happy that she passed the entrance examination. She studied hard for this examination.',
  ],
  'negative': [
    'This is the house where Tom used to live in.',
    'It has taken me this long to get the information.',
    'I don’t know why she hasn’t been back before this.',
    'Hold your racket like this.',
    'I want to play the violin. The reason why I want to play that instrument is that my sister plays it well.',
    'This is why I never buy beauty products at a convenience store.',
    'My aunt is the founder of this company.',
    'She gave me a wallet and I immediately liked that wallet since the color was pink.',
    'This is my first visit to London.',
    'I heard he did a presentation on his new theory. We have a lot of evidence which supports that theory.',
    'This is how we learn Chinese.',
    'We spent about two hours talking about this and that in a coffee shop.',
    'This or that person may disagree with this proposal.',
    'Perhaps you’d better make a note of this.',
    'I have to inform all the teachers about this.',
    'My mother is not usually this busy.',
    'This is the reason why this book sells well.',
    'I found a new hospital in the grocery store. You should go to that hospital.',
    'I gave my brother a new bike. That bike was the reason why he broke his leg.',
    'This is how he got through the crisis.',
  ],
}
test_data_0326 = { 

      # **Guideword:** 'THAT'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'that' with singular nouns. ► noun phrases ►  pronouns: demonstrative
        
  'positive': [
    'What would you do if you lived on that island by yourself?',
    'Don\'t you know about that student?',
    'How did you come here from that station?',
    'We do not think that that cat is not cute.',
    'Charlie said that he would travel to that island sometime next year.',
    'They said they wanted to watch that film last Sunday.',
    'Could you please move that TV to another room?',
    'Please be quiet in that building.',
    'When we got out of the house, we heard that song which we were familiar with.',
    'I remember that I took that course as well.',
  ],
  'negative': [
    'Those people just moved into the house yesterday.',
    'They are not sure about this fact, but it will be fine.',
    'Did you hear about this new boss?',
    'Would you mind telling me what happened to those people?',
    'Are you sure that no one showed up at the meeting?',
    'How did you do all of this in such a short time?',
    'I am reading this book called World Order.',
    'It is surprising for all of us to know that they are doing great in this company.',
    'Have you ever tried this new chair?',
    'Could you please remind me of the task that I am supposed to finish by the end of the day?',
    'Has Charlie been interested to know about that?',
    'Should we go to this building to take the course?',
    'It is somewhat sad to know that most of them leave the place quite quickly.',
    'Why don\'t you talk to your professor about the assignment?',
    'What I was hoping for him was different from what she was hoping to do in this place.',
    'Where did you go this Sunday?',
    'I heard that you could go upstairs if you want.',
    'What are they going to do if you cannot find any events?',
    'What would you do if there is nothing but this desk in your life?',
    'Those people seem to worry a lot about their future and so do we.',
  ],
}
test_data_0327 = { 

      # **Guideword:** 'THAT', POINTING
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'that' to talk about or point to things which are further away in time and space from the speaker or writer
        
  'positive': [
    'Why did Charlie go to that building?',
    'Have you ever thought about that summer?',
    'Is it true that you still remember that concert?',
    'Do you remember that time when we were all left in the train?',
    'I do not think that that park is the one we have been looking for.',
    'You should not go to that building.',
    'Could you please remind us that we are not supposed to go into that house while they\'re doing the remodiling?',
    'Would you try to get closer to that place?',
    'Where has Charlie been for all that time?',
    'Don\'t go to that park at night.',
    'They love that.',
  ],
  'negative': [
    'Do you know that I love you?',
    'Shall we go to the restaurant tonight?',
    'Haven\'t you ever heard of this famous person?',
    'Are you willing to help us carry the box?',
    'It was surprising to know that he has never been there.',
    'Would you mind doing this instead of me?',
    'Charlie will be there to help you out.',
    'We are going to have our first class of the term next Tuesday.',
    'His answer was not what his professor was expecting.',
    'Have you ever heard this story of his?',
    'She was going to get a new laptop, but she does not have enough money.',
    'Have you already tried the new tea?',
    'I just got a new lamp for my room and I am excited to use it.',
    'Is it true that we are going have a new boss in our team next month?',
    'Do you know anything about it?',
    'It was interesting to hear about it from this professor.',
    'May I ask you a question about your work?',
    'Why did they say that they don\'t trust us?',
    'Where are you right now?',
    'They heard the sound of someone screaming.',
    'Should they need to think about it even when they are not on duty?',
  ],
}
test_data_0328 = { 

      # **Guideword:** 'THAT', ALREADY MENTIONED
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'that' to refer to something which has already been mentioned. ► noun phrases ►  pronouns: demonstrative
        
  'positive': [
    'Do you see the painting on the wall? Artists are attracted to that painting.',
    'I want to play the violin. The reason why I want to play that instrument is that my sister plays it well.',
    'She gave me a wallet and I immediately liked that wallet since the color was pink.',
    'I heard he did a presentation on his new theory. We have a lot of evidence which supports that theory.',
    'Jack wrote a song for me. Ever since, that song has been my favorite.',
    'I went to the park with my friend. That park has three swings.',
    'Cindy gave me a book. I wanted to read that book for a very long time.',
    'I found a new hospital nearby to the grocery store. You should go to that hospital.',
    'Do you see the man wearing a green sweater? That person is my father over there.',
    'I gave my brother a new bike. That bike was the reason why he broke his leg.',
  ],
  'negative': [
    'There’s a building near the station. My uncle is the owner of this building.',
    'That’s the dictionary I have been looking for.',
    'My mom wrote me a letter. This letter makes me cry every time I read it.',
    'My aunt is the founder of this company.',
    'It was yesterday that Jacob explained the accident to me.',
    'After that, she studied in America for two years.',
    'Lara had a beautiful vase in her living room. She likes this vase very much.',
    'My father lends me his watch sometimes. I like this watch because the design is delicate.',
    'That’s why I applied for a week’s leave of absence.',
    'That is the boy whom I talked with yesterday.',
    'We are looking for a new waiter. If you are interested in this job, please give me a call.',
    'We spent about two hours talking about this and that in a coffee shop.',
    'Can I have a bite of that chocolate cake?',
    'This or that person may disagree with this proposal.',
    'I stayed at that hotel for two months.',
    'He got up so early that he saw the sun rise.',
    'Where did you go after that?',
    'That is the park where I often went in my childhood.',
    'I encountered a man I had never seen before. Then I was spoken to by this stranger.',
    'I went to that concert with my sister.',
  ],
}
test_data_0329 = { 

  # **Guideword:** 'THESE'
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** 2.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'these' with plural nouns. ► noun phrases ►  pronouns: demonstrative 
    
  'positive': [
    'My friend gave me these books because he read all of them.',
    'My friend gave me these things.',
    'I took these photos.',
    'I took these things because they looked beautiful.',
    'I have been to these countries because I wanted to visit them.',
    'I have been to these places because my friends stayed there.',
    'These chapters were written and sent out as a serial to my son.',
    'I want to see these people because they are beautiful and famous.',
    'He wakes up early in the morning these days.',
  ],
  'negative': [
    'My friend gave me these because I asked him.',
    'I have been there because they are such beautiful countries.',
    'These are difficult times.',
    'I took these because they could be lovely photos.',
    'He enjoyed their last few days together.',
    'Those clothes are cute.',
    'Those dishes are piled up.',
    'Those who brought me up are dearer to me than those who only brought me forth.',
    'There are those who believe in UFOs.',
    'Those clothes were old.',
    'All of those were amazing.',
    'Those flowers are charming.',
    'Those are only rumors.',
    'Those make your eyes tired.',
    'I am doing those procedures now.',
    'I love this book so much.',
    'You can call this person any time.',
    'You didn\'t know about this at all.',
    'She can buy this pair of shoes if she wants.',
    'This is my first time to eat seafood.',
    'This system is out of date.',
    'I want to buy that desk.',
    'My friend wants to know about that guy.',
    'That house is my friend\'s.',
    'That photo was an amazing one.',
  ],
}
test_data_0330 = { 

      # **Guideword:** 'THESE' POINTING
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'these' to refer to places and things from the speaker's or writer's point of view. 
        
  'positive': [
    'Charlie did not know that these buildings are very famous in Toronto.',
    'These assignments are killing me emotionally.',
    'I like these decorations because they look so beautiful.',
    'I knew you heard about these companies.',
    'You are supposed to work on these tasks.',
    'These photos remind me of my childhood.',
    'These watches mean a lot to me.',
    'These dates are not available for us anymore.',
    'I am personally not a big fan of these projects.',
    'These classes I am taking right now are so interesting that I do not want to miss any lectures.',
  ],
  'negative': [
    'They asked me what this was.',
    'These are the best days of your life.',
    'Where would you want to work on this project?',
    'The questions are these.',
    'Would you be available for those hours by any chance?',
    'Charlie is going to visit Toronto next week to see some of his relatives.',
    'Would you be willing to take this task?',
    'Why did you decide to change your career?',
    'He does not want to lose track of what he has done in the past.',
    'We like listening to the sound of winds.',
    'I did not know a lot about those subjects.',
    'I\'ll take these.',
    'How did you get to this position?',
    'Did she get used to that?',
    'Where did you go for a walk?',
    'What she has done is tremendous and people appreciate it so much.',
    'Those people are waiting in line for many hours to get some rare collectibles.',
    'Describe yourself in a word.',
    'These are not impossible dreams.',
    'We could hear people talking about what we made.',
    'This is something she mentioned at the meeting.',
    'Is it true that those do not belong to you at all?',
    'I am wondering if I am qualified for this position.',
    'This is not the only case that she mentioned.',
  ],
}
test_data_0331 = { 

  # **Guideword:** 'THESE', ALREADY MENTIONED
  # **Guideword type:** USE
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** 1.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'these' to refer to things with immediate relevance or which have already been mentioned. ► noun phrases ►  pronouns: demonstrative
    
  'positive': [
    'UNIQLO, ZARA, and H&M are my favorite fashion brands, and these are all cheap.',
    'I have been around 30 provinces, and these are all nice and beautiful.',
    'I bought three new shoes and these are quite cheap and nice.',
    'My friend has three houses in Tokyo and these are all big and cozy.',
    'I have a TV, laptop, and cell phone in my room, and I usually use these when I stay there.',
    'You can\'t choose what to eat at this restaurant, but these foods here are all nice.',
    'All my bags in my room are cute but old, so I decided to sell these and buy a new one.',
    'There are Kyoto, Osaka, Kobe in Kansai, and you should visit these cities if you are free.',
    'I usually eat an apple, bread, milk, and eggs in the morning because these are healthy.',
    'I have been to 20 countries in Asia because these are close to Japan and easy to go to.',
  ],
  'negative': [
    'These are my favorite fruits.',
    'These people are all my friends.',
    'These are people whom I can trust for life.',
    'These are my treasure which I had since I was a child.',
    'I know these people very well.',
    'Those clothes are cute.',
    'Those dishes have piled up.',
    'Those who brought me up are dearer to me than those who only brought me forth.',
    'There are those who believe in UFOs.',
    'Those clothes were old.',
    'I want to change this cellphone to a new one.',
    'This radio is broken.',
    'I prefer this juice over others.',
    'She can buy this pair of shoes if she wants.',
    'This is my first time to eat seafood.',
    'This system is out of date.',
    'That country is the best country I have ever been to.',
    'I want to see that girl.',
    'That house is my friend\'s.',
    'That photo was an amazing one.',
  ],
}
test_data_0332 = { 

  # **Guideword:** 'THOSE'
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** 2.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'those' with plural nouns. ► noun phrases ►  pronouns: demonstrative
    
  'positive': [
    'Please bring down those towers for me.',
    'Those walls are thin.',
    'Those tears are artificial.',
    'I love those dishes so much.',
    'Those dresses suit you.',
    'The price of those materials is too high.',
    'Those words were a little strange.',
    'I don\'t understand those words.',
    'Those jackets must look good on my grandchild.',
    'Those products stopped rusting.',
  ],
  'negative': [
    'These are my favorite fruits.',
    'These people are all my friends.',
    'These are people whom I can trust for life.',
    'These are my treasures which I\'ve had since I was a child.',
    'I know these people very well.',
    'Those are my friends who stay over there.',
    'Those are mine and I can give them to you.',
    'Those were my memories when I was young.',
    'Those are products that require repair.',
    'I don\'t know the difference between those.',
    'I feel better when I see those.',
    'Whenever I am watching those, I get better.',
    'I will add those to the cart and order.',
    'He hid those in the closet.',
    'I will load those into the truck.',
    'Those had bad timing.',
    'Those were put up in the cube.',
    'I want to exchange this cellphone for a new one.',
    'I will fix that radio tomorrow.',
    'I prefer this juice over others.',
  ],
}
test_data_0333 = { 

  # **Guideword:** 'THOSE', ALREADY MENTIONED
  # **Guideword type:** USE
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'those' to refer to things which have already been mentioned. ► noun phrases ►  pronouns: demonstrative
    
  'positive': [
    'I see big buildings over there and those buildings are all ornate.',
    'My father bought nice jackets but those clothes were expensive.',
    'There are delicious desserts at that restaurant and I love those.',
    'My friends play baseball and those people play well.',
    'I want to buy new skirts and those clothes are expensive.',
    'It is black and white and I love those colors.',
    'There are lions and bears in the zoo, and I want to touch those animals.',
    'Many students come to join the festival every year, and those boys and girls always visit that shrine.',
    'The children in this park are all male, and those boys all go to the same school.',
    'He is playing the guitar in the park, but the snow muffles those sounds.',
    'I saw some dreams yesterday and those felt so real.',
    'I love Japanese TV programs because those are funny.',
    'You can use pencils in my room because those are mine.',
    'There have been many memories and those are all nice.',
  ],
  'negative': [
    'Those are my friends who stay over there.',
    'Those are mine and I can give them to you.',
    'Those are products that require repair.',
    'I don\'t know the difference between those.',
    'I feel better when I see those.',
    'Whenever I am watching those, I get better.',
    'I will add those and order.',
    'He hid those in the closet.',
    'I will load those into the truck.',
    'Those were put up in the cube.',
    'Please bring down those towers for me.',
    'Those tears are artificial.',
    'Those clothes suit you.',
    'The price of those materials is too high.',
    'Those words were a little strange.',
    'I don\'t understand those words.',
    'Those clothes will look good on my grandchild.',
    'I love those who are nice and friendly.',
    'Those foods are my favorite.',
    'Those games look fun and I want to play now.',
  ],
}
test_data_0334 = { 

      # **Guideword:** 'THOSE' POINTING
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'those' to talk about or point to things which the speaker or writer perceives to be further away in time and space. 
        
  'positive': [
    'Those old memories are my treasure.',
    'Those buildings are all my company\'s.',
    'I love those flowers which are sold over there.',
    'Those shops are just over there.',
    'I will call those people who stayed there last night.',
    'I took those food photos which looked delicious.',
    'Those guys who stay there are my friends.',
    'Those were my ideas which my friend just presented.',
    'Those are the types of places you are heading.',
    'My friends love those kinds of food that they cook at that shop.',
  ],
  'negative': [
    'I love that game because it is fun.',
    'These are such nice bags.',
    'You can buy these if you want.',
    'This should be correct.',
    'I can take these kids to the park.',
    'That key is for my house.',
    'These people are kind of bad.',
    'That is my dream.',
    'This is my house.',
    'That window is way too big.',
    'what is that thing over there?',
    'That was so cool.',
    'You can talk to that person because he is reliable.',
    'You can take this gift if you want.',
    'These new shops are nice and clean.',
    'This room is big enough to live in.',
    'That person is my father in law.',
    'I love these pencils so much.',
    'This is my new friend Mike.',
    'This is my first wallet which I bought by myself.',
  ],
}
test_data_0335 = { 

      # **Guideword:** 'THIS', PAST
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'this' with time and date words to refer to the past. 
        
  'positive': [
    'I went skiing with my family this winter.',
    'I was busy all this week.',
    'I met your sister this morning.',
    'She graduated from high school this year.',
    'He took an entrance exam this month.',
    'She was free this evening.',
    'I had a great vacation this summer.',
    'We met for the first time this spring.',
    # 'I had nothing to do this weekend.',
    # do -> weekend (dobj)
    'We will play baseball this afternoon.',
  ],
  'negative': [
    'This is the beginning.',
    'This guy is amazing.',
    'This brings back memories.',
    'Do you want to drink this?',
    'This room stinks.',
    'Please step this way.',
    'This is the first time in two years.',
    'This stings my eyes.',
    'This fabric is thick.',
    'I did not expect this.',
    'This tree has deep roots.',
    'This is one of the last resources we can use.',
    'This is what I\'ve been waiting for.',
    'Stay out of this.',
    'This is artificial beauty.',
    'I\'m leaving this company.',
    'You won\'t get away with this.',
    'This medicine tastes sweet.',
    'This is good wine.',
    'I will cross this river.',
  ],
}
test_data_0336 = {

  # **Guideword:** 'THIS', IN NARRATIVES
  # **Guideword type:** USE
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** None
  # **CEFR level:** C2
  # **CAN-DO:** Can use 'this' with nouns and noun phrases in a narrative to create a sense of immediacy.

  'positive': [
    "There's this flame of passion between them.",
    "It's a story where there's this old man who makes a marionette that comes to life.",
    "In our group there was this girl, tiny and fragile, very sensitive; she had a special way with words.",
    "There was this girl at this school close to mine, and she was a great pianist.",
    "There was this awesome song I heard once, everyone loved it.",
    "I just don't understand why there is this impatience for a developer to push a game out the door as fast as possible.",
    "There was this circuit-training boot camp class that was just brutal.",
    # parser error
    # "I remember back in school when we were chatting with Tanzanian kids, there was this one guy named Innocent.",
    "There was this girl from middle school who used to wear grandma sweatshirts all the time.",
    "Sure but there is this post on reddit showing how the artist made the piece.",
    "There probably have been many such situations, but there is this one girl I still could punch myself for.",
    "During his day he noticed a small boy appeared to be following him; where ever he stood, there was this boy behind him.",
    "I've been doing some research, and apparently there is this Australian guy who gives tutorials on how to make stuff.",
  ],
  'negative': [
    "This starts to feel like a class debate, I love it.",
    "I think everything's been debunked at this point.",
    "There are quite a few people of this sort.",
    "There are few men who can not do this.",
    "You must not open this box until there are instructions to do so.",
    "Why are there no bands like this in Japan?",
    "This is all the money there is.",
    "There is one down this way.",
    "There is a cool breeze this evening.",
    #Parser error 'there' should be adverb
    # "The song that was playing there was this one.",
    "It was enough that this was the end, and there was no way out.",
    "This spring, there was a huge transformation in my life.",
    "I arrived this morning.",
    "This was right after the height of his popularity.",
    "Yeah when I first started playing there was this one uruk.",
    "Although I doubt it will get there, this has the potential to turn downright ugly.",
    "I'm actually going up there this weekend for the first time!",
    "I don't see anything there that states that.",
    "But there's some stuff there that is not terrible.",
    "It looked to me like there were two.",
    "Because of this there is some superstition around left-handed people.",
    "Even if you think something like this, there is no need to vomit these opinions on someones facebook page.",
    "Would it be better to do this there?",
    "I'm pretty sure if let's say LA Galaxy did this there would be the same uproar as if let's say Zenit did it.",
  ],
}
test_data_0337 = {

  # **Guideword:** 'THIS' WITH NOUN AND POSSESSIVE
  # **Guideword type:** FORM/USE
  # **Super category:** DETERMINERS
  # **Sub category:** demonstratives
  # **Lexical Range:** None
  # **CEFR level:** C2
  # **CAN-DO:** Can use 'this' + noun + 'of' + possessive pronoun to highlight something, often in a positive way.

  'positive': [
    "What is more, not only is this rare talent of theirs used for public pleasure but also for international sports success, which makes us all proud.",
    "This characteristic of his is shown in every situation of his life.",
    "This picture of hers is near life‐size.",
    "This arm of mine is as strong as steel.",
    "This car of yours is a real gas guzzler.",
    "This explanation of hers is nothing but an excuse.",
    "This plan of theirs seems awesome.",
    "I corresponded with so many good people from the UG, which is one of the driving factors in this idea of mine.",
    "Check out this comment of mine, and good luck!",
    "It is impossible that this plan of hers will work.",
    "Believe you me, I am watching this thread of yours for sales!",
    "After this claim of yours, I stopped reading your post.",
    "Have fun in this quest of yours.",
    "I know this accusation of yours is very popular amongst my fellow atheists.",
  ],
  'negative': [
    "This is a bag of her own making.",
    "This famous potter makes all of her vessels by hand.",
    "Her cooking was out of this world.",
    "This is a picture of her own painting.",
    "Nothing was heard of her after this.",
    "This is his way of doing things.",
    "A friend of mine is coming this evening.",
    "This cat is a great friend of mine.",
    "A part of this land is mine.",
    "The men of this village went to the mine this morning.",
    "This has happened through no fault of mine.",
    "What business is this of yours?",
    "You just pulled this trick out of your bag in the nick of time.",
    "If this is of your own cat, have you tried doing it in different rooms just to make things a bit more interesting?",
    "This period of your experience is extremely important and necessary.",
    "This of course takes time.",
    "There are plenty of theological justifications for this, of course.",
    "I asked this to another commenter, but they didn't take public transportation a lot.",
    "Do you have any advice for somebody looking to do a trip like this of their own?",
    "I asked this of my parents too.",
    "Do we have any pictures like this of our galaxy?",
    "I highlight the sober part, because that showed me I can totally do this on my own.",
  ],
}
test_data_0338 = { 

      # **Guideword:** EMOTIONAL DISTANCE
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** demonstratives
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'that' and 'those' to convey emotional distance, often to express disapproval.
        
  'positive': [
    'Don’t talk to me with that tone.',
    'Those types of people are fake friends.',
    'Those pretentious girls better stay away from me.',
    'Do not bring in that kind of business to the table.',
    'Be aware of those sketchy people.',
    'Those so-called models are not your role models.',
    'That sort of behavior is not permitted in this household.',
    'Those nasty bugs need to disappear from my house.',
    'I will not put up with that kind of attitude, young lady.',
    'That kind of motivation is cruel.',
  ],
  'negative': [
    'On that day, my brother drove me to school.',
    'I don\'t think there is any way that I can wear that well.',
    'The sale of the product is delayed.',
    'In  that case, you can stay with us for an extra day.',
    'That must have been so hard for your mother.',
    'This contract is invalid.',
    'I needed that money to buy a present for Anne.',
    'The cat has been here for too long.',
    'That’s Carl playing volley ball over there.',
    'It was necessary that I write this thesis.',
    'I need those books in my room.',
    'At that time, I had a huge crush on Paul.',
    'That means that it is easy to get tired of.',
    'There was nothing that corresponded to that.',
    'We like to ride bicycles.',
    'Is that all you are asking for?',
    'That essay will be fine.',
    'I like those candies that you always carry around.',
    'That is too good to be true.',
    'I didn\'t say that with bad intentions.',
  ],
}
test_data_0339 = {

  # **Guideword:** WITH NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** possessives
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use possessive determiners 'my', 'your', 'his', 'her' and 'our' before nouns.
  # ► noun phrases ► possessive pronouns

  'positive': [
    'There\'s a difference between what you describe and what my neighbors have.',
    'There are lots of convenience stores near my house.',
    'I\'m not sure leaving your dream job makes sense after a year even if it is for a promotion.',
    'Your life seems like a lot of fun and I want to be like you.',
    'They gave our money to him.',
    'His sister is older than my older brother.',
    'I somehow had to carry my sister\'s bag since she broke her right arm.',
    'Our company doesn\'t work on the weekend.',
    'There are a bunch of nice guys in our school compared with your school.',
    'It\'s amazing that we can recognize our problem and maintain the proper will to break the addiction.',
  ],
  'negative': [
    'This pencil is not mine, but I will keep it.',
    'These bags are all yours and you have to take them to the airport by yourself.',
    'I didn\'t know that this house is hers.',
    'It is pretty hard for me to eat sushi because it is so fresh and smelly.',
    'Sansa wanted you to come to the restaurant we went last time and eat together.',
    'I have never told him to go out and get some water for me.',
    'She had to take care of herself since she has lost many of the pieces before.',
    'Their class sounds like much more fun compared to mine.',
    'I feel like they don\'t stand that well on their own, and therefore I will start doing a lot more comparative reviews.',
    'I love hearing about someone actually defending themselves in their own home with a weapon.',
    'she killed herself because people actually hated her so bad.',
    'I don\'t agree with it, but I do sympathize with them.',
    'Unless you give him reason to, he won\'t even think to ask.',
    'Most of us barely know about world history since we mainly study Japanese history.',
    'I would love for you to elaborate on how you think I\'m harming him.',
    'Mostly she seems extremely nervous every time they put her on camera.',
    'I would like to introduce myself.',
    'She wanted me to stay, but I had to go home as soon as possible, so I left.',
    'Christianity has grown up like most other religions and divorced itself from obnoxious piety.',
    'I can\'t say anything about its reliability.',
  ],
}

test_data_0340 = { 

      # **Guideword:** SINGULAR NOUN +''S'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use ''s' after singular or proper nouns to indicate possession.
        
  'positive': [
    'I just came back from Cindy’s birthday party.',
    'I thought this was Peter’s jacket.',
    'This is my teacher’s diary.',
    'My mom’s friend works at the bank.',
    'Justin’s sister is the smartest girl in my class.',
    'Spencer’s brand new bag was stolen this morning.',
    'Janet’s father made a speech at the city hall last night.',
    'I borrowed my aunt’s car to go to Canada.',
    'Katherine’s attitude at the party was unacceptable.',
    'My father’s friend lives in Singapore.',
  ],
  'negative': [
    'My brother is sick in bed right now.',
    'Everyone is heading to the auditorium.',
    'He’s a good friend to all of us.',
    'She’s studying for the biology test tonight.',
    'My mother has been a school teacher for over ten years.',
    'Cindy is talking on the phone with her friend from school.',
    'Molly has been working on a project with Kevin for a long time.',
    'It makes me sad to think that no one’s listening to her.',
    'Someone is going to have to cook for dinner.',
    'Anyone is allowed to use the coffee machine.',
    'My daughter is going to study at a college in Ireland next year.',
    'My dad is fishing with his friends this week.',
    'Everybody is watching a French movie in the classroom.',
    'My sister is selling all her stuffed toys.',
    'Louis has been doing volunteer work ever since he graduated from high school.',
    'Lily is working at the supermarket this summer.',
    'Lately, Kevin has been taking the bus to go to school.',
    'Unfortunately, Jasmine is taking a break from her acting career.',
    'My mom is angry at me for not washing the dishes.',
    'Jack is the owner of the bar near the beach.',
  ],
}
test_data_0341 = { 

      # **Guideword:** WITH QUANTIFYING DETERMINERS + 'OF'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use quantifying determiners + possessive determiners + 'of' + noun. ► noun phrases
        
  'positive': [
    'I spent all of my money on cosmetics.',
    'Many of her students choose to study abroad.',
    'Julia let some of her classmates play with her dog.',
    'You should sell some of your books.',
    'I\'ve had much of his wine.',
    'You have waited most of your life.',
    'I was happy to see all of my friends at my birthday party.',
    'Carry is good at playing the violin unlike many of her friends.',
    'She is generous enough to give me all of her video games.',
    'I invited some of our friends to the party.',
    'Many of our friends take ballet lessons.',
    'I should let you know that Jason ate many of your candies.',
    'I want to save all of your lives.',
    'Some of your students are originally from Australia.',
    'All of our food had been eaten by Rebecca.',
  ],
  'negative': [
    'She is good at all kinds of martial arts.',
    'Let\'s buy some snacks for the sleepover.',
    'You should have some water before you get dehydrated.',
    'All sorts of attempts were made.',
    'There are a lot of photos in her album.',
    'I need more information to write the report.',
    'There are a lot of boxes under the Christmas tree.',
    'These days, a lot of students have smartphones.',
    'Some lucky guy in the world won her love.',
    'I will invite a few friends to the dinner party tomorrow.',
    'All students are required to buy the latest computer.',
    'All plans for this week have been canceled.',
    'Some people can be very rude to others.',
    'He respects his father to some extent.',
    'She baked a lot of cookies for tomorrow’s reception party.',
    'Jake stole my wallet and took all the cash.',
    'A lot of cats had gone missing.',
  ],
}
test_data_0342 = { 

      # **Guideword:** 'THEIR'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use possessive determiner 'their'. ► noun phrases ► possessive pronouns
        
  'positive': [
    'They expressed their deep love of their country in their own ways.',
    'I hurt their feelings.',
    'I want to be by their side.',
    'They are doing their best.',
    'Their parents broke up their relationship.',
    'Birds fly with their wings.',
    'Their car was stolen.',
    'Their hands touched.',
    'I was really moved by their song.',
    'Parents love their children.',
  ],
  'negative': [
    'Her tears ruined her make‐up.',
    'I\'ll do my best.',
    'My father loves my mother.',
    'You should put more of your heart into your business.',
    'He drew her out of her room.',
    'Blow on your porridge to cool it.',
    'He put his hand on his heart.',
    'He did his duty both to his lord and to his father.',
    'I beg your pardon.',
    'He has his hands in his pockets.',
    'She buried her face in her hands.',
    'She held her baby to her bosom.',
    'I\'m obsessed with my work.',
    'His room is better than his office.',
    'Your reward will depend on your services.',
    'He held his head in his hands.',
    'It caught my eyes.',
    'My hobby is walking my dog.',
    'How dare you forget your duty and raise your hand against your own father?',
    'Her beauty was her ruin.',
  ],
}
test_data_0343 = { 

      # **Guideword:** IRREGULAR PLURAL NOUN + ''S'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use ''s' after irregular plural nouns to indicate possession.
        
  'positive': [
    'I can tell the children\'s feelings.',
    'She has women\'s ideal style.',
    'It is the children\'s dream.',
    'People\'s feelings are all different.',
    'I want to know the people\'s ideas.',
    'I understand people\'s thoughts.',
    'Men\'s rooms are normally dirty.',
    'Children\'s toys are expensive.',
    'Women\'s favorite thing to do is eating chocolate.',
    'I know what men\'s society is like.',
  ],
  'negative': [
    'They use some knives to make a carving.',
    'Billiards is played all over the world.',
    'I drank a glass of water.',
    'Athletics is good for young people.',
    'How many people?',
    'I have a pair of scissors.',
    'I bought some books at the store.',
    'I have many books.',
    'Her jeans are black.',
    'The people were scared.',
    'Those glasses are his.',
    'She has a lot of money.',
    'My trousers are too tight.',
    'Darts is a popular game in England.',
    'The news is at 6.30 p.m.',
    'I want to trust people.',
    'People must depend on one another.',
    'Linguistics is the study of language.',
    'The people can now live in peace.',
    'He has ten watches.',
  ],
}
test_data_0344 = { 

      # **Guideword:** 'ITS'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use possessive determiner 'its' before nouns to refer to a singular inanimate subject or object. 
        
  'positive': [
    'The cat arched its back.',
    'The earth turns on its axis.',
    'The bird flapped its wings.',
    'The snail extruded its horns.',
    'The dog showed its teeth.',
    'Don\'t judge a book by its cover.',
    'The iguana stuck out its tongue.',
    'The cow swished its tail.',
    'The TV series is in its fifth season.',
    'The child favors its mother.',
  ],
  'negative': [
    'What day is it today?',
    'That\'s how it is.',
    'There is no harm in it.',
    'It is always the guilty party who raises the alarm.',
    'It is threatening to snow.',
    'It\'s still early.',
    'It\'s good weather today.',
    'It is hot every day.',
    'There is no help for it.',
    'I feel that it\'s well within my limits.',
    'It\'s just as good.',
    'It\'s a small world.',
    'Whose deal is it?',
    'Is it still raining?',
    'It\'s under consideration.',
    'It is easy to die for one\'s faith.',
    'What time is it now?',
    'It is raining.',
    'It is a cold day, isn\'t it?',
    'It is not altogether hopeless.',
  ],
}
test_data_0345 = { 

      # **Guideword:** GENERIC 'THEIR'
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'their' before nouns to refer to a generic body or group of people expressed as a singular subject. ► generic pronouns
        
  'positive': [
    'Birds and beasts feed their young.',
    'Seemingly happy people have their own problems too.',
    'Children are the manifestation of a bond between their parents.',
    'They sold their technology for millions of dollars.',
    'They\'re in a league of their own.',
    'Some students fail because they try to copy off their neighbors.',
    'At that age, parents typically start staying with their children in that country.',
    'Persimmons do not quickly lose their sourness.',
    'Birds fly with their wings.',
    'I love their new song.',
  ],
  'negative': [
    'They belong to different schools.',
    'They look like they are really enjoying themselves.',
    'They run away when they see me.',
    'They say whatever they feel like.',
    'They look like they are having fun.',
    'They only use money that they have.',
    'They think that they understand that.',
    'Even though they were poor, they were happy.',
    'They were glad when they saw the souvenir.',
    'They seem like they will win that match.',
    'They are clever students, aren\'t they?',
    'They look like they are happy.',
    'They sound strange.',
    'They have times where they go fishing too.',
    'They return to Kyoto tomorrow.',
    'They say what they want to say.',
    'They never meet but they quarrel.',
    'They returned from whence they had come.',
    'Those don\'t look like they have any relation to each other, do they?',
    'They married when they were young.',
  ],
}
test_data_0346 = { 

      # **Guideword:** PLURAL NOUN + 'S''
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 's'' after plural nouns to indicate possession.
        
  'positive': [
    'My parents’ house is far from here.',
    'My aunt came back after ten years’ absence.',
    'The families\' houses are all big.',
    'There is a ladies’ room over there.',
    'That is our brothers\' dream.',
    'He is the girls\' favorite.',
    'Those boys\' favorite sport is football.',
    'The boys\' colleges are quite expensive every semester.',
    'This is the sisters’ school.',
    'Kids’ clothes are cheaper than adults\' clothes.',
  ],
  'negative': [
    'Tom\'s computer isn\'t working.',
    'My friend\'s wife\'s sister is a restaurant owner.',
    'This is John\'s school.',
    'The men’s bathroom is over there.',
    'All of my wife\'s friends are beautiful.',
    'I was introduced to Ken and Mary\'s friend.',
    'I\'ve got an appointment at the dentist\'s at eleven o\'clock.',
    'These are children’s toys.',
    'The politician\'s hypocrisy was deeply shocking.',
    'This is my children’s school.',
    'Do you still have yesterday\'s newspaper?',
    'Shall we go to Luigi\'s for lunch?',
    'Jack Sparrow\'s ship is the Black Pearl.',
    'Don\'t step on the cat\'s tail.',
    'Is Saint Mary\'s an all-girls school?',
    'A cat\'s tail is cute.',
    'The city\'s population increased.',
    'The owl’s eyes are black.',
    'John\'s patience is running out.',
    'This is the men’s restroom.',
  ],
}
test_data_0347 = { 

      # **Guideword:** OF + NOUN PHRASE ''S'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use ''s' after a noun phrase with of to indicate possession.
        
  'positive': [
    'This is a friend of my sister\'s.',
    'I brought an acquaintance of my sister\'s.',
    'Your new bag is more expensive than that flashy one of my brother\'s.',
    'My house is smaller than an old house of Jane\'s.',
    'Her old phone is much cheaper than that new iPhone of my mother\'s.',
    'These are some nice shirts of my father\'s.',
    'She likes to borrow an old laptop of my sister\'s.',
    'This is a new notebook of Jane\'s.',
    'Your notebook is nicer than that new one of your brother\'s.',
    'That was a game of Ken\'s.',
  ],
  'negative': [
    'My sister-in-law’s present to me was a home-baked pound cake.',
    'New Year’s Eve is our wedding anniversary.',
    'Pablo Picasso’s Guernica looks like a comic strip to me.',
    'The women’s shoes section is on the first floor.',
    'Is Saint Mary\'s an all-girls school?',
    'The families\' houses are all big here.',
    'These are children’s toys.',
    'This women\'s college is quite expensive to get in.',
    'This is my children’s school.',
    'She said, “Girl talk is fun.”',
    'My aunt came back after ten years’ absence.',
    'John\'s patience is running out.',
    'The accident was nobody’s fault.',
    'It must be someone else’s work.',
    'This is John\'s school.',
    'Osamu Tezuka’s comic deals with universal ideas.',
    'Those boys\' favorite sport is football.',
    'This is the men’s restroom.',
    'The cat\'s tail is cute.',
    'This is my sister\'s school.',
    'I just went with my father\'s'
  ],
}
test_data_0348 = { 

      # **Guideword:** 'ONE'S'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'one's' to indicate possession, referring to people in general. 
        
  'positive': [
    'One should associate with one\'s equals.',
    'I never thought how much one\'s parents determine one\'s prospects in life.',
    'Being ambitious often means being eager to exhibit one\'s skill at the right time.',
    'The place of one\'s birth will always be relevant.',
    'It can be hard to control one\'s impulses.',
    'I think one\'s worth should not be determined by one\'s wealth.',
    'One should not be ashamed to learn from one\'s inferiors.',
    'The job requires reliance on one\'s own abilities to accomplish the task.',
    'One must be careful with one\'s health.',
    'Going to the casino for the first time, I realized how quickly one runs out of one\'s money.',
  ],
  'negative': [
    'Is there anyone you like?',
    'He is blind in one eye.',
    'There isn\'t anyone in here either.',
    'One must sow before one can reap.',
    'I prefer this one more.',
    'I can\'t trust anyone anymore.',
    'This one is much cheaper than that one.',
    'She hates to be the one to tell him.',
    'That cannot be made by anyone.',
    'I don\'t know anyone here.',
    'You cannot defeat anyone.',
    'They are at one with one another.',
    'Anyone can play there.',
    'I didn\'t get one.',
    'I don\'t hate anyone.',
    'The more one has, the more one wants.',
    'Is there anyone there?',
    'I got the same one with you.',
    'There isn\'t anyone in the room.',
    'I should buy this one.',
  ],
}
test_data_0349 = {

  # **Guideword:** SINGULAR NOUN ENDING IN 'S' + APOSTROPHE
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** possessives
  # **Lexical Range:** None
  # **CEFR level:** C2
  # **CAN-DO:** Can use an apostrophe after singular nouns ending in 's', to indicate possession.

  'positive': [
    'However, I believe that in order to maintain its popularity, the programme should keep some of the series\' aspects the same, but alter some others. ',
    'Did you also make note of the moss\' color?',
    'I didn\'t like the bus\' design, can you show me another one?',
    # tagged tennis as plural noun
    # 'Tennis\' rules are especially easy to learn.',
    'He was one of chess\' great players.',
    'James\' wife was especially beautiful when she was young.',
    'He became the class\' first graduate.',
    # tagged as plural
    # 'Rabies\' spread has been terrible in that region this summer.',
    'Gas\' smell is made to be particularly pungent to be able to detect leaks.',
    'The cross\' sheer size was quite striking in the town\'s skyline.',
  ],
  'negative': [
    'I am not sleepy yet.',
    'I don\'t know how to beat him.',
    'The pencil is mine',
    'This drama is quite a long-running series.',
    'There is yet time.',
    'The buses\' were all changed overnight.',
    'Please come by to pick up his delivery.',
    'The players\' attitudes set good examples for the children.',
    'I\'m not done for yet, you\'ll see!',
    'Things are not yet right.',
    'The evil is not yet suppressed.',
    'The money is not yet accounted for.',
    'The children\'s voices could be heard from down the street.',
    'Our cats are treated very well.',
    'You should make things happen.',
    'Think about frugality and avoid this next time',
    'The time is not enough.',
    'Make the best use of resources to hire an excellent person',
    'The matter is not yet settled.',
    'He is not very excited about his parents\' constant nagging.',
    'The particular details have yet to be hammered out.',
    'The exhibit\'s dates are still not decided.',
  ],
}
test_data_0350 = {

  # **Guideword:** ''S' WITH ELLIPTED NOUN
  #   **Guideword type:** FORM
  #   **Super category:** DETERMINERS
  #   **Sub category:** possessives
  #   **Lexical Range:** None
  #   **CEFR level:** C2
  #   **CAN-DO:** Can use ''s' without a following noun when the noun has already been mentioned or is obvious in the context.

  'positive': [
    'Olivia\'s experiences probably differ from the narrator\'s. ',
    'He started to shake me and meanwhile I heard a familiar voice; it was my father\'s.',
    'Suddenly, after two weeks, I realised that my bank account was empty and so was my friend\'s.',
    'Thanks for sending me yesterday\'s work; did you also finish today\'s?',
    'I just beat that team\'s record and I can still beat your team\'s.',
    'Speaking of bright colors, have you seen the car\'s?',
    'That company\'s cards\' captions are always so stupid; read this card\'s.',
    'The professor\'s views were different from the students\'.',
    'Today\'s weather is much better than yesterday\'s.',
    'Malaria\'s treatment is much more difficult than diabetes\'.',
    'My school\'s team was much better than your school\'s.',
    'My father\'s income was much higher than my mother\'s.',
  ],
  'negative': [
    'I should have finish today\'s homework first.',
    'I haven\'t decided this project\'s content.',
    'This is my house.',
    'Have you copied his work?',
    'Stick to what he said.',
    'Try to avoid the bottle\'s lip.',
    'He has not come down yet.',
    'The child can\'t walk yet.',
    'I\'m not done for yet, you\'ll see!',
    'Things can still be changed.',
    'He is not surrendering.',
    'She is her children\'s angel.',
    'He is not yet gone.',
    'No news is as yet at hand.',
    'The time is not yet ripe.',
    'The opportunity is not yet ripe.',
    'The matter is not yet settled.',
    'He is not yet fifty.',
    'The particulars are not yet at hand.',
    'The exhibits are as yet incomplete.',
    'The evil is not yet suppressed.',
    'The money is not yet accounted for.',
  ],
}
test_data_0351 = { 

      # **Guideword:** ''S + 'S'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** possessives
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use two possessive ''s' constructions in the same noun phrase. 
        
  'positive': [
    'Charlie’s room’s wallpaper is light blue.',
    'Amy’s mom’s cooking is really good.',
    'Olivia’s mom’s dog is called Benny.',
    # 'Molly’s brother’s book is very interesting.',
    # Molly: RB
    'Ray’s grandpa’s grave is very big.',
    'David’s son’s paintings are breathtaking.',
    'The girl’s brother’s school was shut down.',
    'Jack’s house’s roof is a mix of red and green.',
    'Julie’s teacher’s class is very popular.',
    'Harry’s dad’s company is where my brother works at.',
  ],
  'negative': [
    'Ken’s girlfriend is a world wide model.',
    'I shouldn’t blame you for not knowing.',
    'We didn’t like the architect.',
    'It’s Monday so I need to go to my pilates class.',
    'You mustn’t rely on your parents financially.',
    'I haven’t heard back from the consulting firm yet.',
    'My sister’s cat was sick till recently.',
    'We need your help this weekend.',
    'The mayor’s office is huge.',
    'That’s not a very nice thing to do.',
    'Mary’s brother forgot to feed the dog.',
    'Katie’s school is famous for the beautiful scenery.',
    'Milly’s father used to work as a pilot.',
    'I haven’t seen a single game of football before.',
    'Our daughter’s grade are flawless.',
    'We don’t have to watch a movie if you don’t feel like it.',
    'Isabelle’s room was too messy to invite a friend over.',
    'I don\'t think there is any way that I can wear that well.',
    'That’s Carl playing volley ball over there.',
    'Rebecca wasn’t a part of the hockey team.',
  ],
}
test_data_0352 = {

  # **Guideword:** WITH PLURAL NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of quantifying determiners
  #  with plural nouns ('some', 'lots of', 'a lot of' and numbers).

  'positive': [
    'I have got lots of friends since I was born.',
    'You see a lot of items priced as much or higher than what the price should be new.',
    'Some people need a wake-up call or need to hit rock bottom before they get help.',
    'There are four people in my family.',
    'Our radio station has a lot of different types of listeners.',
    'You used to have some special pencils, but they are all broken now.',
    'A week has seven days.',
    'Lots of things are going through my mind, and I can\'t deal with all of them.',
    'I still think that my mother has some boyfriends at the same time.',
  ],
  'negative': [
    'I\'ve spent a lot of time with real paint.',
    'There has been a lot of research into the causes of this disease.',
    'He gave me a great deal of advice before my interview.',
    'My father gives me some information about his company.',
    'I didn\'t make much progress today.',
    'This looks like a lot of trouble to me.',
    'Don\'t be afraid to go sit down and rest and have some water if you feel you\'re overheating.',
    'I might have to try a cup of tea with some sugar before going to bed.',
    'A football game is expensive and requires a lot of knowledge of the rules and equipment while soccer is cheap and easy.',
    'I need some air to think about my future.',
    'You would love to eat some Thai food with rice.',
    'There is lots of evidence, but it is not enough to prove he is innocent.',
    'I like to work with my customers and still make some money.',
    'It sounds like there is a lot of hair in your house because your house is a barber shop.',
    'I personally don\'t want to exchange freedom for some safety.',
    'We went fishing and ate a lot of fish which we caught.',
    'Some sheep ran away from me when I got to the zoo.',
    'The world can be a terrible place, but it is full of a lot of beauty and kindness, too.',
    'She gets lots of love from her family.',
    'I think most people probably have some fear of childbirth.',
    'I saw three sheep in Hokkaido.',
  ],
}
test_data_0353 = {

  # **Guideword:** WITH SINGULAR NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of quantifying determiners with singular nouns ('a', 'every').
  # ► determiners: articles

  'positive': [
    'There\'s a difference between what you describe and what my neighbors have.',
    'I\'m not sure leaving your dream job makes sense after a year even if it is for a promotion.',
    'Every major chain grocery store with a seafood section has live lobster.',
    'My friend went back home because she got a headache.',
    'You seem extremely nervous every time they put her on camera.',
    'Every time when I go to the bookstore, I feel like I want to buy all books in the store.',
    'I practice baseball every day after the school finishes.',
    'I watch this marathon every year.',
    'I can\'t speak for every single shop in Tokyo because there are thousands of them.',
    'That\'s a step-down from dream job.',
    'There\'s a difference between what you describe and what my neighbors have.',
    'My neighbors\' dog seems to be exclusively an outdoor dog.',
  ],
  'negative': [
    'I think your son will feel the same way about the money.',
    'I don\'t like his new shoes because the color is strange.',
    'My father has kept the secrets of his high school days.',
    'You can go to Thailand with your summer clothes.',
    'I am sure that my friends come here in their own cars.',
    'She is one of my best friends in my life.',
    'Her friends are on the way to the party now.',
    'Our school will be closed for the holiday.',
    'Your pencils are all gone, and I don\'t know where they are.',
    'Your link has been removed.',
    'They gave their money to him so they can take his wife.',
    'My kids wouldn\'t be raised properly.',
    'You\'re making it alright to let his parents affect his mood like that.',
    'Their cameras are much older than mine.',
    'I still remember your brothers and sisters.',
    'My life and your life are totally different.',
    'His bags are still in my room and he hasn\'t come to get them yet.',
    'My whole books are all in my room and they are still clean.',
  ],
}
test_data_0354 = { 

  # **Guideword:** WITH PLURAL NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** 2.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use an increasing range of quantifying determiners with plural nouns ('all', 'both', 'a few').
    
  'positive': [
    'I will invite a few friends to the dinner party tomorrow.',
    'I will need both cars tomorrow morning.',
    'All students are required to buy the latest computer.',
    'I need to borrow a few things from her.',
    'Can you run to the store and buy me a few things?',
    'Both parents are against my marriage with John.',
    'We will donate all clothes to the foundation.',
    # 'All plans for this week has been canceled.',
    # parser's problem: plans->All(nsubj)
    'She needs to buy a few things for the new school year.',
    'I need both jackets for the family trip.',
  ],
  'negative': [
    'Your love is all I need.',
    'For once and for all, be honest with your feelings.',
    'I need both ham and cheese to make a sandwich.',
    'All of a sudden, the lights went off, and everyone started panicking.',
    'She is both a writer and a painter.',
    'This software is sold both in Japan and in the United States.',
    'I have two brothers and both are married.',
    'I’ll meet you both in front of the museum.',
    'Let the both of us work hard together.',
    'Let’s drink alcohol all night long.',
    'I need a little more time to finish this.',
    'We you be all right on your own?',
    'They all get along well.',
    'My teacher wished me all the best.',
    'It’s confusing how they all look alike.',
    'Is everything all right at the restaurant?',
    'He can both read and write Hebrew.',
    'Both Christina and Regina are pretty.',
    'You can take either of the two, but not both.',
    'The bank clerk should apologize to both of us.',
    'My house kept a symbol, as all of the great houses did.',
  ],
}
test_data_0355 = { 

  # **Guideword:** WITH PLURAL AND UNCOUNTABLE NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use a range of quantifying determiners ('some', 'any', 'no', 'more', 'a lot of') with both plural nouns and uncountable nouns.
    
  'positive': [
    'Let\'s buy some snacks for the sleepover.',
    'I need more information to write the report.',
    'I’ll give you some advice on house repairing.',
    'There are a lot of boxes under the Christmas tree.',
    'These days, a lot of students have smartphones.',
    'There are a lot of photos in her album.',
    'You should have some water before you get dehydrated.',
    'You should buy more clothes for your daughter.',
    'I don’t have any friends living abroad.',
    'Mary’s grandmother has a lot of kittens.',
    'Some men at the gate are looking at you.',
    'Some lucky guys in the world have all the money.',
    'You must make money by yourself by more ways than just working at a company.',
    'Any information he gave was not accurate.',
    'I have no ideas for the new movie.',
    'That was some milk on the ground.',
  ],
  'negative': [
    'Some say it’s true, some not.',
    'Some are famous for being troublesome.',
    'The wolf was smarter than any of the hounds in the kennel.',
    'I was as good as anyone in this house.',
    'He tried not to look down any more often than he had to.',
    'They won’t trouble us any more.',
    'I used to live in a town no bigger than this.',
    'He will visit us no later than the end of this month.',
    'He is no different from what he used to be.',
    'I can’t say no to my boss.',
    'She stayed the night at an empty parking lot.',
    'Betty weighs more than Anna does.',
    'She’s more beautiful than her sister.',
    'He is all the more beloved because he is naive.',
    'After the accident, I started caring for my family more than ever.',
    'They got more and more angry.',
    'I have gotten more and more sleepy.',
    'I don’t have to go to school anymore.',
    'Some like cities, while others like the countryside.',
  ],
}
test_data_0356 = { 

  # **Guideword:** WITH SINGULAR NOUNS
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** 2.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use an increasing range of quantifying determiners with singular nouns ('each', 'an', 'one' and numbers). 
    
  'positive': [
    'There is one tall girl in the park.',
    'I have one hour left before going to school.',
    'You only have one kind friend who you can trust.',
    'She has a long pencil.',
    'Each day had been worse than the day that had come before it.',
    'The man who is walking in the street has a great bag.',
    'One man had two axes.',
    'There is a park where you can play baseball.',
    'It takes one minute from here to there.',
    'There is an apple on the table.',
    'Each minute the runner gets more and more tired.',
    '45 percent of Millennials don\'t expect to own a house.',
  ],
  'negative': [
    'It takes twenty minutes from here to there.',
    'I can take each of you to there if you want.',
    'These three bags are all nice.',
    'Each of you guys is nice.',
    'I have two hours left before going to school.',
    'There are three tall girls in the park.',
    'I have some flowers to give.',
    'You would buy some food for the party.',
    'Some people are pretty friendly.',
    'I want to sing some songs for you.',
    'Some of my friends went to Korea.',
    'I can\'t play any musical instruments.',
    'I don\'t have any clothes to put on today.',
    'She doesn\'t have anything to talk about.',
    'Do you have any friends who you can trust?',
    'She can\'t go anywhere now.',
    'I go to school every day.',
    'Everyone can go anywhere they want.',
    'I want to visit every prefecture in Japan.',
    'Every place has it\'s own history.',
    'You can see him everywhere in this town.',
    'I still have many things to do.',
    'Many people like to play soccer.',
    'I still have too much homework.',
    'There are many books in that library.',
    'She told me many things that I can\'t remember.',
    'All the people are fr iendly here.',
  ],
}
test_data_0357 = { 

  # **Guideword:** 'MUCH' WITH UNCOUNTABLE NOUNS, NEGATIVE
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'much' with uncountable nouns in negative contexts. 
    
  'positive': [
    'I did not have much time left, so I could not finish it up.'
    # 判定は正しいけどパーサーは変。（have->left, ccomp）
    'They do not have much money for getting a new car.',
    'It is likely that we don\'t have much water left in our pool because of this weather.',
    'We will not own much money anymore so we better give up.',
    'All he knew was he did not get much money to give away to other people.',
    'You should not have drunk this much tea.',
    'I do not see much anger on her face.',
    # 'We believe there is not much safety assured here.',
    # パーサーが謎の挙動をしていて…（例；is->safety, nsubj）
    'They could not have found much evidence to prove it was true.',
    'She didn\'t give me much advice before my meeting.',
  ],
  'negative': [
    'I had much time left, but I could not finish it up.',
    'They have much money for getting a new car.',
    'It is likely that much of the homes still have water despite the severity of the hurricane.',
    'We owe much money so you\'d better give up.',
    'All he knew was he got out much of his money to give away to other people.',
    'You should drink much water every day.',
    'I see much anger on her face.',
    'We believe there is much security in this building.',
    'They have found much evidence to prove it was true.',
    'She gave me much advice before my meeting.',
    # 以上追加
    'I would have much more to do this afternoon.',
    'They did not give me enough information.',
    'Do not touch anything before they finish their work.',
    'I do not want to believe that there are many bugs.',
    'There are many more to come.',
    'I cannot believe he did so much before I came here.',
    'It is not pretty much because of her work.',
    'Charlie could not see much of what hid behind the curtain.',
    'I do not need to worry much about what comes next.',
    'They have not done enough to make me feel relieved.',
    'They will not go through this.',
    'I need to remind them that they do not need to do all of this.',
    'I woke up early in the morning to finish whatever left to do from the day before.',
    'She could not catch much about what her professor said to her.',
    'I was concerned about us, but everything went well.',
    'It is so difficult to complete much of what we are told to do.',
    'You are not much of a detective, are you?',
    'We haven\'t had much of a summer this year.',
    'It is not much of a place for taking a rest in the middle of the day.',
    'He feels he has not done much today.',
  ],
}
test_data_0358 = { 

  # **Guideword:** 'MANY' WITH PLURAL NOUNS, NEGATIVE
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'many' with plural nouns in negative contexts. 
    
  'positive': [
    'There are not many seats left in the cinema.',
    'I did not get many tickets.',
    'I could not find many ways to accommodate everyone in this camp.',
    'He couldn\'t assign the new recruits to many tasks.',
    'She doesn\'t have many friends.',
    'It is not many years, but a few, since he went to the island.',
    'There were not many times when he could wake up by himself.',
    'They don\'t have many sons but many daughters.',
    'There are not many steps to achieve it.',
    'I think he didn\'t have many coins at that time.',
    # 以下追加
    'Nobody eats this many tomatoes.',
    'I no longer have many friends.',
    'Many people have never slept for 24 hours.',
    'Neither mother nor father had been to many countries.',
    'Nobody had read books with this many pages.',
    'I didn\'t know Shibuya station had so many people.',
    'Many people don\'t know "cloth", "clothe" and "clothes" are different words.',
    'Not a single person had many papers.',
    'Tokyo has never had so many events in a day.',
    'Few people believe that the first version of this product had so many defects.',
  ],
  'negative': [
    'Do you know where to find this many pairs of shoes?',
    'I wonder if they are really into helping this many high school kids out.',
    'Was it true that there used to be many empty seats in his concert?',
    'This summer I tried to help many people try new things.',
    'Would you want to take care of the many kids in this office?',
    'They wanted to get as many cars as possible.',
    'Charlie succeeded in having many cats in his house.',
    'Charlie wanted to join the local soccer team which already holds many members.',
    'He does not know how to drive a car.',
    'Have you ever seen those people in Toronto?',
    'Take as much as you want, since I have a bunch.',
    'Where will you be heading to at 9 a.m. tomorrow?',
    'She likes writing about this stuff because she likes it.',
    'The family never found some parts of the machine and gave up fixing it.',
    'My professor does not own any pets and she thinks it is totally fine.',
    'I agree with you that they should not get too many of these.',
    'This is not much of a place where you can find your ideal career.',
    'She ended up finding the best way to get out of her routine.',
    'I heard they went to the beach the other day.',
    'What would you order in this menu if you are in this restaurant?',
    'They have never experienced this much injustice in their life.',
    'Do we need to get some tomatoes in this farmer\'s market?',
    'My sibling is supposed to bring some money back to the house.',
    'I already told him that I would not buy anything extra this time.',
    'How can you convince him to purchase this much rice?',
    'I heard her calling the names.',
    'Could you hold this bag full of apples for a while?',
    # 以下追加
    #'Nobody hadn\'t read this book with many pages.', #NOTE: this should not be marked 'negative'
  ],
}
test_data_0359 = { 

      # **Guideword:** 'SO MANY' WITH PLURAL NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'so many' and 'too many' with plural nouns. 
        
  'positive': [
    'Jake and I had so many adventures together.',
    'You have too many books on the shelf.',
    'I have so many books to read by the end of the week.',
    'Cristina came up with so many ideas.',
    # 'So many tasks are yet to be done.',
    # parser: are->So(advmod)
    'I forgot to bring so many things and I feel like crying.',
    'My mom and I visited so many temples during the summer.',
    'Lindsey has too many bananas in her bag.',
    'My mom bought too many apples at the market.',
    'I told her that I couldn’t eat so many cookies.',
  ],
  'negative': [
    'Rebecca had eaten all of the food.',
    'That suitcase is too heavy.',
    'I invited some of our friends to the party.',
    'I need more information to write the report.',
    'Many of her students choose to study abroad.',
    'The psychology test was too easy for me.',
    'There are a lot of photos in her album.',
    'That novel is too long for a college assignment.',
    'She is generous enough to give me all of her video games.',
    'I am too sleepy to get any work done.',
    'Many people are unaware of the accident that happened last week.',
    'Jason went to the party and ate too much.',
    'All plans for this week has been canceled.',
    'Julia let some of her classmates play with her dog.',
    'I should let you know that Jason ate many of your candies.',
    'She is good at all kinds of martial arts.',
    'My sister is too young to watch a horror movie.',
    'All students are required to buy the latest computer.',
    'Carrie is good at playing the violin unlike many of her friends.',
    'Some of the people here are originally from Australia.',
  ],
}
test_data_0360 = { 

  # **Guideword:** DETERMINER + 'OF' + DETERMINER
  # **Guideword type:** FORM
  # **Super category:** DETERMINERS
  # **Sub category:** quantity
  # **Lexical Range:** 2.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use a range of quantifying determiners + 'of' + determiner ('all of', 'some of', 'both of', 'many of', 'any of', number + 'of', 'each of'). ► pronouns: quantity
    
  'positive': [
    'Both of my parents are doctors.',
    'Some of my friends are going to college in the United Kingdom.',
    'Some of the teachers at my school are nice.',
    'Many of my relatives live in South Africa.',
    'I got all of my money stolen on the subway.',
    'Both of my sisters are graduating from college this year.',
    'Two of my friends came to the hospital to see me yesterday.',
    'I can’t find any of my dictionaries.',
    'She didn’t invite any of her friends from school to the party.',
    'I spent some of my money on a computer.',
    'I want to protect all of my family.',
    'I’ll get angry with both of the kids if they don’t cut it out.',
    'He had spoken to each of the members in turn.',
    'One of the horses reared.',
    'Two of the desks were painted white.',
    'I will pick up three of the packages.',
  ],
  'negative': [
    'Let\'s buy some snacks for the sleepover.',
    'You should have some water before you get dehydrated.',
    'I don’t have any friends living abroad.',
    'I have no idea where she is hiding.',
    'You must make money by yourself in some way or other.',
    'All sorts of attempts were made.',
    'I listen to all kinds of music.',
    'All the men were gone.',
    'All murders are wrong.',
    'Many species of insects are on the verge of extinction.',
    'Many kinds of flowers come out in the middle of April.',
    'Each student must have their laptop.',
    'Each member of the group must cooperate with one another.',
    'There were flowers on both banks of the river.',
    'Both styles of writing became a subject of calligraphic art.',
    'I got half the size of the cake.',
    'We both had many things we wanted to discuss.',
    'I put both hands up in support of that proposal.',
    'Of all the choices, you chose the same one as I did.',
    'I was late for my job all because of the traffic accident.',
    'She is good at all kinds of martial arts.',
  ],
}
test_data_0361 = { 

      # **Guideword:** WITH PLURAL NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** 3.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use a wide range of quantifying determiners with plural nouns ('several', 'millions of', 'a few of').
        
  'positive': [
    'I will send a few of those photos next time.',
    'He prays several times a day.',
    'A small group rules over millions of people.',
    'The telephone rang several times.',
    'I take only a few of those classes seriously.',
    'The dam retains millions of tons of water.',
    'A few of the parts have gone up in price.',
    'His discovery of the truth led to the saving of millions of lives.',
    'He scored several times.',
    'He took several days off.',
  ],
  'negative': [
    'I\'ve got plenty of money.',
    'He has plenty of fight in him.',
    'We still have plenty of time.',
    'Did you spend a lot of money?',
    'There aren\'t a lot of young people.',
    'I do a lot of overtime.',
    'You\'ll be there in plenty of time.',
    'There is plenty of room.',
    'I had a lot of free time.',
    'There was a lot of humidity today.',
    'You\'ve got plenty of time.',
    'I got plenty of sleep.',
    'There is plenty of fish in Japan.',
    'I can handle a lot of alcohol.',
    'I\'m having a lot of fun now.',
    'I\'m in a lot of trouble.',
    'There is plenty of food.',
    'There is a lot of snow this winter.',
    'We have plenty of provisions.',
    'I ate a lot of salad.',
  ],
}
test_data_0362 = { 

      # **Guideword:** WITH UNCOUNTABLE NOUNS
      # **Guideword type:** FORM/USE
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use quantifying determiners with uncountable nouns, often in informal and/or spoken contexts ('a little', 'a bit of' and 'a little bit of').
        
  'positive': [
    'I will eat a little food before leaving the house.',
    'Take a little time for yourself.',
    'There is just a little sand in my shoe.',
    'I can speak a little bit of Thai.',
    'We should have a little rain this evening.',
    'He likes a bit of wine every evening.',
    'I have a little bit of shampoo still in my hair.',
    'I\'m happy to give you a little water if you need it.',
    'He has a bit of spinach in between his teeth.',
    'There\'s still a bit of milk in the refrigerator.',
  ],
  'negative': [
    'The telephone rang several times.',
    'She has a little bit of a cough.',
    'I am growing little by little.',
    'I got plenty of sleep.',
    'I have gotten used to it little by little.',
    'I ate a lot of salad.',
    'He prays several times a day.',
    'You\'ll be there in plenty of time.',
    'It affords little reading.',
    'There was a lot of humidity today.',
    'There is plenty of food.',
    'I\'m having a lot of fun now.',
    'I had a lot of free time.',
    'Did you spend a lot of money?',
    'They were a little bit scared by the news.',
    'I\'m in a lot of trouble.',
    'I can handle a lot of alcohol.',
    'A small group rules over millions of people.',
    'He scored several times.',
    'He took several days off.',
  ],
}
test_data_0363 = { 

      # **Guideword:** WITH PLURAL AND UNCOUNTABLE NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of quantifying determiners with both plural nouns and uncountable nouns ('most', 'enough', 'plenty of', 'loads of').
        
  'positive': [
    'Remember to drink plenty of water.',
    'There is not enough money.',
    'I don\'t have enough time.',
    'Most people think so.',
    'Authors have a lot of imagination.',
    'I haven\'t had enough sleep.',
    'Loads of people are having fun.',
    'Most doctors make a lot of money.',
    'We had loads of fun.',
    'You\'ve got plenty of rice.',
  ],
  'negative': [
    'That\'s enough.',
    'I like Kyoto the most.',
    'I have not eaten enough.',
    'It\'s plenty long enough.',
    'I am most terribly sorry.',
    'That\'s bright enough.',
    'We have sufficient amounts of water.',
    'I didn\'t explain well enough.',
    'He doesn\'t sleep enough.',
    'This is a most critical moment.',
    'He\'s most persistent.',
    'It\'s most unlikely.',
    'I\'m the most beautiful in the world.',
    'This is the most important.',
    'I am most thankful for the blessing.',
    'The bath is not hot enough.',
    'You don\'t try hard enough.',
    'I like you the most.',
    'It isn\'t good enough.',
    'It is a most unexpected idea.',
  ],
}
test_data_0364 = { 

      # **Guideword:** 'MUCH' WITH UNCOUNTABLE NOUNS, INTERROGATIVE
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'much' with uncountable nouns in interrogative contexts. 
        
  'positive': [
    'How much bread is necessary for the dinner?',
    # 'Isn\'t there much cheese left?',
    # parser does not find this sentence question form
    'How much milk is there now?',
    'How much money do you have?',
    'Do we have much water left?',
    'Do they make much noise?',
    'Do you have much money?',
    'How much rain has fallen this year?',
    'How much milk do you drink in a week?',
    'Do you have much news from her since she left?',
  ],
  'negative': [
    'It will take a good many days.',
    'How much is this shirt?',
    'Many young people are out of work in Europe.',
    'There are a lot of apples.',
    'There are lots of people in the park.',
    'A great many people told me to leave.',
    'I’m glad that I have many many good friends.',
    'I added so much butter to the dough already.',
    'We have a lot of water.',
    'I read 3 books in as many days.',
    'I felt sick because I was bit by so many bugs.',
    'I was much confused.',
    'I ate many cookies today.',
    'Read as many books as you can.',
    'I ate as many cookies as you did.',
    'I cried a lot when I thought I lost you',
    'I saw many cars.',
    'We don’t have a lot of bread.',
    'There is lots of snow.',
    'Do you have many friends in this city?',
  ],
}
test_data_0365 = { 

      # **Guideword:** 'SO MUCH', 'TOO MUCH' WITH UNCOUNTABLE NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'so much' and 'too much' with uncountable nouns.
        
  'positive': [
    'My sister spends too much time dressing.',
    'I have so much free time.',
    'You can never have too much vacation.',
    'I am having so much fun.',
    'Don’t make so much noise.',
    'There was so much nature there.',
    'I have spent too much money.',
    'This work is taking way too much effort.',
    'I received too much money so I\'ll give it back.',
    'I am sorry to have given you so much trouble.',
  ],
  'negative': [
    'You have too much to do.',
    'There was much confusion.',
    'You talk too much.',
    'How much milk did you drink yesterday?',
    'How much is this shirt?',
    'There isn’t much news today.',
    'That\'s ever so much better.',
    'There is a loss of so much.',
    'I ate as many cookies as you did.',
    'That\'s saying too much.',
    'How much butter should I add?',
    'There isn’t much cheese.',
    'Ho much water do you have?',
    'Drank too much.',
    'Thank you ever so much.',
    'You work too much.',
    'My hand shakes so much that I can not write.',
    'We don’t have much bread.',
    'I like it ever so much.',
    'I can not eat so much.',
  ],
}
test_data_0366 = { 

      # **Guideword:** 'MANY' WITH PLURAL NOUNS, INTERROGATIVE
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'many' with plural nouns in interrogative contexts. 
        
  'positive': [
    'How many pairs of shoes do you have?',
    'How many rooms are there in your house?',
    'How many family members does she have?',
    'How many students are there in the school?',
    'How many hamburgers do you want?',
    'How many books did he buy?',
    'How many golf balls did he reserve?',
    'How many pens will you buy?',
    'How many games did he play?',
    'How many cakes do you need?',
    'Have you got many friends in England?',
  ],
  'negative': [
    'You enjoy many advantages.',
    'There are many types.',
    'Don’t make so much noise.',
    'I received too much money so I\'ll give it back.',
    'He wrote many books.',
    'I am having so much fun.',
    'My sister spends too much time dressing.',
    'I fell many times.',
    'He does not use many words when he speaks.',
    'He is endowed with many talents.',
    'You talk too much.',
    'I have so much free time.',
    'That\'s saying too much.',
    'This work is taking way too much time.',
    'You can never have too much money.',
    'How much is this shirt?',
    'It has many causes.',
    'Many thanks for your kindness.',
    'There are many variant editions.',
    'There were many incidents.',
  ],
}
test_data_0367 = { 

      # **Guideword:** DETERMINER + 'OF' + DETERMINER
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** 3.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of quantifying determiners + 'of' + determiner ('half of', 'enough of', 'none of',).► pronouns
        
  'positive': [
    'Half of the melons were eaten.',
    'We have had enough of the fighting.',
    'Half of the students are absent.',
    'I have had enough of these plays.',
    'It\'s none of your business.',
    'The latter half of the week was fine.',
    'We have had enough of this rain.',
    'None of us are free from the blame.',
    'Half of the town burnt down in the fire.',
    'Half of your apples are rotten.',
  ],
  'negative': [
    'I\'m often half asleep.',
    'That\'s bright enough.',
    'It\'s only half-past nine.',
    'Let\'s share the expenses half‐and‐half.',
    'I haven\'t had enough sleep.',
    'We have enough water.',
    'You aren\'t putting enough effort in.',
    'Flowers are best when they are half open.',
    'Words aren\'t enough.',
    'I did half the distance on foot.',
    'There are not enough funds.',
    'It has four and a half mats.',
    'I only want half an hour.',
    'Is a bottle of beer enough?',
    'One may see with half an eye.',
    'You don\'t try hard enough.',
    'It\'s not half bad.',
    'That\'s a natural enough suspicion.',
    'It\'s plenty long enough.',
    'I have half a mind to go.',
  ],
}
test_data_0368 = { 

      # **Guideword:** MODIFYING
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can modify determiners with adverbs. ► adverbs
        
  'positive': [
    'Nearly every actor on this show has false teeth.',
    'We meet nearly every day.',
    'Almost every student at my high school goes to college.',
    'Almost all of the museums are closed for the end of the year.',
    'I used up nearly all the money.',
    'It is operated nearly all day.',
    'He reads manga almost every night.',
    'Almost all of our conversation was in Japanese.',
    'I go to the seaside nearly every summer.',
    'Almost all girls are kind.',
  ],
  'negative': [
    'Mike is sometimes late for school.',
    'She plays the piano very well.',
    'He always gets a perfect score.',
    'Honestly, I don’t trust the man.',
    'I met him yesterday.',
    'I sometimes play succor with friends.',
    'I will definitely finish the work by Monday.',
    'Yesterday, I had lunch with him.',
    'He usually gets up at seven.',
    'I usually get up at 7 in the morning.',
    'He got up too late.',
    'He runs fast.',
    'I am always hungry.',
    'We had lunch at the restaurant.',
    'It is too cold to swim.',
    'I will watch the movie tomorrow night.',
    'You are often late for school.',
    'We often go shopping.',
    'I am usually at home.',
    'We had a party at our house.',
  ],
}
test_data_0369 = { 

      # **Guideword:** 'LITTLE/FEW'
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use modifier + 'little' + uncountable nouns and modifier + 'few' + countable nouns, to indicate a lack of something or not as much as expected of something.► adverbs
        
  'positive': [
    'We had very little snow last year.',
    'Very little rain fell this month.',
    # "business" can be either countable or uncountable
    #'We do very little business in the summertime.',
    'There are very few jobs available owing to the depression.',
    'I can make very little money on this article.',
    'There are still few opportunities for people from that community.',
    'Why are there so few people present?',
    'I met very few people here.',
    'It is sad that so few people give money to help the hungry.',
    'I have so little time at the end of the month.',
  ],
  'negative': [
    'I was thankful that I could see so little.',
    'She usually eats very little at home.',
    'I threw away a little.',
    'That novelist produces very little.',
    'It is unbecoming in a man of his means to give so little.',
    'We know very little about it.',
    'This hotel has very little to recommend it.',
    'I\'ll send those documents in a few.',
    'The shop attracts very few',
    'Please give me a little, too.',
    'It is sad for such a rich man to give so little.',
    'They see each other very little.',
    'It shows that he is miserly that a man of his means gives so little.',
    'I\'ll be there in a few.',
    'I think they have a few we could use.',
    'He has a few days free.',
    'He has a few.',
    'She ate very little this morning.',
    'I urinate very little.',
    'It was a case of the many against the few.',
  ],
}
test_data_0370 = { 

      # **Guideword:** 'EITHER', 'NEITHER' WITH SINGULAR NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'either' and 'neither' with singular nouns.
        
  'positive': [
    'Either method will work.',
    'Neither style is mine at all.',
    'Neither story is true.',
    'Neither claim is convincing.',
    'I like neither house.',
    'She told me to take either bag.',
    'Either way is fine.',
    'Neither time will work for me.',
    'Either day is OK.',
    'Neither singer is promising.',
  ],
  'negative': [
    'She doesn\'t like math either.',
    'That is not what I want either.',
    'Hanako didn\'t come today either.',
    'He didn\'t go, and neither did I.',
    'I don\'t think it\'s either of them.',
    'I can\'t do it either.',
    'I can\'t put up with him either.',
    'I am not good at either swimming or dancing.',
    'He who runs after two hares will catch neither.',
    'I don\'t want to run either.',
    'Neither of my parents is living.',
    'I can\'t catch up with him either.',
    'I can\'t sleep today, either.',
    'I don\'t like children either.',
    'He can\'t run fast, and neither can I.',
    'Neither is a good option.',
    'There isn\'t anyone in here either.',
    'She can\'t swim and neither can I.',
    'I haven\'t seen either of them lately.',
    'That won\'t get fixed today either.',
  ],
}
test_data_0371 = { 

      # **Guideword:** 'EITHER', 'NEITHER' + 'OF' + DETERMINER WITH PLURAL NOUNS
      # **Guideword type:** FORM
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'either' and 'neither' + 'of' with plural noun phrases or pronouns.► pronouns
        
  'positive': [
    'Neither of the parties would compromise on their opinions.',
    'I haven\'t seen either of them lately.',
    'Either of those would be fine.',
    'Neither of these are correct.',
    'Neither of the stories was true.',
    'I know neither of his brothers.',
    'You may take either of the glasses.',
    'Either of the jackets looks good on you.',
    'Either of the two veins that serve the eye can be damaged accidentally when welding.',
    'Neither of these steps was trivial.',
  ],
  'negative': [
    'Neither time will work for me.',
    'She and I were both premature infants.',
    'I like neither house.',
    'He who runs after two hares will catch neither.',
    'I haven\'t seen either one lately.',
    'Neither is still living.',
    'I don\'t think it\'s either brother.',
    'Neither singer is promising.',
    'I want to hold on to you with both hands.',
    'I can\'t catch up with him either.',
    'I eat both fish and meat.',
    'She can\'t swim neither can I.',
    'Both sides tried to avoid conflict.',
    'Please raise both your hands.',
    'Either method will work.',
    'I am not good at either swimming or dancing.',
    'I can\'t put up with him either.',
    'Both contains no scents or coloring.',
    'I attached a copy of both sides.',
    'Neither story is true.',
  ],
}
test_data_0372 = { 

      # **Guideword:** HYPERBOLE
      # **Guideword type:** USE
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use determiners in hyperbole, often in informal contexts ('millions of', 'loads of', 'tons of').
        
  'positive': [
    'We have tons of so-called vice presidents at our company.',
    'I\'m surprised that guy is still alive, he must be millions of years old.',
    'We had loads of fun.',
    'The bombers dropped tons of firebombs.',
    'He has millions of things to do.',
    'She has loads of natural charm.',
    'We have tons of responsibility.',
    'I\'m getting loads of comments on my page.',
    'The dam must have millions of tons of water.',
    'There are loads of books lying on the table.',
  ],
  'negative': [
    'The population of Japan is seventy million.',
    'She died worth millions.',
    'Starting with nothing, he made millions.',
    'This computer loads slowly so I was troubled.',
    'The profits run up into the millions.',
    'It weighs three tons.',
    'All lay loads on a willing horse.',
    'Don\'t dump your loads here.',
    'My camera loads easily.',
    'He is worth millions.',
    'She has natural charm.',
    'This program loads support for most SCSI controllers.',
    'Thus, the loads of the network fax are reduced.',
    'That\'s loads better.',
    'On whose head is the blood of millions?',
    'This rifle loads easily and shoots accurately.',
    'He loads too many duties on his assistant.',
    'The ship has a displacement of 24 tons.',
    'This stone weighs five tons.',
    'He has invested millions in the enterprise.',
  ],
}
test_data_0373 = { 

      # **Guideword:** 'MANY A' WITH SINGULAR NOUNS, FOR FOCUS
      # **Guideword type:** FORM/USE
      # **Super category:** DETERMINERS
      # **Sub category:** quantity
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'many a' or 'many an' + singular noun for emphasis and focus.
        
  'positive': [
    'There\'s many a twist in the road ahead.',
    'Many an empty chariot flew through the empty field.',
    'Many a time did she cry in secret.',
    'There\'s many a good tune played on an old fiddle.',
    'I have spent many a day trying to solve this problem.',
    'It seems he spent many a night unable to sleep.',
    'Many a man has chased after her.',
    'He was the hero of many a romance in his day.',
    'Many a good cow has an evil calf.',
    'It was such a snowfall as had not been seen for many a year.',
  ],
  'negative': [
    'Nagasaki is a town with many hills.',
    'There were a huge number of works there.',
    'A grave and punctilious man will have many children.',
    'The cloud of suspicion hangs over her.',
    'As many as three thousand people were in the audience.',
    'He is not so much a scholar as a writer.',
    'So many changes have been made since I saw it.',
    'How many days are there in a year?',
    'They do as many in a day as possible.',
    'The bulk of his work is in the urban area.',
    'He never spoke a word.',
    'The occurrence of a cloud of dust being raised into the sky.',
    'How many pieces do you sell a day?',
    'He has as many as a thousand pupils.',
    'A public man has many claims on his time.',
    'You may be many things but a father isn\'t one of them.',
    'Many places on the machiya line have been there for such a long time.',
    'He\'s not so much a scholar as a writer.',
    'It is such a harvest as has not been seen for many years.',
    'How many points is a try worth?',
    'Haven\'t you any better ones?',
    'Eggs are sold at so many for a yen.',
    # This type of attachment hard to detect.
    # 'You can only do so many a day.',
    'I see quite a number of new faces.',
    'If you buy so many in a lump, they will be cheaper.',
  ],
}
test_data_0374 = { 

      # **Guideword:** AFFIRMATIVE WITH 'WILL'
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the affirmative form with 'will'.
        
  'positive': [ #This is specifically targeting the future continuous
    'They will be learning about that next year.',
    'I will be staying there.',
    'It will be stopping in the next city.',
    'I will be swimming in the ocean over my vacation.',
    'Results will be coming out soon.',
    'I\'ll be doing my best.',
    'He will be working on this for the next 3 years.',
    'You will definitely be sleeping more soundly on this mattress.',
    'I will certainly be coming to the event.',
    # 'The day when you\'ll regret would come.',
    # parser: ROOT->day(ROOT)
    'I will be emailing you after the class.',
    'The rice will be burning if they cook dinner.',
  ],
  'negative': [
    'Will you visit Kyoto next month?',
    'They won’t practice soccer tomorrow.',
    'I won\'t study English tomorrow.',
    'It will not be raining tomorrow.',
    'Are they going to come tomorrow?',
    'It isn’t going to be fine next Sunday.',
    'Will you open the door?',
    'He won\'t wash his car tomorrow afternoon.',
    'Will he come to school tomorrow?',
    'We won\'t go on a picnic next week.',
    'Will you do your homework after school?',
    'I will not be watching TV tonight.',
    'He won’t be going to school tomorrow.',
    'I am going to be ten years old next year.',
    'Will they use this desk?',
    'He was laid off against his will.',
    'Will you call me back later?',
    'It will be colder tomorrow',
    'Will you read English before dinner?',
    'My friend won’t come here.',
    'I won\'t let you do it.',
  ],
}
test_data_0375 = { 

      # **Guideword:** FUTURE ARRANGEMENTS
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use the future continuous with 'will' to talk about an event or action in progress at a specified time in the future.
        
  'positive': [
    'I’ll be talking with him about the matter at noon tomorrow.',
    'The train will be passing the station in a few minutes.',
    'My daughter will be studying in the library tomorrow morning.',
    'This time tomorrow we’ll be attending the sales meeting.',
    'I’ll be seeing him soon.',
    'I’ll be playing tennis at 10 a.m. tomorrow.',
    'He will be playing soccer at three o’clock tomorrow.',
    'I will be watching TV at home this time tomorrow.',
    'He will be working in Tokyo at this time next year.',
    'I will be waiting for you at three o’clock.',
  ],
  'negative': [
    'My father has worked at the bank since 2000.',
    'She hasn’t had a bite of bread since yesterday.',
    'My brother has had a toothache for three days.',
    'It will not be sunny tomorrow.',
    'They won’t play baseball next week.',
    'I’ve known her since she was just a kid.',
    'You won\'t believe me if I tell you.',
    'I will send you a letter.',
    'I will go with her family tomorrow.',
    'I haven’t smoked for over two years.',
    'They have lived here for seven years.',
    'They’ve been married for five years.',
    'His theory has been the subject of much discussion since then.',
    'I have been busy since this morning.',
    'I won\'t study math tomorrow.',
    'It will be a long way to go.',
    'It will be great if you come with us.',
    'My grandfather has been dead for two years.',
    'You will know if you go there.',
    'You will be here tomorrow.',
  ],
}
test_data_0376 = { 

      # **Guideword:** AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the affirmative form with 'will' and 'shall'.
        
  'positive': [
    'I will be driving there this Thursday evening.',
    'My vacation will be ending in two weeks.',
    'It shall be touching down shortly.',
    'He shall be receiving a stiff punishment.',
    'I shall be living in Egypt starting next year.',
    'The president shall be speaking at the ceremony.',
    'We shall be waiting for you.',
    'I\'ll be reading you a section of my book tonight.',
    'He will be typing up the results by this evening.',
    'I\'ll be arriving in a minute.',
  ],
  'negative': [
    'I will have finished my homework when my parents go home.',
    'Will you be able to go to the rest of your classes?',
    'How long will it take to get there?',
    'Will you show me the way to the station?',
    'Which shall I take?',
    'How long will it take to the hotel?',
    'I won\'t be late for practice again.',
    'When will there be another chance?',
    'What shall I do now?',
    'Will you stop talking?',
    'Shouldn\'t we be working together?',
    'Shall I hold those for you?',
    'Won\'t we be taking a break?',
    'Will you show us around?',
    'Where shall we go next?',
    'Shall we open another bottle?',
    'What shall I wear?',
    'I don\'t know how long it will still be there.',
    'What shall I do?',
    'Won\'t you be playing with the rest of the orchestra?',
    'Shouldn\'t he be running the show?',
  ],
}
test_data_0377 = { 

      # **Guideword:** NEGATIVE WITH 'WILL'
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the negative form with 'will' ('won’t').
        
  'positive': [
    'The doctor won\'t be operating on you today.',
    'I won\'t be giving up my spot.',
    'You won\'t be getting away with this for long.',
    'They won\'t be changing any laws.',
    'He won\'t be crying wolf anymore.',
    'I won\'t be abandoning any of my friends.',
    'The door won\'t be opening any time soon.',
    'This cough won\'t be stopping any time soon.',
    'Your boss won\'t be letting you go home tonight.',
    'I won\'t be coming for practice again.',
  ],
  'negative': [
    'Where will we be meeting?',
    'My vacation will be ending in two weeks.',
    'I won\'t email you.',
    'Will you be playing with me?',
    'Will you be showing us around?',
    'How long will it take to the hotel?',
    'I will be arriving there this Thursday evening.',
    'I will be swimming in the ocean.',
    'Will you be able to go to the rest of your classes?',
    'Won\'t you show me the way to the station?',
    'What will you have?',
    'He will be defeated.',
    'I won\'t stay there.',
    'You will definitely do it.',
    'They will be hanging out this weekend.',
    'Will you be stopping any time soon?',
    'How long will it take to get there?',
    'It will be raining later today.',
    'When will there be another chance?',
    'Time won\'t come back.',
  ],
}
test_data_0378 = { 

      # **Guideword:** QUESTIONS
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'yes/no' and 'wh-' question forms with 'will'. 
        
  'positive': [
    'What time will you be leaving?',
    'Will you be drinking tonight?',
    'When will you be coming home?',
    'Will you be watching a movie?',
    'What will you be doing?',
    'Will you be working today?',
    'Will you be joining us?',
    'Will you definitely be coming?',
    'Will you be buying a flower?',
    'Will you be playing a game?',
  ],
  'negative': [
    'If you acknowledge your fault, I will pardon you.',
    'They will hang out.',
    'I will take the will for the deed.',
    'I will clean up my room.',
    'I will buy you dinner.',
    'I will resend it.',
    'The day will come when there will be no war.',
    'It will rain today.',
    'I will pay you back.',
    'He will be back.',
    'The time will come when you repent for it.',
    'I will take the bus.',
    'I will decide when we will play.',
    'Time will come back.',
    'He will make a big deal of it.',
    'I will continue it.',
    'You will receive no pay.',
    'I will watch that.',
    'My grandfather willed me his old watch.',
    'This will hurt more than it will help.',
    #Added to check for future continuous
    'Will you go to the museum?',
    'Who will write the book?',
  ],
}
test_data_0379 = { 

      # **Guideword:** POLITENESS
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the future continuous with 'will' as a polite question form, in place of the present simple or future simple.  
        
  'positive': [
    'Will he be coming to the meeting?',
    'Will you be waiting for her when her plane arrives tonight?',
    'will he be studying at the library tonight?',
    'Will you be feeling thirsty after working in the sun?',
    'Will you be bringing your friend to the pub tonight?',
    'Will you be watching TV when she arrives tonight?',
    'Will she be going to the party tonight?',
    'Will I be sleeping in this room?',
    'Will Jim be coming with us?',
    'Will I be staying in this room?',
    'Who will be helping out?',
    'Won\'t you be joining us?',
  ],
  'negative': [
    'You\'ll be missing the sunshine once you\'re back in England.',
    'I will take the bus.',
    'I will continue it.',
    'Will you work today?',
    'I\'ll be eating with Jane this evening so I can tell her.',
    'When he is in Australia he will be staying with friends.',
    'What will you do?',
    'Will you come without fail?',
    'Next year will she still wear a size six?',
    'Will you buy a flower?',
    'I will resend it.',
    'I\'ll be seeing Jim at the conference next week.',
    'Unfortunately, sea levels will still be rising in 20 years.',
    'Will you watch a movie?',
    'He will be back.',
    'I will buy you dinner.',
    'Tomorrow he\'ll still be suffering from his cold.',
    'we will still be driving through the desert.',
    'In an hour I\'ll still be ironing my clothes.',
  ],
}
test_data_0380 = { 

      # **Guideword:** EXPECTATIONS WITH 'MIGHT' OR 'MAY'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future continuous
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use the future continuous with 'might' or 'may' to talk about an event or activity potentially in progress at a specified or understood time in the future.
        
  'positive': [
    'He may be studying in the library.',
    'This time next week I may be sun-bathing in Bali.',
    'You may be missing the sunshine once you\'re back in England.',
    'He may be walking to the grocery store today.',
    'Tom may be going downtown.',
    'I guess you might be feeling thirsty after working in the sun.',
    'She might be taking a shower.',
    'By Christmas I may be skiing like a pro.',
    'Jack may be coming to see us tomorrow.',
    'Just think, next Monday you may be working in your new job.',
  ],
  'negative': [
    'I might see you tomorrow.',
    'Might we just interrupt for a moment?',
    'There may not be very many people there.',
    'May I use that?',
    'He may be wrong.',
    'It may rain tomorrow.',
    'He asked if he might borrow the car.',
    'She might be in London by now.',
    'Might I ask you a question?',
    'May we come a bit later?',
    'It looks nice, but it might be very expensive.',
    'He might take you for a girl.',
    'We may be late for the meeting.',
    'May I borrow the car tomorrow?',
    'You may need a new job.',
    'I may go to the movies tomorrow.',
    'You may not borrow the car until you can be more careful with it.',
    'They wanted to know if they might come later.',
    'She may not come to the party.',
    'It’s quite bright, so it might not rain today.',
  ],
}
test_data_0381 = { 

      # **Guideword:** 'BE ABOUT TO'
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future expressions with be
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present forms of 'be' + 'about to'.  
        
  'positive': [
    'She\'s about to open her presents.',
    'I\'m about to get on the bus.',
    'I\'m about to ask you something.',
    'The press conference is just about to start now.',
    'She is about to open the secret box.',
    'They are about to call you.',
    'The countdown is about to start.',
    'He is about to suggest it.',
    'He is just about to fall asleep.',
    'I\'m about to study English.',
  ],
  'negative': [
    'I\'m going to study English.',
    'I was about to kill him.',
    'I was about to go to bed.',
    'I was just about to close my shop.',
    'I was always about to drown.',
    'I was about to go out when he called on me.',
    'His smartphone was about to break.',
    'What would you like to talk about today?',
    'The meeting was just about to end when he arrived.',
    'The bus was about to leave.',
    'I was just about to be fooled.',
    'He was pretty much about to die.',
    'He was about to run.',
    'She was about to say.',
    'I was about to fall asleep.',
    'He was just about to become a murderer.',
    'I was about to use the shower.',
    'He was almost about to cry.',
    'The parade was about to start.',
    'I was just about to give up on that.',
  ],
}
test_data_0382 = { 

      # **Guideword:** 'BE DUE TO'
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future expressions with be
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present form of 'be' + 'due to'. 
        
  'positive': [
    'My husband is due to get another raise.',
    'I am due to have a meeting.',
    'Some of the doctors are due to have a qualifying exam in the coming weeks.',
    'They are due to go on vacation in august',
    'They are due to have another lunch.',
    'We are due to have some good luck finally.',
    'The train is due to arrive any minute now.',
    'She is due to arrive tomorrow.',
    'He is due to start work next week.',
    'I am due to go in for another appointment.',
  ],
  'negative': [
    'It is believed that Dinosaurs became extinct due to a meteor impact.',
    'I was absent yesterday due to a cold.',
    'The river banks collapsed due to heavy rain.',
    'The game was postponed due to rain.',
    'My younger brother is sleeping due to his illness.',
    'His failure was due to his incompetence.',
    'He has anemia due to an iron deficiency.',
    'Arrival may be delayed due to the heavy traffic.',
    'The collapse of the Mayan civilization was likely due to a relatively mild drought.',
    'The sum originally due to the bank has been doubled because of the interest.',
    'His death was due to heart-failure.',
    'I was late due to a traffic accident.',
    'I\'m having trouble due to a lack of funds.',
    'He cannot do chores due to work.',
    'I was hospitalized due to a fracture.',
    'I am sleep deprived due to the heat.',
    'He will be absent due to private business.',
    'My homework is due on Friday.',
    'He notes that the increase in births in 2008 was due to the fact that it was a leap year.',
    'I stayed in bed due to an illness.',
  ],
}
test_data_0383 = { 

      # **Guideword:** 'BE TO'
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future expressions with be
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the present form of 'be' + 'to'.
        
  'positive': [
    'She is to fly to Australia soon.',
    'A new factory is to start hiring workers starting next week.',
    'They are to develop new tools.',
    'He is to report on his findings at the meeting.',
    'I am to be his companion on his journey.',
    'The child is to go to boarding school.',
    'Either he or I am to be in charge of the new team.',
    'Your homework is to be placed in my mailbox before the weekend.',
    'That is to stop diarrhea.',
    'You are to meet with all of the representatives.',
  ],
  'negative': [
    'Mistakes are mainly due to carelessness.',
    'I am going to go to the art gallery.',
    'I am going to go to work.',
    'She is going to be a teacher.',
    'She\'s about to open her presents.',
    'That rumor is going to spread.',
    'He is just about to fall asleep.',
    'I am going to sleep.',
    'The countdown is about to start.',
    'The press conference was just about to start now.',
    'Everything is going to be fine.',
    'That is due to the weakness of an average man.',
    'I am going to kill him.',
    'The credit is due to you.',
    'Her absence is due to an illness.',
    'I am going to go fishing.',
    'I\'m about to study English.',
    'He is going to quit his school club.',
    'The train is due to arrive in Tokyo at ten.',
    'He looks like he is going to cry.',
  ],
}
test_data_0384 = { 

      # **Guideword:** IMMEDIATE FUTURE WITH 'BE ABOUT TO'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future expressions with be
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'be about to' to talk about the immediate future, often with 'just'. 
        
  'positive': [
    'I\'m about to go out.',
    'I\'m about to check in.',
    'She\'s about to leave on a trip to England.',
    'He is about to head off to school.',
    'The plane is just about to start.',
    'I am just about to go to bed now.',
    'I\'m just about to buy the ingredients now.',
    'I am just about to go walk the dog.',
    'I\'m about to go and pick my daughter up.',
    'I\'m just about to drop off the luggage now.',
  ],
  'negative': [
    'He was just about to be fooled.',
    'We were just about to buy the wrong picture.',
    'I was just about to get hit by a car.',
    'I was just about to close my shop.',
    'She was just about to give up on that.',
    'I was just about to call you.',
    'Everything is going to be fine.',
    'I am going to kill him.',
    'I am going to go to the art gallery.',
    'I am going to go to work.',
    'She is going to be a teacher.',
    'He looks like he is going to cry.',
    'We were just about to leave when it rained.',
    'He is going to quit his school club.',
    'We were just about to enter the room.',
    'I am going to go fishing.',
    'I am going to sleep.',
    'I was just about to do that.',
    'They were just about to get started anyhow.',
    'That rumor is going to spread.',
  ],
}
test_data_0385 = { 

      # **Guideword:** OBLIGATIONS AND  INSTRUCTIONS WITH 'BE TO'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future expressions with be
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'be to' talk about future obligations and to give instructions. 
        
  'positive': [
    'You are to vote in the Upper House election in July.',
    'I’m to clean up my room before I’m allowed to go out.',
    'We are to receive a pay raise in line with inflation in September.',
    'He is to have a dinner with the president tomorrow.',
    'We are to look after our neighbors’ dog while they are away.',
    'He is to have a physical check up next week.',
    'Work is to begin this week on the new bridge across the Nile.',
    'We’re not to smoke in the office.',
    'The Prime Minister is to make a state visit to Haiti next week.',
    'A man is to appear in court later this morning charged with the murder of his father.',
  ],
  'negative': [
    'I expected you to help me with my assignment which I have to report to my boss this Friday.',
    'My mother did not do anything but sit in the room crying all day long.',
    'I mean to end this relationship if you do not change your behavior.',
    'I make it a rule to send a good night message every night to my boyfriend.',
    'Don’t consider me to always be obedient to you.',
    'The customer thinks it\'s not easy to install the application by herself.',
    'Not to betray a secret of colleague to others is not easy.',
    'I want to go sing Karaoke by myself.',
    'I found it difficult to make my boss appreciate my efforts.',
    'She is determined to go to college to get a better job.',
    'He decided to change his carrier.',
    'I like coffee strong in the morning to clear my head.',
    'To choose first food restaurant is helpful to make meaningful use of lunch time.',
    'I chose to join the tennis circle from spring.',
    'It might be controversial to broadcast the sticky human resources issue.',
    'They thought it was fun to go to the hip-hop club together.',
    'My scooter didn\'t stop moving, but kept making a noise when I stepped on the pedal.',
    'It seems not easy for him to finish the report by tomorrow.',
    'I told her to get off of the swingset.',
    'Company appointed her to supervise the project team.',
  ],
}
test_data_0386 = { 

      # **Guideword:** SCHEDULES
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future expressions with be
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'be due to' and, more formally, 'be to' talk about things that are scheduled or expected. 
        
  'positive': [
    'The train is due to arrive at 8:00.',
    'The film is due to start at 8 pm.',
    'President Abe is to visit America next week.',
    'David is due to take his final exams next week before the end of the semester.',
    'We are to meet at 5.',
    'They are to get married in July.',
    'She is to arrive at Tokyo today.',
    'I am to meet the US President tomorrow.',
    'Half of our employees are due to retire in five years.',
    'We are due to arrive at Haneda airport at 10:00 p.m.',
  ],
  'negative': [
    'He canceled a trip during the summer vacation due to a drop in his income.',
    'Due to the heavy snow train service was halted.',
    'She couldn\'t get the praise that was due to her.',
    'The due date is next Friday.',
    'Your assignment is past due.',
    'Due to a technical problem, the car suddenly flipped over and its driver died.',
    'It’s due on Friday.',
    'Today\'s match was put off due to the rainy weather.',
    'I took a break from the company due to a cold.',
    'Mistakes are mainly due to carelessness.',
    'I\'m due for a promotion this spring.',
    'Her absence is due to an illness.',
    'Due to bad weather, the plane is delayed.',
    'We are closed today due to a power outage.',
    'He did not get money that was due to him for his work.',
    'The accident took place due to a variety of factors.',
    'This homework is due tomorrow, okay?',
    'The band broke up due to the vocalist\'s brainwashing issue.',
    'He couldn\'t run due to an injury.',
    'I’ll double-check the due date for the project outline.',
  ],
}
test_data_0387 = { 

      # **Guideword:** 'BE GOING TO'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future in the past
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use the simple past form of 'be' + 'going to' to talk about the future from a point in the past. ► 'be going to' 
        
  'positive': [
    'I thought I was going to die.',
    'He looked like he was going to smile.',
    'I felt like my wallet was going to be stolen in the subway abroad.',
    'Hillary Clinton was going to claim her victory as the first female president.',
    'I often thought I was going to be late for the bus.',
    'I didn\'t know what was going to happen.',
    'He left as if he was going to be sick.',
    'I was going to buy a new book.',
    'I thought that I was going to go to Osaka tomorrow.',
    'That\'s just what I was going to say.',
  ],
  'negative': [
    'That rumor is going to spread.',
    'It looks like it is going to rain.',
    'I am going to pick up that garbage.',
    'I’m going to go to America.',
    'I am going to go shopping in January.',
    'We are going to search for him.',
    'We are going to go to that facility.',
    'I am going to play alone.',
    'We are going to have a storm.',
    'He is going to kill me.',
    'I am going to gain weight.',
    'I am going to become strong too.',
    'We’re going to lose my house.',
    'Everything is going to be fine.',
    'My eyes are going to go bad.',
    'It is going to rain tomorrow.',
    'You are going to love it.',
    'He is going to write a book.',
    'We are going to make alcohol.',
    'I am going to go to the ocean today.',
  ],
}
test_data_0388 = { 

      # **Guideword:** 'WOULD'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future in the past
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'would' to talk about the future from a point in the past.► 'would'
        
  'positive': [
    'He answered that he would go.',
    'I thought I would die.',
    'He would be 60 years old when he died.',
    'He failed, as I said he would.',
    'He thought that she would become a singer.',
    'I thought that he would go there.',
    'He said he would study hard.',
    'You said you would do your best.',
    'I thought that it would rain yesterday.',
    'I knew it would be a good show.',
  ],
  'negative': [
    'Would you like to go for dinner with me?',
    'I would like to play tennis.',
    'Would you like to hang out together next time?',
    'I would like to go with you.',
    'What would you like to do while you\'re here?',
    'Would you like something to drink?',
    'Would you like another helping?',
    'Would you please pass me the book?',
    'Would you mind holding this?',
    'I would like to know.',
    'Would you mind if I asked you for your phone number?',
    'Would you like to dance with me?',
    'Would you like to come to our party tonight?',
    'Would you send me that by next Monday?',
    'Would you like to eat together?',
    'What would you like to eat?',
    'I would like to go to Central station.',
    'Would you like to go shopping with me?',
    'Would you like to take a look at it?',
    'Would you mind if I asked you to work today?',
  ],
}
test_data_0389 = { 

      # **Guideword:** 'BE ABOUT TO'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future in the past
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the simple past form of 'be' + 'about to' (often with 'just') to talk about the immediate future from a point in the past. 
        
  'positive': [
    'She was just about to take a bath when the bell rang.',
    'I was about to buy the wrong picture.',
    'I was just about to go out shopping when you telephoned.',
    'She was just about to order that from you now.',
    'Just two hours ago, we were about to enter the room.',
    'We were about to leave when it rained.',
    'I was about to go out, when the bell rang.',
    'I was just about to leave the house when the telephone rang.',
    'We were just about to leave when she telephoned.',
    'I was about to be fooled.',
  ],
  'negative': [
    'He is about to be a man.',
    'The sun is about to sink below the horizon.',
    'I am going to kill him.',
    'I am going to go to work.',
    'He is going to quit his school club.',
    'I\'m just about to buy the ingredients now.',
    'He is just about to head off to school.',
    'She\'s just about to leave on a trip to England.',
    'I\'m just about to drop off the luggage now.',
    'I\'m just about to go and pick my daughter up.',
    'My mum is about to take a bath.',
    'I am just about to go to Hakata station too.',
    'Everything is going to be fine.',
    'I am just about to go to bed now.',
    'He looks like he is going to cry.',
    'I am just about to go walk the dog.',
    'She is going to be a teacher.',
    'That rumor is going to spread.',
    'That precipice is about to crumble.',
    'The plane is just about to start.',
    'The doorknob is about to come off.',
  ],
}
test_data_0390 = { 

      # **Guideword:** 'BE ON THE POINT OF'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future in the past
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the simple past form of 'be' + 'on the point of' + '-ing' to talk about things that were expected to happen soon after a point in the past. 
        
  'positive': [
    'The film was on the point of starting.',
    'I was on the point of drowning.',
    'I got to the station when the train was on the point of leaving.',
    'She was on the point of going out of her apartment.',
    'He was rescued just when he was on the point of drowning.',
    'I was on the point of going out when the phone rang.',
    'The train was on the point of starting.',
    'He was on the point of leaving.',
    'Our party was on the point of splitting apart.',
    'I was on the point of getting out when the bus began to move.',
  ],
  'negative': [
    'You are open to attack at every point.',
    'He is on the point of death.',
    'The point of the knife is broken.',
    'He is on the point of leaving for Canada.',
    'What is the point of dating without games?',
    'That is my point of view.',
    'The train is on the point of leaving.',
    'The Cabinet is on the point of failing.',
    'He broke the point of his pencil.',
    'That bank is on the point of failing.',
    'That settles the point.',
    'I came to the point at once.',
    'The poor girl was on the point of death.',
    'The enemy soldier died on the point of his spear.',
    'He lies at the point of death.',
    'That is his weak point.',
    'That\'s the point.',
    'Come to the point.',
    'I will come to the point at once.',
    'I refused point-blank.',
  ],
}
test_data_0391 = { 

      # **Guideword:** 'BE DUE TO'
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future in the past
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use the simple past form of 'be' + 'due to' to talk about scheduled events in the future from a point in the past. 
        
  'positive': [
    'They backed out of the deal the day before they were due to sign the contract.',
    'He was due to appear in court again on Monday.',
    'Last I heard, their first baby was due to be born next January.',
    'The baby was due to arrive on Monday.',
    # dependencies error, ROOT -> bus (ROOT)
    # 'What time was the bus due to arrive?',
    'The meeting was due to be held in three months\' time.',
    'The parliamentary session was due to end on May 27.',
    'The chairman was due to retire next month.',
    'He was due to arrive tomorrow.',
    # dep errors, but not consistent with each other
    # 'When was the package due to arrive?',
    # 'When were you due to speak at the event?',


  ],
  'negative': [
    'It is due to your age.',
    'His death was due to wine.',
    'The game was postponed due to rain.',
    'He is due to arrive tomorrow.',
    'The war was due to various causes.',
    'The accident was due to careless driving on his part.',
    'His failure was due to his incompetence.',
    'Their success was due to his inhuman efforts.',
    'The fire must be a case of arson.',
    'He is going to be absent due to a cold.',
    'His failure in business was due to his own laziness.',
    'Dreams are due to the fatigue of the internal organs.',
    'It was due to an accident or fortuity.',
    'I thought that it was just due to stiff shoulders.',
    'Their first baby is due in January.',
    'This problem was due to a mistake on the customer\'s part.',
    'The fire was due to leakage of electricity.',
    'This was due to the closure of Yase Amusement Park in 2001.',
    'The school closure was due to the heavy snow.',
    'This was due to a failed abortion according to the Masukagami.',
  ],
}
test_data_0392 = { 

      # **Guideword:** AFFIRMATIVE
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the affirmative form with 'will'.
        
  'positive': [
    'He will have been living in Japan for three years next month.',
    'If you play games tonight, you will have been putting off your studies for a whole week straight.',
    'I will have been reading this book at least once a year for 10 years this year.',
    'I will have been living here for 20 years by next month.',
    'By the time I come home, my mother will have been cooking dinner for at least an hour.',
    'If I go to Disneyland next week, I will have been visiting the park for 7 years.',
    'In another ten minutes, I will have been doing my homework for 5 hours.',
    'You will have been going to that university for 10 years next fall.',
    'I will have been working on it and made quite a bit of progress by the time you come back.',
    'The exams will have been going on for 3 days at that point, nobody will have any free time.',
  ],
  'negative': [
    'By ten thirty, we will have turned off the TV and gone to bed.',
    'He has visited Sydney once before.',
    'I have lost the watch.',
    'He will have wait until I call him.',
    'I have never lost my wallet.',
    'The picture has already arrived at the museum.',
    'Yuri has never ridden a horse.',
    'He has recently returned from Tokyo.',
    'The train has just arrived at the station.',
    'He has been awarded prizes more than ten times.',
    'Summer has come.',
    'She has already left home.',
    'You’ve bought a new car, haven’t you?',
    'I have just finished my homework.',
    'I have met him before.',
    'He has recently published a book.',
    'The Hollywood star has never disappointed me as an actor.',
    'Akira hasn’t come home from school yet.',
    'I have lost my way in the woods before.',
    'Kate has watched that DVD many times.',
  ],
}
test_data_0393 = { 

      # **Guideword:** NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** None
        
  'positive': [
    'I won\'t have been living here for six months yet on June 23rd.',
    'He won\'t have been cooking anything yet by the time we get home.',
    'I won\'t have been finishing up the work yet by the time my friend comes.',
    'You won\'t have been volunteering there for more than half a year at most by then.',
    'She won’t have been avoiding the chores.',
    'They will not have been working on this homework for more than a few days by next Monday.',
    'You won\'t have been writing your report for more than a couple hours by tomorrow.',
    'We won\'t have been waiting around for more than about fifteen minutes.',
    'She won’t have been driving a car for more than a year yet by her birthday.',
    'I won\'t have been reading the book for too long by next Sunday.',
  ],
  'negative': [
    'When I come at 6:00, will you have been practicing long?',
    'I will have been waiting here for three hours by the time you get out of work at six o\'clock.',
    'Next year I will have been working here for four years.',
    'If I go to Disneyland next week, I will have been there five times.',
    'He will have lived in Japan for three years next month.',
    'I will have done it by the time you come back.',
    'He will have been waiting until I call him.',
    'By ten thirty, we will have been watching TV for five hours.',
    'Will she have bought a new bag tomorrow afternoon?',
    'He won\'t like waiting for us to eat dinner.',
    'When I finish this course, I will have been learning English for twenty years.',
    'I will have read this book by tomorrow.',
    'Won\'t they have arrived by 5:00?',
    'Will you have finished this homework by next month?',
    'The exams will have finished by Wednesday.',
    'By 2001 I will have been living in London for sixteen years.',
    'Will you have read the book by next Sunday?',
    'Will you have eaten when I pick you up?',
    'The concert will have finished by the time she gets there.',
    'Will you have finished the work when your friend comes?',
  ],
}
test_data_0394 = { 

      # **Guideword:** LOOKING BACK FROM A POINT IN THE FUTURE
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future perfect continuous
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the future perfect continuous to look back to the past from a point in the future and to emphasise the duration of an activity or event.
        
  'positive': [
    'You will have been waiting for more than two hours when her plane finally arrives.',
    'I will have been reading forty-five books by Christmas.',
    'When I finish this course, I will have been learning English for twenty years.',
    'I will have been waiting here for three hours by six o\'clock.',
    # 'When I come at 6:00, will you have been practicing long?',
    # youのposが","判定される．
    'James will have been teaching at the university for more than a year by the time he leaves for Asia.',
    'They will have been talking for over an hour by the time Thomas arrives.',
    'By 2001 I will have been living in London for sixteen years.',
    'Next year I will have been working here for four years.',
    'At five o’clock, I will have been waiting for thirty minutes.',
  ],
  'negative': [
    'Will she have bought a new bag tomorrow afternoon?',
    'She is having dinner.',
    'You are walking in the park.',
    'She won’t have driven her car by next year.',
    'I won\'t have been here for six months on June 23rd.',
    'The exams will have finished by Wednesday.',
    'I won\'t have finished the work when my friend comes.',
    'When I come at 6:00, would you have been practicing long?',
    'I won\'t have finished my homework when you come.',
    'He will have wait until I call him.',
    'Won\'t they have arrived by 5:00?',
    'He will have lived in Japan for three years next month.',
    'He is doing his homework.',
    'Will you have eaten when I pick you up?',
    'By the time you read this I won\'t have left.',
    'I am playing tennis now.',
    'At this rate, they won\'t have any more to do by next weekend.',
    'By ten thirty, we would have been watching TV for five hours.',
    'You are studying English.',
    'I will have done it by the time you come back.',
  ],
}
test_data_0395 = {

  # **Guideword:** ASSUMPTIONS
  # **Guideword type:** USE
  # **Super category:** FUTURE
  # **Sub category:** future perfect continuous
  # **Lexical Range:** None
  # **CEFR level:** C2
  # **CAN-DO:** Can use the future perfect continuous to make assumptions about the present.

  'positive': [
    "I'm sure you will have been waiting here for ages.",
    "It is supposed that I will have been living in London for many years by then.",
    "I assume that you will have been learning English for a long time.",
    "She expects that he will have been trying his hardest to solve the problem.",
    "The boss expects that all of you will have been preparing yourselves for the big meeting.",
    "It is expected that they will have been working at my company until then.",
    "I estimate that you will have been waiting for at least thirty minutes.",
    "I assume you will have been studying hard for the exam.",
    "They hope that you will have been looking forward to the meeting.",
    "In order to be ready for the challenge, it is expected that you will have been training for years before the actual event date.",
  ],
  'negative': [
    "On Thursday, I will have been working for one year.",
    "I will have read forty-five books by Christmas.",
    "I will have been here for six months on June 23rd.",
    "By the time you read this I will have left.",
    "You will have finished your report by this time next week.",
    "Won't they have arrived by 5:00?",
    "Will you have been waiting long by the time I can pick you up?",
    "I've wanted to visit China for years.",
    "She's known Robert since she was a child.",
    "I've hated that music since I first heard it.",
    "I've heard a lot about you recently.",
    "We've understood everything.",
    "I’ve just been cleaning the car.",
    "It’s been snowing",
    "What have you been buying?",
    "I’ve been going to Spain on holiday every year since 1987.",
    "I haven’t been eating much lunch lately. I’ve been going to the gym at lunchtimes.",
    "She’s been playing tennis on and off for three years.",
    "This time next week I will be sun-bathing in Bali.",
    "How long have you been waiting for me?",
  ],
}
test_data_0396 = {

  # **Guideword:** AFFIRMATIVE
  # **Guideword type:** FORM
  # **Super category:** FUTURE
  # **Sub category:** future perfect simple
  # **Lexical Range:** None
  # **CEFR level:** B2
  # **CAN-DO:** Can use the affirmative form with 'will'.

  'positive': [
    'By the time I get home, Zoe will have cooked dinner for both of us.',
    'By the time he graduates, he will have completed five years of study.',
    'I will have been here for six months on June 23rd.',
    'She will have gotten ready by the time they leave the house.',
    'By the time you read this I will have left.',
    'The robbers will have taken all the money by the time anyone arrives.',
    'Laura will have cleaned out the apartment before she gives back the key.',
    'You will have finished your report by this time next week.',
    'If all goes well, by June 2012, I will have finished my university degree.',
    'Jack will have finished his homework by the time his mother gets home.',
  ],
  'negative': [
    'They will have been talking for over an hour by the time Thomas arrives.',
    'How many times will he have been to Kyoto if he goes there again?',
    'How long will you have lived in Japan by next year?',
    'How many times will you have visited England if you visit again?',
    'You will have been waiting for more than two hours when her plane finally arrives.',
    'He will have been waiting for 3 hours when I call him.',
    'Will you have read the book by next Sunday?',
    'I won\'t have finished the work when my friend comes.',
    'How long will the house have stood there by next summer?',
    'They\'ll say they have waited for weeks already when we call them.',
    'When I come at 6:00, will you have been practicing long?',
    'At the end of this month, I will have been staying in this country exactly for three years.',
    'Will you have eaten when I pick you up?',
    'At five o’clock, I will have been waiting for thirty minutes.',
    'Will she have gotten her passport by then?',
    'I will have been reading this book for 6 months by Christmas.',
    'By ten thirty, we will have been watching TV for five hours.',
    'Won\'t they have arrived by 5:00?',
    'I won\'t have read the book by next Sunday.',
    'Will you have finished the work when your friend comes?',
  ],
}
test_data_0397 = {

      # **Guideword:** NEGATIVE
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the negative form with 'will'. 
        
  'positive': [
    'She won’t have been to TDL four times.',
    'She won’t have driven her car for months.',
    'She won’t have gone to England three times.',
    'I will not have started high school by then.',
    'I won\'t have finished the work when my friend comes.',
    'I will not have learned much from my teacher by the end of this semester.',
    'Ken will not have played tennis for ten years.',
    'You won’t have lived until you try this chocolate cake.',
    'I won\'t have read the book by next Sunday.',
    'She won’t have bought a new bag yet.',
  ],
  'negative': [
    'The match will have finished by the time I leave work.',
    'I will have worked here for three years next year.',
    'Will she have gotten her passport by then?',
    'How many times will you have visited England if you visit there again?',
    'She will have gotten ready by the time they leave the house.',
    'The robbers will have taken all the money by the time anyone arrives.',
    'How long will you have lived in Japan by your next birthday?',
    'Next year I will have worked for this company for 10 years.',
    'With my next trip I will have been to Tokyo five times.',
    'Will you have finished the work when your friend comes?',
    'Will you have read the book by next Sunday?',
    'Will she have bought a new bag by tomorrow afternoon?',
    'In 5 years time I will have graduated from university.',
    'By the time he graduates, he will have completed five years of study.',
    'Jack will have finished his homework by the time his mother gets home.',
    'You will have finished your report by this time next week.',
    'Will she have driven her car by next year?',
    'Will you have eaten when I pick you up?',
    'Will she have been to TDL four times by then?',
    'She will have bought a new bag by tomorrow afternoon.',
  ],
}
test_data_0398 = { 

      # **Guideword:** EVENTS COMPLETED IN THE FUTURE
      # **Guideword type:** USE
      # **Super category:** FUTURE
      # **Sub category:** future perfect simple
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use the future perfect simple with 'will' to talk about something which is expected to be completed (or not completed) by a certain point in the future.
        
  'positive': [
    'John will not have eaten the whole cake, by the time the birthday party starts.',
    'By the time he graduates, he will have completed five years of study.',
    'In 5 years time I will have graduated from university.',
    'By the time you read this I will have left.',
    'You will have finished your report by this time next week.',
    'You will have finished by the time I am ready.',
    'The football player will have signed the contract by the beginning of July.',
    'The match will have ended by the time I can leave work.',
    'By next June I will have gone to Spain.',
    'Before they come, we will not have finished cleaning up the house.',
  ],
  'negative': [
    'Will she go to TDL for a fourth time?',
    'I will visit Tokyo five times in the next year.',
    'I will finish this book, if it kills me.',
    'Will she have to buy a new bag tomorrow afternoon?',
    'Will you be done by the time I am ready?',
    'She will not have to finish her work.',
    'Will she have her car by next year?',
    'She won’t drive her car before next year.',
    'Will our children have to return from school early today?',
    'Will they arrive soon?',
    'She will not have dinner tonight.',
    'It will not stop raining.',
    'I won’t have to turn it in this year.',
    'Will you read the book by next Sunday?',
    'How long will you have to live in Japan?',
    'I will not be in high school by next year.',
    'How many times will you have to go to England for your new job?',
    'You will not have been studying the English tenses for long at this point.',
    'Ken will not play tennis after his surgery.',
    'He will not leave.',
  ],
}
test_data_0399 = { 

      # **Guideword:** WITH ADVERBS
      # **Guideword type:** FORM
      # **Super category:** FUTURE
      # **Sub category:** future perfect simple
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use the future perfect with adverbs (in the normal mid-position). 
        
  'positive': [
    'We will possibly have returned home by five o\'clock.',
    'We will maybe have met Julie.',
    'She will probably have cooked dinner.',
    'I will maybe have finished this book.',
    'It will possibly have stopped raining.',
    'Luke will maybe have been sick for two weeks tomorrow.',
    'You will probably have finished your report by this time next week.',
    'They will surely have left Japan.',
    'You will surely have studied the English tenses.',
    'He will almost certainly have arrived by now.',
  ],
  'negative': [
    'Next week you will have had this car for twenty five years!',
    'Anthony won\'t have arrived by then.',
    'Next Monday we will have been married for ten years.',
    'By the time he graduates, he will have completed five years of study.',
    'Tomorrow Justin will have been single for a whole week.',
    'Won\'t they have arrived by 5:00?',
    'Her heel will have fully healed by the summer.',
    'They\'ll have had their dinner by then.',
    'We are on vacation. So by the time we get back, we will have rested and relaxed.',
    'In September I will have lived here for eight years.',
    'She\'ll have forgotten everything.',
    'By the time he wakes up, we will have prepared lunch for everyone.',
    'Will you have eaten when I pick you up?',
    'By tomorrow, their life will have changed completely.',
    'By next month, you will have received your promotion.',
    'I\'ll have finished when you arrive.',
    'The snow will have stopped by April.',
    'I will have been here for six months on June 23rd.',
    'They won\'t have finished working on the car tomorrow.',
    'By the time you read this I will have left.',
  ],
}
