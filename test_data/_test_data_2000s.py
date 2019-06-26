test_data_2001 = { 

        # **Super category:** Sentences forms 1
        # **Sub category: **SV
        
  'positive': [
    'I don\'t agree with your plan.',
    # 'Dogs bark.',
    # parser's problem
    'Dogs barked.',  # これならいける
    'My back hurts.',
    'She\'s doing well at school.',
    'I came home early today.',
    'I live in a small apartment.',
    'The two sisters walked home together.',
    'Many people died in the war.',
    'The concert just ended.',
    # 'I went to the supermarket to buy some fruit.',
    # TODO: to不定詞用法判定
    # to不定詞の用法を判定できないのでできませんでした
    'I spoke to her yesterday and told her I was sorry.',
    'I\'ll send you a postcard when I get to Spain.',  # get
  ],
  'negative': [
    'I want a drink.',
    'He\'s trying to reach the top.',
    'I live a simple life.',
    # 'She loves to sing while listening to music.',
    # parser's problem
    'The girls are learning how to dance.',
    'The dominant lion becomes the head of his pride.',
    'I am getting a little tired of all this rain.',
    'My grandmother is slowly going deaf.',
    'I sometimes go jogging in the park.',
    'A cold beer tastes great in the summer.',
    'I give my dog a reward when he does the trick.',
    'He\'s feeding his dog a snack.',
    'She showed us the correct number.',
    'Everyone calls her Mary.',
    'My kids are driving me crazy.',
    'Many people find coffee in the morning indispensable.',
    'She is painting the wall blue.',
    'Regular exercise keeps you healthy.',
    'They keep their way all morning.',
  ],
}
test_data_2002 = { 

        # **Super category:** Sentences forms 1
        # **Sub category: **SVO
        
  'positive': [
    'My boss often complains that I don\'t work hard enough.',
    'They can\'t decide which way to go.',
    'I surely regret eating that dish.',
    'We discussed whether we should join the union.',
    'I left a note for her on the kitchen table.',
    'I don\'t think this method is going to work.',
    'Her mom is helping her with her dress.',
    'You should walk your bike on the sidewalk.',
    'Today she will begin intensive training for the race.',
    'I bought a new set of golf clubs for my father.',
    'They have agreed to work together on the new project.',  # agree
    'I forgot to ask my wife to buy more groceries.',  # forgot
    'I watched the sunrise from the top of the mountain.',  # watched
  ],
  'negative': [
    'He asked me to marry him.',  # SVOO
    'The mountain suddenly appeared from behind the clouds.',
    'The students in this class behave well.',
    'Turn right when you get to the stop sign.',
    'He\'s talking on the phone.',
    # 'I lay around in my room all day today.',
    # parser's problem: lay->day, dobj
    'I\'m getting bored with my job.',
    'This wine is of very high quality.',
    'Her job is to provide customer support.',  # 補語がto不定詞のとき、beがcopula扱いにならないようですね
    'She served as a maid at a hotel for a year.',
    'The recent layoffs cost him his job.',
    'My little girl asks me many questions.',
    'His ideas won him great popular support.',
    'I bought my father a new set of golf clubs.',
    'I had my report finished.',
    # 'Please let me do that.',
    # 'The kids are helping their mom do the laundry.',
    'Name tags help people to recognize you.',
    # 以下追加
    'A supervisor gives us a briefing, before the conference',
  ],
}
test_data_2003 = { 

        # **Super category:** Sentences forms 1
        # **Sub category: **SVC
        
  'positive': [
    'These are all great books.',
    'Recently I\'ve become very interested in wine.',
    'I am getting a little tired of all this rain.',
    'My grandmother is slowly going deaf.',
    'Things sometimes go bad but they usually come good again.',
    'Something smells very strange.',
    'Your plan sounds good to me.',
    'The weather forecast looks good for this week.',
    'I\'ve been feeling exhausted recently.',
    'His dream came true.',
    'My wife says it\'s my responsibility to do the dishes.',
  ],
  'negative': [
    'Chicks chirp.',
    'I came home early today.',
    'Camels can live without water for several days.',
    'The two sisters walked home together.',
    'Children learn quickly.',
    'I feed my cattle primarily grain that is plentiful around my village.',
    'She showed us the correct number.',
    'She is teaching her daughter how to read.',
    'My dog brought me the newspaper.',
    'She is reading her child a story.',
    'She loves to sing while listening to music.',
    'The girls are learning how to dance.',
    'I hope the weather clears up soon.',
    'They should stop that absurd fighting.',
    'My kids are driving me crazy!',
    'She is finding it hard to adapt to her new school.',
    # 'They make each other happy.',
    # parser's problem: happy->other (nmod:npmod)
    'The birth of their daughter made them very happy.',
    'I felt something touch my shoulder.',
  ],
}
test_data_2004 = { 

        # **Super category:** Sentences forms 1
        # **Sub category: **SVOO
        
  'positive': [
    'I\'ll send you a postcard when I get to Spain.',
    'She showed us the correct number.',
    'She\'s writing herself a note before she forgets.',
    'My dog brought me the newspaper.',
    'She offered me some cookies.',
    'He gave Sally a ring.',
    # parser's problem
    # 'His ideas won him great popular support.',
    # 'I feed my cattle primarily grain that is plentiful around my village.',
  ],
  'negative': [
    'She forgot to ask her boss if she could take the day off.',  # ask主語なし
    'I forgot to ask my wife to buy more groceries.',  # ask主語なし
    'I will give the idea of careful consideration.',
    'She is painting the wall blue.',
    'Get your hands dirty if you care.',
    'I pushed the door open for her.',
    'The cold weather turned the leaves gold.',
    'I saw you standing in front of the store.',
    'I\'ll talk to you later.',
    'A cat is lying in the sun.',
    'She looked to see if anyone required her aid.',
    'The factory workers begin early in the morning.',
    'My husband and I just moved to a new house.',
    'They said something to him.',
    'She was starting to lose patience with him.',
    'Can you see that tiny bird over there?',
    'All of the data has finished printing.',
    'I\'m beginning to have some doubts about him.',
    'Her job is to provide customer support.',
    'I work as a secretary in a bank.',
    'They have agreed to work together on the new project.',
    'He appears to be quite eccentric.',
    'I fell asleep on the flight.',
  ],
}
test_data_2005 = { 

        # **Super category:** Sentences forms 1
        # **Sub category: **SVOC
        
  'positive': [
    # 'She named her dog Max.',
    # parser's problem: Max(NN)->dog, compound
    'She is finding it hard to adapt to her new school.',
    # 'She is painting the wall blue.',
    # parser's problem: blue(NN)->wall, compound
    'Regular exercise keeps you healthy.',
    'The police forced John to talk.',
    # 'Please let the blind down.',
    # parser's problem: let->down (compound:prt)
    'I felt something touch my shoulder.',
    'The kids are helping their mom do the laundry.',
    'This medicine will help you get better.',
    'He doesn\'t want his wife to spend much money.',
    'I told John to see a doctor.',
    # 以下追加
    'She is painting the wall bright.',
    'I believe the man reliable.',
    'These words made our boss happy.',
    'I noticed someone stand by the door.',
    'Everyone reported him to be the best man for the job.',
    'Will you please let me go in his place?',
  ],
  'negative': [
    'I watched the sunrise from the top of the mountain.',
    'Something smells very strange.',
    'A cold beer tastes great in the summer.',
    # 'Staying at home and renting a movie sounds like fun.',
    'The weather forecast looks good for this week.',
    'She feels embarrassed about her mistake.',
    'I don\'t agree with your plan.',
    'I spoke to her yesterday and told her I was sorry.',
    'The factory workers begin early in the morning.',
    'She\'s leaving for work now.',
    'Coffee always sells well in the morning.',
    'I hope he shows up soon.',
    'They should stop that absurd fighting.',
    'He hopes to find a job soon.',
    'I wonder what animals think about.',
    'She started talking at an early age.',
    'She showed us the correct number.',
    # 'She is teaching her daughter how to read.',
    # parser's problem: teaching->read, xcomp (expected: advcl:to)
    'The waiter brought us our cocktails.',
    # 'I bought my father a new set of golf clubs.',
    # parser's problem: bought->set, xcomp
    # 'His ideas won him great popular support.',
    # parser's problem: won->support, xcomp
    # 以下追加
    'Staying at home movie sounds like fun.',
  ],
}
test_data_2006 = {

        # **Super category:** Sentences forms 1
        # **Sub category: **There + be
        
  'positive': [
    'There are all great books.',
    'There are some books in my bag.',
    'There is a library in our town.',
    'There is much water in the lake.',
    'There was an old shrine in the village.',
    'Is there a computer on the desk?',
    'There is a picture on the wall.',
    'There weren\'t any animals in that forest.',
    'There isn\'t a school in the town.',
    'There are seven days in a week.',
  ],
  'negative': [
    'Let\'s go over there.',
    'I\'m heading over there now.',
    'It doesn\'t snow over there.',
    'The toilet is over there.',
    'I\'ll go over there next Wednesday.',
    'I read that book over there on the desk.',
    'Let\'s have a meeting over there.',
    'It seems comfortable to live over there.',
    'I am not going to go over there tonight.',
    'The sales slip for this is over there.',
    'The two sisters walked home together.',
    'Children learn quickly.',
    'My dog brought me the newspaper.',
    'She is reading her child a story.',
    'I hope the weather clears up soon.',
    'They make each other happy.',
    'The birth of their daughter made them very happy.',
    'I felt something touch my shoulder.',
    'I don\'t know about that.',
    'You can call me anytime.',
  ],
}
test_data_2007 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **肯定文
        
  'positive': [
    'There\'s a difference between what you describe and what my neighbors have.',
    'There are lots of convenience store near my house.',
    'Your life seems much fun and I want to be like you.',
    'They gave their money to him so they can take his wife as trade.',
    'His sister is older than my older brother.',
    'I somehow had to carry my sister\'s bag since she broke her right arm.',
    'There are a bunch of nice guys in our school compared with your school.',
    'It\'s fantastic that we can recognize our problem and maintain the proper will to break the addiction.',
    'You can call me anytime if you need me.',
    'I like to sing a Japanese song.',
  ],
  'negative': [
    'I didn\'t know the fact.',
    'I don\'t agree with it.',
    'I can\'t say anything about its reliability.',
    'She doesn\'t like you at all.',
    'You can\'t go out now because you have to do your work.',
    'My father doesn\'t know how to cook.',
    'You shouldn\'t be here right now.',
    'You don\'t play any musical instruments.',
    'I haven\'t done my homework yet.',
    'You wouldn\'t like it if you know the truth.',
    'Do I know you?',
    'Do you like to play any sports?',
    'Did she know that you can\'t come tomorrow?',
    'Can you speak English well?',
    'Will you come to the party tomorrow?',
    'May I help you?',
    'What kinds of foods do you like the most?',
    'Where have you been before?',
    'When was your last time to play baseball with us?',
    'How do you know about that?',
  ],
}
test_data_2008 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **否定文
        
  'positive': [
    'I shouldn\'t have been here since I was sick.',
    'You can\'t come with us because you should stay with your family.',
    'I can\'t say anything about its reliability.',
    'She doesn\'t like you at all.',
    'You can\'t go out now because you have to do your work.',
    'She won\'t be here next week.',
    'You may not enter the room.',
    'You don\'t play any musical instruments.',
    'I haven\'t done my homework yet.',
    'You wouldn\'t like it if you know the truth.',
    'Did she know that you can\'t come tomorrow?',
  ],
  'negative': [
    'Do you like to play any sports?',
    'Does she want me to be with you?',
    'Can you speak Japanese well?',
    'Could you bring me some water?',
    'Are you sure about what you just said?',
    'Am I correct?',
    'What time is it now?',
    'Will you come to the party tomorrow?',
    'May I help you?',
    'What kinds of foods do you like the most?',
    'Where have you been before?',
    'Have you used this machine before?',
    'When was your last time to play baseball with us?',
    'How do you know about that?',
    'My husband and I just moved to a new house.',
    'They have agreed to work together on the new project.',
    'She\'s writing herself a note before she forgets.',
    'My dog brought me the newspaper.',
    'His ideas won him great popular support.',
    'A flu virus infected the whole class.',
  ],
}
test_data_2009 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **yes/no question
        
  'positive': [
    'Do you like to play any sports?',
    'Did she know that you can\'t come tomorrow?',
    'Does she want me to be with you?',
    'Can you speak Japanese well?',
    'Could you bring me some water?',
    'Are you sure about what you just said?',
    # 'Am I correct?',
    # parser's problem: am->correct, ccomp
    'Do you know someone who can trust?',
    'Should I stay here with you?',
    'Will you open the door for me?',
  ],
  'negative': [
    'What time is it now?',
    'What kinds of foods do you like the most?',
    'Where have you been before?',
    'When was your last time to play baseball with us?',
    'How do you know about that?',
    'What do you know about me?',
    'What did you do yesterday?',
    'When did you go to bed last night?',
    'What animal do you like the most?',
    'What will you do next week?',
    'Where will you go tomorrow?',
    'Why did you go back home so early?',
    'Why don\'t you join us?',
    'How did you know about this accident?',
    'How can I know that you\'re sick?',
    'How do you get here from your house?',
    'Which books do you like?',
    'My husband and I just moved to a new house.',
    'They have agreed to work together on the new project.',
    'She\'s writing herself a note before she forgets.',
  ],
}
test_data_2010 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **wh question
        
  'positive': [
    'What time is it now?',
    'What kinds of foods do you like the most?',
    'Where have you been before?',
    # TODO wh question
    # 'When was your last time to play baseball with us?',
    'How do you know about that?',
    'What will you buy at the store tomorrow?',
    'When did you go to bed last night?',
    'Why did you go back home so early?',
    'Why don\'t you join us?',
    'How do you get here from your house?',
  ],
  'negative': [
    'Do you like to play any sports?',
    'Did she know that you can\'t come tomorrow?',
    'Does she want me to be with you?',
    'Does it make any senses?',
    'Do I know you?',
    'Did you go to the school yesterday?',
    'Can you speak Japanese well?',
    'Could you bring me some water?',
    'Are you sure about what you just said?',
    'Are you going to play baseball tomorrow?',
    'Am I correct?',
    'Do you know someone who can trust?',
    'Should I stay here with you?',
    'Should I stay or go now?',
    'Would you mind if I use the restroom?',
    'Would you like to eat with me?',
    'Will you open the door for me?',
    'Were you sad at the moment?',
    'Is it important for you to stay at your house all day?',
    'Are there any restaurants near here?',
    'Tell me about your experience in Madrid.',
    'Study hard and you will pass the exam.',
    'Stop talking or I’ll have to ask you to leave the room.',
    'Don’t be late for the orchestra practice tomorrow.',
    'Jamie and Kelly laughed uncontrollably.',
    'We talked for hours about politics.',
    'The trees were moving in the breeze.',
  ],
}
test_data_2011 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **question tag
        
  'positive': [
    'He respects his father, doesn’t he?',
    'Your favorite food is a cheeseburger, isn’t it?',
    'He has a younger sister, doesn’t he?',
    'Holly didn’t leave the house last night, did she?',
    'You don’t recognize me, do you?',
    'She eats meat, doesn’t she?',
    'Your father is a doctor, isn’t he?',
    'I’m the fastest runner, aren’t I?',
    'You won’t tell anyone my secret, will you?',
    'They weren’t here yesterday, were they?',
  ],
  'negative': [
    'She took a shower before I did.',
    'My oldest sister is a professional violinist.',
    'Our neighbor is an Italian chef.',
    'My new job is to take care of dogs and cats.',
    'The tall man over there is my new teacher.',
    'The pretty maid served us breakfast in bed.',
    'My son should be hiding somewhere.',
    'Our cousins live nearby.',
    'My dad is reading a magazine downstairs.',
    'Amy lives near the train station.',
    'I went abroad to study contemporary music.',
    'Doesn’t she look beautiful in that dress?',
    'Aren’t you hungry after studying so much?',
    'Isn’t he driving you home tonight?',
    'Wasn’t the cake delicious?',
    'Don’t you have to look after your sister after school?',
    'Have you been to Singapore before?',
    'Do you have any siblings?',
    'Hadn’t you met her before?',
    'Could you pass me the salt?',
    'What do you want?',
  ],
}
test_data_2012 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **間接疑問文（できたら）
        
  'positive': [
    'I wonder what dad has to say about this.',
    'Tell me which book is more interesting.',
    'I don’t know who will clean our classroom.',
    'I\'m not sure whether she will come.',
    'I don\'t know when she will come.',
    'I did not realize what Tom was like.',
    # 自由副詞
    # TODO
    # 'Do you know where my bowling shirt is?',
    # 'Do you know where he lives?',
    # 'Do you know why Ken likes Charlotte?',
    # 'Do you know where Susan is?',
  ],
  'negative': [
    'Does he know the answer to this question?',
    'Why do you think he was in New York?',
    'How many people do you think was at the party?',
    'Isn’t he driving you home tonight?',
    'Wasn’t the cake delicious?',
    'Could you pass me the salt?',
    'You won’t tell anyone my secret, will you?',
    'They weren’t here yesterday, were they?',
    'When did she start studying Japanese?',
    'How old is your grandma?',
    'Who is the author of this book?',
    'Why did you ignore me yesterday?',
    'Are you close to Emily?',
    'When are you leaving for Hawaii?',
    'Do you miss your mother?',
    'Who cooked this meatloaf?',
    'Whose rollerblades are those?',
    'Whom would you like to be as famous as?',
    'Did you say you went to Estonia?',
    'How long have you been a vegetarian?',
    'Would you like a cup of tea?',
    'How much is this black leather wallet?',
    'When do you usually work out?',
    # 以下追加
    'You can ask me when it doesn\'t work',
    'The festival goes on whether it rains or not.',
    # 'Do what you want to do.',  # 関係代名詞what
    # 'This is what love is all about.',  # 関係代名詞what
  ],
}
test_data_2013 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **命令形
        
  'positive': [
    'Open the door for me, will you?',
    'Help me tidy up my room.',
    'Don’t put all your eggs in one basket.',
    'Have some more chicken soup.',
    'Keep off the grass.',
    'Tell me about your experience in Madrid.',
    'Study hard and you will pass the exam.',
    'Stop talking or I’ll have to ask you to leave the room.',
    'Don’t be late for the orchestra practice tomorrow.',
    'Feel free to call me whenever you like.',
    'Be quiet.',
    'Don\'t be late.',
    'Let\'s go shopping.',
  ],
  'negative': [
    'My friend wants me to help her find a new apartment.',
    'A widower is a man whose wife has died.',
    'I just met a girl whose brother I used to play soccer with.',
    'I like stories which have happy endings.',
    'The engagement ring which I want is too expensive.',
    'The guy you were talking to is my boyfriend.',
    'The woman that lives next door is an English teacher.',
    'The most straightforward emotion that we discover in the human mind is curiosity.',
    'The reason why I am calling you is to ask you a favor.',
    'My brother John, who is a chef, lives in London.',
    'Jim, who speaks French, works as a tourist guide.',
    'My sister is acting like an idiot.',
    'I was busy sweeping up the fallen leaves.',
    'I spent all morning cleaning up after the party.',
    'I want to be a policeman soon.',
    'I’m going to Egypt to do some scuba diving.',
    'He grew up to be a famous architect.',
    'I don’t have the right tools to fix your bicycle.',
    'It is difficult to get up in the morning.',
    'Having reserved seats was excellent.',
  ],
}
test_data_2014 = { 

        # **Super category:** Sentences forms 2
        # **Sub category: **感嘆文
        
  'positive': [
    'What nice clothes you have!',
    'How fast you run!',
    'How polite that clerk is!',
    'How fast you eat hamburgers!',
    'What a high building that is!',
    'How short this pencil is!',
    'What a pity!',
    'What a pity it is!',
    'What luck!'
    # TODO question判定
    # 'What an awesome concert that was!',
    # 'What a nice beach this is!',
    # 'What a difficult problem this is!',
    # 'What a nice bag you have!',
    # 'How time flies!',
  ],
  'negative': [
    'Who is the author of that book?',
    'Help me tidy up my room.',
    'Tell me about your experience in Madrid.',
    'Study hard and you will pass the exam.',
    'Don’t be late for the orchestra practice tomorrow.',
    'I just met a girl whose brother I used to play soccer with.',
    'I like stories which have happy endings.',
    'How old is your youngest sister?',
    'Do you know where my bowling shirt is?',
    'Does he know the answer to this question?',
    'When did she start studying Japanese?',
    'Why did you ignore me yesterday?',
    'Whom would you like to be as famous as?',
    'Your favorite food is a cheeseburger, isn’t it?',
    'They weren’t here yesterday, were they?',
    'My oldest sister is a professional violinist.',
    'Our neighbor is an Italian chef.',
    'Wasn’t the cake delicious?',
    'Why are you so beautiful?',
    'This is a great opportunity for you.',
  ],
}
test_data_2015 = { 

        # **Super category:** Verbs
        # **Sub category: **自動詞
        
  'positive': [
    'My brother swims fast.',
    'My baseball team didn’t play well last night.',
    # parser error?
    # looked -> wearing xcomp
    # 意味場では適当/本来は look atでcompound:prtになってほしい
    # 'I looked at the girl wearing the pink dress.',
    'Are you going to the school festival?',
    'I work for a large firm in Paris.',
    'Jamie and Kelly laughed uncontrollably.',
    'We talked for hours about politics.',
    'The trees were moving in the breeze.',
    'The match starts at 3 o’clock.',
    'When the rain stopped, we went for a walk.',
    'Our father lived till he was fifty-two.',
  ],
  'negative': [
    'Some students teased the new teacher.',
    'Ellen has beautiful eyes.',
    'I know Monet very well.',
    'My boyfriend kissed my sister!',
    'Could you move your car, please?',
    'Marriage hasn’t changed her at all.',
    'Gregory tried to stop her from leaving.',
    'Kate set a chair next to the bed.',
    'Michelle used to run a Chinese restaurant.',
    'My parents lent me the car to visit my friend.',
    'Please write your name here.',
    'Taylor was found guilty of starting the fire.',
    'Please bring coffee.',
    'The girls carry water to their village.',
    'Could you phone the neighbors?',
    'She loves rainbows.',
    # parser error
    # week -> cold (amod)
    # 'I caught a cold last week.',
    'Lily conveyed the message.',
    'Alice wrote a love poem on a restaurant poem.',
    'Antony eats mashed potatoes with gravy sauce.',
  ],
}
test_data_2016 = { 

        # **Super category:** Verbs
        # **Sub category: **他動詞
        
  'positive': [
    'Some students teased the new teacher.',
    'Ellen has beautiful eyes.',
    'My boyfriend kissed my sister!',
    'Could you move your car, please?',
    'Taylor was found guilty of starting the fire.',
    'Marriage hasn’t changed her at all.',
    'Gregory tried to stop her from leaving.',
    'Kate set a chair next to the bed.',
    'Michelle used to run a Chinese restaurant.',
    'My parents lent me the car to go to the movies.',
    'He was living a life of luxury abroad.',  # live
  ],
  'negative': [
    'Our father lived till he was fifty-two.',
    'My brother swims really fast.',
    'My baseball team didn’t play well last night.',
    'I looked at the girl wearing the pink dress.',
    'Are you going to the school festival?',
    'I work for a large firm in Paris.',
    'Jamie and Kelly laughed uncontrollably.',
    'We talked for hours about politics.',
    'The trees were moving in the breeze.',
    'The match starts at 3 o’clock.',
    'When the rain stopped, we went for a walk.',
    'Joe’s doing well in his new job.',
    'The sun was setting and a red glow filled the sky.',
    'Kevin couldn’t read or write.',
    'The area has changed greatly in the last decade.',
    'The historical museum opens at 10 o’clock.',
    'The light was shining.',
    # 意味不明
    # 'In the evenings, Lucy sits o the front porch to admire her lawn.',
    'To escape the midday sun, the cats lie in the shade under our cars.',
    'James went to the cafe to grab some coffee.',
  ],
}
test_data_2017 = { 

        # **Super category:** Verbs
        # **Sub category: **意味が近いにもかかわらず、自動詞と他動詞で形が異なる動詞
        
  'positive': [
    'The sun rises in the east.',
    'Raise your hand if you have any questions.',
    'Your cat is sitting on the sofa.',
    'Please seat yourself.',
    'My mother always lies on the bed.',
    'He always lays himself on the bed on weekends.',
    'You may sit in the hallway when you do not read.',
    'Tom set the football down in the end zone after the touchdown.',
    'Yesterday I lay on the grass.',
    'I laid your hammer on the workbench.',
  ],
  'negative': [
    'The door opened.',
    'The car stopped.',
    'I opened the door.',
    'I stopped the car.',
    'He stood on the box.',
    'He stood the box.',
    'My watch broke.',
    'He broke my watch.',
    'The typhoon is approaching.',
    'The typhoon is approaching the Tokai Area.',
    'That man smiled.',
    'He looked at me strangely.',
    'My mother caught a big fish.',
    'Do you agree with me?',
    'He apologized to the professor for his lack of punctuality.',
    'She is kind.',
    'He used his entire fortune.',
    'I tell him the news.',
    'My sister held her to be guilty.',
    'I arrive at Tokyo station.',
  ],
}
test_data_2018 = { 

        # **Super category:** Verbs
        # **Sub category: **一つの動詞で自動詞と他動詞で意味が異なる動詞
        
  'positive': [
    'My little sister runs every morning.',
    'My little brother runs an Italian restaurant.',
    'Her house stands on the hill.',
    'I cannot stand him anymore.',
    'The boy attended to what his client was saying.',
    'The counselor attended the meeting.',
    'This document can read in different ways.',
    'I read this book yesterday.',
    'This car should sell at a high price.',
    'I sold this car three days ago.',
    'This box will do for a seat.',
    'I have to do my math tonight.',
  ],
  'negative': [
    'I arrived at the Starbucks.',
    'He swims so fast.',
    'I bought a new laptop.',
    'I made this bento box for my sister.',
    'The train reached the station.',
    'I entered the office.',
    'We will discuss the news.',
    'I agreed with him.',
    'She complained about the service.',
    'He graduated from Tokyo University.',
    'She seems to be happy.',
    'Will you marry me?',
    'She gave me a gift.',
    'She made him angry.',
    'Look at the boy.',
    'I can cut this cake.',
    'I will use this table.',
    'I sent you a letter.',
    'I opened the door.',
    'She doesn’t smoke.',
  ],
}
test_data_2019 = { 

        # **Super category:** Verbs
        # **Sub category: **自動詞と他動詞が紛らわしい単語
        
  'positive': [
    'I will answer you tomorrow.',
    'A policeman addressed the man suddenly.',
    'We approach that mountain.',
    'You can reach my house by walk.',
    'She attended my part.',
    'The counselor attended the meeting.',
    'We entered the room.',
    'I must consider how to get to the station.',
    'We discussed that problem.',
    'My brother entered medical school.',
    'Where did she leave?',
    'My sister marries my friend.',
    'My teacher mentioned the score of the exam.',
    'My friends somehow obey me.',
    'I oppose your new idea.',
    'You resemble my friend.',
    'I have never visited her at home.',
    'You must apologize to him for the delay.',
    'I agreed with him.',
    'This textbook belongs to me.',
    'She complained to me that the exam was too difficult for her.',
    'She complained about the service.',
    'I hope for him to come.',
    'There is no reason why I should listen to you.',
    'What college did you graduate from?',
    'He graduated from Tokyo University.',
    'His parents objected to his going abroad.',
    'He apologized to the professor for his lack of punctuality.',
  ],
  'negative': [
    'I arrived at the Starbucks.',
    'I made this bento box for my sister.',
    'She gave me a gift.',
    'She made him angry.',
    'Look at the boy.',
    'My little brother runs an Italian restaurant.',
    'I cannot stand him anymore.',
    'I read this book yesterday.',
    'I sold this car three days ago.',
    'She is kind.',
    'He used his entire fortune.',
    'I tell him the news.',
    'My sister held her to be guilty.',
    'I arrive at Tokyo station.',
    'He looked at me strangely.',
    'I adjusted the seat to my height.',
    'The analysis of the substance confirmed the presence of nitrogen.',
    'He lacks willpower.',
    'I mixed a little sugar into the flour.',
    'I was passing, so I dropped in.',
  ],
}
test_data_2020 = { 

        # **Super category:** Tenses (Past, Present)
        # **Sub category: **現在形
        
  'positive': [
    'My father works for a trading company.',
    'I live near the park entrance.',
    'I practice yoga every day.',
    'I always sleep on airplanes and buses.',
    'She always eats quickly.',
    'You are still a baby.',
    'I promise I won\'t let you down.',
    'I get up at seven every morning.',
    'My dream is to relax in a Japanese bath.',
    'We have a family reunion every year.',
    'I am always proud of him.',
  ],
  'negative': [
    'I\'m going to join the party tonight.',
    'He is running in the park.',
    'I came here yesterday, too.',
    'I enjoyed meals and snacks.',
    'My grandfather built it about 50 years ago.',
    'We were here many years ago.',
    'My sister e-mailed me today.',
    'I hoped you could do me a favor.',
    'He has visited Sydney once before.',
    'He has been awarded prizes more than ten times.',
    'I have been busy since this morning.',
    'My grandfather has been dead for two years.',
    'I have never lost my wallet.',
    'They’ve been married for five years.',
    'I haven’t smoked for over two years.',
    'We\'ll have to wait and see.',
    'I will be there this Thursday evening.',
    'You will be surprised.',
    'Soon we\'ll be second-year students.',
    'I\'ll give you a form.',
    'I won\'t give you a birthday present from now on.',
    'I\'ll get on it right away.',
  ],
}
test_data_2021 = { 

        # **Super category:** Tenses (Past, Present)
        # **Sub category: **過去形
        
  'positive': [
    'Some students teased the new teacher.',
    'Gregory tried to stop her from leaving.',
    'Kate set a chair next to the bed.',
    'Michelle used to run a Chinese restaurant.',
    'Our father lived till he was fifty-two.',
    'My baseball team didn’t play well last night.',
    'We talked for hours about Korean politics.',
    'We invited them to our party, but they decided not to come.',
    'James went to the cafe to grab some coffee.',
    'Laura passed her exam because she studied very hard.',
  ],
  'negative': [
    'He was carrying a sleeping bag.',
    'They had been at church.',
    'My brother swims really fast.',
    'I work for a large firm in Paris.',
    'The match starts at 3 o’clock.',
    'Joe’s doing well in his new job.',
    'The historical museum opens at 10 o’clock.',
    'Katie will make a speech at the graduation ceremony tomorrow.',
    'Jane is going to be a psychiatrist in the future.',
    'It is common knowledge that Lucy is good at writing songs.',
    'I will make an appointment at the hair salon this afternoon.',
    'I promise you that we will go to Disney Land together.',
    'I am proud of the fact that my mother works for the president.',
    'I love taking my dog out for a walk.',
    'Jessie should be at the station by now.',
    'I will watch a movie with my cousin tonight.',
    'They will definitely win the debate tournament.',
    'My sister is going to buy a new clock for me.',
    'Because of the earthquake, my family has to move to a new house.',
    'Both Jake and Rosie can speak French.',
    'I am going to the library to do some research on a case from a few years ago.',
    'I will make some pasta if you are hungry.',
  ],
}
test_data_2022 = { 

        # **Super category:** Tenses (Past, Present)
        # **Sub category: **freq advs 普通の位置
        
  'positive': [
    'I work at home twice a week.',
    'The theory is generally accepted.',
    'I sometimes sing in the shower.',
    'I often read in bed at night.',
    'I have frequently read that novel.',
    'I seldom put salt on my food.',
    'Vegetarians never eat meat.',
    'I normally get good marks.',
    'He ordinarily gets up at seven.',
    'I usually walk to work.',
    'I occasionally go to bed late.',
    'I hardly ever get angry.',
    'The medicine has to be taken every six hours.',
    'I always study after class.',
    'My father took me to watch the football every Saturday.',
    'The Oscar ceremony takes place in March every year.',
    'He\'s phoned me up every day.',
    'They go swimming four times a week.',
    'She takes the medicine three times a day.',
    'They usually take a bath twice a day.',
    'I brush my teeth twice a day.',
    'We eat three times a day.',
    'The contract is for the regular delivery of 1,000 high performance rubber tires every month.',
  ],
  'negative': [
    'Fortunately, Ben evidently passed the exam.',
    'Quietly, Harry tried to say something in the special tongue.',
    'John clumsily spilled the beans.',
    'I have every confidence in him.',
    'I loved her dearly.',
    'A sharp knife cuts cleanly.',
    'Fortunately for me, I did not lose my head.',
    'Personally, John obviously left early.',
    'He angrily walked out of the room.',
    'I clean forgot about it.',
    'The paper comes out daily.',
    'He went away yesterday.',
    'He was dead drunk.',
    'He tried harder to get good marks than I.',
    'The next flight goes direct to Rome.',
    'Max deliberately was shouting loudly.',
    'Probably she will not be there.',
    'The door was wide open.',
    'Frankly, you are mistaken.',
    'Word your ideas clearly.',
  ],
}
test_data_2023 = { 

        # **Super category:** Tenses (Progressive)
        # **Sub category: **現在進行形
        
  'positive': [
    'The flower shop is opening in ten minutes.',
    'He is waiting on the other side of the station.',
    'We are practicing English for our trip to England.',
    'The water is not boiling yet.',
    'Believe me when I say I am telling the truth.',
    'She is wearing a golden necklace.',
    'Maria is playing the main role in the play.',
    'I can sense something fishy is going on.',
    'It seems like you’re managing this work very well.',
    'I’m having the time of my life on this cruise.',
  ],
  'negative': [
    'Katie will make a speech at the graduation ceremony tomorrow.',
    'Jane is going to be a psychiatrist in the future.',
    'I will watch a movie with my cousin tonight.',
    'They will definitely win the debate tournament.',
    'Gregory tried to stop her from leaving school.',
    'I will make some pasta if you are hungry.',
    'We invited them to our party, but they decided not to come.',
    'James went to the cafe to grab some coffee.',
    'Laura passed her exam because she studied very hard.',
    'Michelle used to run a Chinese restaurant.',
    'He was carrying a sleeping bag.',
    'When you were in the park, we were practicing soccer.',
    'She was studying when I left home this morning.',
    'I was just telling Julia about our exciting trip to Fiji.',
    'She was dating another man when I met her.',
    'I was having dinner when you called me last night.',
    'He was painting a picture of a ship.',
    'Mike was in the kitchen when I got home last night.',
    'You weren’t reading a book then.',
    'I was watching television at 7 o’clock yesterday.',
  ],
}
test_data_2024 = { 

        # **Super category:** Tenses (Progressive)
        # **Sub category: **過去進行形
        
  'positive': [
    'He was carrying a sleeping bag.',
    'When you were in the park, we were practicing soccer.',
    'She was studying when I left home this morning.',
    'I was just telling Julia about our exciting trip to Fiji.',
    'She was dating another man when I met her.',
    'I was having dinner when you called me last night.',
    'He was painting a picture of a ship.',
    'Mike was cooking in the kitchen when I got home last night.',
    'You weren’t reading a book then.',
    'I was watching television at 7 o’clock yesterday.',
  ],
  'negative': [
    'The flower shop is opening in ten minutes.',
    'He is waiting on the other side of the station.',
    'We are practicing English for our trip to England.',
    'The water is not boiling yet.',
    'Believe me when I say I am telling the truth.',
    'She is wearing a golden necklace.',
    'Maria is playing the main role in the play.',
    'I can sense something fishy is going on.',
    'It seems like you’re managing this work very well.',
    'I’m having the time of my life on this cruise.',
    'I’m taking the morning yoga class for a while.',
    'I’m working on the new project with Rosa.',
    'I’m trying to find a new girlfriend right now.',
    'We’re going to Spain next month.',
    'Unfortunately, I’m working all day tomorrow.',
    'My mom will pick me up from school next week.',
    'I should get a haircut very soon.',
    'I feel like something bad is going to happen.',
    'You will be surprised to hear this.',
    'I decided to join a band this year.',
  ],
}
test_data_2025 = { 

        # **Super category:** Tenses (Future)
        # **Sub category: **未来形
        
  'positive': [
    'We’re going to Spain next month.',
    'My mom will pick me up from school next week.',
    'I feel like something bad is going to happen.',
    'You will be surprised to hear this.',
    'I’m going to work on a new project with Rosa.',
    'My mother is going to come to Japan next year.',
    'I’m going to have a phone interview tomorrow morning.',
    'Amy will attend a dance class tonight.',
    'They will carry all the luggage for us.',
    'We shall be traveling all night.',
  ],
  'negative': [
    'I saw him carrying a fruit basket at the hospital.',
    'When you were in the park, we were practicing soccer.',
    'She was studying when I left home this morning.',
    'I was just telling Julia about our exciting trip to Fiji.',
    'Mike was in the kitchen when I got home last night.',
    'You weren’t reading a book then.',
    'I was watching television at 7 o’clock yesterday.',
    'She is wearing a golden necklace.',
    'Maria is playing the main role in the play.',
    'Claudia forgot to feed her dog this morning.',
    'My baseball team didn’t play well last night.',
    'We talked for hours about Korean politics.',
    'Kate set a chair next to the bed.',
    'Michelle used to run a Chinese restaurant.',
    'Gina gave me a first-edition book for my birthday.',
    'My mother used to dream of being a flight attendant.',
    'I spent all of my money on cosmetics.',
    'I can’t understand what you are saying.',
    'Our neighbor is an Italian chef.',
    'The pretty maid served us breakfast in bed.',
    'Hurry up, the bus is about to leave!',
    'I\'m just on the point of leaving.',
  ],
}
test_data_2026 = {

        # **Super category:** Tenses (Future)
        # **Sub category: **未来進行形
        
  'positive': [
    'She will be studying English.',
    'You will be waiting for him when his plane arrives.',
    'He will be reading books this time tomorrow.',
    'This time next week, I will be sunbathing in Bali.',
    'It will be raining when you get to Tokyo.',
    'How many people will be staying at the hotel tomorrow?',
    'Will it be snowing tonight?',
    'He will be waiting by 3 o’clock.',
    # parser error: copula文判定
    # 'He will be playing tennis at 3 o’clock.',
    'Jake will not be attending the conference.',
    'Ken will be driving a car this evening.',
  ],
  'negative': [
    'Hurry up, the bus is about to leave!',
    'My mother is going to come to Japan next year.',
    'I’m going to have a phone interview tomorrow morning.',
    'Amy will attend a dance class tonight.',
    'They will carry all the luggage for us.',
    'My basketball team lost the game last night.',
    'Gina gave me a first-edition book for my birthday.',
    'I can’t understand what you are saying.',
    'Our neighbor is an Italian chef.',
    'The pretty maid served us breakfast in bed.',
    'We’re going to visit Thailand this summer.',
    'He will clean his room once he gets back from vacation.',
    'I haven’t done a jigsaw puzzle since I was a child.',
    'We have been good friends for about forty years.',
    'We haven’t bought our tickets for the show yet.',
    'I have never visited a museum in London.',
    'I have wanted to talk to Anna for a very long time.',
    'He has been in the garage all day.',
    'I haven\'t been getting enough sleep lately.',
    'I have invited Regina’s family to dinner.',
  ],
}
test_data_2027 = { 

        # **Super category:** Tenses (Perfect)
        # **Sub category: **現在完了進行形
        
  'positive': [
    'I have been living in New York for five years.',
    'I have been reading this book.',
    'I\'ve been waiting to speak with you.',
    'She has been overdoing things recently.',
    # parser error: 受動態と誤認識
    # 'He\'s been acting distant lately.',
    'He has been acting distant lately.',
    'The building work next door has been going on all year long.',
    'He has been waiting to see you since morning.',
    'I\'ve been studying English for about ten years.',
    # parser error: 受動態と誤認識
    # 'It\'s been raining since last Friday.',
    'It has been raining since last Friday.',
    # parser error: growingが分詞判定
    # 'We\'ve been growing olives here for about one hundred years.',
  ],
  'negative': [
    'I lost the watch which my uncle had given me.',
    'She had been a swimmer before she had a baby.',
    'I will have finished my homework by 10 a.m. tomorrow.',
    'He went out after he had brushed his teeth.',
    'It came out that she had been embezzling money from her company.',
    'My grandfather has been dead for two years.',
    'They had been planning their escape for months.',
    'After he had turned off the TV, Roy set to work.',
    'She did not speak to me until I had finished my coffee.',
    'The fishing boat had been drifting for five days when it was found.',
    'The man had run away when the police arrived.',
    'I found the eraser I had lost the day before yesterday.',
    'I lost my eraser I had bought the day before.',
    'By that time I had finished my work.',
    'I have been busy since this morning.',
    'Mr. Tanaka had been looking for this file before I arrived.',
    'He has been awarded prizes more than ten times.',
    'She had been to Paris before she was fifteen.',
    'The plane had already taken off before they got to the airport.',
    'My brother had been living only on water when the search party found him.',
  ],
}
test_data_2028 = { 

        # **Super category:** Tenses (Perfect)
        # **Sub category: **過去完了形
        
  'positive': [
    'I felt good because I had finished my homework.',
    'She had been a swimmer before she had a baby.',
    'He went out after he had brushed his teeth.',
    'The writer had finished writing the book before he left Japan.',
    'The train had already left before he got to the station.',
    'She had had several proposals of marriage before she was twenty.',
    'We had already finished dinner when our father came home.',
    'I had never talked with her before that time.',
    'I went back to the store, but someone had already bought that camera.',
    'She had been to Paris before she was fifteen.',
  ],
  'negative': [
    'My brother had been living only on water when the search party found him.',
    'I will have finished my homework by 10 a.m. tomorrow.',
    'It came out that she had been embezzling money from her company.',
    'I have never lost my wallet.',
    'My grandfather has been dead for two years.',
    'She has been overdoing things recently.',
    'The fishing boat had been drifting for five days when it was found.',
    'The building work next door has been going on all year long.',
    'They’ve been married for five years.',
    'I will have finished my homework by the time he comes.',
    'You have been living in New York for five years.',
    'In a week, she will have practiced the violin for three years.',
    'A Mr. Abe has been waiting to see you since morning.',
    'It’s been raining since last Friday.',
    'I have been reading Tolstoy’s War and Peace.',
    'I have been busy since this morning.',
    'Mr. Tanaka had been looking for this file before I arrived.',
    'He has been awarded prizes more than ten times.',
    'They had been planning their escape for months.',
    'I haven’t smoked for over two years.',
  ],
}
test_data_2029 = { 

        # **Super category:** Tenses (Perfect)
        # **Sub category: **過去完了進行形
        
  'positive': [
    'It came out that she had been embezzling money from her company.',
    # parser error
    # copula判定
    # 'He had been playing tennis before I arrived at the park.',
    'The fishing boat had been drifting for five days when it was found.',
    'I had been sleeping for more than ten hours when my mother woke me up.',
    'She had been walking for three hours when I called her.',
    'He had been sleeping when I called him.',
    'He had been working at the company before he left Japan.',
    'He had been looking for this file before I arrived.',
    'They had been planning their escape for months.',
    'My brother had been living only on water when the search party found him.',
  ],
  'negative': [
    'I felt good because I had finished my homework.',
    'He is waiting on the other side of the station.',
    'I\'m going to have breakfast.',
    'He went out after he had brushed his teeth.',
    'My grandfather has been dead for two years.',
    'My brother is coming.',
    'She has been overdoing things recently.',
    'We\'re reading our horoscopes for next month.',
    'The building work next door has been going on all year long.',
    'The water is not boiling yet.',
    'The writer had finished writing the book before he left Japan.',
    'You have been living in New York for five years.',
    'We had already finished dinner when our father came home.',
    'We are having a competition in October.',
    'I have been reading Tolstoy’s War and Peace.',
    'I\'m telling the truth.',
    'We are practicing English for our trips to America and Brazil.',
    'They’ve been married for five years.',
    'I went back to the store, but someone had already bought that camera.',
    'They are meeting right now.',
  ],
}
test_data_2030 = { 

        # **Super category:** Tenses (Perfect)
        # **Sub category: **未来完了形
        
  'positive': [
    'I will have been to Hawaii three times if I go there again.',
    'In a week, she will have practiced the violin for five years.',
    'I will have finished my homework by 10 a.m. tomorrow.',
    'I won’t have finished my work when my friend comes.',
    'When you wake up, these fancies will have gone.',
    'He will have left his home when his parents come home.',
    'People will have forgotten all about it in a month.',
    'I won’t have read the book by next Sunday.',
    'The lake will have frozen by tomorrow.',
  ],
  'negative': [
    # 使役
    'I will have it done by the time you come back.',
    'Leslie has to go to the bank this afternoon.',
    'Tom will have been studying English for three years next month.',
    'I have invited Regina’s family to dinner.',
    'Jack will eat a banana tomorrow.',
    'Jackson could be seriously injured.',
    'I won’t dance with your father.',
    'We have been good friends for about forty years.',
    'I will have been seeing him for five years by fall next year.',
    'I haven\'t been getting enough sleep lately.',
    'I have wanted to try this chocolate for a while.',
    'He has liked Katie since he was in the seventh grade.',
    'He has been in the garage all day.',
    'He will have been studying for two hours until I call him.',
    'We haven’t bought our tickets for the show yet.',
    'I haven’t done a jigsaw puzzle since I was a child.',
    'He will have been reading the book until this evening.',
    'I have never visited a museum in London.',
    'They will have been playing in the park until it gets dark.',
    'I have wanted to talk to Anna for a very long time.',
    'She has a sister who goes to preschool.',
  ],
}
test_data_2031 = { 

        # **Super category:** Tenses (Perfect)
        # **Sub category: **未来完了進行形
        
  'positive': [
    'Tom will have been studying English for three years next month.',
    'Claudia will have been talking with her friend until her mom tells her to stop.',
    # parser error: 'aux'
    # been -> tennis/ expected been -> playing
    # 'You will have been playing tennis for twenty years by the time you graduate from college.',
    'Joseph will have been playing the piano for two hours until his mother comes home.',
    'I will have been seeing him for five years by fall next year.',
    'Jonathan will have been sleeping by the time I call him.',
    'Larry will have been playing baseball until his mother picks him up.',
    'He will have been reading the book until this evening.',
    'He will have been studying for two hours until I call him.',
    'They will have been playing in the park until it gets dark.',
  ],
  'negative': [
    'I will have been to Hawaii three times if I go there again.',
    'In a week, she will have practiced the violin for five years.',
    'I won’t have finished my work when my friend comes.',
    'I will have it done by the time you come back.',
    'Before she was a high school student, she had been playing the piano for ten years.',
    'My father has finished his beer.',
    'When you wake up, these fancies will have gone.',
    'He will have left his home when his parents come home.',
    'People will have forgotten all about it in a month.',
    'We have been good friends for about forty years.',
    'My father had been repairing the car when I arrived home.',
    'I won’t have read the book by next Sunday.',
    'She has been reading a book about parenting for four hours.',
    'When I arrived at the airport, the plane had taken off.',
    'He has liked Katie since he was in the seventh grade.',
    'She had smoked before she was twenty years old.',
    'I have never visited a museum in London.',
    'I have wanted to talk to Anna for a very long time.',
    'The lake will have frozen by tomorrow.',
    'She has been overdoing work recently.',
  ],
}
test_data_2032 = { 

        # **Super category:** Modal verbs 1
        # **Sub category: **can
        
  'positive': [
    'She can speak four languages.',
    'Can you read that sign from this distance?',
    'Can I help you with those bags?',
    'Do the best you can.',
    'How can I have done that?',
    'I doubt whether I can finish the work on time.',
    'She can\'t be working at this hour!',
    'I doubt whether I can finish the work on time.',
    'And in that case, I can go back by railway.',
    'Everything is so out-of-the-way down here that I should think very likely it can talk.',
  ],
  'negative': [
    'The vending machine has soda in cans.',
    'I was wearing cans so I didn\'t hear anything.',
    'I\'m looking for a good pair of closed cans.',
    'I wish you could see her after birds.',
    'I could go further in that time.',
    'You have a can-do character or way of dealing with a problem.',
    'Her can-do attitude is what made her our choice for the job.',
    # 'Nobody has yet been willing to open up that can of worms.',
    # 'Many tin cans would be waiting to be opened with refractory can openers.',
    'He spent ten years in the can for armed robbery.',
    'You\'ll need a can of tuna for this recipe.',
    'How many candidates are there for the job?',
    'We walked along the canal for a couple of miles.',
    'They died in a canoeing accident.',
    'Another three days of editing, and we\'ll have the movie in the can.',
    'There may be other problems that we don\'t know about.',
    'You mustn\'t carry your jokes too far!',
    'He said he would see his brother tomorrow.',
    'If you\'re annoyed with him, you should tell him.',
    'Will she be able to cope with the work?',
  ],
}
test_data_2033 = { 

        # **Super category:** Modal verbs 1
        # **Sub category: **could
        
  'positive': [
    'When I was younger, I couldn\'t get up early.',
    'Excuse me, could I say something?',
    'Could you turn that music down a little, please?',
    'It is not inconceivable that she could be lying.',
    'You could always call Susie and see if she will babysit.',
    'This place could do with a good cleaning.',
    'I could murder a cup of tea!',
    'The master could\'ve been drinking in that bar when the armed robber broke into.',
    'I can\'t imagine this large ship Titanic could\'ve sunk.',
    'Amy says it\'s the government\'s fault, and I couldn\'t agree more.',
  ],
  'negative': [
    'If the party is awful, we can always leave.',
    'He can be really annoying at times.',
    'The doctors are doing all that they can, but she\'s still not breathing properly.',
    'You can just go to bed!',
    'As it is, I can\'t get out at the door.',
    'I doubt whether I can finish the work on time.',
    'She can\'t be working at this hour!',
    'I doubt whether I can finish the work on time.',
    'And in that case, I can go back by railway.',
    'Everything is so out-of-the-way down here that I should think very likely it can talk.',
    'There may be other problems that we don\'t know about.',
    'You mustn\'t carry your jokes too far!',
    'He said he would see his brother tomorrow.',
    'If you\'re annoyed with him, you should tell him.',
    'Will she be able to cope with the work?',
    'There needs to be more effort from everyone.',
    'I brought him some sandwiches because I thought he might be hungry.',
    'You should find this guidebook helpful.',
    'He oughtn\'t to do that.',
    'I\'d better leave a note so they\'ll know I\'ll be late.',
  ],
}
test_data_2034 = { 

        # **Super category:** Modal verbs 1
        # **Sub category: **be able to
        
  'positive': [
    'I am able to speak five languages.',
    'I\'ve never been able to do crosswords.',
    'I will be able to attend the meeting tomorrow.',
    'Applicants must be able to speak fluent French.',
    'Will she be able to cope with the work?',
    'I\'m sorry that I wasn\'t able to phone you yesterday.',
    'Get a good night\'s sleep and you\'ll feel better able to cope.',
    'You don\'t need to be able to read music to learn guitar.',
    'I haven\'t been able to access Facebook since last night.',
    'I was able to get some sleep on the plane.',
  ],
  'negative': [
    'I\'m sure I shan\'t be able!',
    'He is an able student.',
    'This problem is now being looked at by some of the ablest minds in the country.',
    'He is more than able in management.',
    'He is an able seaman.',
    'Every able-bodied young man served in the army.',
    'I was unable to attend the meeting.',
    'Art is not something that is come-at-able by dint of study.',
    'Critical thinking is able to many things.',
    'Ables are supposed to supervise others.',
    'She\'s a very capable judge.',
    'I think both sexes are equally capable of looking after children.',
    'If she were constitutionally capable of slumping, she would.',
    'Rebecca was, without question, the most capable technician on the team.',
    'They\'ve got a very capable lawyer working on the case.',
    'These are nuclear-capable aircraft.',
    'She\'s very knowledgeable about music.',
    'In Python, we say that a value is iterable when your program can iterate over it.',
    'The system is new, but so far it seems to be reliable.',
    'Her articles are always readable and informative.',
  ],
}
test_data_2035 = { 

        # **Super category:** Modal verbs 1
        # **Sub category: **may
        
  'positive': [
    'I may see you tomorrow before I leave.',
    'There may be some evidence to suggest she\'s guilty, but it\'s hardly conclusive.',
    'I worry about the destructive effect that violent films may have on children.',
    'How may I help you?',
    'Could you tell me where I may seat?',
    'She may well not want to travel alone.',
    'May you have a long and fruitful marriage.',
    'He may be waiting for us.',
    'Building a new children\'s home will cost much money but, be that as it may, there is an urgent need for the facility.',
    'What, may I ask, was the point of repeating the tests?',
  ],
  'negative': [
    'She was crowned queen of the May.',
    'My mother\'s birthday is in May.',
    'Komaba has many people on May Festival.',
    'Therefore, May in the Southern Hemisphere is the seasonal equivalent of November in the Northern Hemisphere and vice versa.',
    'The zodiac signs for the month of May are Taurus and Gemini.',
    'Maybe they\'ll come tomorrow.',
    'There were 200, maybe 300, refugees on the boat.',
    'I thought maybe my phone message had scared him off.',
    'Visual analogies are maybe the most common nonsounding analogies.',
    'There are no ifs, buts or maybes.',
    'In an area of Mexico, we can find showy orchid named Mayflower.',
    'The Mayflower passengers not being accustomed to winter weather much colder than back home.',
    'There are frequently over a dozen options, and most are mayonnaise-based.',
    'They were flattered to be invited to dinner by the mayor.',
    'She is my girlfriend, Mayuri.',
    'There needs to be more effort from everyone.',
    'I brought him some sandwiches because I thought he might be hungry.',
    'You should find this guidebook helpful.',
    'He oughtn\'t to do that.',
    'I\'d better leave a note so they\'ll know I\'ll be late.',
  ],
}
test_data_2036 = { 

        # **Super category:** Modal verbs 1
        # **Sub category: **might
        
  'positive': [
    'She might\'ve taken it with her to read on the plane.',
    'She is as well as might be expected.',
    'Might I ask a question?',
    'I wonder if I might have a quick look at your newspaper?',
    'I thought you might like to consider a holiday.',
    'You might at least try to look like you\'re enjoying yourself!',
    'For the little extra it\'ll cost, we might just as well stay for another night.',
    'I might have known he\'d still be in bed at noon.',
    'To my mind, there are two factors which might have a very negative effect in the short and medium term.',
    'Alice\'s first idea was that it might belong to one of the doors of the hall.',
    'I brought him some sandwiches because I thought he might be hungry.',
  ],
  'negative': [
    'Pizarro defeated the might of the Inca Empire with only a few hundred men.',
    'She struggled with all her might to get free.',
    # 'They shouted with might and main but nobody came to rescue them.',
    # 'Might is right.',
    'He\'s always behind the might of the nation.',
    'He flexed his mighty muscles.',
    'An arm is said to be mighty if all its segments are strong.',
    'All their costs have risen mightily.',
    'They struggled mightily at first.',
    'There\'s no point now in regretting the might-have-beens.',
    'There should be other problems that we don\'t know about.',
    'You mustn\'t carry your jokes too far!',
    'He said he would see his brother tomorrow.',
    'If you\'re annoyed with him, you should tell him.',
    'Will she be able to cope with the work?',
    'There needs to be more effort from everyone.',
    'You should find this guidebook helpful.',
    'He oughtn\'t to do that.',
    'I\'d better leave a note so they\'ll know I\'ll be late.',
  ],
}
test_data_2037 = { 

        # **Super category:** Modal verbs 1
        # **Sub category: **may/mightの慣用表現
        
  'positive': [
    'Otherwise, he might well have lost his life.',
    'For all the use we are to her, we might well go back to the ship.',
    'If the Americans had had less influence on affairs, the war might well have been avoided.',
    'You might well be able to come up with more ideas of your own.',
    'What he said may well be true.',
    'One might as well be hanged for a sheep as a lamb.',
    'You might as well expect parched beans to flower.',
    'For all the good it has done, I might just as well not have bought this medicine.',
    # parser's problem
    'Come on now, you may as well tell us.',
    'You may as well chew your food well.',
  ],
  'negative': [
    'May this letter find you well and happy!',
    'I may not have understood your email well.',
    'I think he may not be feeling well.',
    'It might turn out well.',
    'The work isn\'t progressing as well as it might.',
    'She is as well as might be expected.',
    'The garden may be English style as well.',
    'Now we may be well assured that the case was not thus, but far otherwise, with the early Christians.',
    'We may stand aloof from a person as well as from a thing that displeases us.',
    'I might go back home as well.',
    'The documentary may present both sides of the problem very well.',
    'I may not do it as well as Marie can.',
    'It\'s not all my fault, Simon may be there as well.',
    'The museum has many works by Picasso as well as other modern painters.',
    'I thought he might be hungry.',
    'There needs to be more effort from everyone.',
    'I brought him some sandwiches because I thought he might be hungry.',
    'You should find this guidebook helpful.',
    'He oughtn\'t to do that.',
    'I\'d better leave a note so they\'ll know I\'ll be late.',
  ],
}
test_data_2038 = { 

        # **Super category:** Modal verbs 2
        # **Sub category: **must
        
  'positive': [
    'You must\'ve had a tough time.',
    'I mustn\'t bite my nails.',
    'When you got lost in the forest, you must have been very frightened.',
    'There must be a phone directory in the office somewhere.',
    'Try to imagine what life must have been like for Neolithic man 10,000 years ago.',
    'You must be joking if you think I\'m going to stand in the rain watching you play tennis!',
    'I must say, I don\'t think much of her dress.',
    'It\'s been a fantastic couple of weeks but all good things must come to an end.',
    'Why must it always rain when we want to have a picnic?',
  ],
  'negative': [
    'If you live in the country, a car is a must.',
    'A raincoat is a must in the rainy season.',
    'This is a must book for all students here.',
    'It\'s a moderately entertaining film but it\'s certainly not a must-see.',
    'The cashmere scarf is this season\'s must-have.',
    'When I come here, I remember the room smelt like a must.',
    'Making must is the first step in winemaking.',
    'A portion of selected unfermented must may be kept to be added as a sweetening component.',
    'The flowers have a musty scent.',
    'The room is full of mustiness.',
    'He\'s a slender man with a trim mustache.',
    'They can do without tins of mustard or pickles.',
    'The seeds can also be pressed to make mustard oil.',
    'The mustard agent was first used effectively in World War I by the German army.',
    'Some breeders of domestic horses consider the mustang herds of the west to be inbred and of inferior quality.',
    'There needs to be more effort from everyone.',
    'I brought him some sandwiches because I thought he might be hungry.',
    'You should find this guidebook helpful.',
    'He needn\'t do that.',
    'I\'d better leave a note so they\'ll know I\'ll be late.',
  ],
}
test_data_2039 = { 

        # **Super category:** Modal verbs 2
        # **Sub category: **have to
        
  'positive': [
    'I have to go to San Francisco tomorrow on business.',
    'What time do you have to be there?',
    'Do we have to finish this today?',
    'We\'ll have to start keeping detailed records.',
    'Jackie\'s ill so they\'ve had to change their plans.',
    'Now that you\'ve played enough, you have to do your homework.',
    'You\'ll have to pay for this.',
    'I shall have to go and live in that poky little house.',
    # parser's problem: have->whisper, advcl:to; pos of 'to' is 'IN'
    # 'You\'d only have to whisper a hint to Time, and round goes the clock in a twinkling.',
    # parser error
    # has -> give aux
    # 修正は可能だと思うが他に例があるかを見る必要がある。
    # 'My sister has diabetes and has to give herself insulin injections.',
  ],
  'negative': [
    'Many miners have suffered from the effects of coal dust in their lungs.',
    'At least he had the good sense to turn the gas off.',
    'We had a dance and afterward, we sat outside and talked.',
    'May I show you to your table, sir, or would you prefer to have a drink at the bar first?',
    'My father wouldn\'t have any animals in the house.',
    'It is important to have a lot of information in mind.',
    'Since I had nothing to lose, I accepted the offer.',
    'He had his back to me.',
    'What would you have me do?',
    'I won\'t have her talk to me like that.',
    'He\'s a good player, but he has got nothing on his brother.',
    'By the time we get there, Jim will have left.',
    'I don\'t know what her job is but she certainly seems to have money to burn.',
    'He felt he had truly arrived when he got his first part in a Broadway play.',
    'He didn\'t have a lot to say for himself.',
    'Sorry to have interrupted you.',
    'The garden was a haven from the noise and bustle of the city.',
    'He sailed the boat straight to the nearest pirate haven to recruit a real crew.',
    'The government\'s change of policy is intended to reduce the gap between the haves and have-nots in our society.',
    'The company is switching its operations to the offshore tax haven of the Dutch Antilles.',
  ],
}
test_data_2040 = { 

        # **Super category:** Modal verbs 2
        # **Sub category: **needn't
        
  'positive': [
    'You needn\'t do the washing up.',
    'We needn\'t take coats with us.',
    'Tom needn\'t come if he doesn\'t want to.',
    'Diabetes needn\'t mean you can\'t enjoy your food.',
    'We needn\'t tidy up until tomorrow.',
    'You needn\'t do it.',
    'You needn\'t have washed all those dishes.',
    'He needn\'t think I\'m driving him all the way there!',
    'It\'s a wonderful way of getting to see Italy, and it needn\'t cost very much.',
    'I know I needn\'t to but I thought it would be kind.',
    'We needn\'t have sold the car.',
    'Freedom needn\'t mean independence.',
  ],
  'negative': [
    'He doesn\'t need some climbing boots.',
    'You don\'t need 250 g of grated cheese for this recipe.',
    'We don\'t need a coat hook on the back of this door.',
    'All she needed to complete her happiness was a baby.',
    'I called her on the pretext of needing more information.',
    'He doesn\'t need to lose some weight.',
    'I don\'t need to do some shopping on my way home from work.',
    'There doesn\'t need to be any effort from anyone.',
    'Nothing need be done about this till next week.',
    'Need we take your mother?',
    'There\'s a crying need for a better education system.',
    'The findings of this survey are demonstrative of the need for further research.',
    'There is a tremendous need for more low-cost housing.',
    'Will future oil supplies be adequate to meet world needs?',
    'It\'s not by any means a brilliant salary but it\'s adequate for our needs.',
    'I need my shoes mended.',
    'My camera needs repairing.',
    'I need you to push my car.',
    'Does this shirt need ironing?',
    'The pie doesn\'t need to be refrigerated.',
    'Being a teacher needs a high level of motivation.',
  ],
}
test_data_2041 = { 

        # **Super category:** Modal verbs 3
        # **Sub category: **should
        
  'positive': [
    'You shouldn\'t have said anything.',
    'I think it should stay sunny all afternoon.',
    'I agreed that he should continue to see the children.',
    'I don\'t see why he should get more money than me.',
    'I shouldn\'t want to be paid for the work.',
    'I was just getting off the bus when who should I see but my old school friend Pat!',
    'You should\'ve seen Charlie dancing!',
    'Shouldn\'t we call and make a reservation?',
    'They shouldn\'t have so many children if they couldn\'t support them.',
    'There should be an investigation into the cause of the disaster.',
  ],
  'negative': [
    'I rested my head on her shoulder.',
    'The refugees were packed shoulder to shoulder on the boat.',
    'A laminated leather small shoulder bag was on sale.',
    'The scapula is also known as shoulder blade.',
    'A shoulder tag is attached to the left shoulder strap.',
    'Bazooka is a type of shoulder-fired unguided rocket launcher in its own right.',
    'My hair is now shoulder-length and will have to stay that way.',
    'Typically, we fit a rim cylinder lock around shoulder height on a wooden door.',
    'The shoulder sleeve insignia in its color form was commonly only worn on the dress uniform.',
    'The pinch line forms a strong part of the cars shoulder line.',
    'There needs to be more effort from everyone.',
    'I brought him some sandwiches because I thought he might be hungry.',
    'You must find this guidebook helpful.',
    'Thou shalt remain here.',
    'Is not this greater loss than if thou shouldst lose the whole world?',
    'I would like to ask you to lend me this book if you would.',
    'Would you mind telling me your name?',
    'Do you dare speak to the boss about a pay rise?',
    'He came to Japan with us last year.',
    'The machine does not start operation until both the switches are pressed.',
  ],
}
test_data_2042 = { 

        # **Super category:** Modal verbs 3
        # **Sub category: **ought to
        
  'positive': [
    'We ought to clean up before we go home.',
    'She really ought to apologize.',
    'He ought to be home by seven o\'clock.',
    'The curtains ought to be ready on Monday.',
    'Never do more than ought to.',
    'Men and women ought to be able to compete for jobs on an equal footing.',
    'Mum ought to be home from work by now, so I\'ll give her a ring.',
    'He oughtn\'t to do that.',
    'I oughtn\'t to have said that.',
    # parser error
    # 'A big girl ought not to dally with her mamma.',
    'A big girl ought not to putter with her mamma.',
  ],
  'negative': [
    'I fought with my father.',
    'The thought that she might not come annoyed him.',
    'That can\'t be bought with money.',
    'Do not set at nought the decencies of social intercourse!',
    'Expecting her to tell us her mind is like waiting for a raindrop in the drought.',
    'There may be other problems that we don\'t know about.',
    'You mustn\'t carry your jokes too far!',
    'He said he would see his brother tomorrow.',
    'If you\'re annoyed with him, you should tell him.',
    'Will she be able to cope with the work?',
    'You shouldn\'t have said anything.',
    'I think it should stay sunny all afternoon.',
    'I agreed that he should continue to see the children.',
    'I don\'t see why he should get more money than me.',
    'I shouldn\'t want to be paid for the work.',
    'I would like to ask you to lend me this book if you would.',
    'Would you mind telling me your name?',
    'Do you dare speak to the boss about a pay rise?',
    'He came to Japan with us last year.',
    'The machine does not start operation until both the switches are pressed.',
  ],
}
test_data_2043 = { 

        # **Super category:** Modal verbs 3
        # **Sub category: **had better

  'positive': [
    'You\'d better go home now before the rain starts.',
    'He\'d better pay me back that money he owes me soon, or else.',
    'I\'d better not leave my bag there. Someone might steal it.',
    'You\'d better not tell Elizabeth about the broken glass.',
    'Had I better speak to Joan first before I send this form off?',
    'Had we better leave a note for the delivery guy to take the parcel next door?',
    'Hadn\'t we better ring the school and tell them Liam is sick?',
    'What had I better do?',
    'I\'d better be going.',
    # parser's problem: 'had' is the main word
    # 元のparser orderならok
    # 'In any case, you had better go home right away.',
    'I\'d better leave a note so they\'ll know I\'ll be late.',
  ],
  'negative': [
    'He stood near the front to get a better view.',
    'Relations between the two countries have never been better.',
    'It\'s much better to have a small, cozy room than a big, cold one.',
    'Prevention is better than cure.',
    'She is much better at tennis than I am.',
    'It would be better to use the backstair influence.',
    'The invalid grows better and better every day.',
    'Because I had nothing better to do.',
    'She had never sung better.',
    'As I had nothing else better to do to kill time, I began to write a letter.',
    'You\'d best leave it till Monday.',
    'He was dressed in an old coat that had seen better days.',
    'I had nothing to do.',
    'She had just had surgery.',
    'They had had to use what money they had.',
    'There needs to be more effort from everyone.',
    'I brought him some sandwiches because I thought he might be hungry.',
    'You should find this guidebook helpful.',
    'He oughtn\'t to do that.',
  ],
}
test_data_2044 = { 

        # **Super category:** Modal verbs 4
        # **Sub category: **will
        
  'positive': [
    'Ask Gabriela if she\'ll take them.',
    'If a plane window breaks, the cabin will rapidly decompress.',
    'Representatives of the member states will be meeting next week.',
    'As you all will know, election day is next week.',
    'An empty bottle will float.',
    'You\'ll go upstairs and you\'ll go straight to bed as your father told you!',
    'I\'ll see you tomorrow.',
    'He will work one day and loaf the next.',
    'When you\'ve finished that book will you lend it to me?',
    'That\'ll be his mother with him.',
  ],
  'negative': [
    'He is not willing to concede any of his power.',
    'He left me his racehorses in his will.',
    'What he said may well be true.',
    'The government has failed to impose its will upon regional communities.',
    'I would willingly give my life for that of my child.',
    'The willow is one of the four species associated with the Jewish festival of Sukkot.',
    'From an early age, she had a very strong will.',
    'Have you made a will yet?',
    'He was struck out from his father\'s will.',
    'She willed herself to remember his name.',
    'Will-o-the-wisp is a part of the folklore in Brazil, Argentina, Colombia, Venezuela, and Uruguay.',
    'Against their will, they were forced to hand over the money.',
    'It was God\'s will.',
    'After six months in the hospital, she began to lose the will to live.',
    'You might well be able to come up with more ideas of your own.',
    'He can cry at will.',
    'When she remarried, she made a new will.',
    'You may be prosecuted for homicide by willful negligence.',
    'His letter bespeaks his willingness to help.',
    'She left me some money in her will.',
  ],
}
test_data_2045 = { 

        # **Super category:** Modal verbs 4
        # **Sub category: **would
        
  'positive': [
    'I would often go fishing in the river with my grandfather when I was a kid.',
    'I would rather stay here.',
    'I wish you would give up smoking.',
    'If I got money, I would go on a trip.',
    'I thought it would rain yesterday.',
    'I would rather walk than run.',
    'I would rather go hungry than betray my country.',
    'I would rather spend the rest of my life alone than marry someone I don\'t love.',
    'I’d like to see that movie when it comes out.',
    'Would you like to come too?',
    'You said you would do your best.',
    'He thought she would become a singer.',
    'I turned the key but the car wouldn’t start.',
    'I wouldn’t drink anymore if I were you.',
    'I’d like to have some coffee.',
    'If I had gotten money, I would have gone on a trip.',
    'He would like to buy stamps.',
    'I thought he would go there.',
    'She would rather die than go out with you.',
  ],
  'negative': [
    'I will have been to Hawaii three times if I go there again.',
    'You will have been playing tennis for twenty years by the time you graduate from college.',
    'In a week, she will have practiced the violin for five years.',
    'I will have finished my homework by 10 a.m. tomorrow.',
    'I agreed that he should continue to see the children.',
    'I think it should stay sunny all afternoon.',
    'It will be fine tomorrow.',
    'He won’t listen to my advice.',
    'This window won’t open.',
    'He will be in New York by now.',
    'Will you play tennis?',
    'I want to exchange some money.',
    'You shouldn\'t have said anything.',
    'Claudia will have been talking with her friend until her mom tells her to stop.',
    'I want to send this by airmail.',
    'Jonathan will have been sleeping by the time I call him.',
    'I will go, no matter what you say.',
    'Will you go to the supermarket for me?',
    'Teenagers will not do as they are told.',
    'I want to go to Europe someday.',
  ],
}
test_data_2046 = { 

        # **Super category:** Modal verbs 4
        # **Sub category: **used to
        
  'positive': [
    'I used to live here.',
    'I used to practice baseball to win the Koushien.',
    'I used to play the piano.',
    'I used to think I could read people\'s minds.',
    'When we were children, we used to go to the park.',
    'I used to believe in god.',
    'My mom used to wear flashy clothes to stand out.',
    'She used to live in Osaka, but she moved to Tokyo last year.',
    'I used to study English very hard.',
    'He used to have three apple watches.',
  ],
  'negative': [
    'I would rather go hungry than betray my country.',
    'He thought she would become a singer.',
    'Would you like to come too?',
    'I wouldn’t drink anymore if I were you.',
    'I would often go fishing in the river with my grandfather when I was a kid.',
    'I wish you would give up smoking.',
    'If I got money, I would go on a trip.',
    'You said you would do your best.',
    'I want to use this app because it is useful.',
    'Can I use your pen?',
    'You can use this if you want.',
    'I thought it would rain yesterday.',
    'I would rather spend the rest of my life alone than marry someone I don\'t love.',
    'I thought he would go there.',
    'I want to send this by airmail.',
    'I used this phone when I was a kid.',
    'I would rather stay here.',
    'My friends used this bag for the last trip.',
    'This machine can be used anytime.',
    'I turned the key but the car wouldn’t start.',
    'I will use your money if you let me.',
    'If I had gotten money, I would have gone on a trip.',
  ],
}
test_data_2047 = { 

        # **Super category:** Modal verbs 4
        # **Sub category: **would の慣用表現
        
  'positive': [
    'I’d like to send this by airmail.',
    'I would rather stay here.',
    'I would rather go hungry than betray my country.',
    'He would rather take the bus.',
    'My friend would rather die than surrender.',
    'Would you like to come too?',
    'I would rather spend the rest of my life alone than marry someone I',
    'I would rather ride the train than the bus.',
    'I would have liked to come, but I couldn\'t make it.',
    'I\'d like to live by the sea in the future.',
  ],
  'negative': [
    'I would often go fishing in the river with my grandfather when I was a kid.',
    'Would you care to go for a walk?',
    'I wish you would give up smoking.',
    'If I got money, I would go on a trip.',
    'I thought it would rain yesterday.',
    'He would be happier now.',
    'You said that he would come.',
    'Would you pass the salt, please?',
    'I wouldn’t drink any more if I were you.',
    'Would you come with me?',
    'I wish something nice would happen.',
    'I would have been shot.',
    'You said you would do your best.',
    'I thought he would go there.',
    'Would you please open the window?',
    'He thought she would become a singer.',
    'I turned the key but the car wouldn’t start.',
    'If I had gotten money, I would have gone on a trip.',
    'Would you mind my opening the window?',
    'Would you look after the place while I\'m out?',
  ],
}
test_data_2048 = { 

        # **Super category:** Modal verbs 5
        # **Sub category: **助動詞+完了
        
  'positive': [
    'They must have been pleased.',
    'She may have forgotten about you.',
    'She must have dreamed.',
    'My friend can\'t have told a lie.',
    'He should have arrived at his office by now.',
    'He must have been tired last week.',
    'You needn\'t have come here at three o\'clock.',
    'He may have read my diary already.',
    'You should have come to the party last night.',
    'He may have overslept this morning.',
  ],
  'negative': [
    'How can I change your mind?',
    'I have already spent all my money.',
    'She has visited London twice.',
    'Mt. Fuji can be seen from here.',
    'You must be nervous about school.',
    'I have lost my watch.',
    'It could rain later on.',
    'She has studied English for ten years.',
    'May I offer you one more piece of cake?',
    'My brother has just washed the dishes.',
    'Shall I fix you something special?',
    'I have just finished my homework.',
    'I have been doing my homework all day.',
    'You may choose any cake you like.',
    'You can come bowling with us.',
    'My family has climbed Mt. Fuji twice.',
    'He has lived in Kyoto for two years.',
    'Would you like some cotton candy?',
    'I must hear the rest of the story.',
    'She has been in the hospital since last week.',
  ],
}
test_data_2049 = { 

        # **Super category:** Passive voice 1
        # **Sub category: **SVOCのpassive
        
  'positive': [
    'We were made to leave the library by them.',
    'The students were made happy by the victory.',
    'He was elected captain of the basketball team.',
    'This car was painted black by me.',
    'They were made to leave the building by the police.',
    'I was always kept waiting at the station.',
    'I am always kept waiting by my girlfriend.',
    'I was advised by our teacher to study English.',
    'The people were made miserable by war.',
    'He is called Superman by us.',
  ],
  'negative': [
    'That is the park where I often went in my childhood.',
    'Bill always keeps me waiting at school.',
    'Someone saw two men sneak into the office.',
    'I saw a man climb over the fence of the yard.',
    'My mother gave me a watch.',
    'War made the people miserable.',
    'My father made me wait outside his office.',
    'Please let me know the exact date when he will return.',
    'She persuaded her children to clean the room.',
    'The police made them leave the building.',
    'The librarian advised us to read more books.',
    'The victory made the students happy.',
    'The teacher advised the student to study law in college.',
    'We call him superman.',
    'I painted this car black.',
    'Everyone calls the cat Fluffy.',
    'The dentist advised me to brush my teeth after each meal.',
    'Our boss always keeps us waiting at meetings.',
    'The captain made the team members leave the gym.',
    'The doctor advised me to get more sleep.',
  ],
}
test_data_2050 = { 

        # **Super category:** Passive voice 1
        # **Sub category: **SVOOのpassive
        
  'positive': [
    'The watch was given to me by my father.',
    'We are taught math by Mr. Smith.',
    'Her sister was given a ring.',
    'Amelia was shown my friend’s picture by me.',
    'A book was given to her by him.',
    'A ring was bought for me by my boyfriend.',
    'Jackie was awarded the first prize by the association.',
    'His mother was given a carnation by him.',
    'We were given the permission by our manager.',
    'The permission was given to us by our manager.',
  ],
  'negative': [
    'We were made to leave the library by them.',
    'The students were made happy by the victory.',
    'Our manager gave us the permission.',
    'She baked him a chocolate cake.',
    'Bill always keeps me waiting at school.',
    'He was elected captain of the basketball team.',
    'We sent her a doll.',
    'She bought me this new camera.',
    'This car was painted black by me.',
    'They were made to leave the building by the police.',
    'My uncle gave me this book.',
    'She gave her mother a necklace.',
    'I was always kept waiting at the station.',
    'She sold me the watch for thirty dollars.',
    'I am always kept waiting by my girlfriend.',
    'I was advised by our teacher to study English.',
    'The people were made miserable by war.',
    # 'He is called Superman by us.',
    # ブラウザだとcall->Superman(xcomp)なのでそれだとFalseです。
    'The victory made the students happy.',
    'My father bought me a computer.',
  ],
}
test_data_2051 = { 

        # **Super category:** Passive voice 1
        # **Sub category: **否定文 passive
        
  'positive': [
    'These products weren’t made in Japan.',
    'He was not surprised at the news.',
    'This desk is not used.',
    'This picture was not painted by him.',
    'This machine was not broken by him.',
    'Oranges are not grown here.',
    'This book was not read by my brother.',
    'This room is not cleaned enough.',
    'English is not spoken in France.',
    'She was not invited to the party.',
  ],
  'negative': [
    'Where was the watch made?',
    'I was given this stopwatch.',
    'Mt. Fuji can be seen from here.',
    'The photo album was made by my classmates.',
    'Was this apple bought three days ago?',
    'Is this office cleaned every day?',
    'I was surprised.',
    'We were told to put the money in that box.',
    'Was this cafe built last year?',
    'What language is spoken in Japan?',
    'This zoo is loved by everybody!',
    'Was he praised by the teacher?',
    'I was given this booklet about the church.',
    'This festival is held every year.',
    'How many people are invited to the party?',
    'Is this book written by a famous author?',
    'Who was he praised by?',
    'The plate is made of wood.',
    'Was the picture painted by you?',
    'It is made from honey.',
  ],
}
test_data_2052 = { 

        # **Super category:** Passive voice 1
        # **Sub category: **疑問文 passive
        
  'positive': [
    'Will this book be bought by her?',
    'Will this place be visited by many people?',
    # TODO be動詞の受動態が全滅
    # 以前のparserと新しいparserをdetectorによって切り分けるというのを実装するか？
    # 'Were these pictures taken in New York?',
    # 'Is this office cleaned every day?',
    # 'Was this cafe built last year?',
    # 'Was he praised by the teacher?',
    # 'Are you called Taro?',
    # 'Is this book written by a famous author?',
    # 'Was the picture painted by you?',
    # 'Was this apple bought three days ago?',
  ],
  'negative': [
    'These products weren’t made in Japan.',
    'Cakes are being baked by my mother.',
    'The document must be written by her.',
    'He was made to cook breakfast by her mother.',
    'I was told to work here.',
    'I was given this stopwatch.',
    'He was not surprised at the news.',
    'This desk is not used.',
    'The girl was spoken to by a stranger.',
    'I was allowed to drive my father’s car.',
    'she was heard to play the piano.',
    'This zoo is loved by everybody!',
    'This machine was not broken by him.',
    'This festival is held every year.',
    'Oranges are not grown here.',
    'This book was not read by my brother.',
    'My bicycle was broken last night.',
    'The plate is made of wood.',
    'Spanish is spoken in Spain.',
    'English is not spoken in France.',
  ],
}
test_data_2053 = { 

        # **Super category:** Passive voice 2
        # **Sub category: **passive 助動詞
        
  'positive': [
    'The document must be written by her.',
    'The door must not be opened.',
    'A cell phone can be used here.',
    'A driver\'s license has to be gotten to drive a car.',
    'The house will be repaired next month.',
    'These flowers will be arranged by a designer.',
    'Rare animals can be seen in the zoo.',
    'Can the book be borrowed from the library？',
    'This job must be done by him.',
    'This book could be read by many children.',
  ],
  'negative': [
    'He was not surprised at the news.',
    'I was given this stopwatch.',
    'I could practice more but I didn’t.',
    'she was said that she was a professional.',
    'You may come in.',
    'Shall I help you carry your baggage?',
    'I would visit my grandparents when I was a child.',
    'You can choose anything you like.',
    'This zoo is loved by everybody!',
    'I was told to do homework.',
    'He might be angry with me.',
    'You should go to bed early.',
    'This machine was not broken by him.',
    'This festival is held every year.',
    'I must tell the truth to her.',
    'This book was not read by my brother.',
    'My bicycle was broken last night.',
    'Spanish is spoken in Spain.',
    'English is not spoken in France.',
    'I will ask her out.',
  ],
}
test_data_2054 = { 

        # **Super category:** Passive voice 2
        # **Sub category: **passive 進行形
        
  'positive': [
    'The meal is being made now.',
    'The computer is being used by my husband.',
    'Our house is being built.',
    'These trees are being planted by them.',
    'His car is still being repaired.',
    'The car is being washed by Hiroshi.',
    'He is being watched by many people now.',
    'The book is being read by the man.',
    'The city hall is being rebuilt.',
    'The man is being tried for murder.',
  ],
  'negative': [
    'We’re going to New York next month.',
    'I’m taking the morning yoga classes for a while.',
    'He was not surprised at the news.',
    'The document must be written by her.',
    'Can　the　book　be　borrowed　from　the　library？',
    'I’m running around my house.',
    'A cell phone can be used here.',
    'He’s driving my car.',
    'She’s looking for a new job.',
    'This book could be read by many children.',
    'They are dancing.',
    'He’s writing a letter to his girlfriend.',
    'I’m cooking dinner.',
    'She is thinking about you.',
    'My bicycle was broken last night.',
    'This job must be done by him.',
    'Spanish is spoken in Spain.',
    'she was said that she is a professional.',
    'She is going into the supermarket.',
    'Rare　animals　can　be　seen　in　the　zoo.',
  ],
}
test_data_2055 = { 

        # **Super category:** Passive voice 2
        # **Sub category: **passive  完了形
        
  'positive': [
    # 'I have been interested in this band lately.',
    # the pos of 'interested' is JJ
    'Dinner has been cooked by her.',
    'The thief had already been arrested when I got to the police stand.',
    'The building had been destroyed when I arrived there.',
    'The ground has been covered with snow.',
    'My room has been cleaned by my mother now.',
    'I have been moved by him recently.',
    'I have been told a lie by my best friend once.',
    'The song has been sung by many people.',
    'I have been praised by my mother since I was a child.',
  ],
  'negative': [
    'I have lost my way in the woods before.',
    'Kate has watched that DVD many times.',
    'The document must be written by her.',
    'The computer is being used by my husband.',
    'Our house is being built.',
    'This book could be read by lots of children.',
    'These trees are being planted by them.',
    'I have never lost my wallet.',
    'She has already read the book.',
    'The car is being washed by Hiroshi.',
    'He has recently returned from Tokyo.',
    'The city hall is being rebuilt.',
    'I haven’t checked the train schedule yet.',
    'I have been busy since this morning.',
    'Rare animals can be seen in the zoo.',
    'She has just stopped crying.',
    'This job must be done by him.',
    'My father has worked at the bank since 2000.',
    'The man is being tried for murder.',
    'I haven’t smoked for over two years.',
  ],
}
test_data_2056 = { 

        # **Super category:** Passive voice 3
        # **Sub category: **byを取らない動詞 known to etc
        
  'positive': [
    'The desk is made of wood.',
    'He was amazed at the news.',
    'The singer is known to many people.',
    'He was wounded in the war.',
    'She is known to everyone.',
    'I was caught in the shower yesterday.',
    'He is surprised at the new.',
    'He was interested in the book.',
    'I\'m very pleased with my new job.',
    'He was hurt in the car accident.',
    'I was disappointed at his absence.',
    'He was satisfied with the result.',
    'They were delighted at the good news.',
    'Are you frightened of dogs?',
    'She was married to him.',
    'She was killed in action.',
    'The bus is very crowded with students.',
    'The ground was covered with snow.',
    'I\'m terribly shocked at the news of his accident.',
    'The box was filled with cookies.',
    'I\'m excited about going to the movie.',
    'The box was covered with a cloth.',
    'Wine is made from grapes.',
    'I\'m very worried about your health.',
    'He was injured in the car accident.',
  ],
  'negative': [
    'You are cheered up by many people.',
    'That car is driven by my brother.',
    'The photo album was made by my classmates.',
    'This zoo is loved by everybody.',
    'He is finally caught up by others.',
    'The tree was cut down by that person.',
    'You are hated by everyone.',
    'This desk was bought by my mom.',
    'My new dress was fallen apart by the washing machine.',
    'This laptop is used by you.',
    'This computer is made in Japan.',
    'This hotel was built by my family.',
    'I was delayed.',
    'These shoes are worn by me all the time.',
    'My sister was broken up with her boyfriend by her friend.',
    'I was born in 1990.',
    'This hotel is checked in by lots of people every day.',
    'This was found out by a famous actor in Japan.',
    'This problem is figured out by him.',
    'His mother was given a carnation by him.',
    'This CD was recorded by my band.',
    'These pictures were taken by her.',
    'This room is cleaned up by my mom.',
  ],
}
test_data_2057 = { 

        # **Super category:** Passive voice 3
        # **Sub category: **it is said that/ S is said to
        
  'positive': [
    'She is said to be in the hospital now.',
    'It is said that it lost its utility later.',
    'He was said to be killed in the battle.',
    'It is said that he is sick.',
    'Children are said to bring their parents together.',
    'It is said that she is seriously ill.',
    'It is said that the taste of love is bitter.',
    'He is said to be mad',
    'It is said that you are stupid.',
    'He is said to be ill.',
  ],
  'negative': [
    'I have been interested in this band lately.',
    'The teacher said to me, "Get out!"',
    'Jane said that it was time to go home.',
    'The policeman said to them, "Stop."',
    'I have never lost my wallet.',
    'He said to himself that he should go.',
    'She has already read the book.',
    'He has recently returned from Tokyo.',
    'I said that to myself.',
    'My father has worked at the bank since 2000.',
    'The thief had already been arrested when I got to the police stand.',
    'He said to watch out.',
    'The ground has been covered with snow.',
    'I have been moved by him recently.',
    'He said that you ought to go.',
    'He said to her under his breath.',
    'He said he wanted to be a scientist.',
    'The city hall is being rebuilt.',
    'He said goodbye to the family',
    'The man is being tried for murder.',
  ],
}
test_data_2058 = { 

        # **Super category:** Passive voice 3
        # **Sub category: **phrasal verbのpassive voice
        
  'positive': [
    'That house was broken into by fireman.',
    'This room is cleaned up by my mom.',
    'My sister was broken up with her boyfriend by her friend.',
    'He is finally caught up by others.',
    'You are cheered up by many people.',
    'This hotel is checked in by lots of people every day.',
    'My new dress was fallen apart by the washing machine.',
    'This problem is figured out by him.',
    'The tree was cut down by that person.',
    'This was found out by a famous actor in Japan.',
  ],
  'negative': [
    'I could sleep over at your place.',
    'She doesn\'t care about you.',
    'We have to get over this problem.',
    'I can take care of you.',
    'I ran into your friend yesterday.',
    'I will take off to Japan soon.',
    'I have to work out harder.',
    'I can\'t look at your face.',
    'You grow up so fast.',
    'I woke up late this morning.',
    'I usually get up early.',
    'My mom just passed out.',
    'We can hang out sometimes.',
    'I will go back home soon.',
    'She wanted to run away.',
    'Can you hold on a second?',
    'Can you turn off the light?',
    'She gave up this issue.',
    'I will look after him.',
    'I will pick you up at the airport.',
  ],
}
test_data_2059 = { 

        # **Super category:** Infinitive 1
        # **Sub category: ** noun infinitives
        
  'positive': [
    "They planned to put up a statue to the president."
    "Everyone wants to enjoy life.",
    "She likes to be admired.",
    "Two bad habits are to smoke cigarettes and to drink alcohol.",
    "To stop the car suddenly can be dangerous.",
    "To cheat is a sign of weakness.",
    'Our chief purpose has been to break the deadlock in the business negotiations.',
    'To use a Japanese word processor is difficult.',
    'She agreed to help.',
    'Sadly, she didn\'t live to see her grandchildren.',
    'The barometer began to fall slowly.',
    # parser error: xsubj なし
    # 'I\'d prefer not to work but I don\'t have much choice.',
    'Can you tell me how to get there?',
    'It is necessary for corporations to have a sense of social responsibility.',
    'I need to eat something first.',
    'On a hot day, it\'s lovely to hear the chink of ice in a glass.',
    # parser error: butを等位接続詞と認識しない
    # 'I want nothing but to save.',

    'Troops are to take over the role of the fire brigade.',
  ],
  'negative': [
    'We have an important subject to deal with at once.',
    'He was always the first to come and the last to leave the office.',
    'Is there anything good to eat in the refrigerator?',
    'She\'s wise enough to know that.',
    'In America, there is still a persistent movement to restrict imports from Japan.',
    'Who\'s the letter addressed to?',
    'There\'s nothing to see in this gallery.',
    'I mean, marriage is nothing to him.',
    'She was maid to a rich family in London.',
    'This meat is difficult to chew.',
    'I was bored to tears.',
    'Three months is too long to wait.',
    'He will live to be ninety.',
    'He went up to a complete stranger and started talking.',
    'She walked over to the window.',
    'To my complete horror, the car turned right over.',
    # 不定詞の動詞的用法
    'We want a staff assistant to perform secretarial duties for the president.',
    'The Spanish Civil War lasted from 1936 to 1939.',
    # 同格の不定詞(adj)と判断できる。
    'My hope, to travel, never happened.'
  ],
}
test_data_2060 = { 

        # **Super category:** Infinitives 1
        # **Sub category: **infinitives adjective
        
  'positive': [
    'We have an important subject to deal with at once.',
    'He was always the first to come and the last to leave the office.',
    'Is there anything good to eat in the refrigerator?',
    'She\'s wise enough to know that.',
    'There are many things to see in the city.',
    'Jeff has many friends to speak Japanese fluently.',
    'We want a staff assistant to perform secretarial duties for the president.',
    'Please give me something to write with.',
    'I want something to eat.',
    "Joe is the man to see about the job.",
    "Your idea to spend the day together sounds great.",
    "We have no reason to doubt your sincerity.",
    "This must be the best route to take.",
    "Your attitude is the best attitude to have.",
    'There\'s nothing to see in this gallery.',
    'This meat is difficult to chew.',
    'In America, there is still a persistent movement to restrict imports from Japan.',
    # TODO 不定詞判定後で考える
    # 形容詞、副詞どっちでも取れる
    # 'He bought a magazine to read in a train.',
  ],
  'negative': [
    'Our chief purpose has been to break the deadlock in the business negotiations.',
    'I mean, marriage is nothing to him.',
    'She agreed to help.',
    'Who\'s the letter addressed to?',
    'Troops are to take over the role of the fire brigade.',
    'Sadly, she didn\'t live to see her grandchildren.',
    'She was maid to a rich family in London.',
    'I was bored to tears.',
    'They planned to put up a statue to the president.',
    'Three months is too long to wait.',
    'I\'d prefer not to work but I don\'t have much choice.',
    'He went up to a complete stranger and started talking.',
    'She walked over to the window.',
    'To my complete horror, the car turned right over.',
    'Can you tell me how to get there?',
    'The Spanish Civil War lasted from 1936 to 1939.',
    'I need to eat something first.',
    "To use a Japanese word processor is difficult."
  ],
}
test_data_2061 = { 

        # **Super category:** Infinitives 1
        # **Sub category: **infinitives adverb
        
  'positive': [
    'There are many things to see in the city.',
    'Jeff has many friends to speak Japanese fluently.',
    'She lived to be ninety.',
    'Please give me something to write with.',
    'I want something to eat.',
    # TODO 不定詞判定後で考える
    # 'She\'s wise enough to know that.',
    # 'It\'s not likely to happen.',
    # 'He bought a magazine to read in a train.',
    # 'To tell the truth, I don\'t like it.',
    # 'We eat to live.',
  ],
  'negative': [
    'He was always the first to come and the last to leave the office.',
    'I mean, marriage is nothing to him.',
    'She agreed to help.',
    'Who\'s the letter addressed to?',
    'Troops are to take over the role of the fire brigade.',
    'Sadly, she didn\'t live to see her grandchildren.',
    'She was maid to a rich family in London.',
    'This meat is difficult to chew.',
    'I was bored to tears.',
    'They planned to put up a statue to the president.',
    'Three months is too long to wait.',
    'I\'d prefer not to work but I don\'t have much choice.',
    'He went up to a complete stranger and started talking.',
    'She walked over to the window.',
    'To my complete horror, the car turned right over.',
    'The Spanish Civil War lasted from 1936 to 1939.',
    'I need to eat something first.',
    # TODO 不定詞判定後で考える
    # 'In America, there is still a persistent movement to restrict imports from Japan.',
    # 'There\'s nothing to see in this gallery.',
    # 'Can you tell me how to get there?',
  ],
}
test_data_2062 = { 

        # **Super category:** Infinitives 2
        # **Sub category: **SVO to do
        
  'positive': [
    'Do you want me to take you to the airport?',
    'They ordered him to leave the room.',
    # question: Is this the proper sentence? Doesn't look "SVO to do structure".
    # 'All of the staff were made to wear their uniform every day.',
    'The law does not obligate sellers to accept the highest offer.',
    'I\'ve invited Jill to come to dinner on Saturday.',
    'What do you expect him to do?',
    # 'As a schoolboy, he was compelled to wear shorts even in winter.',
    'She begged him not to leave her.',
    'I think I\'d advise him to leave the company.',
    'The security system will not permit you to enter without the correct password.',
  ],
  'negative': [
    'What made you change your mind?',
    'She moved to London in the hope of finding work as a model but failed.',
    'Some prisoners who want to start a family are to be permitted conjugal visits.',
    'Have you found John difficult to talk to?',
    'Our mentor has advised us that we should start working on the project as soon as possible.',
    'The prison authorities permit visiting only once a month.',
    'I suggested that she should consult a doctor.',
    'Give that gun to me.',
    'I found these photos while I was cleaning out my cupboards.',
    'We needed a guide and he was only too happy to oblige.',
    'He has this enviable ability to ignore everything that\'s unpleasant in life.',
    'Can I help you fix the fence?',
    'Why don\'t you let me go?',
    'He went up to a complete stranger and started talking.',
    'I was bored to tears.',
    'You have no right to ask about it.',
    'I\'ve lost the trousers to this jacket.',
    'I heard her sing a lovely song.',
    'He warned us that temperatures would drop the following week dramatically.',
    'Has he found himself a place to live yet?',
  ],
}
test_data_2063 = { 

        # **Super category:** Infinitives 2
        # **Sub category: **SVO V(make, have etc)
        
  'positive': [
    'He lets us use some of his land to grow vegetables.',
    # 'He watched the thieves steal a car.',
    # the pos of steal is VBP
    'I want to help you understand the situation better.',
    'She made us wait for half an hour.',
    'Mandy noticed the boy climb the tree.',
    'John lets the dog sleep on the sofa.',
    # 'She feels the rain fall on her face',
    # parser's problem: feels->fall(nmod:tmod)
    'You can\'t make a cat do anything it doesn\'t want to do.',
    'They saw him climb up the roof.',
    # 'I heard Peter sing a song.',
    # parser's problem: Peter->sing (dep)
  ],
  'negative': [
    'She said she\'d pick it up for me after work.',
    'I had no one to talk to.',
    'We all wanted to have more English classes.',
    'It was predicted that a comet would collide with one of the planets.',
    # 'We arranged to see the bank manager and applied for a loan.',
    'Mrs. Harding asked us to call in on our way home.',
    'This door is always kept locked in winter.',
    'I think it\'s important to listen to both sides of the argument.',
    'We arrived at the airport just in time to catch the plane.',
    'We set off early in order to avoid the traffic.',
    'They spoke quietly so as not to wake the children.',
    'They gave him an opportunity to escape.',
    # 'I know he went with her.',
    'Did you remember to post the letter to your mother?',
    'I decided to go home as soon as possible.',
    'We\'ll be there at about 7.30, provided/providing there\'s not too much traffic.',
    'It is in a park he proposed to her.',
    'His parents saw him awarded the winner\'s medal.',
    'I could hear someone calling my name.',
    'It would be silly of him to spend all his money.',
  ],
}
test_data_2064 = { 

        # **Super category:** Infinitives 2
        # **Sub category: **wh-word to do
        
  'positive': [
    'Sometimes it also means how to dress in that style.',
    'He is a man who doesn\'t know when to quit.',
    'This judges the timing when to complete the cathode recovery operation.',
    'We must find out what job to do next.',
    'When to set off is a difficult problem.',
    'I don\'t know where to turn for help.',
    'I will show you how to manage it.',
    'Have you thought about what to send as a present?',
    'Let us decide when to start.',
    'I told him where to go.',
    'I don\'t know which to take.',
  ],
  'negative': [
    'I rang them yesterday to check when they were arriving.',
    'A little after one o\'clock I got to the town, where I had lunch.',
    'What did you say to him?',
    'You reach a point where you just want to get the thing finished.',
    'This is where we used to play.',
    'Ask him when he\'s next coming home.',
    'I really didn\'t know what I should say to you.',
    'Oh, how nice to see you!',
    'What I am reading now is a how-to book on golf.',
    'If you\'d told me what was wrong, I could have helped.',
    'Air is to us what water is to fish.',
    'How many stops to Harajuku?',
    'Why is she training to be a teacher when she doesn\'t even like children?',
    'What is it you want to buy?',
    'When do you expect to have the project completed by?',
    'I like to have him next to me where I can keep an eye on him.',
    'Where did she go to college?',
    'Do you remember how we used to see every new film as soon as it came out?',
    'How do we get to the town from here?',
    'It\'s pointless to invite him when you know he won\'t come.',
  ],
}
test_data_2065 = { 

        # **Super category:** Infinitives 3
        # **Sub category: **not to do
        
  'positive': [
    'Be careful not to get sick!',
    'I advised a friend of mine not to smoke.',
    'Do not pretend not to know.',
    'I will not fail to come.',
    'Take care not to start a fire.',
    'I decided not to complain.',
    'I\'d prefer not to work but I don\'t have much choice.',
    'Do you mean not to combine?',
    'It\'s not likely to happen.',
    'I managed not to get tan.',
  ],
  'negative': [
    'It is a point to not give up through the end.',
    'It is not open to the public.',
    'These are not related to this report.',
    'The new wall material does not subject to decay.',
    'Your suggestion never brings the discussion to a conclusion.',
    'She is kept by him but not married to him.',
    'I\'m not able to make it.',
    'I do not have anything else to tell you about.',
    'He is not much to blame.',
    'You are not indifferent to me.',
    'This is not going to happen.',
    'He that has not served knows not how to command.',
    'Not that the work is not to my taste.',
    'She\'s not strong enough to go hiking up mountains.',
    'She did not go to bed last night.',
    'I\'m not nice to you.',
    'There is not much to choose between A and B.',
    'A sin that is considered to be not serious.',
    'Do not eat what you are not used to.',
    'I am not habituated to luxury.',
  ],
}
test_data_2066 = { 

        # **Super category:** Infinitives 3
        # **Sub category: **to have done
        
  'positive': [
    'Tom and Mary are said to have broken up.',
    'She seems to have been happy.',
    'He seems to have caught a bad cold last night.',
    'I intended to have gone out.',
    'Mary was sorry to have missed John.',
    'Someone seemed to have broken the window and climbed in.',
    'Before I turn 40, I want to have written a book.',
    'He hoped to have succeeded.',
    'They seem to have had a good time in Rome.',
    'He pretended to have seen the film.',
  ],
  'negative': [
    'It is important to have information in the mind.',
    'It is disgusting to have compassion for one\'s inferiors.',
    'We\'re going to have a wonderful time here in Venice.',
    'The tree grew to have a lot of fruits.',
    'Following a routine check-up, Mrs. Mason was discovered to have heart disease.',
    'You would be wise to have the appropriate vaccinations before you go abroad.',
    'This room needs to have a telephone installed.',
    'The school likes to have a contact number for parents during school hours.',
    'This book is easy enough for you to understand.',
    'I got to have a good appetite.',
    'At some point in the distant future, I would like to have my own house.',
    'I want to have a bottle of beer.',
    'These books appear to have lovely clear print.',
    'I\'ve never done it before, but I\'d like to have a try.',
    'I took the coat back to the shop to have it altered.',
    'Between the second and the third stage, you will have an intermission.',
    'If I had known you were coming, I would have baked a cake.',
    'She likes to have an afternoon nap.',
    'May I show you to your table, sir, or would you prefer to have a drink at the bar first?',
    'I have some business to attend to.',
  ],
}
test_data_2067 = { 

        # **Super category:** Infinitives 3
        # **Sub category: **to be doing
        
  'positive': [
    'He pretended to be sleeping.',
    'He is said to be traveling abroad.',
    'I happened to be waiting for the bus when the accident happened.',
    'He pretended to have been painting all day.',
    'I would have preferred to have been sleeping all afternoon.',
    'Her father seems to be playing golf with his friends.',
    'She seemed to be looking for something she\'d lost.',
    'I\'d really like to be swimming in a nice cool pool right now.',
    'It must be nice to be going to a wedding overseas.',
    'He seemed to be jogging in the park.',
  ],
  'negative': [
    'She felt the spider crawl up her leg.',
    'He asked me not to be late.',
    'Your sister has gone to finish her homework.',
    'I want a sandwich to eat.',
    'I\'ve forgotten where to put this little screw.',
    'To visit the Grand Canyon is my life-long dream.',
    'You made me come with you.',
    'The train is due to arrive at Glasgow Central at 12:12.',
    'To understand statistics, that is our aim.',
    'She\'s old enough to make up her own mind.',
    'It appears to be interesting.',
    'That is a dangerous way to behave.',
    'You\'re not old enough to have grand-children!',
    'I might stay another night in the hotel.',
    'The dog is naughty to destroy our couch.',
    'I am calling to ask you about my dad.',
    'They had better work harder on their homework.',
    'It is important for Jake to be patient with his little brother.',
    'I don\'t have anything to wear.',
    'I decided not to go to London.',
  ],
}
test_data_2068 = { 

        # **Super category:** Infinitives 3
        # **Sub category: **to be done
        
  'positive': [
    'Hurry up, there’s plenty of work to be done.',
    'I wish to be done with my task as soon as possible.',
    'I’ll confirm what’s to be done today.',
    'She was shocked to hear that much remains to be done.',
    'Such things ought not to be done in public.',
    'Unfortunately, my homework is yet to be done.',
    'There are letters to be written.',
    'The garden needs to be weeded.',
    'It is to be hoped that Heaven forgives him that lie.',
    'I didn\'t expect to be invited.',
    'This house is to be let.',
    'There is very little creative work to be done here.',
    'It is not to be done in a day.',
    'Nothing needs to be done today.',
  ],
  'negative': [
    'I would like to have my nails done.',
    'You need to get your homework done by tomorrow.',
    'We have to put right what we have done wrong.',
    'He was elected captain of the basketball team.',
    'I have done nothing related to this mistake.',
    'I am done talking to my sister.',
    'Something must be done to save us.',
    'What have I done to deserve a nice man?',
    'You will have to be responsible for what you’ve done.',
    'I have never done a job related to clinical trials.',
    'It was very careless of you to have done such a thing.',
    'I consider him to have done the right thing.',
    'James was furious at what they had done to him.',
    'What you have done is a disgrace to the family.',
    'By doing this, you will be able to get into a prestigious college.',
    'Our manager gave us the permission.',
    'It is not worth doing such a stupid thing.',
    'Give the book back to me when you have done with it.',
    'I was very happy to be able to see my grandma doing well.',
    'The people were made miserable by war.',
    'I was always kept awaiting at the station.',
  ],
}
test_data_2069 = { 

        # **Super category:** Gerunds
        # **Sub category: **gerunds
        
  'positive': [
    # parser error
    # like IN
    # 'Boys like playing baseball.',
    'Marry is fond of going to concerts.',
    'I dislike being talked back to.',
    'He repents of having been idle in his school days.',
    'My hobby is collecting old stamps.',
    'His careless driving irritates me.',
    'I have a liking for music.',
    'Telling lies is wrong.',
    # parser error
    # It <- meeting nsubj
    # 'It was a pleasure meeting you.',
    # parser error
    # askingがobjと判定されない
    # 'We call that asking for trouble.',
    'Hunting tigers is dangerous.',
    'Flying makes me nervous.',
    'Brushing your teeth is important.',
    'One of his duties is attending meetings.',
    'The hardest thing about learning English is understanding the gerund.',
    'One of life\'s pleasures is having breakfast in bed.',
    'Can you sneeze without opening your mouth?',
    'She is good at painting.',
    'She avoided him by walking on the opposite side of the road.',
    'We arrived in Madrid after driving all night.',
    'My father decided against postponing his trip to Hungary.',
    'There\'s no point in waiting.',
    'When will you give up smoking?',
    'He kept on asking for money.',
    'Jim ended up buying a new TV after his old one broke.',
    'I look forward to hearing from you soon.',
    'I am used to waiting for buses.',
    'She didn\'t really take to studying English.',
    'When will you get around to mowing the grass?',
    'They have a swimming pool in their back yard.',
    'I bought some new running shoes.',
    'She couldn\'t help falling in love with him.',
    # standの扱い（自動詞ならば準主語補語、他動詞ならば動名詞)
    'I can\'t stand being stuck in traffic jams.',
  ],
  'negative': [
    'Who is the man walking down the street?',
    'We can\'t have them forcing their views on everyone else.',
    'Who\'s the girl dancing with your brother?',
    'Seating myself I began to read.',
    'The following day was rainy.',
    'Seeing the policeman, he ran away.',
    'The girl seemed charming to me.',
    'This book is very interesting.',
    'It is going to be marvelous.',
    'A barking dog seldom bites.',
    'She came running to meet me.',
    'I saw three people climbing the hill.',
    'Not knowing what to say, I kept silent.',
    'I\'m playing tennis this afternoon.',
    'I found her drinking my whiskey.',
    # parser error
    # rained -> running xcomp
    # 'It rained heavily, completely running our holiday.',
    # 補文の述語（分詞)
    # TODO: ceilingが分詞判定される。動詞の辞書などを持ち弾くこと
    # 'I looked up and found we had water dripping through the ceiling.',
    # parser error
    # had -> laughing dobj (expected xcomp)
    # 'He had us all laughing.',

    # errorを出すため
    'Answer and ask questions about past intentions and changed plans with "was" and "were going to".',

    # 分詞準主語補語
    'I go shopping twice a week.',
    # standの扱い（自動詞ならば準主語補語、他動詞ならば動名詞)
    # 'He stood there smoking a pipe.',
  ],
}
test_data_2070 = { 

        # **Super category:** Gerunds
        # **Sub category: **gerunds 否定
        
  'positive': [
    'I think this article deserves not reading.',
    'I like not swimming.',
    'I believe never overeating is good for health.',
    'I insisted on his never going there.',
    'I believed him not having told a lie.',
    'Not watching TV is difficult for me.',
    # parser error
    # his -> playing acl
    # 元のparserならOK
    # 'I’m afraid of his not playing soccer with me.',
    'She is proud of not making mistakes.',
    'I’m sure of his not making mistakes.',
    'I regret not saying goodbye to you.',
  ],
  'negative': [
    'We can\'t have them forcing their views on everyone else.',
    'Who\'s the girl not dancing with your brother?',
    'She came running to meet me.',
    'I go shopping twice a week.',
    'I dislike being talked back to.',
    'We call that asking for trouble.',
    'I found her not drinking my whiskey.',
    'His careless driving irritates me.',
    'The following day was rainy.',
    'This book is not very interesting.',
    'It is going to be marvelous.',
    'A barking dog seldom bites.',
    'I don\'t like swimming.',
    'The girl seemed not charming to me.',
    'I\'m playing tennis this afternoon.',
    'It is no good wasting time.',
    'I have a liking for music.',
    'Marry is fond of going to concerts.',
    'He stood there smoking a pipe.',
    'Speaking English well requires a lot of practice.',
    'Boys like playing baseball.',
    'Who is the man walking down the street?',
    'He repents of having been idle in his school days.',
    'Seating myself I began to read.',
    'I saw three people climbing the hill.',
    'Not knowing what to say, I kept silent.',
  ],
}
test_data_2071 = { 

        # **Super category:** Gerunds
        # **Sub category: **gerunds passive
        
  'positive': [
    'I dislike being talked back to.',
    'She is afraid of being arrested by the police.',
    'I\'m afraid of being scolded.',
    'I don\'t like being asked to make a speech.',
    'I like being given a present.',
    'He complained of having been underpaid.',
    'He is ashamed of being scolded by his teacher.',
    'I doubt of their ever having been married.',
    # married->their (dep) を根拠にしていますが、
    # もしかしたら変なのをpositiveにしてしまうかもしれません。
    'I\'m proud of not being scolded by my parents.',
    'The bed showed no sign of having been slept in.',
  ],

  'negative': [
    'I think this article deserves not reading.',
    'We can\'t have them forcing their views on everyone else.',
    'Who\'s the girl not dancing with your brother?',
    'We call that asking for trouble.',
    'I found her not drinking my whiskey.',
    'His careless driving irritates me.',
    'The following day was rainy.',
    'It is going to be marvelous.',
    'A barking dog seldom bites.',
    'I don\'t like swimming.',
    'I’m afraid of his not playing soccer with me.',
    'I\'m playing tennis this afternoon.',
    'I’m sure of his not making mistakes.',
    'It is no good wasting time.',
    'I have a liking for music.',
    'Marry is fond of going to concerts.',
    'Speaking English well requires a lot of practice.',
    'I regret not saying goodbye to you.',
    'Boys like playing baseball.',
    'Who is the man walking down the street?',
    'He repents of having been idle in his school days.',
    'Seating myself I began to read.',
    'I saw three people climbing the hill.',
    'Not knowing what to say, I kept silent.',
    'She is proud of not making mistakes.',
  ],
}
test_data_2072 = { 

        # **Super category:** Infinitives/Gerunds
        # **Sub category: **V doing vs V to do(意味が同じ
        
  'positive': [
    'I have now started to appreciate classical music.',
    'I can\'t stand him advising me all the time.',
    'I propose to study abroad someday.',
    'I prefer him retiring at once.',
    'I love being given a present.',
    'He continues to work hard.',
    'I love to swim.',
    'I hate drawing pictures.',
    'I dislike being talked back to.',
    'She proposed calling off the plan.',
    'He can\'t bear to keep silence.',
    'I don\'t like to be asked to make a speech.',
    'I prefer watching games to playing them.',
    'I hate to discuss user interfaces.',
    # 'Boys like playing baseball.',
    # parser's problem: like is a marker
    'She couldn\'t stand to wait for three hours.',
    'Seating myself I began to read.',
    'She continued reading those documents.',
    'I couldn\'t bear sleeping in the hard bed.',
    'I dislike having tea with him.',
    'Let\'s start talking to friends.',
    'I will begin talking about this topic.',
  ],
  'negative': [
    'I think this article deserves not reading.',
    'I\'m proud of not being scolded by my parents.',
    'We call that asking for trouble.',
    'She is afraid of being arrested by the police.',
    'I\'m afraid of being scolded.',
    'His careless driving irritates me.',
    'The following day was rainy.',
    'It is going to be marvelous.',
    'A barking dog seldom bites.',
    'I’m afraid of his not playing soccer with me.',
    'I\'m playing tennis this afternoon.',
    'I’m sure of his not making mistakes.',
    'It is no good wasting time.',
    'I have a liking for music.',
    'Marry is fond of going to concerts.',
    'The bed showed no sign of having been slept in.',
    'Speaking English well requires a lot of practice.',
    'I regret not saying goodbye to you.',
    'He complained of having been underpaid.',
    'Who is the man walking down the street?',
    'He repents of having been idle in his school days.',
    'Not knowing what to say, I kept silent.',
    'He is ashamed of being scolded by his teacher.',
    'I doubt of their ever having been married.',
    'She is proud of not making mistakes.',
  ],
}
test_data_2073 = { 

        # **Super category:** Infinitives/Gerunds
        # **Sub category: **V doing vs V to do(意味が異なる
        
  'positive': [
    'I tried to skate but fell over at once.',
    'I shall never forget seeing the Queen.',
    'I stopped to smoke.',
    'I meant to call on you, but I couldn\'t.',
    'He stopped speaking and went on to read the letter.',
    'I have stopped smoking.',
    'I regret not saying goodbye to you.',
    'I regret to inform you that my father has died.',
    'Please remember to post this letter.',
    'This new order will mean working overtime.',
    'I tried skating and found it rather hard.',
    'Don\'t forget to write to her.',
    'He went on reading for hours.',
    'I don\'t even remember telling you that.',
    'I want to go on working.',
    'He went on to explain it.',
  ],
  'negative': [
    'I have been sorry and regretting for many years.',
    'I\'ve forgotten her name for the moment.',
    'You must try this sushi.',
    'He deeply regretted what he had said to her.',
    'Go on with your work.',
    'This train doesn\'t stop at small stations.',
    'The party went on until midnight.',
    'She tried her best.',
    'I can\'t remember his name.',
    'The heavy rain stopped the game.',
    'I always remember my mother on Mother\'s Day.',
    'I\'ll remember your kindness forever.',
    'If you forget your password, click here.',
    'Stop a taxi, please.',
    'Things won\'t go on like this now that I\'m the boss.',
    'What do you mean by that?',
    'Her husband\'s death has tried her severely.',
    'Her jacket lay forgotten on the swing.',
    'This present is meant for you.',
    'What does this word mean?',
    'We regret that you have to leave.',
  ],
}
test_data_2074 = {

        # **Super category:** Infinitives/Gerunds
        # **Sub category: **to doing 
        
  'positive': [
    'He is used to waking up early.',
    'Let’s get down to discussing the main topic.',
    'That is the secret to initiating a conversation.',
    'I look forward to seeing you.',
    'He admitted to having a relationship with her.',
    'He faced up to resolving the obstacle.',
    'I\'m committed to visiting there.',
    'When she feels lonely, she resorts to drinking.',
    'I objected to going outside.',
    'When it comes to fishing, he is the best.',
  ],
  'negative': [
    'Sometime in your life, you\'ll have to face up to the responsibility.',
    'Let’s get down to business!',
    'I have a secret desire to go abroad.',
    'I\'ve got much work to do, but I can\'t seem to get down to it.',
    'I\'m looking forward to Saturday!',
    'I have to admit it.',
    'I object to his idea.',
    'He resorts to violence.',
    'She looks to be happy.',
    'He went to Vienna with the object of studying music.',
    'The decision is now generally admitted to have been a great mistake.',
    'The secret to success is keeping your cool.',
    'Be careful not to commit yourself.',
    'I am used to lots of noise.',
    'I’m committed to debt free.',
    'She came running to me.',
    'I came to know him aboard the ship.',
    'He used to wake up early.',
    'That was her only resort.',
    'He faced up to the obstacle.',
    'He admitted having a relationship with her.',
  ],
}
test_data_2075 = {

        # **Super category:** Participles 1
        # **Sub category: **分詞 限定用法
        
  'positive': [
    'He took a picture of the melting snow.',
    'That running man is my cousin.',
    'The man standing over there is the owner of the store.',
    'That is the mansion belonging to my friend.',
    'Look at the plane flying in the sky.',
    'The police are now after the escaped prisoner.',
    'He is reading a book given by his father.',
    'What is the language spoken in Japan?',
    'They found some hidden treasure.',
    'The leaves fallen on the ground were wet and dirty.',
  ],
  'negative': [
    'I will have my hair cut in the afternoon.',
    'I heard her singing the song.',
    'He stood excited about the game.',
    'I found him standing at the door.',
    'He looked pleased with the present.',
    'He sat surprised at the news.',
    'I had the audience laughing.',
    'The baby is fast asleep.',
    # parser's error: something -> burning amod
    # 元のparserならOK
    # 'I smell something burning.',
    'I’ll make myself understood in English.',
    'He heard his name called.',
    'I saw him surrounded by dogs.',
    'He’s alive only to his own interests.',
    'I heard the door opened.',
    'He sat shocked at the news.',
    'I caught him reading my private letters.',
    'I saw him playing tennis.',
    'I saw a man drinking water.',
    'She can get the motorcycle going again.',
    'He looked satisfied with the result.',
  ],
}
test_data_2076 = {

        # **Super category:** Participles 1
        # **Sub category: **分詞 叙述用法

  'positive': [
    'I found him standing at the door.',
    'He looked pleased with the present.',
    'She came running toward me.',
    'I caught him reading my private letters.',
    'He heard his name called.',
    'I must have the wall fixed before it snows.',
    'I saw a man drinking water.',
    'I can’t have you dating the terrible man.',
    'My teacher had me playing the phrase until I mastered it.',
    'He sat surprised at the news.',
    'He sat watching TV.',
    # parser's error: something -> burning amod
    # 元のparserならOK
    # 'I smell something burning.',
    'I kept waiting for him.',
    'I saw him surrounded by dogs.',
    'I heard the door opened.',
    'He sat shocked at the news.',
    'I will have a new dress tailored for my birthday party.',
    'He sat surrounded by dogs.',
    'She had her baby carried to the hospital.',
    'He stood excited about the game.',
    'He stood scolded.',
    'I saw him playing tennis.',
    'I heard her singing the song.',
    'He looked satisfied with the result.',
    'I won\'t have you using my bicycle again.',
  ],
  'negative': [
    'The people questioned gave very different opinions.',
    'I had my friend repair my bicycle.',
    'Seeing the policeman, he ran away.',
    'The man working behind the desk is John.',
    'The classification adopted has lots of advantages.',
    # parser error
    # xcomp
    # 'I telegraphed to Liverpool giving a description of the man.',
    'Mr. Brown is proud of being a working man.',
    'The people singing were students.',
    'He is reading a book given by his father.',
    'Marry said to the yawning nurse, ‘ you can go to sleep if you like.’',
    'He took a picture of the melting snow.',
    'Aroused by the noise, he leaped to his feet.',
    'Seating myself, I began to read.',
    'They found some hidden treasure.',
    'I watched the match because I knew some of the people playing.',
    'That running man is my cousin.',
    'That dog barking furiously is John’s.',
    'A barking dog seldom bites.',
    'Have you seen a flying saucer?',
    'She moved out of the path of the approaching Japanese tour group.',
    'Who is the man wandering down the street?',
    'Left to herself, she began to weep.',
    'Those selected will start to train on Monday.',
  ],
}
test_data_2077 = {

        # **Super category:** Participles 1
        # **Sub category: **分詞 知覚動詞

  'positive': [
    'He saw the window broken by somebody.',
    'I found him standing at the door.',
    'I smell something burning.',
    'I caught him reading my private letters.',
    'I saw a man drinking water.',
    'He heard his name called.',
    'I saw him playing tennis.',
    'I saw him surrounded by dogs.',
    'I heard her singing the song.',
    # 'I heard the door opened.',
    # the pos of 'opend' is VBD
  ],
  'negative': [
    'I’ll have him text you.',
    'I will help you clean up your room.',
    'That running man is my cousin.',
    'She had her baby carried to the hospital.',
    'I will have a new dress tailored for my birthday party.',
    'I can’t have you dating the terrible man.',
    'I will let them enter my room.',
    'I couldn’t get the computer to work.',
    'I made him prepare a bowl of soup.',
    'I had Tom find a restaurant.',
    'My teacher had me playing the phrase until I mastered it.',
    'He looked pleased with the present.',
    'I had my friend repair my bicycle.',
    'My mother made me eat vegetables.',
    'He sat watching TV.',
    'I saw him enter the room.',
    'I must have the wall fixed before it snows.',
    'I kept waiting for him.',
    'He sat shocked at the news.',
    'I won\'t have you using my bicycle again.',
  ],
}
test_data_2078 = {

        # **Super category:** Participles 1
        # **Sub category: **使役動詞 + 分詞

  'positive': [
    'Her mother had her playing the piano.',
    'I had my hair cut.',
    'She had her wallet stolen while she was on the bus.',
    'He got me spoken like him.',
    'I am going to have my car washed tomorrow.',
    'I don\'t want you sitting here all day.',
    'Can you really get that old car going again?',
    'He already had the box opened when we arrived.',
    'I had the wall painted.',
    'I had my car repaired.',
    'I had a suit made.',
    'She made herself understood in English.',
    'I can’t have you dating the terrible man.',
    'My teacher had me playing the phrase until I mastered it.',
    'I won\'t have you using my bicycle again.',
    'She had her baby carried to the hospital.',
  ],
  'negative': [
    'I will help you clean up your room.',
    'I couldn’t get the computer to work.',
    'I don\'t want you to sit here all day.',
    'She made her sister clean the room.',
    'We got the doctor to come.',
    'He looked pleased with the present.',
    'I\'ll let him do so.',
    'I caught him reading my private letters.',
    'I smell something burning.',
    'He sat watching TV.',
    'I\'ll let you know when I get home.',
    'I had John find me a house.',
    'He sat shocked at the news.',
    'He doesn\'t let her drive.',
    'I had my brother paint the wall.',
    'I heard the door opened.',
  ],
}
test_data_2079 = {

        # **Super category:** Participles 2
        # **Sub category: **分詞構文

  'positive': [
    'While reading, I fell asleep.',
    'Living next door, they knew her well.',
    'Talking to strangers, I always feel nervous.',
    'Admitting that you completed it, I can’t trust you.',
    'Seeing a policeman, the thief ran away.',
    'Once having left the premises, you must buy another ticket to re-enter.',
    'I won\'t come until invited properly.',
    'Having a cold, I saw a doctor yesterday.',
    'Going to Tokyo, he watched a baseball game at the stadium.',
    'Having no money, I didn’t buy the book.',
    'Seen from the plane, the island looked like a whale.',
    'Studying hard every day, you’ll pass the exam.',
    'Walking down the street, I found a 1000-yen bill.',
  ],
  'negative': [
    'I heard my name called.',
    'That running man is my cousin.',
    'He sat surrounded by dogs.',
    'I heard him speak English.',
    'I saw him play the piano.',
    'Someone is in that burning house!',
    'His story is boring.',
    'He stood excited about the game.',
    'I saw him crossing the street.',
    'Who is the girl painting a picture over there?',
    'She came running toward me.',
    'He sat surprised at the news.',
    'I saw a lot of excited supporters.',
    'I saw the window opened.',
    'He sat watching TV.',
    'I heard him singing.',
    'It was an exciting game.',
    'He is reading a book given by his father.',
    'The police found the stolen money in the car.',
    'The picture painted by a little girl won the contest.',
  ],
}
test_data_2080 = {

        # **Super category:** Participles 2
        # **Sub category: **完了形の分詞構文

  'positive': [
    'Having seen her before, I couldn’t recall her name.',
    'Having met her, I didn\'t notice her at the party.',
    # 'Having worked until 2 am last night, he must be so sleepy.',
    # parser's problem: ROOT->worked(ROOT)
    'Having finished the work, I am satisfied now.',
    'Having been to France twice, he knows about Paris well.',
    # 'Having overeaten, I can\'t move now.',
    # parser's problem: Having->overeaten(advmod)
    'Having read the book, she returned it to the library.',
    'Having experienced so many deceptions, he is prone to suspect everyone.',
    'Having lived in America for ten years, I can speak English.',
    'Not having been informed, we were completely in the dark.',
    'Having been fat five years ago, she is very beautiful now.',
  ],
  'negative': [
    'Living next door, they knew her well.',
    'Talking to strangers, I always feel nervous.',
    'Tired from a day\'s work, he went to bed as soon as he came home.',
    'Admitting that you completed it, I can’t trust you.',
    'Written in plain Chinese, the book is suitable for a beginner.',
    'Though living next door, I seldom see Susan.',
    'Skiing in Hokkaido, he twisted his ankle.',
    'Living very far from town, she seldom has visitors.',
    'Seeing a policeman, the thief ran away.',
    'Having a cold, I saw a doctor yesterday.',
    'When writing English, I often consult the dictionary.',
    'Going to Tokyo, he watched a baseball game at the stadium.',
    'Seeing this photo, I always remember my school days.',
    'Not knowing what to say, I remained silent.',
    'Having no money, I didn’t buy the book.',
    'Seen from the plane, the island looked like a whale.',
    'A man of responsibility, he didn\'t leave the matter alone.',
    'Liking children as she does, she will surely become a wonderful teacher.',
    'Studying hard every day, you’ll pass the exam.',
    'Walking down the street, I found a 1000-yen bill.',
  ],
}
test_data_2081 = {

        # **Super category:** Participles 2
        # **Sub category: **慣用的な分詞構文

  'positive': [
    'Taking into consideration the fact that she is young, she is doing well.',
    'Considering his age, he looks young.',
    'Anything is possible, provided you have a can-do attitude.',
    'Considering your abilities, you should have done it better.',
    'Judging from the look of the sky, it\'s going to rain.',
    # 'Could you show me how to make my mobile phone ring differently, depending on who\'s calling me?',
    # 'We will start tomorrow, weather permitting.',
    'Strictly speaking, he isn\'t an English teacher.',
    'Speaking of travel, have you ever been to Australia?',
    'Generally speaking, the young are more vital than the elderly.',
  ],
  'negative': [
    'Having met her, I didn\'t notice her at the party.',
    'Living very far from town, she seldom has visitors.',
    'Skiing in Hokkaido, he twisted his ankle.',
    'Seeing the pictures, I remembered my childhood during the war.',
    'Having finished the work, I am satisfied now.',
    'Having been to France twice, he knows about Paris well.',
    'Written in easy English, the book will be read by many people.',
    'The same thing, happening in a large city, would amount to disaster.',
    'Living near my house, he seldom comes to see me.',
    'Tired, I went to bed early.',
    'The storm hit the granary, causing great damage.',
    'Turning to the left there, you will find the factory.',
    'Seeing this photo, I always remember my school days.',
    'Seen from the plane, the island looked like a whale.',
    'Having lived in America for ten years, I can speak English.',
    'Accepting what you say, I still think you are in the wrong.',
    'Foreign investors are active in the Japanese stock market, owning more than 20 percent of the shares of listed companies.',
    'Liking children as she does, she will surely become a wonderful teacher.',
    'Having failed several times, he succeeded at last.',
    'Having been fat five years ago, she is very beautiful now.',
  ],
}
test_data_2082 = {

        # **Super category:** Participles 2
        # **Sub category: **with + 分詞

  'positive': [
    'She was cooking with water running.',
    'He stood in front of us with his arms folded.',
    'She went out of the room with her hair streaming.',
    'He was standing with his eyes shining.',
    'He sat on the sofa with his legs crossed.',
    'The dog sat there with his tongue hanging out.',
    # parser error
    # 'He was walking with his eyes closed.',
    # 'A boy was running, with his dog following him.',
    'He was standing with his arms folded.',
    'He was seated with his legs crossed.',
  ],
  'negative': [
    'Will you be able to meet with me at that time?',
    'She goes to karaoke with me often.',
    'Taking into consideration the fact that she is young, she is doing well.',
    'I am very happy that I could meet with you.',
    'Considering his age, he looks young.',
    'How should we deal with that?',
    'I was glad that I could see the moon together with you.',
    'Please pack that with packaging.',
    'Anything is possible, provided you have a can-do attitude.',
    'Having finished the work, I am satisfied now.',
    'The same thing, happening in a large city, would amount to disaster.',
    'Living near my house, he seldom comes to see me.',
    'I plan on playing tennis with my friend today.',
    'Accepting what you say, I still think you are in the wrong.',
    'Turning to the left there, you will find the factory.',
    'We will start tomorrow, weather permitting.',
    'There are a lot of things that I want to talk about with you.',
    'Strictly speaking, he isn\'t an English teacher.',
    'I want to continue getting along with you.',
    'I like the conversations with you and Jane.',
  ],
}
test_data_2083 = {

        # **Super category:** Comparatives
        # **Sub category: **比較表現 原級

  'positive': [
    'I’ll get in touch with the chief as soon as possible.',
    'Jeff is not as tall as I am.',
    'You should have meals as regularly as possible.',
    'The weather was as nice as it could be.',
    'Gold is not as useful as iron.',
    'You are diligent, but he is several times as diligent as you are.',
    'Toyota Motors produced twice as many cars as Volkswagen.',
    'Conor works as hard as anybody.',
    'My bag is not as big as yours.',
    'Nothing in life could be as dreadful as this.',
    'Gold is not as so useful as iron.',
    'The express train does not travel as so fast as the Shinkansen.',
  ],
  'negative': [
    'The man standing over there is the owner of the store.',
    'As your friend, I feel the need to warn you.',
    'I regard my teacher as a fool.',
    'He came up to me as I was speaking.',
    'As we go up, the air grows colder.',
    'As it was getting dark, we decided to go home.',
    'My father lived like a saint.',
    'Your dog runs faster than Jim’s dog.',
    'My father has finished his beer.',
    'Today is the happiest day of my life.',
    'Jim and Jack are both my friends, but I like Jack better.',
    'The most important thing is to get some sleep.',
    'My father had been repairing the car when I arrived home.',
    'That is the mansion belonging to Mr. Smith.',
    'My aunt is the most beautiful lady in the world.',
    'Hannah is more beautiful than Jonna.',
    'As a young boy, I was a good swimmer.',
    'She can see more clearly with glasses than without them.',
    'Coke is the world’s most popular beverage.',
    'I have found a nicer hotel.',
  ],
}
test_data_2084 = {

        # **Super category:** Comparatives
        # **Sub category: **比較表現 比較級

  'positive': [
    'He likes math better than English.',
    'I am younger than your brother.',
    'Hannah is more beautiful than Jessie.',
    'I have found a nicer hotel.',
    'Jim and Jack are both my friends, but I like Jack better.',
    'Your dog runs faster than Jim’s dog.',
    'They worked harder than anyone else.',
    'Sleeping is more important than taking medicine.',
    'The situation seems more complicated than I thought.',
    'She can see more clearly with glasses than without them.',
  ],
  'negative': [
    'He came up to me as I was speaking.',
    'He is a pitcher in my baseball team.',
    'Coke is the world’s most popular beverage.',
    'Maddy is as smart as her father.',
    'Katie has a talent for making people laugh.',
    'Molly has always been scared of clowns.',
    'As we go up, the air grows colder.',
    'The most important thing is to get some sleep.',
    'Most of the students took a bus to get to school.',
    'The man standing over there is the owner of the store.',
    'You should have meals as regularly as possible.',
    'Gerald bought a new pair of glasses last night.',
    'As a young boy, I was a good swimmer.',
    'Jake is really good at playing golf.',
    'Gold is not as useful as iron.',
    'He is the most popular student in his high school.',
    'My bag is not as big as yours.',
    'Jeff is not as tall as I am.',
    'As it was getting dark, we decided to go home.',
    'My father lived like a saint.',
  ],
}
test_data_2085 = {

        # **Super category:** Superlatives
        # **Sub category: **最上表現 原級

  'positive': [
    'Nothing tastes as good as ice cream.',
    'Nothing is as precious as time.',
    'No other mountain in the world is as high as Mt. Everest.',
    'No one in this beauty saloon is as beautiful as my daughter.',
    'Nothing is as important as one’s health.',
    'No other student in this class is as smart as Billy.',
    'No other state in the United States is as large as Alaska.',
    'Nobody is as rich as Colby.',
    'Nothing is as bad as losing a friend.',
    'No one else in her school is as tall as Jasmine.',
    'No one makes me as frustrated as she does.',
    'No one swims as fast as her.',
  ],
  'negative': [
    'My niece is as sweet as an angel.',
    'Maddy is as smart as her father.',
    'Jeff is not as tall as I am.',
    'Molly has always been scared of clowns.',
    'Hannah is more beautiful than Jessie.',
    'Yuri swims as fast as her mother.',
    'Nobody in my yoga class has been to India.',
    'As it was getting dark, we decided to go home.',
    'No one else in my neighborhood has a dog.',
    'Your dog runs faster than Jim’s dog.',
    'My bag is not as big as yours.',
    'He came up to me as I was speaking.',
    'Sleeping is more important than taking medicine.',
    'Katie has a talent of making people laugh.',
    'The situation seems more complicated than I thought.',
    'My new suitcase is as light as a feather.',
    'They worked harder than anyone else.',
    'As we go up, the air grows colder.',
    'Sandra looks as young as her daughter.',
    'He is the most popular student in his high school.',
  ],
}
test_data_2086 = {

        # **Super category:** Superlatives
        # **Sub category: **最上表現 比較級

  'positive': [
    'Mt. Everest is higher than any other mountain in the world.',
    'Nothing is more important than speaking English.',
    'No one is happier than my mother at this point.',
    'My dog is smarter than any other dog in the neighborhood.',
    'Candice is taller than any other model in the modeling industry.',
    'Millie is prettier than any other girl at her tennis club.',
    'No one is louder than my grandma when she’s angry.',
    'No one is more patient than Alexa, my daughter.',
    'No one is busier than Antony since he has three jobs.',
    'No other mountain in the world is higher than Mt. Everest.',
  ],
  'negative': [
    'John can eat as much as I can.',
    'The situation seems more complicated than I thought.',
    'He likes math better than English.',
    'My score for the biology test was the fifth highest in the class.',
    'Katie has a talent of making people laugh.',
    'Mt. Everest is the highest mountain in the world.',
    'Gerald bought a new pair of glasses last night.',
    'He is the most popular student in his high school.',
    'Carla surprisingly ate the most in the group.',
    'The most important thing is to get some sleep.',
    'The more you know, the more danger you will be in.',
    'Nowadays more and more women are going into politics.',
    'She arrived at the restaurant the earliest of the seven people.',
    'Sleeping is more important than taking medicine.',
    'No other mountain in the world is as high as Mt. Everest.',
    'Their fights are always intense.',
    'She’s desperate and she’s becoming more and more aggressive.',
    'More and more people are playing soccer these days.',
    'The more you think about it, the more anxious you become.',
    'Usain Bolt can run the fastest in the world.',
  ],
}
test_data_2087 = {

        # **Super category:** Superlatives
        # **Sub category: **最上表現 最上級
        
  'positive': [
    'The most important thing is to get some sleep.',
    'The lake is deepest at this point.',
    'The strongest man cannot stop the laws of nature.',
    'This dictionary is by far the most useful of all.',
    'My aunt is the most beautiful lady in the world.',
    'He is happiest when he is left alone.',
    'He is the most sincere man.',
    'Coke is the world’s most popular beverage.',
    'This is the most expensive component in the equipment.',
    'This is the smallest box I’ve ever seen.',
    'He is the most popular student in his high school.',
  ],
  'negative': [
    'I’ve slowly been looking at it more and more positively over the past year.',
    'There are not many choices left anymore.',
    'She became a lawyer after going to graduate school.',
    'The more you know, the more danger you will be in.',
    'Sleeping is more important than taking medicine.',
    'They worked harder than anyone else.',
    'She made them go inside the haunted mansion.',
    'Leslie is more determined than ever.',
    'Jake is really good at playing golf.',
    'Ben is taller than his father now.',
    'Can you give us more information?',
    'Katie has a talent of making people laugh.',
    'Veronica is famous for being a great dancer.',
    'The situation seems more complicated than I thought.',
    'This seems more like an argument than a discussion.',
    'More and more people are playing soccer these days.',
    'My room is larger than hers.',
    'It seems like there are more and more videos every day.',
    'Nowadays more and more women are going into politics.',
  ],
}
test_data_2088 = { 

        # **Super category:** Relative clauses 1
        # **Sub category: **関係代名詞
        
  'positive': [
    'Alexis is a girl whose father is a doctor.',
    'That is the story which my aunt told me.',
    'There is a boy who is running in the park.',
    'The woman who was walking on the street while singing was my mother.',
    'She is a girl who came to my house last week.',
    'Jacob is a boy whom I invited to my birthday party.',
    'The car which crashed into the wall is mine.',
    'The man that lives next door runs his own business.',
    'I want an expensive watch which will last forever.',
    'My psychology professor is the person whom I respect the most.',
  ],
  'negative': [
    'Who do you think will win the election?',
    'Why did you ignore my text message last night?',
    'Who is the man leaning against the wall?',
    'Here comes that smile!',
    'Carla surprisingly ate the most in the group.',
    'I have had enough of your bad attitude.',
    'What happened to be nice to people?',
    'Where did your father fly from?',
    'Candice is taller than any other model in the modeling industry.',
    'Today’s weather is like that of Italy.',
    'Millie is prettier than any other girl at her tennis club.',
    'Of the two methods, this seems to be better than that.',
    'No one is more patient than Alexa, my daughter.',
    'Which movie do you like the best?',
    'No one is busier than Antony since he has three jobs.',
    'I don’t understand why she broke up with Edward.',
    'She’s desperate and she’s becoming more and more aggressive.',
    'More and more people are playing soccer these days.',
    'The more you know, the more danger you will be in.',
    'Usain Bolt can run the fastest in the world.',
  ],
}
test_data_2089 = { 

        # **Super category:** Relative clauses 1
        # **Sub category: **前置詞の目的語になる関係代名詞
        
  'positive': [
    'The jungle in which the tribe lived was full of strange and unusual animals.',
    'I have a female friend whom I get along with so well.',
    'The circumstances which we are born in doesn’t define us.',
    'Charles liked the people with whom he lived.',
    'That is the boy whom I talked with yesterday.',
    'She’s wearing my shirt which I’ve been looking for.',
    'The person with whom he is negotiating is the Chairman of a large company.',
    'It is a club to which many people belong.',
    'He is the man whom we are dependent on.',
    'It was the river in which the children preferred to swim.',
  ],
  'negative': [
    'My psychology professor is the person whom I respect the most.',
    'The woman who was walking on the street while singing was my mother.',
    'That is the story which my aunt told me.',
    'Who is the man leaning against the wall?',
    'What happened to be nice to people?',
    'She is a girl who came to my house last week.',
    'Where is the leaflet that I gave you?',
    'The lady who is standing over there is a tour guide.',
    'Alexis is a girl whose father is a doctor.',
    'Jacob is a boy whom I invited to my birthday party.',
    'This is the water hose that we use.',
    'That is the fish that my grandpa likes.',
    'Here is the paper that I bought for you.',
    'Today’s weather is like that of Malaysia.',
    'This is the silver ring that Mary wants to buy.',
    'The man that lives next door runs his own business.',
    # 'I want an expensive watch which will last forever.',
    # last->forever(advmod)
    'Why did you ignore my text message last night?',
    'The car which crashed into the wall is mine.',
    'Where did your father fly from?',
  ],
}
test_data_2090 = { 

        # **Super category:** Relative clauses 1
        # **Sub category: **関係代名詞の限定用法
        
  'positive': [
    'I have a female friend whom I get along with so well.',
    'She has a brother who has become a doctor.',
    'He is the man whom we are dependent on.',
    # 'She moved to New York in which she studied music.',
    # parser's problem
    'That is the boy whom I talked with yesterday.',
    'The lady who is standing over there is a tour guide.',
    'That is the fish that my grandpa likes.',
    'This is the silver ring that Mary wants to buy.',
    'The jungle in which the tribe lived was full of strange and unusual animals.',
    'It was the river in which the children preferred to swim.',
  ],
  'negative': [
    'Angelina has daughters, who are college students.',
    'I gave him a CD, which I bought yesterday.',
    'Ethiopia, which I love, is a beautiful country.',
    'Prepare yourself for an education, which is demanding, but also really rewarding.',
    'Rosa went to the library with Jane, who you met yesterday.',
    'Larry got married to Anne, whom I haven’t met before.',
    'I bought a book, which is written in Latin.',
    'He has two sons, who are studying macroeconomics.',
    'The event happened in 1976, when I was still a baby.',
    'I used to be a golf caddie, which was funny because I don’t enjoy golf.',
    'She moved to New York where she studied music.',
    'I am working at the supermarket, which is just over the street.',
    'She moved to New York, where she studied music.',
    'She has a brother, who has become a doctor.',
    'She traveled to Osaka, where I went last summer.',
    'Elephants, which I really like, have a good memory.',
    'My father, who lives in Hokkaido, showed me around Sapporo.',
    'My younger sister, who lives in Tokyo, is a rock singer.',
    'I got a high score on the test, which encouraged me a lot.',
    'I went to the hotel early, which was a great choice.',
    'Glasgow, where I lived, always rains.',
  ],
}
test_data_2091 = { 

        # **Super category:** Relative clauses 1
        # **Sub category: **関係代名詞の非限定用法
        
  'positive': [
    'Larry got married to Anne, whom I haven’t met before.',
    # 'I am working at the supermarket, which is just over the street.',
    'My father, who lives in Hokkaido, showed me around Sapporo.',
    'Rosa went to the library with Jun, who you met yesterday.',
    'Glasgow, in which I lived, always rains.',
    'I gave him a CD, which I bought yesterday.',
    'He has two sons, who are studying macroeconomics.',
    'I got a high score on the test, which encouraged me a lot.',
    # 'She moved to New York, which she studied music in.',
    'She has a brother, who has become a doctor.',
  ],
  'negative': [
    'That is the boy whom I talked with yesterday.',
    'The lady who is standing over there is a tour guide.',
    'Mike is the person who told me the truth.',
    'I want an expensive watch which will last forever.',
    'He is the man whom we are dependent on.',
    'She lives in a house that has a red door.',
    'She has an uncle who lives in London.',
    'It was the river in which the children preferred to swim.',
    'The recipe book that my grandmother used is special to me.',
    'I need a dress that I can wear to a wedding.',
    'The car which crashed into the wall is mine.',
    'That is the fish that my grandpa likes.',
    'He is my father who is thirty years old.',
    'She moved to New York, where she studied music.',
    'Reese has a sister who often writes to her.',
    'I envy people whose jobs are also their hobbies.',
    'I have a female friend whom I get along with so well.',
    'Here are the photos that were taken by Miranda.',
    'This is the silver ring that Mary wants to buy.',
    'The jungle in which the tribe lived was full of strange and unusual animals.',
    'My psychology professor is the person whom I respect the most.',
    'Glasgow, where I lived, always rains.',
  ],
}
test_data_2092 = {

        # **Super category:** Relative clauses 2
        # **Sub category: **関係副詞
        
  'positive': [
    'There are times when I wonder why I like her.',
    'This is where the accident happened.',
    'This is where we used to play.',
    'Tell me when you came back home.',
    'It was on the day when motorcars were rare.',
    'This is a case where practice makes perfect.',
    'Tell me the reason why you were absent yesterday.',
    'Could you tell me the bank where I can change money？',
    'The reason why he did it is unknown.',
    '1979 is when I was born.',
    'This is the mansion where Mr. and Mrs. Johnson lived.',
    'This happened during the time when you were away.',
    'This is the reason why this book sells well',
    'This is how we learn English.',
    'That\'s where you come in.',
    'Now is when they need you most.',
    'May I ask you why you quit your previous job?',
    'This is how he got through the crisis.',
    'You can go where you like.',
    'Where there’s a will, there’s a way.　',
    'I went to Paris, where I stayed for three days.',
    'Please call again at ten o’clock, when the boss will be back.',
  ],
  'negative': [
    'He is the man who I met in the library yesterday.',
    'This is the only pen that I have right now.',
    'The guy whose fly was open talked eloquently.',
    'He is a teacher who lives in New York.',
    'The girl who is playing the guitar over there is my sister.',
    'I want a watch which will last forever.',
    'I have a friend whose father is a singer.',
    'The woman who was walking on the street while singing was my mother.',
    'I want to have the dog which was there at that time.',
    'The car which crashed into the wall is mine.',
    'We saw a lot of people and cars that were leaving this town.',
    'I understand the thing which you said at that time.',
    'The man that lives next door runs his own business.',
    'I want to have the dog that I saw there at that time.',
    'I\'m sorry, but I\'ve lost the book which you lent me.',
    'She is the person whom I respect the most.',
    'They used some terms whose meanings I didn’t know.',
    'This is the house which he lives in.',
    'This is what we wanted to know.',
    'I know the girl whom you like.',
  ],
}
test_data_2093 = {

        # **Super category:** Relative clauses 2
        # **Sub category: **関係副詞の限定用法
        
  'positive': [
    'This is the reason why this book sells well.',
    'That is the park where I often went in my childhood.',
    'The accident happened during the time when you were away.',
    'I went to the park where I saw a suspicious person.',
    'I came home at night when my wife opened the door.',
    'Please let me know the exact date when he will return.',
    'I stayed at the hotel where you had stayed two years ago.',
    'This is the house where Tom used to live in.',
    'The is the mansion where Mrs. Robinson lives.',
    'The reason why he had resigned remained unknown.',
  ],
  'negative': [
    'How about having dinner at the restaurant in that hotel, where the food is good and the prices are reasonable?',
    'I went to the movie theater, where I lost my wallet.',
    'Larry got married to Anne, whom I haven’t met before.',
    'The author’s house in London, where he wrote many stories, has recently been repaired.',
    'Our family moved to Washington, where we lived for seven years.',
    'My father, who lives in Hokkaido, showed me around Sapporo.',
    'I went to the park, where I saw a suspicious person.',
    'This morning Holly got on a bus, where she happened to meet her old friend.',
    'We came to a fountain, where we rested for a short while.',
    'The ship drifted for a week, where the crew was rescued.',
    'Please call again at ten o’clock, when the boss will be back.',
    # 'I was about to go out when he came to visit me.',
    'I went to Nagasaki, where I stayed for three weeks.',
    'He went to Europe, where he got married to an Italian woman.',
    'He has two sons, who are studying macroeconomics.',
    'We got up at six, when I took a shower.',
    'I got a high score on the test, which encouraged me a lot.',
    'Samuel visited me yesterday, when I went out.',
    'I went to Fukushima, where I met my friends.',
    'Glasgow, where I lived, always rains.',
  ],
}
test_data_2094 = {

        # **Super category:** Relative clauses 2
        # **Sub category: **関係副詞の非限定用法

  'positive': [
    'I went to the park, where I saw a suspicious person.',
    'Our family moved to Washington, where we lived for seven years.',
    'I went to Italy, where I had lunch.',
    'Alex went to Paris by train, where she took a plane to London.',
    'I went to Rome, where I saw many buildings.',
    'We got up at six, when I took a shower.',
    'Samuel visited me yesterday, when I went out.',
    'She went camping last weekend, when it was freezing.',
    'I came home at night, when my wife opened the door.',
    'I went to Fukushima, where I met my friends.',
    'She moved to New York, where she studied music.',
  ],
  'negative': [
    'Now is the time when they need you most.',
    'The is the mansion where Mrs. Robinson lives.',
    'The recipe book that my grandmother used is special to me.',
    'She has a brother, who has become a doctor.',
    'I am working at the supermarket, which is just over the street.',
    'This is how we learn Chinese.',
    'Rosa went to the library with Jun, who you met yesterday.',
    'That is the park where I often went in my childhood.',
    'That is the boy whom I talked with yesterday.',
    'The reason why he had resigned remained unknown.',
    'Mike is the person who told me the truth.',
    'You can go where you like.',
    'This is how he got through the crisis.',
    'Please let me know the exact date when he will return.',
    'The last time that I saw him, he was in good health.',
    'The jungle in which the tribe lived was full of strange and unusual animals.',
    'I stayed at the hotel which you had stayed for two years before.',
    'It was the river in which the children preferred to swim.',
    'May I ask you why you quit your previous job?',
  ],
}
test_data_2095 = {

  # **Super category:** Relative clauses 2
  # **Sub category: **関係副詞の目的格の省略

  'positive': [
      'Do it how you can.',
      'This is where I live.',
      'He\'s changed a great deal from when I used to know him.',
      'When the cherry blossoms come out is a lovely time of year.',
      'Sunday is when I am free.',
      'That\'s why I came.',
      'That\'s how he did it.',
      'I\'ll take you where we shall get a better view.',
      'Tell me why you were late.',
      'That\'s how the accident happened.',
      'Where he is weakest is in his facts.',
      'This is how he got through the crisis.',
      'This is how we learn Chinese.',
      'May I ask you why you quit your previous job?',
      'You can go where you like.',
  ],
  'negative': [
      'Samuel visited me yesterday, when I went out.',
      'She moved to New York, where she studied music.',
      'Now is the time when they need you most.',
      'I went to Italy, where I had lunch.',
      'Alex went to Paris by train, where she took a plane to London.',
      'I am working at the supermarket, which is just over the street.',
      'That is the park where I often went in my childhood.',
      'I came home at night, when my wife opened the door.',
      'She has a brother, who has become a doctor.',
      'The jungle in which the tribe lived was full of strange and unusual animals.',
      'I stayed at the hotel which you had stayed for two years before.',
      # 'Please let me know the exact date when he will return.',
      'The is the mansion where Mrs. Robinson lives.',
      'I went to Rome, where I saw many buildings.',
      'She went camping last weekend, when it was freezing.',
      'It was the river in which the children preferred to swim.',
      'Our family moved to Washington, where we lived for seven years.',
      'I went to Fukushima, where I met my friends.',
      'I went to the park, where I saw a suspicious person.',
      'Rosa went to the library with Jun, who you met yesterday.',
      'The last time that I saw him, he was in good health.',
      'The recipe book that my grandmother used is special to me.',
      'Mike is the person who told me the truth.',
      'The reason why he had resigned remained unknown.',
      'We got up at six, when I took a shower.',
      'That is the boy whom I talked with yesterday.',
  ],
}
test_data_2096 = {

        # **Super category:** Relative clauses 3
        # **Sub category: **複合関係代名詞
        
  'positive': [
    'Whatever happens, we must be calm.',
    'I can’t believe you whatever you may say.',
    # parser error keep -> it nsubj
    # TODO: This sentence is not a wh question.
    # 'Whoever finds it may keep it.',
    'Whoever it is, I don\'t want to see them.',
    'They ate whatever food they could find.',
    'I want to buy whatever things you have.',
    # parser error comes -> wins nmod:in
    # TODO: This sentence is not a wh question.
    # 'Whichever of you comes in first wins.',
    'I\'ll do whatever you want.',
    'I’ll try to get whatever you want.',
    'I want to borrow whichever CDs you have.',
    'Whichever you choose, make sure you don’t regret your choice.',
    'We employ whoever wishes to work with us.',
    'You can give the present to whomever you like.',
    'Don’t open the door whoever may come.',
    'Please take whichever card you want.',
  ],
  'negative': [
    'Anyone of you that comes in first wins.',
    'Whenever it is possible, I walk to the station.',
    'Go wherever he tells you to go.',
    'However much he eats, he never gets fat.',
    'They ate any food that they could find.',
    'My mind, however, didn’t change.',
    'However you do it, the result will be the same.',
    'I don’t care however late you are.',
    'However fast you may run, you can’t beat me.',
    'No matter who it is, I don\'t want to see them.',
    'An artist goes wherever there is work.',
    'Wherever you may go, I won’t forget about you.',
    'Whenever I go to Las Vegas, I always stay at the same hotel.',
    'Whenever I see him, he smiles at me.',
    'Sit wherever you like.',
    'My daughter followed me wherever I went.',
    'Whenever I hear that song, I think of you.',
    'Anybody that finds it may keep it.',
    'Wherever you are, you must do your best.',
    'I\'ll do anything that you want.',
    'I am determined to reach my goal, however long it takes.',
    'The novel, however interesting it is, is not good for children.',
    'Whenever I saw you, you were hungry.',
    'However rich you are, you must not be lazy.',
    'Martin’s parents took him wherever they went and never let him go to stay home.',
    'Whatever is he doing with that rod?',
  ],
}
test_data_2097 = { 

        # **Super category:** Relative clauses 3
        # **Sub category: **複合関係副詞
        
  'positive': [
    'I’ll give you some advice whenever you need me to.',
    'However much you succeed, you have to continue your effort.',
    'I don’t care however late you are.',
    'Do it however you like.',
    'I’ll take you wherever you want to go.',
    'My daughter followed me wherever I went.',
    'Whenever I call on him, he is absent.',
    'However much he gives her, she wants more.',
    'Whenever I saw you, you were hungry.',
    'Wherever you may go, I won’t forget about you.',
    'Wherever you are, I think of you all the time.',
    'Sleep wherever you like.',
    'Wherever you go, you\'ll find that sign.',
    'Whenever I see him, he smiles at me.',
  ],
  'negative': [
    'You may do whatever you like this afternoon.',
    'My son is innocent, whatever you think.',
    'At any time when I saw you, you were hungry.',
    'You can have whichever doll you like best.',
    'No matter when I call on him, he is absent.',
    'You can meet whoever wants to meet you.',
    'Do it in whatever way that you like.',
    'Whichever you buy, new computers will be sold soon.',
    'I want to borrow whichever CDs you have.',
    'I’ll try to get whatever you want.',
    'We employ whoever wishes to work with us.',
    'Whichever you may get you must give it to your sister.',
    'Whoever calls on me, tell them I am out.',
    'Whatever has a beginning also has an ending.',
    'She is whatever the majority of men regard pretty.',
    'Whatever he says I will do it by myself.',
    'No matter how much he gives her, she wants more.',
    'Whatever may happen you need not worry.',
    'Don’t open the door whoever may come.',
    'Whichever wins, he will be satisfied.',
    'Whoever you may see, you must not talk to him.',
    'Whatever happens, we must be calm.',
    'You may tell whoever wants to know about it.',
    'No matter where you go, you\'ll find that sign.',
    'I didn’t want to go to the party; however, I went.',
    'Sleep at any place where you like.',
    'I’ll buy the car, whatever the cost.',
  ],
}
test_data_2098 = { 

        # **Super category:** Subjunctive mood 1
        # **Sub category: **条件文 0(if S Vp, S Vp)
        
  'positive': [
    'If it rains, humidity becomes higher.',
    'If you cool water down, it freezes.',
    'An object falls to the ground if it is in the air.',
    'If time goes by, buildings decay.',
    'If I am a coward, you are another.',
    'If I drink alcohol, I get drunk.',
    'If you heat ice, it melts.',
    'If you expose the paper to sunlight, it tans.',
    'If it rains, the grass gets wet.',
    'If you are under 15 years old, the entrance fee is free.',
  ],
  'negative': [
    'If it rains today, you will get wet.',
    'If it‘s true, I will never see him again.',
    'If I were you, I would apologize to him.',
    'If it rains tomorrow, I won\'t go out.',
    'If only there were forty-eight hours in a day!',
    'As if I didn’t know that already!',
    'If you have any trouble, please contact me.',
    'If I find your sunglasses, I will keep it.',
    'If I spoke Italian, I would be work in Italy.',
    'If I had worked harder at school, I would have a better job now.',
    'If you don\'t hurry, you will miss the train.',
    'If you don\'t have your ID card, you won\'t be able to pay by check.',
    'If I were a superman, I could help you.',
    'If it had rained, you would have gotten wet.',
    'If I had accepted the promotion, I would have been working in Millan.',
    'If he was sick, why didn\'t you take him to a hospital?',
    'If you went to bed earlier, you would not be so tired.',
    'If I were not busy, I could do it now.',
    'If you are hungry, I will cook lunch right now.',
    'If you weren\'t afraid of spiders, you would have picked it up and put it outside.',
  ],
}
test_data_2099 = { 

        # **Super category:** Subjunctive mood 1
        # **Sub category: **条件文1 (if S Vp, S Vf)
        
  'positive': [
    'If it rains today, you will get wet.',
    'If it‘s true, I will never see him again.',
    'If it rains tomorrow, I won\'t go out.',
    'If I find your sunglasses, I will keep it.',
    'If you don\'t have your ID card, you won\'t be able to pay by check.',
    'If you don\'t hurry, you will miss the train.',
    'If it is rainy tomorrow, the athletic meet will be postponed.',
    'I will go shopping if I have free time tomorrow.',
    'If you study hard now, you will do well on the test.',
    'If you are hungry, I will cook lunch right now.',
  ],
  'negative': [
    'If I were you, I would apologize to him.',
    'If you have any trouble, please contact me.',
    'If I were a superman, I could help you.',
    'If I had accepted the promotion, I would have been working in Millan.',
    'I wish I had been born in the moon.',
    'If it rains, the grass gets wet.',
    'If I were not busy, I could do it now.',
    'If only there were forty-eight hours in a day!',
    'If you cool water down, it freezes.',
    'If I am a coward, you are another.',
    'If you heat ice, it melts.',
    'If he was sick, why didn\'t you take him to a hospital?',
    'If you are under 15 years old, the entrance fee is free.',
    'If you weren\'t afraid of spiders, you would have picked it up and put it outside.',
    'If it rains, humidity becomes higher.',
    'If I spoke Italian, I would be work in Italy.',
    'An object falls to the ground if it is in the air.',
    'If I had worked harder at school, I would have a better job now.',
    'If I drink alcohol, I get drunk.',
    'If it had rained, you would have gotten wet.',
    'If you went to bed earlier, you would not be so tired.',
  ],
}
