test_data_1000 = { 

      # **Guideword:** 'THE ONE(S) THAT', FOR FOCUS
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** substitution, one, ones, none
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'The one(s) that' + clause in subject position, for focus. ► focus
        
  'positive': [
    'The one that we want is not found elsewhere.',
    'The one that is particularly cute is that kid.',
    'The one that she liked was Kevin’s painting.',
    'The one that became the largest is Martin’s company.',
    'The one that got her attention was Leslie’s performance.',
    'The one that got away is always bigger.',
    'The one that sold the most is that song.',
    'The one that I requested was not there.',
    'The one that became most popular is Laura’s song.',
    'The one that drew that picture is him.',
  ],
  'negative': [
    'Who is the one that I loved before?',
    'It seems that no one knows the truth.',
    'He is the master that one once served under.',
    'Kindness is a characteristic that one has had from birth.',
    'I’m the one who\'s supposed to say that.',
    'It is an image of Buddha that one can see and feel',
    'One hand is stronger and used more than the other',
    'The one who caught that fish was me.',
    'This house is the double of that one.',
    'The weather is all that one can desire.',
    'The last word that one speaks in life is important.',
    'It\'s such a good feeling to let one\'s hair down.',
    'I think that the method is the best one.',
    'The one who sang that was him.',
    'She is the one that drove your car last week.',
    'The mountain that we climbed was that one.',
    'I will take the one that is more expensive.',
    'That was one of the causes of the incident.',
    'That is one of the inevitabilities of history.',
    'That is one of the big towns in America.',
  ],
}
test_data_1001 = { 

  # **Guideword:** OBJECT
  # **Guideword type:** FORM
  # **Super category:** PRONOUNS
  # **Sub category:** indefinite - thing, -one, -body etc
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of indefinite pronouns as objects. 
    
  'positive': [
    'I know everyone in this library.',
    'My mother knows everything about me.',
    'I have someone who I can trust.',
    'I would like to have something to eat.',
    'My sister doesn\'t have anyone who can go to the library with her.',
    'I have nothing to do now.',
    'She can do everything she wants.',
    'I don\'t know anybody in this room.',
  ],
  'negative': [
    'There is nowhere around this area for sightseeing.',
    'I looked everywhere, but I couldn\'t find it.',
    'He wants to go somewhere next month.',
    # weblioに拠ると***whereは副詞なので、目的語とは取れない
    'Everyone is looking at you.',
    'Someone is sleeping in my bed.',
    'Something might happen over there.',
    'Is anyone in this room?',
    'No one can do better than you.',
    'You go to school for nothing.',
    'If something happens, just let me know.',
    'I want to work for someone who needs help.',
    'Everything can be right for you.',
    'Everything has been changed since I left here two years ago.',
    'Something is wrong here.',
    'Nobody noticed what is going on here.',
    'Anything that anyone points to as showing otherwise is merely a symptom of the bigotry prevalent in that culture.',
    'Everywhere was filled with people on that day.',
    'I have to take drugs to feel that happy about anything.',
    'Somewhere out in the spaces, we can not touch, you have found the words of my dad.',
    'Someone gave me this book.',
    'I won\'t tell your secret to anyone.',
    'Couldn\'t somebody help me, please?',
    'Somewhere would be much better than this place.',
  ],
}
test_data_1002 = { 

  # **Guideword:** 'EVERYTHING', SUBJECT
  # **Guideword type:** FORM
  # **Super category:** PRONOUNS
  # **Sub category:** indefinite - thing, -one, -body etc
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'everything' as subject, with a singular verb. 
    
  'positive': [
    'Everything is quiet here.',
    'Everything has changed since I left here two years ago.',
    'Everything is going to be okay.',
    'I know that everything looks great here.',
    'Everything will work out.',
    'Everything I\'ve read goes along similar lines.',
    'Everything is a good memory.',
    'I hope everything will work out fine.',
    # 'It seems like everything is wrong.',
    # parser error
    # 前のparser orderならOK
    'Everything about you is fake.',
  ],
  'negative': [
    'Something might happen over there.',
    'If something happens, just let me know.',
    'Something is wrong here.',
    'Something I don\'t want is coming.',
    'I hope something brings him here.',
    'Anything that anyone points to as showing otherwise is merely a symptom of the bigotry prevalent in that culture.',
    'Anything you might have is useless.',
    'Is there anything interesting?',
    'You can do anything if you want.',
    'My mother knows everything about me.',
    'She did everything she could think of.',
    'I used everything for looking for my sister.',
    'I will buy everything in this store.',
    'Do your parents know everything about what happened last night?',
    'Now you can see everything in this world.',
    'I did everything I could do to graduate from this university.',
    'Just do everything you want to do in the future.',
    'I know something about Hannah.',
    'She knows nothing about this issue.',
    'I can do anything if you want me to.',
  ],
}
test_data_1003 = { 

      # **Guideword:** OBJECT OR COMPLEMENT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** 2.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use an increasing range of indefinite pronouns as objects or complements of prepositions. 
        
  'positive': [
    'She called someone to help her.',
    'I don\'t have anyone who I can invite.',
    'Do you know anyone who can play baseball?',
    'Do you have the CD "The search for everything?"',
    'I don\'t want anything for now.',
    'I need someone who I can trust.',
    'I need everyone to help with my work.',
    'Do you know anybody who can come here in an hour?',
    'I can bring someone for the next game.',
    'I need somebody who I can consult about this issue.',
    'He invited everybody in the class to the party.',
    'I want something to drink.',
    'You can take everyone to the class.',
    'She wants to talk with everyone here.',
    'I want everyone to come to the party.',
  ],
  'negative': [
    'I don\'t want any for now.',
    'Anything will do.',
    'Does anyone know what is going on?',
    'Somebody talked about that issue.',
    'Someone knew the truth before.',
    'Everybody made up their mind.',
    'Everything he said is true.',
    'Everyone loves cats and dogs.',
    'Something about him annoyed me.',
    'Does anyone go to watch the movie with me?',
    'Everyone has their own laptop.',
    'Everyone didn\'t come to the party.',
    'Someone call the police.',
    'Everyone go home now.',
    'Does anyone want to study with us?',
    'Everyone likes to play baseball.',
    'Bill can do it if anybody can.',
    'Everyone is going to work tomorrow.',
    'Everyone calls me Mike.',
    'Everyone already got home safe.',
    'Someone came to your house yesterday.',
    'Everyone plays football in Japan.',
    'Would anyone like to join us?',
    'Does anyone know the truth?',
    'Somebody told you fake information.',
    'Everyone lives near here.',
  ],
}
test_data_1004 = { 

      # **Guideword:** SUBJECT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of indefinite pronouns ('someone', 'everyone') as subjects, with a singular verb. 
        
  'positive': [
    'Everyone goes home now.',
    'Someone came to your house yesterday.',
    'Someone talked about that issue.',
    'Everyone plays football in Japan.',
    # 'Everyone play football in Japan.',
    # football->Everyone(compound)
    'Everyone loves cats and dogs.',
    'Someone told you fake information.',
    'Everyone likes to play baseball.',
    'Everyone has their own laptop.',
    'Everyone is going to work tomorrow.',
    'Someone knew the truth before.',
    'Everyone calls me Mike.',
    'Everyone lives near here.',
    'Everyone already got home safe.',
    'Everyone didn\'t come to the party.',
    'Someone is calling the police.',
  ],
  'negative': [
    'She called someone to help her.',
    'She will tell someone about the issue.',
    'I don\'t have anyone who I can invite.',
    'I will do anything for this company.',
    'Does he know anyone who can help?',
    'Somebody talked about that issue.',
    'I can bring someone for the next game.',
    'I need somebody who can consult about this issue.',
    'He can help someone who needs help.',
    'I want someone who can stay with me.',
    'You can take everyone to the class.',
    'I can see everyone from here.',
    'I can take someone to my house.',
    'Everybody made up their mind.',
    'Everything he said is true.',
    'I can tell everyone about your secret.',
    'I need someone who can teach me English.',
    'Do you know anyone who can play baseball?',
    'Do you have the CD "The search for everything?"',
    'I need everyone to help with my work.',
    'Something about him annoyed me.',
    'Does anyone go to watch the movie with me?',
    'She wants to talk with everyone here.',
    'She will tell someone about tomorrow\'s event.',
    'Does anyone want to study with us?',
    'Do you know anybody who can come here in an hour?',
    'Bill can do it if anybody can.',
    'He invited everybody in the class to the party.',
    'I want everyone to come to the party.',
    'I should bring someone for the baseball game.',
    'I don\'t want anything for now.',
    'I need someone who I can trust.',
    'I want something to drink.',
    'Somebody told you fake information.',
    'Does anyone know the truth?',
    'Does anyone like to join us?',
    'She needs to bring everyone on the trip.',
  ],
}
test_data_1005 = { 

      # **Guideword:** NEGATIVE + 'ANYTHING'
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'anything' after a negative verb form. 
        
  'positive': [
    'I thought that he didn\'t find anything nice.',
    'We cannot say anything about the project yet.',
    'Charlie is not getting anything yet.',
    'I am especially intrigued by the fact that the dog didn\'t bring anything edible.',
    'How did you not get anything out of the event?',
    'Didn\'t you find anything in particular?',
    'She doesn\'t have anything to say.',
    'They didn\'t bring anything to the event.',
    'I don\'t need to find anything blue.',
    'They could not find anything to eat for dinner that night.',
  ],
  'negative': [
    'I don\'t have anyone who can invite.',
    'Anything will do.',
    'Where did you go to the meeting?',
    'Did you hear that something happened to him?',
    'It is getting so humid lately.',
    'Is it true that they didn\'t attend the class?',
    'They think it is not something to worry about.',
    'I want to eat something sweet.',
    'Is there anything I can do to help you?',
    'It is true that something gold brings money to you?',
    'What is the true benefit of having something fun to do?',
    'Is she doing anything bad for her?',
    'Where have you been till this late?',
    'I want something to eat for lunch.',
    'Is there anything you can do to let the kids have fun?',
    'I did not mean to do so.',
    'We have been waiting for you, but you did not show up after all.',
    'She does not like it that we are trying to find the treasure.',
    'You definitely need to find something fun.',
    'When are you going to live in Toronto?',
    'There is this guy coming named Charlie.',
    'I started sweating at the moment.',
  ],
}
test_data_1006 = { 

      # **Guideword:** WITH ADJECTIVE, SPECIFYING
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can modify 'something' or 'anything' with an adjective, to make it more specific.
        
  'positive': [
    'Do you need anything tasty for dinner?',
    'You need to get approval to get something specific for the event.',
    'How did you find something fun to do here?',
    'They do not need anything golden for the party.',
    'Where would you go to get something festive?',
    'I didn\'t bring anything formal for the party.',
    'I need something new to wear.',
    'What is something special that you brought with you?',
    'Could you find something expensive to wear for the party?',
    'You need to wear something comfortable.',
  ],
  'negative': [
    'They said they did not expect anything, which turned out to be true.',
    'They promised me that they would bring something.',
    'Where is it that I can find the best Mexican food here?',
    'You all need to get something for the classes.',
    'The only place I feel free is here.',
    'Did you hear him singing in such a beautiful voice?',
    'Have you ever used the airport in Toronto?',
    'They have some real food here.',
    'Skip anything that gets in the way and get things done by 9.',
    'Who wants to get a mattress?',
    'Last time I saw them, they were playing a video game.',
    'Do you believe in Santa Clause?',
    'A chicken patty is a little spicier than a beef patty.',
    'Have you finished anything yet?',
    'He went for a walk last night, but he has not come up with something to do for the holidays.',
    'How long have you been spending your time hanging around here?',
    'There are some things I want to get done before the end of this month.',
    'We did not catch what they said at the end of the speech.',
    'Brokaw is the second oldest dorm in the school, which is quite something.',
    'The reality may be more complicated than anything we can imagine.',
  ],
}
test_data_1007 = { 

      # **Guideword:** WITH 'TO' INFINITIVE, SPECIFYING
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can modify 'something' or 'anything' with 'to' infinitive, to make it more specific.
        
  'positive': [
    'Do you need anything to eat for dinner?',
    'You need to wear something to show respect.',
    'They do not need anything to drink for the party.',
    'I didn\'t bring anything to wear that\'s formal for the party.',
    'Where did you go to get anything to celebrate it?',
    'You need to have the approval to get something to bring to the event.',
    'What did you bring as something to drink?',
    'How did you find something to do here?',
    'Could you find something to wear for the party?',
    'Do they need something to wear right now?',
  ],
  'negative': [
    'You forgot to take me for a walk last night, and I am a little angry about it.',
    'They gave something to him.',
    'I have been wondering about the same issue since last night.',
    'They won\'t give anything to me.',
    'You need to finish eating right now.',
    'Something went wrong with this machine.',
    'It is important to find the effective strategy.',
    'What happens if there are more than three people here?',
    'Have you found some solutions yet?',
    'Some people say it is important to have a big goal for the future.',
    'It is difficult to make some true friends.',
    'What kind of future do you see with this product?',
    'Isn\'t it funny that there are so many people in this country with no entertainment?',
    'Did you hear anything new from her at all?',
    'What do you think about the issue?',
    'Would you mind buying something fancy for me?',
    'I thought it might be a matter of time if they can finish something big and innovative.',
    'How did you find anything for the party?',
    'I did not find the best solution, but I will keep trying.',
    'How do you know about this organization?',
  ],
}
test_data_1008 = { 

      # **Guideword:** WITH 'ELSE'
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use indefinite pronouns with 'else'.
        
  'positive': [
    'Did you want anything else?',
    'Don\'t cut in when someone else is speaking.',
    'I have heard nothing else from him yet.',
    'She had nothing else to drink.',
    'I have something else to do.',
    'I\'ll get the traders to exchange that for something else.',
    'I can\'t do anything else.',
    'Please have someone else do it.',
    'Is there something else that I have to change?',
    'We\'ve had nothing else this week.',
  ],
  'negative': [
    'I never knew there could be anything so special.',
    'I have something particular in mind.',
    'I have something to do right after school.',
    'I think something happened to him.',
    'He never leaves anything to chance.',
    'I need to get something off my chest.',
    'Don\'t do anything stupid.',
    'We should do something nice for them.',
    'Why didn\'t he say anything to me?',
    'I don\'t think we can do anything for him.',
    'Shall we eat something?',
    'Is there anything wrong with that?',
    'I have to say I don\'t know anything about it.',
    'Is there anything to eat in the fridge?',
    'He is either braver than others or else he is just silly.',
    'I don\'t hold anything against him.',
    'She wants to sell something new to our customers.',
    'I want to drink something.',
    'I felt something unusual.',
    'Is anything broken?',
    'What else can I do?',
    'I have something to tell you.',
  ],
}
test_data_1009 = { 

      # **Guideword:** 'SOMETHING' IN VAGUE EXPRESSIONS
      # **Guideword type:** USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'something' in vague expressions, to refer to things in a non-specific way. 
        
  'positive': [
    'Do you want to see a movie or something?',
    'Maybe she’s cleaning the bathroom or something.',
    'She was his grandmother\'s grandmother or something.',
    'He is a lawyer or something.',
    'Are you going on a trip or something over the vacation?',
    'The castle was flinging oil or pitch or something.',
    'I heard he was a cripple or something of the sort.',
    'We\'ll need bread or oatcakes or something.',
    'He works as an investment banker or something like that.',
    'After the concert, we can have a pizza or something else.',
    'I need a change in my life or something.',
  ],
  'negative': [
    'I didn\'t have anything to eat,',
    'Is there anything in particular you need?',
    'I need something to eat right now.',
    'I didn\'t want to do anything.',
    'If there is anything unclear, please contact me.',
    'Nothing is impossible.',
    'I don\'t have anything to hide.',
    'They have nothing to drink.',
    'Health comes before everything else.',
    'You can do nothing.',
    'I want something hot.',
    'Something is missing.',
    'There is little else to go on.',
    'Would you like something to drink?',
    'Is anyone else coming?',
    'I have nothing to say.',
    'I want nothing special.',
    'Everybody else followed suit.',
    'She wants something special for her birthday.',
    'I do not have anything else to tell you about.',
    'There isn\'t anything I\'d like to eat.',
    'Do you want anything else?',
    'I can tell you something special.',
    'I will use that for something else.',
    'I want to drink something cold.',
    'Everyone else is waiting.',
    'I have something to tell you.',
    'Something has come between the two.',
    'She needs to drink something hot.',
    'Give me something cold to drink.',
  ],
}
test_data_1010 = { 

      # **Guideword:** SUBJECT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of indefinite pronouns ('something', 'nobody') as subjects, with a singular verb. 
        
  'positive': [
    'Nobody can take your place.',
    'Something happened over there.',
    'Something made him do such a stupid thing.',
    'Nobody can surpass him.',
    'Something is wrong with him.',
    'Nobody will be the wiser.',
    'Nobody can play tennis.',
    'Nobody hates him.',
    'Something is going on here.',
    'Something is strange.',
  ],
  'negative': [
    'There is nobody I love more than you.',
    'Do you have something to drink?',
    'I want to drink something.',
    'Anybody would be better than nobody.',
    'Everybody\'s business is nobody\'s business.',
    'I felt something unusual.',
    'Shall we eat something?',
    'The defendant said something.',
    'There was nobody in the house.',
    'I woke up to find nobody there.',
    'I was lonely, with nobody to play with.',
    'You said something, but I couldn\'t catch it.',
    'She knows something about him.',
    'I need something cold right now.',
    'It\'s nobody else\'s fault.',
    'I see nobody on the road.',
    'Is there nobody that you are dating right now?',
    'There is something funny about him.',
    'I think I\'ll draw something.',
    'I saw nobody around.',
  ],
}
test_data_1011 = { 

      # **Guideword:** OBJECT OR COMPLEMENT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** 3.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use a wide range of indefinite pronouns as objects or complements. 
        
  'positive': [
    'I think I\'ll draw something.',
    'When I arrived at his house there wasn\'t anyone there.',
    'I felt nothing unusual.',
    'There is nobody I love more than you.',
    'I need something cold right now.',
    'You have something to say about everything, don\'t you?',
    'You don\'t know anything.',
    'Love is everything.',
    'I wish that I would be able to meet everyone.',
    'Is there nobody that you are dating right now?',
  ],
  'negative': [
    'Everyone has one wish.',
    'Everyone gets excited.',
    'Something made him do such a stupid thing.',
    'Everyone likes the way he talks.',
    'Everything is all right.',
    'Nobody will be the wiser.',
    'Everything is cute.',
    'Nobody can play tennis.',
    'Everyone was crying.',
    'Everything is going well.',
    'Something is going on here.',
    'Nobody hates him.',
    'Everything is constantly changing.',
    'Nobody can take your place.',
    'Everything is so perfect.',
    'Everyone knows about this.',
    'Nobody can surpass him.',
    'Something is wrong with him.',
    'Something is strange.',
    'Something happened over there.',
  ],
}
test_data_1012 = { 

      # **Guideword:** PREMODIFIERS, INTENSIFYING
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use premodifiers with indefinite pronouns, often to intensify. 
        
  'positive': [
    'There was almost nobody in the house.',
    'I have nearly everything I need.',
    'Almost nobody can play tennis.',
    'I see absolutely nobody on the road.',
    'It\'s surely nobody else\'s fault.',
    'Love is absolutely everything.',
    'There is almost nobody I love more than you.',
    # 'Almost everyone gets excited.',
    # gets -> Almost (advmod)
    'I have been nearly everywhere in this town.',
    'She has nearly everything that everyone wants to have.',
  ],
  'negative': [
    'He saw something in the garden.',
    'There is nothing to eat.',
    'There is nowhere as beautiful as Paris.',
    'I heard something about that.',
    'Isn\'t there anything we can do?',
    'We can go anywhere you\'d like this summer.',
    'I gave everything to Sally.',
    'Keith is looking for somewhere to live.',
    'You may invite anybody you want to your birthday party.',
    'There is something funny about him.',
    'He would give anything to get into Oxford.',
    'I think I\'ll draw something.',
    'Fido would follow you anywhere.',
    'I looked everywhere for my keys.',
    'Everyone is sleeping in my bed.',
    'They can choose anything from the menu.',
    'I want to drink something.',
    'The defendant said something.',
    'She knows something about him.',
    'Did you say something?',
  ],
}
test_data_1013 = {

      # **Guideword:** SUBJECT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** 3.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use the full range of indefinite pronouns as subjects, with a singular verb. 
        
  'positive': [
    'No one wanted to speak.',
    'Anyone would have done the same.',
    'Nobody was in that room.',
    'Everyone here is close in age.',
    'I love my job because everyone is passionate about what they do.',
    'Everything is free so take whatever you want.',
    'Nobody wants to play with me.',
    'Nobody knows about the incident.',
    'Nothing in life is free.',
    'Everyone understood the joke.',
  ],
  'negative': [
    'Everywhere I go, people are much the same.',
    'I use the bus to get to school, or sometimes I walk when the weather is fine.',
    'I have looked for my watch everywhere.',
    'They enjoy listening to pop music.',
    'He has run up debts everywhere.',
    'My husband is good at washing dishes, but that is the only housework that he can do.',
    'My father is a lawyer and he is good at debating.',
    'There is kindness to be found everywhere.',
    'My dogs like to play with the frisbee.',
    'There is fear everywhere.',
    'We adore our kittens.',
    'They watch television with their parents everyday.',
    'The sun shines everywhere.',
    'It is crowded everywhere.',
    'Judging from the way she treats people, it is obvious that she is anything but kind.',
    'She enjoys great popularity everywhere.',
    'I see Bob everywhere.',
    'They absolutely love playing volley ball.',
    'My big sister is anything but neat.',
    'My daughters enjoy walking around the park.',
  ],
}
test_data_1014 = { 

      # **Guideword:** WITH RELATIVE CLAUSES, FOCUS
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use indefinite pronouns with a relative clause to form complex noun phrases, to give focus.
        
  'positive': [
    'Something we can learn from this is that we should never lie to each other.',
    'I want to talk with someone who is in charge of the investigation.',
    'Somebody up there loves me.',
    'We are having difficulty in finding somebody who is qualified for the job.',
    'There was something which showed uncertainty in his reply.',
    'Something that I like a lot is my teddy bear.',
    'We need someone who can speak Italian.',
    'Everything that I had faith in vanished.',
    'We are looking for somebody who can use a computer.',
    'Someone that I respect a lot is my brother.',
  ],
  'negative': [
    'Everywhere is covered in snow.',
    'There is over three hundred dollars in the account right now.',
    'There is something in what he says.',
    'There is kindness to be found everywhere.',
    'The engine sounds like something is broken.',
    'He is regarded as a nobody in this group.',
    'She thinks that she is somebody.',
    'No matter where I go, people are much the same.',
    'I felt like cursing somebody.',
    'I love my job because everyone is passionate about what they do.',
    'It seems that he was playing tennis or something.',
    'Someone is ringing the doorbell.',
    'There is someone at the door.',
    'I wanted to hear something about her first.',
    'I told nobody about the accident.',
    'Everything is free so take whatever you want.',
    'Millie wanted to say something or other.',
    'Everyone likes to have ice cream.',
    'I know something about the accident.',
    'The sun shines everywhere.',
  ],
}
test_data_1015 = { 

      # **Guideword:** VAGUE EXPRESSIONS
      # **Guideword type:** USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use indefinite pronouns in vague expressions to refer to things in a non-specific way. 
        
  'positive': [
    'We should watch television or something.',
    'I saw him at the restaurant or somewhere else.',
    'Did you see a policeman or someone like that?',
    'I think she is watching a movie or something.',
    'We think he has a fever or something like that.',
    'He wasn’t angry or anything.',
    'Do you have a stapler or something like that?',
    'We didn’t get a message or anything.',
    'It seems that he was playing tennis or something.',
    'Millie wanted to say something or other.',
  ],
  'negative': [
    'Everything has a beginning and an end.',
    'Something we can learn for this is that we should never lie to each other.',
    'I know something about the accident.',
    'Everything is working well according to the schedule.',
    'Please look for anything out of the ordinary.',
    'There is kindness to be found everywhere.',
    'I want to talk with someone who is in charge of the investigation.',
    'My wife and daughter mean everything to me.',
    'I asked the teacher about everything that I could think of.',
    'There was something of uncertainty in his reply.',
    'Nothing compares to Jessica’s voice.',
    'We are looking for somebody who can use a computer.',
    'There is something over three hundred dollars in the account right now.',
    'Everyone likes to have ice cream.',
    'My parents will do everything in their power to protect him.',
    'Someone is ringing the doorbell.',
    'I don’t agree to everything he says about rich people.',
    'Something that I like a lot is my teddy bear.',
    'Everything that I had faith in vanished.',
    'Someone that I respect a lot is my brother.',
  ],
}
test_data_1016 = { 

      # **Guideword:** 'ANYTHING', FOCUS
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'anything' with post-modifiers to form complex noun phrases as subjects with a singular verb, to give focus. 
        
  'positive': [
    # 'I would do anything for my beautiful and intelligent daughter.',
    'Anything else can be postponed.',
    'Anything in between us should be eliminated.',
    'Anything that will stop you from smoking is something that you should look into.',
    'Anything that connects you to the criminal will be examined.',
    'Anything that allows you to do what you are passionate about is something you should pursue.',
    'Anything to show my talent in bowling is important.',
    'Anything to impress my dear mother would be a good gift.',
    'It\'s hard for me to find anything to show my strong love for you.',
    'Anything other than that can be discussed later.',
  ],
  'negative': [
    'I will take care of everything that comes up.',
    'They can sell anything, but their company isn\'t so great.',
    'She can\'t do anything.',
    'I’ll let you know if anything happens while you’re gone.',
    'I could do anything if you were my child.',
    'I am skeptical whenever he says anything.',
    'They collect anything and everything.',
    'Anyone would be willing to take a risk at this point.',
    'Anything is possible with a little help from friends.',
    'I want everything that Kate has to myself.',
    'Should anyone enter the house, let me know.',
    'If we were to do anything, we should give her a second chance.',
    'In order to win him over, I would do anything.',
    'If you have something to share, please do so at the beginning of the meeting.',
    'If you have anything, I will add it to the list.',
    'Jasmine said something about visiting California.',
    'He could do anything, we just have to wait.',
    'I thought he was kind, but he was nothing like that.',
    'Robert is sweet to my younger sister.',
    'We must avoid hurting people.',
  ],
}
test_data_1017 = { 

      # **Guideword:** 'ANYTHING', ELLIPSIS
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** indefinite - thing, -one, -body etc
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'anything' in an ellipted clause, ('if there is anything ...'). 
        
  'positive': [
    'Anything you are concerned about, consult my son.',
    'Anything that should be reported, I will take care of.',
    'Anything you want to say, now is the time to do so.',
    'Anything you want, the genie can give you.',
    'Anything you want to ask me, I’d be willing to answer.',
    'Anything I can do, you should just let me know.',
    # 'Anything you think is important, I will add to the list.',
    'Anything you need, just let me know.',
    'Anything else you need, just drop by my office.',
    'Anything to share, please do so at the beginning of the meeting.',
  ],
  'negative': [
    'I can\'t find anything to show my strong love for you.',
    'I think everyone should have a fair chance.',
    'If everything falls apart, we are done.',
    'Somebody must have forgotten to turn the lights off.',
    'Do you need someone to take you home tonight?',
    'Everybody seems tired today.',
    'You should try to find anything that allows you to do what you are passionate about.',
    'Is there something that we should do for her?',
    'Everyone is this room is a victim.',
    'If you know anyone from the group, you must come to the party.',
    'Is there anything you want you to know about me?',
    'I’ll let you know if anything happens while you’re gone.',
    'Anyone would be willing to take a risk at this point.',
    'Should anything happen to the house, let me know.',
    'I would give anything for my beautiful and intelligent daughter.',
    'Anything is possible with a little help from friends.',
    'Jasmine told us that she had something to say to the group.',
    'Isabelle is someone who adores animals.',
    'Jack is somebody I dream about these days.',
    'Everyone knows what she did to me a few years ago.',
  ],
}
test_data_1018 = { 

      # **Guideword:** 'YOU', GENERAL
      # **Guideword type:** USE
      # **Super category:** PRONOUNS
      # **Sub category:** generic use
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'you' to refer to people in general. 
        
  'positive': [
    'You are allowed to take a picture of the inside.',
    'You will regret it if you don\'t buy this.',
    'Even if you are lost, this application will help you.',
    'Brushing your teeth is healthy.',
    'You may not enter through this door.',
    'You can do anything you want because it is your life.',
    'When you have free time, you can use this application to study English.',
    'If you are alone, just call this number.',
    'If you cook this, it will take a long time to finish.',
  ],
  'negative': [
    'I\'ll kill you.',
    'You are one of my best friends.',
    'Your house is far from here.',
    'You really are earnest, aren\'t you?',
    'You can come to my house anytime.',
    'I\'ll come with you if you like.',
    'Where are you right now?',
    'You look like you are in good shape.',
    'Will you come to the class tomorrow?',
    'You don\'t talk much.',
    'Do you still talk with my friend?',
    'You may bring him with you the next time you come.',
    'I\'ll lend you the money if you need it.',
    'You look cold, don\'t you?',
    'You like basketball, don\'t you?',
    'You should come to our party tonight.',
    'I would say you are the cutest in my class.',
    'Can I borrow your pen?',
    'I wish you all good luck.',
    'Do you have someone you like?',
    'You have done very well this time.',
  ],
}
test_data_1019 = { 

      # **Guideword:** 'ONE', GENERAL, FORMAL
      # **Guideword type:** USE
      # **Super category:** PRONOUNS
      # **Sub category:** generic use
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'one' to refer to people in general, in formal contexts. 
        
  'positive': [
    'This is where one can live forever.',
    'One can swim as deep as fish can.',
    'One must be careful of one\'s health.',
    'One is solicitous about one\'s home.',
    'One should not be ashamed to learn from one\'s inferiors.',
    'It\'s best to stop before one runs out of one\'s money.',
    'One should keep to the company of one\'s equals.',
    'One must obey one\'s parents.',
    'One can read this book in an hour.',
    'It was in 1993, if one remembers rightly.',
  ],
  'negative': [
    'These are the same as the ones released in September.',
    'The ones standing over there are my siblings.',
    'The ones I hear most often are these songs.',
    'You need to solve these problems one by one.',
    'It is one thing to make statements but another to demonstrate by action.',
    'He had several Japanese dictionaries and lent me one.',
    'The ones who shout at me don\'t bother me.',
    'Local columnists were not entirely of one opinion.',
    'They are the ones who quit university together.',
    'That applies to Japanese companies rather than European ones.',
    'If you’re ordering the mild curry, I’ll have the spicy one.',
    'The documents below are the ones that I sent.',
    'You cannot do two things at one time.',
    'It is fine if you do just the ones you understand.',
    'Goods which are different to the ones I ordered were sent.',
    'People enter the room one by one.',
    'I was sent goods which were different to the ones I ordered.',
    'He showed us the one way to solve the problem.',
    'When you\'ve seen one, you\'ve seen them all.',
    'Just the ones that I indicated would be fine.',
  ],
}
test_data_1020 = { 

      # **Guideword:** 'WE', 'US', GENERAL
      # **Guideword type:** USE
      # **Super category:** PRONOUNS
      # **Sub category:** generic use
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'we' and 'us' to refer to people in general.
        
  'positive': [
    'We can all assume that working is not easy.',
    'We all know that squirrels hibernate.',
    'Here, we can see the two people suffering.',
    'Some of us pray every day while others are not religious.',
    'Let us all fight for our freedom.',
    'We must stand up together and fight them.',
    'We all know that stealing is a crime.',
    'We must be aware of the fact that no one is born evil.',
    'We can see people using smartphones everywhere.',
    'Something we can learn from this is that we should never lie to other.',
  ],
  'negative': [
    'Could you give us an example?',
    'I don’t agree to everything he says about rich people.',
    'We didn’t get a message or anything.',
    'There are seven of us here.',
    'The hats suit us very well.',
    'She showed us the room.',
    'The two of us drank three glasses of beer.',
    'Don’t worry, the victory rests with us.',
    'There is definitely chemistry between us.',
    'We should start packing our suitcases now.',
    'Will you go out with us later?',
    'We think he has a fever or something like that.',
    'She invited us to the event.',
    'Let us see which of us is stronger.',
    'The three of us will do our best.',
    'We should watch television or something.',
    'The enemy is superior to us in numbers.',
    'He will give a lecture for us tomorrow.',
    'It is rough with just the two of us.',
    'I don’t think he knows where we are.',
  ],
}
test_data_1021 = { 

      # **Guideword:** GENDER NEUTRAL
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** generic use
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'they/them' to refer back to indefinite pronouns when we do not know the number or gender.
        
  'positive': [
    'Even if someone asks you where I am, you must not tell them.',
    'If someone ignores you, it means they are angry at you.',
    'If someone steals my tiara, I will not forgive them.',
    'If any students visit my office, tell them to wait for an hour.',
    'If any of my clients call, tell them I am busy for the afternoon.',
    'If anyone wants to contact me, give them my phone number.',
    'If someone lies to me, I will get mad at them.',
    'If anyone is thirsty, they can drink tap water.',
    'If anyone wants to buy presents, let them do that.',
    'If someone wants money from you, they are either poor or vicious.',
  ],
  'negative': [
    #anything with 'they/them' is technically ambiguous
    'They might have had something to eat.',
    'Please look for anything out of the ordinary.',
    'Do you have a stapler or something like that?',
    'I know them from work.',
    'Everything is working well according to the schedule.',
    'I must memorize some of these terms.',
    'Jack must be more handsome than anyone in this room.',
    'Let them eat anything they want.',
    'We didn’t get a message or anything.',
    'They must know someone in Hollywood.',
    'Did you see a policeman or someone like that?',
    'They should have something to wear.',
    'No one was allowed to go to his room.',
    'Everything has its beginning and end.',
    'My wife and daughter mean everything to me.',
    'I asked the teacher about everything that I could think of.',
    'He wasn’t angry or anything.',
    'We think he has a fever or something like that.',
    'Nothing compares to Jessica’s voice.',
    'They must be aware of this accident.',
  ],
}
test_data_1022 = { 

      # **Guideword:** GENDER NEUTRAL
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** generic use
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'he/she', 'he' or 'she' or 'they' to refer back to gender neutral singular nouns or indefinite pronouns when we are not sure of the gender.
        
  'positive': [
    'If someone ignores you, it means they are angry at you.',
    'If a participant wants to leave the building, he or she must be stopped.',
    'If somebody wants some juice, they should pay for it.',
    'If a student needs a place to study, he or she can come to my office.',
    'If anyone is thirsty, they can drink tap water.',
    'If a child has to go to the bathroom, he or she must speak up.',
    'If customer approaches you, he or she must not be ignored.',
    'If someone wants money from you, they are either poor or vicious.',
    'If a patient wants more medicine, he or she must consult the nurse.',
    'If a patient wants more medicine, he/she must consult the nurse.',
    'If someone lies to you, that means they don’t care for you.',
    'If somebody arrives, give this cake to him or her.',
    #moved from negatives
    'He or she must not be married.',
    'He or she should have arrived here by now.',


  ],
  'negative': [
    'If they want to buy presents, let them do it.',
    'If someone lies to me, I will get mad.',
    'I need someone who can make me tea.',
    'Even if they ask you where I am, you must not tell them.',
    'We need to find somebody who is willing to clean his mess.',
    'Jessica would follow him wherever he goes.',
    'Jack must be more handsome than anyone in this room.',
    'If he wants to contact me, give him my phone number.',
    'A will is the final thing a person writes before death.',
    'They must know who she truly is.',
    'If he steals my tiara, I will not forgive him.',
    'They are smart enough to solve his issue on their own.',
    'If my client calls, tell him I am busy for the afternoon.',
    'If she visits my office, tell her to wait for an hour.',
    'I should ask if they know where she is from.',
    'Is your cat a boy or a girl?',
    'They should have something to wear.',
    'They might have something to eat.',
  ],
}
test_data_1023 = { 

      # **Guideword:** 'EACH OTHER'
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** reciprocal
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'each other' as the object of a verb or complement of a preposition to talk about the mutual behaviour of two or more people.
        
  'positive': [
    'They have made up with each other.',
    'We can\'t understand each other.',
    'They had a connection with each other.',
    'They have but slight relations with each other.',
    'The brothers love each other.',
    'Our families are allied with each other.',
    'They are on bad terms with each other.',
    'The two parties have joined hands with each other.',
    'They took each other by the hand.',
    'Let us stand by each other.',
  ],
  'negative': [
    'There are no other restrictions.',
    'You are too worried about other people.',
    'There is no other plan.',
    'I sweat more than other people.',
    'How much are they each?',
    'There is no other way.',
    'I can\'t tell one from another.',
    'We each had made a change by 2002.',
    'It\'s none other than Tom.',
    'A governor is elected in each prefecture.',
    'It was the chiefs of each department.',
    'Each article has its uses.',
    'Each man has his likes and dislikes.',
    'Let each man do his part.',
    'Each department is placed under a minister.',
    'Each man has his strong and weak points.',
    'It is inferior to the other.',
    'Each one has his own room.',
    'There is no other resource.',
    'You are kind to other people.',
  ],
}
test_data_1024 = { 

      # **Guideword:** 'ONE ANOTHER', FORMAL
      # **Guideword type:** FORM/USE
      # **Super category:** PRONOUNS
      # **Sub category:** reciprocal
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'one another' as the object of a verb or complement of a preposition to talk about the mutual behaviour of two or more people, often in formal contexts. 
        
  'positive': [
    'My sons need to learn to respect one another.',
    #parser mistakenly parsed one another as an adjective to modify christmas
    #'We last saw one another last Christmas when I was still dating Caroline.',
    'These are the two theories that conflict with one another.',
    'Men must depend on one another to survive.',
    'They got tired of the act of fighting with one another.',
    'My professors are really good at communicating with one another.',
    'My daughters do a good job at getting along with one another.',
    'My students are good at cooperating with one another.',
    'There are three people who are opposed to one another.',
    'The act of competing with one another is tiring.',
  ],
  'negative': [
    'Conor, Emily and Isabelle fell down one after the other.',
    'This story shows the benevolence shown to one from another person.',
    'I saw one of them at the supermarket last week.',
    'The moment one separates from another person is hard to watch.',
    'She panicked and called people one after another.',
    'The students arrived at the party one after another, until the room was packed.',
    'No one should be treated so horribly.',
    'She tends to leap from one topic to another.',
    'Another plan is to share one bed with two people.',
    'This is a poem composed in reply to another one.',
    'We talked of one thing and another.',
    'Bad incidents happened one after another.',
    'This is the money that one has entrusted to another person.',
    'Robert says one thing and means the other.',
    'It is easy for one thing to be similar to another.',
    'I need another one to wipe the floor.',
    'I want another one of those cookies.',
    'Bring me another glass of wine.',
    'We should meet in person at one place or another.',
    'Please pass her another one.',
  ],
}
test_data_1025 = { 

      # **Guideword:** 'EACH ...' + 'THE OTHER(S)', AS COMPLEMENT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** reciprocal
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'each' (+ noun or pronoun) as subject followed by 'the other(s)' a complement of a preposition, to refer to two related things. ► pronouns: quantity
        
  'positive': [
    'Each of them must come up with a plan different from the others.',
    'Each person must rely on the others.',
    'Each of them has respect for the other.',
    'Each of them have differing opinions from the others.',
    'Each of them is dependent on the others.',
    'Each of them should do a speech on a different topic from the other.',
    'Each member is different from the others, so stop generalizing.',
    'Each person has the right to talk to the others.',
    'Each girl has a different pet than the others.',
    'Each girl has differing ideas from the others of the group.',
  ],
  'negative': [
    'They cannot understand each other’s language.',
    'Maria and Robert loved each other very deeply.',
    'Let’s keep each other company.',
    'We congratulated each other on our success.',
    'My mom and I have sympathy with each other.',
    'The other boy was too busy staring at the girl.',
    'The other building was built forty years ago.',
    'I am related to the other girl.',
    'Each of these girls has their own cars.',
    'Their seats were facing each other.',
    'They passed by each other.',
    'He told me to plant the flowers away from each other.',
    'They fought against each other.',
    'Friends should trust each other at all times.',
    'They embraced each other at the party.',
    'We see each other every other day.',
    'I went to the new museum the other day.',
    'Tom and Jack became reconciled with each other.',
    'We often met each other at a banquet.',
    'They finally became independent from each other.',
  ],
}
test_data_1026 = { 

      # **Guideword:** 'EACH ... THE OTHER(S)', AS OBJECT
      # **Guideword type:** FORM
      # **Super category:** PRONOUNS
      # **Sub category:** reciprocal
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use 'each' (+ noun or pronoun) as subject followed by 'the other(s)' as object , to refer to two related things. ► pronouns: quantity
        
  'positive': [
    'Each participant should be cooperating with the others.',
    'Each store is in good relationship with the others.',
    'As it turned out, each invited the other to their birthday party.',
    'Each catalog has at least one page that is the same as the others.',
    'Each girl is familiar with the others’ brothers.',
    'Each of them are jealous of the others’ fortune.',
    'Each of them likes the others’ project.',
    'Each one knows a secret of the others.',
    'Each of the workers will pair up with one of the others.',
    'Each cook should eat the cake baked by the others.',
  ],
  'negative': [
    'A governor is set over each prefecture.',
    'On the other hand, traveling is expensive and we are better off staying home.',
    'There is a riot in each corner of the district.',
    'We are in sympathy with each other.',
    'Our families are allied with each other.',
    'There is a chief in each department.',
    'The hours clash with each other.',
    'His statement are inconsistent with each other.',
    'We can’t understand each other thoroughly.',
    'They became reconciled with each other.',
    'They held hands with each other.',
    'The plans interfere with each other.',
    'Place the desks apart from each other.',
    'They have but slight relations with each other.',
    'The brothers are at variance with each other.',
    'The two parties have joined hands with each other.',
    'She flew to the other side of the world.',
    'The other house is in Michigan.',
    'They are ignorant of each other\'s intentions.',
    'I should let the other party know about this.',
  ],
}
test_data_1027 = { 

      # **Guideword:** WORD + WORD
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can form alternative questions with two words from the same class combined with 'or'. 
        
  'positive': [
    'Can I have a cup of tea or coffee?',
    'Do you want to have rice or bread for dinner?',
    'Did she go to the school or library yesterday?',
    'Is your phone the new or old one?',
    'Can you buy some snacks or foods for my birthday?',
    'Does he like you or me the most?',
    'Is your new car expensive or cheap?',
    'Do you have something cool or interesting?',
    'Does he like to play tennis or football?',
    'Is he a good or bad person?',
  ],
  'negative': [
    'Either you or he has the CD.',
    'I found a wallet and I reported it to the police.',
    'That animal is not a giraffe but a panda.',
    'You can keep either this book or that one.',
    'He loves both you and I.',
    'He can speak not only Chinese but Japanese.',
    'I can neither write nor speak French.',
    'Study hard, and you will pass the entrance exam.',
    'I want pens, notebooks, textbooks and glasses.',
    'You and I are wrong.',
    'Both you and she are college students.',
    'Neither you nor I am healthy.',
    'You and I are students.',
    'He has lived in Hokkaido and in Okinawa.',
    'He is very rich, but he is not happy.',
    'She had a fever, so she was absent from school.',
    'Not only you but I am to blame.',
    'Mike or John will be elected chairperson.',
    'You, he and I are good friends.',
    'Study hard, or you will fail the entrance exam.',
  ],
}
test_data_1028 = { 

      # **Guideword:** PHRASE + PHRASE
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can form alternative questions with two phrases combined with 'or'. 
        
  'positive': [
    'Do you drink coffee at breakfast or after lunch?',
    'Do you like people who like cats or people who like dogs?',
    'Shall we take a break or finish it now?',
    'Will it be sunny or rainy again tomorrow?',
    'Is your bag the red one or the black one?',
    # 'Was that the correct answer or the wrong one?',
    # Was -> that (dep)
    'Do they take the express train or the night bus?',
    'Have you ever tried Chinese dumplings or Japanese sushi?',
    'Is this area in the city or in the countryside?',
    'Would you like sugary coffee or watery tea?',
  ],
  'negative': [
    'You either run from things or you face them.',
    'Let\'s give it a try, sink or swim.',
    'Either you come with us, or you stay with him.',
    'Either he is wrong or I am.',
    'You may take either the apple or the pear.',
    'I don’t drink or smoke.',
    'This game will make or break us.',
    'You can have either pudding or jelly for dessert.',
    'We either save the world or kill all of them.',
    'I can\'t say either yes or no.',
    'He is either in London or in Paris.',
    'It is thought that he was either murdered, or died of disease.',
    'Either email or call me when you get any information about the incident.',
    'It\'s performed by either two or four dancers.',
    'Either he is to blame, or I am.',
    'Please choose either red, pink, blue or black.',
    'Either you can talk to her or Jack will.',
    'You either love or hate this.',
    'It will either rain or be windy.',
    'You can arrive here either by car, by train or by plane.',
  ],
}
test_data_1029 = { 

      # **Guideword:** 'OR SOMETHING ELSE', VAGUE
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can form alternative question with 'or something else' as the second alternative to a noun phrase, to refer to something non-specific. 
        
  'positive': [
    'Do you like cats or something else?',
    'Does he play baseball or something else?',
    'Do you want to eat dinner or something else?',
    'Is she being nice or is it something else?',
    'Is there any special place you want to visit or something else there?',
    'Do they take a train or something else?',
    'Would you like coffee or something else?',
    'Do they hate you or is it something else?',
    'Did you only buy a bag or something else?',
    'Is he your boyfriend or something else?',
  ],
  'negative': [
    'You can arrive here either by car, by train or by plane.',
    'The defendant said something.',
    'Either you talk to her or Jack does.',
    'I think I\'ll draw something.',
    'I don’t drink or smoke.',
    'It\'s performed by either two or four dancers.',
    'Something made him do such a stupid thing.',
    'Let\'s give it a try, sink or swim.',
    'Please choose either red, pink, blue or black.',
    'Something is wrong with him.',
    'Something is strange.',
    'Something is going on here.',
    'I need something cold right now.',
    'Either email or call me when you get any information about the incident.',
    'I felt something unusual.',
    'Something happened over there.',
    'I want to drink something.',
    'You may take either the apple or the pear.',
    'There is something funny about him.',
    'You either run from things or you face them.',
    'It will either be rainy or windy there.',
  ],
}
test_data_1030 = { 

      # **Guideword:** CLAUSE + CLAUSE
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can form alternative questions with two clauses combined with 'or'.
        
  'positive': [
    'Do I have to go to the class or can I skip the class?',
    'Did you invite him or did he come here by himself?',
    'Do you like him or does he like you?',
    'Can I borrow this or do I have to buy a new one?',
    'Is she nice or am I too generous?',
    'Should I take a train or is it better to take a taxi?',
    'Did you have the party or will you have it next week?',
    # 'Are you normal or do other people make you crazy?',
    # normal -> do (conj:or)
    'Should I stay or should I go?',
    'May I leave the room or should I stay here until the end?',
  ],
  'negative': [
    'I don’t drink or smoke.',
    'Either you come with us, or you stay with him.',
    'Did you go to the party or the bar yesterday?',
    'Please choose either red, pink, blue or black.',
    'Either he or I am wrong.',
    'You can arrive here either by car, by train or by plane.',
    'You may take either the apple or the pear.',
    'Do you want to eat dinner or something else?',
    'I can\'t say either yes or no.',
    'You can have either pudding or jelly for dessert.',
    'Do you like cats or dogs?',
    'Is he a devil or an angel?',
    'We either save the world or kill all of them.',
    'Do you go to the school or stay at home?',
    'Do you like cats or something else?',
    'Do they use a train or something else?',
    'Do you like red or white wine?',
    'He is either in London or Paris.',
    'Is your bag red or black?',
    'Do you drink tea or coffee?',
  ],
}
test_data_1031 = { 

      # **Guideword:** 'OR NOT'
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can form alternative questions using 'or not' to substitute for a clause, sometimes to express annoyance or impatience. 
        
  'positive': [
    'Is he getting better or not?',
    'Is this cheaper than the last one or not?',
    'Was she an Empress or not?',
    'Is this free of charge or not?',
    'Is this water drinkable or not?',
    'Is this game fun or not?',
    'Have you been to Japan or not?',
    'Can I use your laptop or not?',
    'Is this a dream or not?',
    'Do you have a pen or not?',
  ],
  'negative': [
    'I don\'t know if they are going to come here or not.',
    'I am in the middle of considering whether or not to attend that meeting.',
    'Let\'s see if it is true or not.',
    'I don\'t care if I go or not.',
    'I am worried about whether that is the same article or not.',
    'I can\'t tell whether it is going to rain or not.',
    'It\'s up to you whether to go or not.',
    'It is a question whether he will succeed or not.',
    'Please examine whether you are okay with these contents or not.',
    'You will decide whether that\'s bad or not.',
    'I doubt whether it is true or not.',
    'Bring him whether he will come or not.',
    'I don\'t know whether he likes shrimp or not.',
    'I can\'t decide whether I should tell him or not.',
    'I don\'t know if it has any effect or not.',
    'It doesn\'t matter whether we win or not.',
    'Whether he comes or not, I\'ll go.',
    'I am hesitating about if I will see it or not.',
    'I will make sure about whether that can be sent or not.',
    'It is OK either way, whether the data is there or not.',
    # periodなし、例外を返すため
    'Grocery bags...decide if the supermarket gives grocery bags or not',
  ],
}
test_data_1032 = { 

      # **Guideword:** STRONG ALTERNATIVE
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can form alternative questions using an extreme alternative to give greater pragmatic force. 
        
  'positive': [
    'Are you coming with us or staying here all alone?',
    'Do you really think we should use those hideous old plates or should we use new ones?',
    'Did you stay in all night and watch TV or did you do something interesting?',
    'Do you want to go for a run or sit on the couch all day?',
    'Will you agree to sign the contract or will you get left behind?',
    'Is the new-found fame a blessing or a curse?',
    # 'Are you with us or against us?',
    # Are -> Are (conj:or)
    'Is this idea good for the company or terrible?',
    'Did you clean your room or leave it filthy?',
    'Did she give the performance of her life or did she choke on stage?',
  ],
  'negative': [
    'Maybe you could pay a visit or give her a brief call?',
    'Will he try to take part in this competition?',
    # 'Are there trains or buses from the airport to Belgium?',
    'Are you allowed to quit your job?',
    # 'Do you like the oceans or the mountains?',
    'Would you like to share this plate with me?',
    'Would you like some vanilla ice cream?',
    # 'Did he send a postcard to his mother yesterday or two days ago?',
    'Does Richard want to go to the park?',
    'Would you like mayonnaise on it?',
    'How are you feeling today?',
    'I was wondering if you knew the population of this city.',
    # 'Would you like to eat pizzas or hamburgers?',
    'Mom wants to know if you are hungry.',
    'Has he been studying for several years?',
    'Did Ken get his ears pierced yesterday?',
    'Maybe you could visit her another time or wait in this office?',
    'Which is best, to water the plant every day or just once a week?',
    # 'Did you buy the blue ball or the red ball?',
    'Jackie has a little brother?',
  ],
}
test_data_1033 = { 

      # **Guideword:** ELLIPTED MODAL, HEDGING
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can form alternative questions with two clauses and ellipsis in the second clause, often as a hedging device.
        
  'positive': [
    'Will he study or work there for the next several years?',
    'Will he send a postcard to his mother or just call her?',
    'Could you visit her another time or wait in this office?',
    'Will they buy a house or rent somewhere?',
    'Could I learn a new skill or try to meet some new people there?',
    'Could you write this down or remember it for me?',
    'Should we go down this road or turn back?',
    'Will it be often warm outside or be cool in the spring?',
    'Can you help me or point me to somebody who will?',
    'Maybe you could pay a visit or give her a brief call?',
  ],
  'negative': [
    'There are dogs in your sister’s room, aren’t there?',
    'Maybe he wasn’t doing it on purpose.',
    'Are you allowed to quit your job?',
    'Would you like some vanilla ice cream or chocolate?',
    'Who would want to play with kids?',
    'There is food in the fridge, isn’t there?',
    'Maybe it was just a joke to him.',
    'What made you do such a cruel thing?',
    'Will he try to take part in this competition?',
    'Olivia is on her way here?',
    'Jackie has a little brother?',
    'Why would you let her play with your toys?',
    'Are you coming with us or not?',
    'Ken got his ears pierced yesterday?',
    'Has he been studying for several years?',
    'There are many kids here, aren’t there?',
    'Why did she get that job?',
    'There isn’t a single book in this room, is there?',
    # 'Would you like mayonnaise or ketchup on it?',
    # ketchup : VB, ketchup -> you (nsubj)
    'There isn’t a cat in this house, is there?',
  ],
}
test_data_1034 = { 

      # **Guideword:** ELLIPSIS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** alternatives
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can form alternative questions with two or more clauses and ellipsis in the second or third clause. 
        
  'positive': [
    'Can you pass me the salt or cook something more salty?',
    'Will you go on the cruise or tour the harbor?',
    'Will you stay here or go away?',
    'Was she just proving a point or trying to make us mad?',
    'Did you pick up the package or go home directly?',
    'Are you dating Ben or meeting as friends?',
    'Is she going to Barcelona or staying in Vietnam?',
    'Do you want me to stay in your room or leave the room immediately?',
    'Can we take the bus, ride the train, or get Liam to drive us?',
    'Will he take the call or ignore it again?',
  ],
  'negative': [
    'On Sundays either Linda or I am on duty.',
    'Is it not common for young girls to have a smartphone?',
    'I was only talking for a minute or two.',
    'Has she not achieved her goal yet?',
    'Are you going to sell the car or not?',
    'Have we not found a director yet?',
    'My car is broken, or I would have been on time.',
    'Does Jack not have his own bike?',
    'By one or two o\'clock in the morning, I\'ll finish this task.',
    'Everyone likes Italian food, or at least spaghetti.',
    'Could you not cough in front of me?',
    'She runs about a mile or two every day.',
    'Hilary or Barnard will return the book for me.',
    'I\'ve got two or three appointments in the afternoon.',
    'Would you like your steak rare or medium?',
    'He is rich, or at least he appears to be rich.',
    'He doesn\'t believe in ghosts or witches.',
    'The movie starts one Tuesday or Thursday.',
    'Bring a pencil or you\'ll have to borrow one.',
    'Prices are going up, or that\'s what I heard.',
  ],
}
test_data_1035 = { 

  # **Guideword:** QUESTION TAGS
  # **Guideword type:** FORM
  # **Super category:** QUESTIONS
  # **Sub category:** tags
  # **Lexical Range:** 1.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use a limited range of question tags.
    
  'positive': [
    'You don\'t know where they live, do you?',
    'They cannot imagine the situation, can they?',
    'You haven\'t heard the results, have you?',
    'Charlie didn\'t stop his workout, did he?',
    'It is true that many people made it to the cave, isn\'t it?',
    'She has done a lot to this company, hasn\'t she?',
    'He bought a new pair of scissors, didn\'t he?',
    'Their professors did not cancel their meeting, did they?',
    'My classmate showed up to the final exam, didn\'t she?',
    'There are more than two ways to succeed in life, aren\'t there?',
  ],
  'negative': [
    'I have heard of it before.',
    'Haven\'t they finished their vacation already?',
    'She has not lived her life up.',
    'Can\'t you see the beautiful blue sky from here?',
    'Didn\'t he say so in the last meeting?',
    'Isn\'t it wrong to say something is wrong at first place?',
    'It isn\'t a good thing to say so.',
    'You know why they have been working out so hard lately.',
    'Do you know if there are any other things I forgot to mention?',
    'What you have done means so much to them.',
    'I really am not interested in that.',
    'Won\'t you go to the basketball game tomorrow?',
    'Haven\'t you done anything yet?',
    'He cannot stop thinking about the dream he had yesterday.',
    'It is a fact that we have never tried this meal before.',
    'I saw a black car getting close to me and felt danger.',
    'Do you know if the library is open today?',
    'Do not eat breakfast in this room.',
    'They do not speak my language, which is totally fine with me.',
    'I heard her saying I do not know English, which is clearly false.',
  ],
}
test_data_1036 = { 

      # **Guideword:** NEGATIVE MAIN CLAUSES + AFFIRMATIVE QUESTION TAGS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** tags
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of affirmative 'be', 'do' and 'have' tags with negative main clauses.
        
  'positive': [
    'You don\'t like tomatoes, do you?',
    'Ken isn\'t nice, is he?',
    'You didn\'t touch the ring, did you?',
    'They don\'t like golf, do they?',
    'Megumi isn\'t a nurse, is she?',
    'She didn\'t go to Kyoto yesterday, did she?',
    'This picture isn\'t very nice, is it?',
    'You aren\'t coming to the party tomorrow, are you?',
    'You haven\'t met him, have you?',
  ],
  'negative': [
    'You won\'t be noisy, will you?',
    'You won\'t marry her, will you?',
    'This picture is nice, isn\'t it?',
    'Open the door, will you?',
    'You like dogs very much, don\'t you?',
    'Turn on the light, will you?',
    'Let’s play soccer, shall we?',
    'Let\'s go fishing, shall we?',
    'You are a student, aren’t you?',
    'They have seen a UFO, haven\'t they?',
    'Tom lives in Tokyo, doesn\'t he?',
    'You can swim, can\'t you?',
    'Your father is a teacher, isn’t he?',
    'Let\'s play soccer, shall we?',
    'This is prettier than that, isn\'t it?',
    'He was going to go to Tokyo today, wasn\'t he?',
    'You can speak French very well, can\'t you?',
    'Carry this desk, will you?',
    'He likes playing baseball, doesn’t he?',
    'He is a good man, isn\'t he?',
    'You like sushi, don\'t you?',
    'You like tomato, don\'t you?',
  ],
}
test_data_1037 = { 

      # **Guideword:** AFFIRMATIVE MAIN CLAUSES + NEGATIVE QUESTION TAGS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** tags
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of 'be', 'do', 'have' and modal verb tags with negative main clauses.
        
  'positive': [
    'He is a good man, isn\'t he?',
    'They have seen a UFO, haven\'t they?',
    'You are a student, aren’t you?',
    'He likes playing baseball, doesn’t he?',
    'Tom lives in Tokyo, doesn\'t he?',
    'You can speak French very well, can\'t you?',
    'You like sushi, don\'t you?',
    'You like tomato, don\'t you?',
    'This picture is nice, isn\'t it?',
    'Your father is a teacher, isn’t he?',
  ],
  'negative': [
    'You don\'t like tomato, do you?',
    'You weren\'t at home yesterday, were you?',
    'You won\'t come to the party tomorrow, will you?',
    'Ken isn\'t very nice, is he?',
    'You won\'t marry her, will you?',
    'They don\'t like golf, do they?',
    'She didn\'t go to Kyoto yesterday, did she?',
    'Megumi isn\'t a nurse, is she?',
    'Yuri didn\'t meet Ken yesterday, did she?',
    'Don’t be noisy, will you?',
    'Please don\'t touch the ring, will you?',
    'You won\'t finish the work today, will you?',
    'He isn\'t busy, is he?',
    'We shouldn\'t be noisy here, should we?',
    'You couldn’t lend me your book, could you?',
    'This isn\'t a nice picture, is it?',
    'The children didn\'t go to school yesterday, did they?',
    'He doesn\'t speak English, does he?',
    'Your husband doesn’t smoke, does he?',
    'You have never been to Tokyo, have you?',
  ],
}
test_data_1038 = { 

      # **Guideword:** AFFIRMATIVE MAIN CLAUSES + AFFIRMATIVE QUESTION TAGS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** tags
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of affirmative tags with affirmative clauses.
        
  'positive': [
    'You can run faster than me, can you?',
    'He comes to the class everyday, does he?',
    'So you are sorry now, are you?',
    'Marcus keeps you on a short leash, does he?',
    'He’s going to do it today, is he?',
    'I can stay here, can I?',
    'You think you’re funny, do you?',
    'She can cook Japanese food, can she?',
    'You went to the party yesterday, did you?',
    # went -> did (advcl) （対応済み）
    'So they are getting married, are they?',
  ],
  'negative': [
    'Tom lives in Tokyo, doesn\'t he?',
    'You can speak French very well, can\'t you?',
    'Your father is a teacher, isn’t he?',
    'He was going to go to Tokyo today, wasn\'t he?',
    'The children didn\'t go to school yesterday, did they?',
    'Let\'s not go fishing today, shall we?',
    'You wouldn\'t carry this desk for me, would you?',
    'You weren\'t at home yesterday, were you?',
    'Megumi isn\'t a nurse, is she?',
    'They have seen a UFO, haven\'t they?',
    'This picture is nice, isn\'t it?',
    'You couldn’t lend me your book, could you?',
    'You like dogs very much, don\'t you?',
    'This picture isn\'t very nice, is it?',
    'You won\'t finish the work today, will you?',
    'Don’t be noisy, will you?',
    'You won\'t marry her, will you?',
    'You won\'t touch the ring, will you?',
    'This is prettier than that, isn\'t it?',
    'You have never been to Tokyo, have you?',
  ],
}
test_data_1039 = { 

      # **Guideword:** 'RIGHT' AS AN INFORMAL TAG
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** tags
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'right' as a tag in informal contexts.
        
  'positive': [
    'You\'re kidding, right?',
    'Blonde hair is awesome, right?',
    'You get it, right?',
    'Today was cool, right?',
    'You are going out now, right?',
    'Friends are precious, right?',
    'It\'s been about a month, right?',
    'That is sad, right?',
    'That\'s a novel, right?',
    'It is night there, right?',
  ],
  'negative': [
    'That will heal right away.',
    'Are you free right now?',
    'Is everything all right?',
    'I want to go home right now.',
    'Is it right or wrong?',
    'I am really happy right now.',
    'That is right on the money.',
    'Turn right at the next intersection.',
    'Are you sure it\'s all right?',
    'I suppose you\'re right.',
    'My gut feelings are often right.',
    'Will you be all right?',
    'We decided right away.',
    'That\'s right.',
    'It has the right firmness.',
    'I will fix that right away.',
    'The car turned right over.',
    'I will go there right away.',
    'Serve you right.',
    'That disappeared right away.',
  ],
}
test_data_1040 = { 

      # **Guideword:** TAGS WITH IMPERATIVES AS SOFTENERS
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** tags
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use an affirmative or negative tag after an imperative clause to soften the imperative.
        
  'positive': [
    'Keep quiet, will you?',
    'Don’t bother me, will you?',
    'Don’t tell anyone, will you?',
    'Keep your mouth shut, will you?',
    'Just give me a minute, will you?',
    'Ask him about it, can you?',
    'Let’s help her set the table, shall we?',
    'Stop talking and open your books, will you?',
    'Go upstairs and study, will you?',
    # parser mistakendly parsed "write" as noun
    #'Write to me, won’t you?',
  ],
  'negative': [
    'Haven’t we discussed this earlier today?',
    'Did she marry his older brother?',
    'Has she opened a bank account yet?',
    'Don’t you have a medical conference to attend to?',
    'Can we take a minute to pray?',
    'Can’t we call a taxi?',
    'Matt will spend his summer in Thailand.',
    'Doesn’t he have two sisters?',
    'Won’t you buy her a birthday present?',
    'Can’t you just lie to your dad?',
    'Hasn’t she been to Seoul before?',
    'Won’t you come and play with me?',
    'Do we have to read this book?',
    'Shall we invite the happy couple to our party?',
    'Shall we share a bucket of popcorn?',
    'Will you change the toilet paper?',
    'Won’t we visit her at the hospital?',
    'Will you come and play with me?',
    'Didn’t she quit school last spring?',
    'Will you open the window?',
  ],
}
test_data_1041 = { 

      # **Guideword:** TAGS WITH 'THERE' + 'BE'
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** tags
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use affirmative and negative forms of question tags with 'there' + 'be'. 
        
  'positive': [
    'There is something we can do, isn’t there?',
    'There are dogs in your sister’s room, aren’t there?',
    'There isn’t a cat in this house, is there?',
    'There isn’t anyone in the room, is there?',
    'There is food in the fridge, isn’t there?',
    'There is a key to this door, isn’t there?',
    'There aren’t many options, are there?',
    'There are towels in the bathroom, aren’t there?',
    'There are many kids here, aren’t there?',
    'There isn’t a single book in this room, is there?',
  ],
  'negative': [
    'There is a tree, some flower beds and a church on the road.',
    'What should be done with these files?',
    'There is no way she got married.',
    'What is the real reason you came to japan?',
    'There have been so many terror attacks throughout history.',
    'There is the problem of immigration in Germany.',
    'What must be done by the end of the day?',
    'There should be a new restaurant here.',
    'Can you hear me singing in the shower?',
    'There is a new movie coming up next week.',
    'There’s a paper, a pen and a notebook on the table.',
    'There are many books in the new library in San Francisco.',
    'There used to be a museum in this city.',
    'There is a library near my house.',
    'There is a dog at the door.',
    'There is no use arguing with stupid teachers.',
    'There are no oranges in the supermarket.',
    'There must be someone waiting for you.',
    'There must be something flying around.',
    'There are so many useful recipes in this magazine.',
  ],
}
test_data_1042 = {

  # **Guideword:** MAIN VERB 'BE'
  # **Guideword type:** FORM
  # **Super category:** QUESTIONS
  # **Sub category:** wh-
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'wh-'words + main verb 'be' + subject to form 'wh-' questions. 
    
  'positive': [
    'How is your day?',
    'How are your parents so far?',
    'What are you up to recently?',
    'What is the source for this information?',
    'When was the last time we talked?',
    'Where were the rest of them?',
    'Who is your new boyfriend?',
    'Where are you now?',
    # How -> was dep
    # 'How was the baseball game yesterday?',
    'Why are you so sure about it?',
  ],
  'negative': [
    'What time is it now?',
    'Why don\'t we go to eat at that restaurant next week?',
    'Where do you want to go in Tokyo?',
    'Why don\'t you come to my place this weekend?',
    'How did you get home yesterday?',
    'What did you do last night?',
    'What do your parents know about me?',
    'Where did you stay last night?',
    'What are you doing now?',
    'Where are you heading?',
    'Why are you thinking like that?',
    'When will you come to my place today?',
    'Why did you go to the school today?',
    'Why don\'t you come with me?',
    'Can you take me to the library tomorrow?',
    'Can we meet up this morning?',
    'Do we have homework for tomorrow\'s classes?',
    'Do you know about the accident today?',
    'Have you talked with my mother?',
    'Have you studied history this week yet?',
    'Are there any restaurants near your house?',	
  ],
}
test_data_1043 = { 

  # **Guideword:** WITH AUXILIARY 'DO'
  # **Guideword type:** FORM
  # **Super category:** QUESTIONS
  # **Sub category:** wh-
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'wh-'words + auxiliary 'do' + subject + main verb to form 'wh-'questions. ► present simple;  ► past simple
    
  'positive': [
    'Why do you wish to leave?',
    'Why do you laugh at his jokes?',
    'Why do we have dreams?',
    'What do you like to watch?',
    'What time do you go to sleep?',
    'When did you go home yesterday?',
    'When do you usually wake up?',
    'Where do you stay usually?',
    'Where did you go yesterday?',
    'What did you do yesterday?',
  ],
  'negative': [
    'What have you done?',
    'What time have you finished your work?',
    'What have you said to your mother?',
    'Where have you been?',
    'Where have you gone recently?',
    'Where have you bought your cute clothes?',
    'what are you doing now?',
    'What are you eating?',
    'What are you cooking?',
    'Where are you going?',
    'Where are you eating lunch?',
    'How are you doing?',
    'How is your family doing?',
    'Where can I go for this vacation?',
    'What can I help you?',
    'Where should I go?',
    'When are you going out of your house?',
    'How could I know about it?',
    'What will you do tomorrow?',
    'Where will you go next month?',
  ],
}
test_data_1044 = { 

      # **Guideword:** WITH AUXILIARY 'HAVE'
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** wh-
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'wh-'words + auxiliary 'have' to form 'wh-'questions. ► present perfect  ►  past perfect
        
  'positive': [
    'What have you done?',
    'What time have you finished your work?',
    'What have you said to your mother?',
    'Where have you been in Japan?',
    'Where have you gone recently?',
    'Where had you bought gifts for my birthday?',
    'How have you been so far?',
    'How had your mother been?',
    'Why had you been away for such a long time?',
    'Why have you lied to me until now?',
  ],
  'negative': [
    'what are you doing now?',
    'Where are you going?',
    'How are you doing?',
    'How is your family doing?',
    'What can I help you with?',
    'Where should I go?',
    'How can I know about it?',
    'How can I help you?',
    'When can I go home?',
    'How often do you go to that coffee shop?',
    'How much is this watch?',
    'How far is your company from here?',
    'What will you do tomorrow?',
    'Where will you go next month?',
    'Why do you wish to leave?',
    'What time do you go to sleep?',
    'When did you go home yesterday?',
    'When do you usually wake up?',
    'Where do you stay usually?',
    'Where did you go yesterday?',
  ],
}
test_data_1045 = { 

  # **Guideword:** WITH AUXILIARY 'BE'
  # **Guideword type:** FORM
  # **Super category:** QUESTIONS
  # **Sub category:** wh-
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use 'wh-'words + auxiliary 'be' to form 'wh-'questions. ► present continuous ► past continuous
    
  'positive': [
    'What are you doing now?',
    'Where are you heading?',
    'Why are you thinking like that?',
    'Where is your father going tomorrow?',
    'Why are we staying here?',
    # what->is, cop
    # 'What is my brother doing there?',
    'What were you doing at this shop?',
    'How are you doing today?',
    'How is your mother doing recently?',
    # what->is, cop
    # 'What are you expecting?',
  ],
  'negative': [
    'Why don\'t we go to eat at that restaurant next week?',
    'Where do you like the best in Japan?',
    'Why don\'t you come to my place this weekend?',
    'How did you do yesterday?',
    'What will you do tomorrow?',
    'What do your parents know about me?',
    'Where did you come from yesterday?',
    'How many people are there?',
    'Why did you go to the school today?',
    'Why don\'t you come with me?',
    'What languages can you speak?',
    'What are you up to recently?',
    'How often do you swim?',
    'How far is it from here to school?',
    'What time are you free today?',
    'Where will you buy the new shoes?',
    'What kind of foods do you like the best?',
    'Where was he at that time?',
    'When is your birthday?',
    'The large shop over there is where you bought the ring.',
  ],
}
test_data_1046 = { 

      # **Guideword:** MODAL VERBS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** wh-
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'wh-'words + modal verbs + subject + main verb to form 'wh-'questions.
        
  'positive': [
    'What can I help you with?',
    'Where should I go?',
    'How can I learn more about it?',
    'How can I help you?',
    'When can I go home?',
    'What will you do tomorrow?',
    'Where will you go next month?',
    'Why should I stay here?',
    'Why should we wait for you?',
    'What must I do before going back home?',
  ],
  'negative': [
    'What have you done?',
    'What time have you finished your work?',
    'What have you told your mother?',
    'How have you been so far?',
    'How has your mother recently been?',
    'Why have you been away for such a long time?',
    'What are you doing now?',
    'Where are you going?',
    'How are you doing?',
    'How is your family doing?',
    'How often do you go to that coffee shop?',
    'How much is this watch?',
    'How far is your company from here?',
    'Why do you wish to leave?',
    'What time do you go to sleep?',
    'Where do you stay usually?',
    'Where did you go yesterday?',
    'I can cook anything for you.',
    'You should stay with us.',
    'Will you go to school tomorrow?',
    'Would you like to have lunch with me?',
    'Could you open the door for me?',
  ],
}
test_data_1047 = { 

      # **Guideword:** NEGATIVE QUESTONS, SUGGESTIONS
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** wh-
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use negative question 'why don't' + pronoun + verb, to make a suggestion or invitation. 
        
  'positive': [
    'Why don\'t you join us?',
    'Why don\'t we go there together?',
    'Why don\'t you come to my house?',
    'Why don\'t we have lunch together?',
    'Why don\'t you come with us?',
    'Why don\'t we throw the party at your house?',
    'Why don\'t you study harder?',
    'Why don\'t we have time to talk a bit?',
    'Why don\'t you go to the office?',
    'Why don\'t we watch a movie at my house?',
  ],
  'negative': [
    'Why do you feel lonely?',
    'Why do you laugh?',
    'Why is she crying?',
    'Why do we sleep late every day?',
    'Why were you late this morning?',
    'Why are you here?',
    'Why were you absent yesterday?',
    'Why did you run away?',
    'Why are they so happy?',
    'Why do you want water?',
    'Why are you so sure?',
    'This is why I hate you.',
    'That is why I didn\'t go to the party yesterday.',
    'Why do you stay with us?',
    'Why are you so sad?',
    'This is why you study so hard.',
    'Why do you want to stay with me?',
    'Why do you sing well?',
    'Why are you so free these days?',
    'This is why I love to swim.',
    'That\'s why I watch movies every night.',
    "Why didn't you go there?",
  ],
}
test_data_1048 = { 

      # **Guideword:** NEGATIVE QUESTIONS WITH MODALS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** wh-
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use 'wh-'words + the negative form of modal verbs + subject + main verb to form 'wh-'questions.
        
  'positive': [
    'Why couldn\'t you get a haircut?',
    'Why can\'t we go home?',
    'Why won\'t you come to see the flowers?',
    'Why don\'t we take a walk?',
    'Why don\'t you join in the conversation?',
    'Why don\'t you try to be more cheerful?',
    'Why don\'t you have girlfriend?',
    'Why don\'t we play together?',
    'Why don\'t we go somewhere?',
    'Why shouldn\'t you come with me?',
  ],
  'negative': [
    'Why do you laugh?',
    'Why do we have dreams?',
    'Why did you do that?',
    'Why do you wish to resign?',
    'Why did you open the box?',
    'Why do you have ants in your pants?',
    'I can see why.',
    'Why do I even care?',
    'Why should I be afraid?',
    'Why were you late this morning?',
    'Why did you run away?',
    'Why should you die?',
    'Why is she crying?',
    'That is why I did it very well today.',
    'Why do you wish to leave?',
    'Why do you hang back?',
    'Where did I go wrong?',
    'Why were you absent yesterday?',
    'I wonder why they do not like the proposal.',
    'Why do you think so?',
    'Why did you quit?',
  ],
}
test_data_1049 = { 

      # **Guideword:** NEGATIVE QUESTIONS WITH MAIN VERBS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** wh-
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use 'wh-'words + the negative form of auxiliary 'do' + subject + main verb to form 'wh-'questions.
        
  'positive': [
    'Where haven’t we explored this matter thoroughly?',
    'Why don’t we have a pony?',
    'How didn’t you say anything about this issue?',
    'When didn’t she reply to our letter in the past?',
    'Why don’t they find a new science tutor?',
    'What didn’t she tell me about her mother?',
    'Why didn’t he buy me a purse?',
    'Why don’t we rent some clothes?',
    'Why didn’t you close the door properly?',
    'Why don’t we shut down the store?',
  ],
  'negative': [
    'Will you come and play with me?',
    'When did she graduate from that school?',
    'Where did we have dinner last night?',
    'Why did we decide to bake a cake?',
    'What do we do if she doesn’t want to talk to us?',
    'When do we have to go to the airport?',
    'Why would she do that to her brother?',
    'When do I get to have my own room?',
    'Write to me, won’t you?',
    'When did she cure her disease?',
    'When did she come back from soccer practice.',
    'Why did he eat alone?',
    'Where did you find my daughter?',
    'Why did you ignore me when I said hello?',
    'Why did she let them come to her house?',
    'What do you think about my new album?',
    'Where did they have their wedding at?',
    'Just give me a minute, will you?',
    'What can we say when someone is heartbroken?',
    'Won’t we visit her at the hospital?',
  ],
}
test_data_1050 = { 

      # **Guideword:** FOCUS
      # **Guideword type:** USE
      # **Super category:** QUESTIONS
      # **Sub category:** wh-
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use 'wh-'questions as a focusing device, often in a narrative or argument.
        
  'positive': [
    'So why do they support this belief?',
    'What else is there to say?',
    'But why would anyone ever listen to her?',
    'Then what is most important thing to do in this situation?',
    'So why on earth would there be a knife here?',
    'What made them think that way?',
    'So where was it that they hid the money?',
    'Then why would anyone want to buy that product?',
    'So what must be done to solve this?',
    'But when could she have gone there?',
  ],
  'negative': [
    'Is she the same age as us?',
    'Can we meet up on another day?',
    'Candice is who I like most.',
    'Is it fine for me to listen this conversation?',
    'I don’t know where this rumor spread from.',
    'Ken and Jack are friends?',
    'Let me know where he is hiding.',
    'Am I the one to be blamed for the accident?',
    'Tell me why I have to go to this school.',
    'Would it be fine if I watched you dance?',
    'There isn’t a single book in this room, is there?',
    'Did they end up living together?',
    'Are we allowed to go outside?',
    'There aren’t many options, are there?',
    'There is food in the fridge, isn’t there?',
    'Would we be able to join the baseball team?',
    'Is she supposed to be here?',
    'There are towels in the bathroom, aren’t there?',
    'There is a key to this door, isn’t there?',
    'Will you teach me how to code?',
  ],
}
test_data_1051 = { 

  # **Guideword:** MODAL VERBS
  # **Guideword type:** FORM
  # **Super category:** QUESTIONS
  # **Sub category:** yes/no
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of modal verbs + subject + main verb to form 'yes/no' questions.  ► can
    
  'positive': [ 
    'Can you check the towels out at the front desk?',
    'Should I go to the wellness center every day?',
    'Could you help me learn how to drive a golf cart?',
    'Won\'t you spare some change?',
    'Will we go to the restaurant this evening to celebrate your 22nd birthday?',
    # we以下従属節であるかのような判定がでます。ちょっとやりようが思いつかなかいです。
    'Can you do me a favor?',
    'May I go to the golf club this evening with my friends?',
    'Wouldn\'t you come to the commencement in June?',
    'May I ask you a question?',
    'Will you come to counseling this afternoon?',
    # 以下追加した例文 
    'I can\'t find my CD, can you bring some music please?',  # 重文の例
    #'Do you think he really knows you cannot swim?', targeted structure is 'MODAL +Subj' in main clause only  # 二重従属の例
  ],
  'negative': [
    'Which movie will you watch on Saturday?',
    'Where can I pick up my gown and cap?',
    'Who else would be at the party which will be held this Friday?',
    'I know you will be able to help me choose which dress fits me the best.',
    'They won\'t know the surprise until they get into the room.',
    'She told him that she could go to the gym with him.',
    'Who else do you think would be watching the World Cup right now?',
    'Is there any way I can succeed in this business?',
    'Do you know who else is going to have a class with Ms. Green?',
    'I did not expect her to show up at this meeting and I thought it was very bold.',
    'They will not be here next Tuesday because they are going to take a vacation.',
    'Which website can I get this plane ticket at the lowest price?',
    'He will not be asking many questions because he is a little shy.',
    'How many hours do you think you will work next week?',
    'I do not know anything about this topic, but I still disagree with violation of human rights.',
    'They should not know about this, because it is too much information.',
    'Which restaurant will you go to for lunch today?',
    'I might come back tomorrow evening and keep on working on the project.',
    'They would have no idea where they should go for a walk.',
    'He may be able to help me fix this trouble with my laptop.',
    'Are you going to sleep on your legs?',
    # 以下追加した例文
    'I can\'t find my CD, did you really leave it there?',  # 重文の例
    'What can you do for me?',  # 疑問代名詞WPの例
  ],
}
test_data_1052 = { 

      # **Guideword:** MAIN VERB 'BE'
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use main verb 'be' + subject to form 'yes/no' questions. 
        
  'positive': [
    'Are you sure about that?',
    'Is it ok to stay at your house?',
    # 'Am I correct?',
    # parser's problem: ROOT->Am(ROOT)
    'Is he angry?',
    'Are you free this afternoon?',
    # 'Is this your bag?',
    # parser's problem: ROOT->Is(ROOT)
    'Is it more important than your family?',
    'Are there any people over there right now?',
    'Are they happy about this?',
    'Is your sister crazy?',
  ],
  'negative': [
    'What is this?',
    'What are you doing?',
    'Who is this?',
    'Who are you talking with?',
    'Whom are you talking to?',
    'Where is he going?',
    'Where are you heading?',
    'How is it going?',
    'How are you doing?',
    'Why are you alone?',
    'Did you come to work yesterday?',
    'Did you have dinner yesterday?',
    'Will you come to my house tomorrow?',
    'Will you join us?',
    'Have you done anything special?',
    'Have you been to other countries before?',
    'Why don\'t you join us?',
    'Do you like to play baseball?',
    'Do you play any musical instruments?',
    'Does he like to play baseball?',
  ],
}
test_data_1053 = {
    # **Guideword:** MODAL VERBS
    # **Guideword type:** form
    # **Super category:** questions
    # **Sub category:** yes/no
    # **Lexical Range:** 2
    # **CEFR level:** A2
    # **CAN-DO:** Can use an increasing range of modal verbs + subject + main verb to form 'yes/no' questions.
    'positive': [
        "Will you come by bus?",
        "Will you come with any friends?",
        "Could you meet me at my home at 7 pm?",
        "Could you look for it?",
        "Would you like to go with me to the U2 concert?",

        "Will you come with me?",
        "Can I ask you something?",
        "Might I ask the president a question?",
        "May I borrow your pen, please?",
        "Can't John see Mary?",
        # "Can't John see Mary today?"はうまくいかない。
        "Won't you have another piece of cake?",
    ],
    'negative': [
        'Have you been to Tokyo?',
        'Have you been sick?',
        "I've just watched a football competition with my family and friends.",
        'Have you watched it?',
        'I left my mobile in your house, have you seen it?',

        "What will come of it?",
        "The best place is La Baule, which is Europe's biggest beach.",
        "It has the latest technology.",
        "It was the most expensive mobile phone in the shop.",
        'I have never tried it.',

        "I bought a beautiful pink skirt and a white top.",
        "Lysiane is taller than me and she has short black hair.",
        "It is a beautiful old city and there is an old wall around it.",
        "I left my small white bag.",
        "Don't forget to wear old, comfortable clothes.",

        "What have you done?",
        "Do you think you may go camping this summer?",
        "How old could Phillis possibly be, you ask.",
        "What can that mean?",
        "How dared he complain?",
    ],
}

test_data_1054 = { 

      # **Guideword:** LEXICAL VERBS WITH 'DO'
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use auxiliary 'do' + subject + main verb to form 'yes/no' questions. 
        
  'positive': [
    'Did you come to work yesterday?',
    'Did you have dinner yesterday?',
    'Do you like to play baseball?',
    'Do you play any musical instruments?',
    'Does he like to play baseball?',
    'Do I know you?',
    'Does she like you?',
    'Does your mother know that you didn\'t go to work yesterday?',
    'Does it make sense?',
    'Do you love her?',
  ],
  'negative': [
    'What do you like to do?',
    'What kinds of sports do you play?',
    'What did you do yesterday?',
    'What did he buy at that shop?',
    'What does he know about you?',
    'Where did you go yesterday?',
    'Where do you want to go?',
    'Where did you go last night?',
    'When do you wake up?',
    'When did you play baseball?',
    'Why don\'t you stay with us?',
    'Why do you think like that?',
    'Will you come to my house tomorrow?',
    'Will you join us?',
    'Have you done anything special?',
    'Have you been to other countries before?',
    'Why don\'t you join us?',
    'Are they happy about this?',
    'Is your sister crazy?',
    'Are you sure about that?',
  ],
}
test_data_1055 = { 

      # **Guideword:** AUXILIARY 'BE'
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use auxiliary 'be' + subject + the '-ing' form (continuous form) to form 'yes/no' questions.
        
  'positive': [
    'Are you doing ok?',
    'Are you going to school now?',
    'Is he eating lunch at the office?',
    'Is your father running in the park?',
    'Are you reading that book?',
    'Are you playing baseball this weekend?',
    'Are we watching the movie together?',
    'Are they bringing snacks to school?',
    'Is she listening to music?',
    # 'Am I doing correctly?',
    # parser's problem: ROOT->I(ROOT)
  ],
  'negative': [
    'Are you sure about that?',
    'Am I correct?',
    'Are you happy now?',
    'Is she sad?',
    'Do you play baseball?',
    'Do you usually stay here?',
    'Do they come to the class?',
    'Did she buy this cute bag?',
    'Does he walk here every day?',
    'Do you feel happy?',
    'What are you doing?',
    'Whom are you talking to?',
    'Where are you going?',
    'What is he eating?',
    'What are you thinking of?',
    'Did you play any sports before?',
    'Did you sleep well yesterday?',
    'Did she come with us?',
    'Did he go to the class yesterday?',
    'Did you use this laptop this week?',
  ],
}
test_data_1056 = {
    # **Guideword:** AUXILIARY 'HAVE'
    # **Guideword type:** form
    # **Super category:** questions
    # **Sub category:** yes/no
    # **Lexical Range:** none
    # **CEFR level:** A2
    # **CAN-DO:** Can use auxiliary 'have' + subject + the '-ed' form to form 'yes/no' questions.  ►  present perfect
    'positive': [
        'Have you been to Tokyo?',
        'Have you watched it?',
        "Has the postman called yet?",
        'I left my mobile in your house, have you seen it?',
        "Have you ever been to Iceland?",

        "Have you ever gone swimming at Coney Island?",
        "Has the post man been here yet?",
        "Have you gone skating yet this winter?",
        # "Has anybody ever been there?",
        "Has anybody been there?",
        "Have you ever met John?",
    ],
    'negative': [
        'Are you sick?',
        "I've just watched a football competition with my family and friends.",
        "Will you come by bus?",
        "Will you come with any friends?",
        "What will come?",
        "Could you meet me at my home at 7 pm?",

        "Could you look for it?",
        "Would you like to go with me to the U2 concert?",
        "Will you come with me?",
        "The best place is La Baule, which is Europe's biggest beach.",
        "It has the latest technology.",

        "It was the most expensive mobile phone in the shop.",
        'I have never tried it.',
        "I bought a beautiful pink skirt and a white top.",
        "Lysiane is taller than me and she has short black hair.",
        "It is a beautiful old city and there is the old wall around the city.",

        "I left my small white bag.",
        "Don't forget to wear old, comfortable clothes.",
        "What have you done?",
        "Did you ever visit a church before?",
        "Did they always come here?",
    ],
}
test_data_1057 = { 

      # **Guideword:** NEGATIVE QUESTIONS WITH 'BE'
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use main verb 'be' + 'n't' to form negative 'yes/no' questions.
        
  'positive': [
    # 'Weren’t you and Tom there?',
    # ROOT -> Were (ROOT)
    'Isn’t she something?',
    'Isn’t there lots of water in that region?',
    'Aren’t they angry?',
    'Isn\'t he busy now?',
    'Aren’t you a student?',
    'Isn’t she strict?',
    'Isn’t he a soccer player?',
    'Isn’t it expensive?',
    'Aren’t you happy?',
  ],
  'negative': [
    'Don’t you like classical music?',
    'Shouldn\'t we help that child?',
    'Doesn’t she play the guitar?',
    'Can’t you swim?',
    'Don’t you like sushi?',
    'Didn’t you go shopping yesterday?',
    'Didn’t they invite their boss to their wedding reception?',
    'Doesn’t he drink alcohol?',
    'Don’t they sell many parts?',
    'Won’t it be rainy tomorrow?',
    'Didn\'t she know it?',
    'Can’t we take a photo here?',
    'Didn’t they leave a lot of food?',
    'Don\'t you have dinner?',
    'Don’t you come with us?',
    'Won’t you go shopping tomorrow?',
    'Can’t you drink much?',
    'Don’t you know his name?',
    'Doesn\'t he play soccer?',
    'Won\'t he come to our party?',
  ],
}
test_data_1058 = { 

      # **Guideword:** NEGATIVE QUESTIONS, AUXILIARY VERBS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use auxiliary 'do' and 'have' + 'n't' + subject + main verb to form negative 'yes/no' questions. 
        
  'positive': [
    'Don’t you like classical music?',
    'Haven’t you come with us before?',
    'Don’t they sell many parts?',
    'Haven’t you heard his name?',
    'Doesn\'t he play soccer?',
    'Haven’t you eaten sushi once before?',
    'Didn’t you go shopping yesterday?',
    'Don\'t you have dinner?',
    'Hasn’t she ever played the guitar?',
    'Doesn’t he drink alcohol?',
  ],
  'negative': [
    'Wasn’t she sick last week?',
    'Aren\'t you tired?',
    'Can’t you swim?',
    'Shouldn’t she go there now?',
    'Isn’t there lots of water in that region?',
    'Aren’t you a student?',
    'Weren’t you and Tom there?',
    'Isn’t he a soccer player?',
    'Aren’t you happy?',
    'Can’t I go home?',
    'Isn\'t he busy now?',
    'Can’t we take a photo here?',
    'Won’t it be rainy tomorrow?',
    'Aren’t they angry?',
    'Won\'t he come to our party?',
    'Shouldn\'t we help that child?',
    'Isn’t it expensive?',
    'Isn’t she strict?',
    'Isn’t she something?',
    'Won’t you go shopping tomorrow?',
    'Can’t you drink much?',
  ],
}
test_data_1059 = { 

      # **Guideword:** NEGATIVE QUESTIONS MODAL VERBS
      # **Guideword type:** FORM
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use modal verbs + 'not' + subject + main verb to form 'yes/no' questions. 
        
  'positive': [
    'Can’t you swim?',
    'Can’t I go home?',
    'Won\'t he come to our party?',
    'Shouldn’t she go there now?',
    'Can’t we take a photo here?',
    'Shouldn\'t we help that child?',
    'Won’t you go shopping tomorrow?',
    'Can’t you drink much?',
    'Can’t Ken ski very well?',
    'Won’t it be rainy tomorrow?',
  ],
  'negative': [
    'Don’t you know his name?',
    'Didn’t you do your homework?',
    'Didn’t John use this computer?',
    'Weren’t you and Tom there?',
    'Didn’t they see the movie last night?',
    'Don’t you remember my birthday?',
    'Don’t you like eggs?',
    'Isn’t Bob a college student?',
    'Don\'t you have dinner?',
    'Doesn’t she play tennis?',
    'Isn’t she strict?',
    'Isn\'t he busy now?',
    'Isn’t he a soccer player?',
    'Don’t you like classical music?',
    'Isn’t it expensive?',
    'Aren’t you a student?',
    'Don’t you like sushi?',
    'Wasn’t this letter written in English?',
    'Aren’t they angry?',
    'Don’t they sell many parts?',
    'Aren’t you happy?',
  ],
}
test_data_1060 = { 

      # **Guideword:** SEEKING AGREEMENT
      # **Guideword type:** USE
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use negative 'yes/no' questions to involve the listener or reader by seeking agreement. 
        
  'positive': [
    'I think she likes you. Don\'t you get it?',
    'We will get married soon. Isn\'t it great?',
    'There are so many people who came for your birthday. Aren’t you happy?',
    'She replied to my letter. Isn\'t it amazing?',
    'He helped me with my homework. Isn\'t he nice?',
    'The movie was amazing. Don\'t you agree?',
    'He has a nice and expensive car. Isn\'t he cool?',
    'Many people helped me a lot. Isn\'t it wonderful of them?',
    'I got a 95 on the last exam. Isn\'t it good?',
    'It is crazy and I don\'t think I should do it. Don\'t you think so, too?',
  ],
  'negative': [
    'Can’t Ken ski very well?',
    'Can’t you swim?',
    'Don’t they sell many parts?',
    'Can’t you drink much?',
    'Aren’t you a student?',
    'Didn’t they see the movie last night?',
    'Didn’t John use this computer?',
    'Won’t you pass me the salt?',
    'Didn’t you do your homework?',
    'Didn’t Hiro go there?',
    'Won’t you have another cup of tea?',
    # 'Don’t you like classical music?',
    'Won\'t he come to our party?',
    # 'Aren’t you happy?',
    # 'Don’t you remember my birthday?',
    'Won’t you go shopping tomorrow?',
    # 'Don’t you know his name?',
    'Isn’t Bob a college student?',
    'Won’t you close the door?',
    # 'Don’t you like eggs?',
  ],
}
test_data_1061 = { 

      # **Guideword:** NEGATIVE QUESTIONS WITH 'NOT', EMPHASIS
      # **Guideword type:** FORM/USE
      # **Super category:** QUESTIONS
      # **Sub category:** yes/no
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can form negative questions with uncontracted 'not' to emphasise a point in an argument. 
        
  'positive': [
    'Have we not found a director yet?',
    'Did you not lock the windows?',
    'Are they not aware of the consequences?',
    'Has she not achieved her goal yet?',
    # parser error: have -> normal (dep)
    # 'Is it not normal for young girls to have a smartphone?',
    'Can we not talk about my divorced wife?',
    'Does Jack not have his own bike?',
    'Could you not cough in front of me?',
    'Do you not want a cup of lemonade?',
    'Did she not tell you about the change of policy?',
    'Is he not going with you to the store?',

  ],
  'negative': [
    'Liam wasn’t suited for the position anyways.',
    'The school is not open every Sunday.',
    'Lydia hasn’t completed her physics assignment yet.',
    'We are not sleeping at the park tonight.',
    'Rosa wasn’t at the board meeting yesterday.',
    'Jack did not explain to me the dangers of going to the river.',
    'Ken had not been to a casino before.',
    'The pedestrians were not aware of the car coming by.',
    'Wasn’t she on the movie we saw a while ago?',
    'The cat was not named after my aunt.',
    'She is not the victim here.',
    'Lucy was not familiar with the notion of individualism.',
    'The boy did not introduce himself to me.',
    'Not only did they go to Spain, but they also traveled around other countries in Europe.',
    'Aren’t we supposed to shut the curtains?',
    'Paul is not capable of hacking a computer.',
    'Russia is not next to Australia.',
    'It is not easy to ride a horse.',
    'Jessica definitely didn’t buy that ugly sweater.',
    'Lucy is not a full time student this year.',
  ],
}
test_data_1062 = { 

      # **Guideword:** 'LOOK FORWARD TO'
      # **Guideword type:** FORM/USE
      # **Super category:** VERBS
      # **Sub category:** phrasal-prepositional
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use 'look forward to' as a fixed expression followed by an '-ing' form or noun phrase, usually at the end of correspondence. 
        
  'positive': [
    'I am looking forward to our meeting.',
    'I look forward to receiving your application.',
    'Julia is looking forward to observing the museum.',
    'I look forward to working with Nancy.',
    'We look forward to visiting you in Spain.',
    'We look forward to serving you again.',
    'I look forward to baking cupcakes with you.',
    'I am looking forward to hearing stories of your youth.',
    'I look forward to spending some time with my cat this summer.',
    'I look forward to meeting your daughter tomorrow.',
    'Surprisingly, he looks forward to growing older.',
  ],
  'negative': [
    'There’s one more thing to look forward to.',
    'The mayor is looking to reduce the crime rate.',
    'Your letter has been forwarded to me from my former address.',
    'Mike is moving quickly forward with the work.',
    'Nurses look after patients in hospitals.',
    'I looked hard in the dark but couldn’t see anything.',
    'Shift your thinking forwards to the next generation.',
    'A lot of women still hesitate to come forward in domestic violence cases.',
    'Things are looking good for both Anna and Sophia.',
    'From that moment forward, Ben took his studies seriously.',
    'Look at the children playing in the garden.',
    'Jonathan is arriving at the airport around six.',
    'Please tell her that I am looking for her.',
    'You’re not looking quite yourself.',
    'My mom doesn’t look like she’s training dogs.',
    'You’re rather forward to say such things.',
    'My mother doesn’t like traveling abroad.',
    'I am excited about my birthday next month.',
    'I am looking for a math tutor.',
    'Our plans are going forward smoothly.',
  ],
}
test_data_1063 = { 

      # **Guideword:** VERB + PARTICLE + PREPOSITION + OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal-prepositional
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use a limited range of verbs + particle + preposition + noun or pronoun. 
        
  'positive': [
    'He looks down on us.',
    'You have to look out for other cars when you drive.',
    'I really look up to my grandfather.',
    'We have run out of tea.',
    'I\'d better stop now and get on with my studying.',
    'I can\'t keep up with the changes in the climate.',
    'She will come around to my opinion.',
    'He always comes up with a new idea.',
    'Do you get along with your host family.',
    'So you had better go walking or join a club, but don\'t forget to keep away from junk food.',
  ],
  'negative': [
    'Could you take out the trash?',
    'Pay attention to the ceiling.',
    'I brought her up when I was only a teenager.',
    'He looked at her.',
    'I will look into this problem.',
    'I can’t make out what you\'re saying.',
    'Do you believe in fairies?',
    'I caught sight of Tom in a crowd.',
    'I always look after my grandmother.',
    'We take part in the chorus contest.',
    'He agrees with her.',
    'Turn on the room light, please.',
    'He’s always bringing up the past.',
    'The airplane my sister was riding on took off.',
    'The referee added on 5 minutes for the stoppage time.',
    'He turned on the big radio.',
    'I called on my aunt three days ago.',
    'She ran away.',
    'She insists on women\'s rights.',
    'I think the paint smell brought her headache on.',
  ],
}
test_data_1064 = { 

      # **Guideword:** VERB + PARTICLE + PREPOSITION + OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal-prepositional
      # **Lexical Range:** 2.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use an increasing range of verb + particle + preposition + noun or pronoun.
        
  'positive': [
    'I must brush up on my French before going to Paris next month.',
    'She broke up with Daniel after dating him for five years.',
    'Don’t blow up at me, its not my fault.',
    'We should come up with a unique idea.',
    'Local authorities backed down on their threats to build on that part of the beach.',
    'When Ben saw the bear, he backed away from it.',
    'I hope you will back me up on this.',
    'Rioting broke out in the city after the government raised the fuel prices again.',
    'I will sleep in with your dog today.',
    'Several prisoners broke out of jail.',
  ],
  'negative': [
    'Tommy blew up the red balloon.',
    'The facts in the case just don’t add up.',
    'He applied for a scholarship for next semester.',
    'That company does not carry out tests on animals.',
    'How does this letter come across?',
    'I hope you can account for the time you were out.',
    'It took Kylie several hours to calm down.',
    'I’m banking on you to help with the charity event.',
    'She needs to work fewer hours; otherwise she will burn out.',
    'I advise against walking alone in this neighborhood.',
    'He appealed to the court to change its decision.',
    'Sara is bringing up her children by herself.',
    'A vacation of sunbathing doesn’t appeal to me.',
    'The police blocked off the street after the explosion.',
    'When the police started asking questions, the suspect clammed up.',
    'The light bulb burnt out.',
    'Jenna fell in the parking lot and blacked out.',
    'Burglars broke into my car last night.',
    'We need to allow for unexpected charges along the way.',
    'I was cleaning up and came across old photos of you.',
  ],
}
test_data_1065 = { 

      # **Guideword:** PHRASAL-PREPOSITIONAL VERB, STRANDED PREPOSITION
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal-prepositional
      # **Lexical Range:** None
      # **CEFR level:** C1
      # **CAN-DO:** Can use verb + particle + preposition, where the preposition is separated from its complement. ► Prepositions
        
  'positive': [
    'I should tell you about the person I look up to.',
    # a pronoun should not exist between verb and particle
    #'I\'ll tell you where to drop me off at.',
    'That is the house I moved out of.',
    'Choose wisely which friends to hang out with.',
    'Tell me where you\'re going to set off to.',
    'What time should I wake up at?',
    'What time did you get up at?',
    'What did you come up with?',
    'That is the dorm which Sophie moved out of.',
    'My father is someone I have to put up with.',
  ],
  'negative': [
    'Many couples do not want to take on the responsibility of bringing up a family.',
    'Could you look after my bag while I go and buy the tickets?',
    'Do you get on with your neighbors?',
    'What time did you wake up this morning?',
    'She fixed us up with a violin teacher.',
    'She brought up three kids all alone.',
    'We\'d better set off before the rush-hour traffic starts.',
    'Do you always look up every new word in a dictionary?',
    'We just put the accident down to bad luck.',
    'The taxi broke down on the way to the airport and I thought I nearly missed my flight.',
    'The lecture went on till 6 o\'clock.',
    'Somebody broke into his car and stole his radio.',
    'We need to sort the problem out.',
    'He\'ll catch up with us in a minute.',
    'It\'s difficult to make out what she is saying.',
    'The plane took off an hour late.',
    'The book first came out in 1997.',
    'The team only had an hour to put the stage up before the concert.',
    'We look forward to meeting you on the 22nd.',
    'Do you want me to take off my shoes?',
  ],
}
test_data_1066 = { 

      # **Guideword:** VERB + DIRECT OBJECT + PARTICLE + PREPOSITION + OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal-prepositional
      # **Lexical Range:** None
      # **CEFR level:** C2
      # **CAN-DO:** Can use a direct object with some prepositional verbs as well as an object of the preposition.
        
  'positive': [
    'She brought the new design up at the meeting.',
    'My mother brought three kids up in a small apartment.',
    'It was at that time that our future business partner let us in on the secret.',
    'The team put the stage up before the concert.',
    'It’s difficult to make the handrwriting out in his letter.',
    'Carrie and Liz need to sort the problem out in their code.',
    'There are people giving chocolate out at the table over there.',
    'My grandma used to put food out for the cats.',
    'They handed their voucher in at the front desk.',
    'The journalist thought the story over at his desk with a cup of coffee.',
  ],
  'negative': [
    'Don’t put the garbage on the dining table.',
    'Dealing with a financial crisis is not easy.',
    'Olives are one of my favorite vegetables.',
    'I should move the snow from the pathway.',
    'You need to wake up earlier than today.',
    'Coping with Olivia is so difficult.',
    'Looking down on others is considered to be rude.',
    'Many people are implicated in the affair.',
    'The police are certain to get him in the end wherever he may go.',
    'I was determined not to give up.',
    'I don’t speak Spanish or French.',
    'Putting up with four kids is genuinely tiring.',
    'My grandfather scrubbed behind the freezer.',
    'I tidied up the room before my mom came back.',
    'Leslie is not a vegetarian anymore.',
    'Tidying up the car is not very pleasant.',
    'The teacher didn’t let us talk about the issue in class.',
    'Katie switched the computer on.',
    'We are not many days from the examination.',
    'Cleaning the washing machine is something I do very often.',
  ],
}
test_data_1067 = { 

  # **Guideword:** VERB + PREPOSITION + OBJECT
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** prepositional
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of prepositional verbs followed by noun or pronoun objects. 
    
  'positive': [
    'Just over the top of the hill, they came across settlements.',
    'They looked for mushrooms among the trees.',
    'I did not agree with him, but his ideas sound legit to most people.',
    'Did you think of an idea?',
    'The wall will be covered with paint.',
    'The city insisted on building towers near the river.',
    'Where will you meet with Mandy tomorrow afternoon?',
    'We listen to music every day at the breakfast table.',
    'You should not interfere with things that don\'t concern you.',
    'I had to go through archives for the correct pages.',
    'I could not think of anything when I saw her.',
    'When you stand on tables, you make them dirty.',
  ],
  'negative': [
    'Help him with moving the drawer!',
    'They accused me of losing the key for their room.',
    'He added more chips to the dish.',
    'What he talked about in the meeting was so irrelevant to the issue.',
    'Can you let me do my assignment on my own?',
    'What are you going to get there?',
    'All of them heard the sound of the fire alarm although they were far from their dormitory.',
    'Would you be able to buy some spinach for the dinner tonight?',
    #Tagger error (IN like)
    # 'They always forget that I do not really like oatmeal at all.',
    'I was at Grand Station, but I did not know where to go next.',
    'Why do you think you need a driver\'s license?',
    'I bought a huge cotton candy that I could not possibly finish.',
    'They did not pay attention to what their teacher said.',
    'Where should I go to get a new television for my apartment?',
    'This is one of the best songs I have ever heard.',
    'We could not agree to buy the new desks.',
    'When I heard the news, I was so worried.',
    'Whichever choices you make, you are going to succeed.',
    'Do you know how to automate tasks?',
    'If it does not work, you do not need to pay at all.',
    'I think that I can find some in the Dollar Store.',
  ],
}
test_data_1068 = { 

      # **Guideword:** VERB + PREPOSITION + OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** prepositional
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of prepositional verbs followed by noun or pronoun objects.
        
  'positive': [
    'Turn to the left, please.',
    'In fact, our company needs to train some staff on how to deal with the complaints of customers.',
    'I believe in the power of democracy.',
    'She insists on women\'s rights.',
    'Whenever you hear this sound, look to the skies to make sure everything is alright.',
    'He agrees with her.',
    'He looked at her.',
    'I always end up looking for my grandmother.',
    'If you need more information, please look at the information sheet at the entrance.',
    'He stared at the wall.',
    'We’ll think about ideas for a new marketing campaign and see what we can come up with.', # think about ideas
  ],
  'negative': [
    'Monica was so excited when John asked her to go out with him.',
    'I am looking forward to meeting you next week.',
    'Jacob always has his professional experience to fall back on.',
    'I think the paint smell brought her headache on.',
    'She will come around to my opinion.',
    'John brings years of professional experience to the party.',
    'He always comes up with a new idea.',
    'I get along with my colleagues.',
    'He looks down on us.',
    'I can\'t keep up with the changes in climate.',
    'Please put your clothes away; they are lying all over the floor.',
    'We take part in the chorus contest.',
    'Pay attention to the ceiling.',
    'Sorry for the interruptions, please carry on with your story.',
    'I really look up to my grandfather.',
    'We should do away with these old rules.',
    'You have to look out for other cars when you drive.',
    'Do you get along with your host family.',
    'We have run out of tea.',
  ],
}
test_data_1069 = { 

      # **Guideword:** PREPOSITIONAL VERB, STRANDED PREPOSITION
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** prepositional
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use verb + preposition, where the preposition is separated from its complement. 
        
  'positive': [
    'We can’t agree on which grant we should apply for.',
    'That book is too valuable to part with.',
    'This is what I have been looking for.',
    'Her apartment was broken into.',
    'She says love is worth killing for.',
    # this is JJ + PREP
    #'What kind of music are you interested in?',
    'What are you talking about?',
    'This bed looks as if it has been slept in.',
    'Alice had no one to play with.',
    'There aren’t any that I know of.',
  ],
  'negative': [
    'I still don’t understand why it’s such a big deal that she went to prom with him.',
    'Someone broke into her apartment.',
    'I only know anything about this one thing.',
    'I must brush up on my French before going to Paris next month.',
    'From there, it’ll take about half an hour to our house.',
    'The operation was done for the best reasons.',
    'Gail has much about which to be happy.',
    'I’m banking on you to help with the charity event.',
    'She was under a great deal of pressure.',
    'That company does not carry out tests on animals.',
    'I advise against walking alone in this neighborhood.',
    'They’ve moved back into the country.',
    'Burglars broke into my car last night.',
    'I told you about this book earlier.',
    'Gina is a friend of mine.',
    'Local authorities backed down on their threats to build on that part of the beach.',
    'She was a fine manager, one who was admired by them all.',
    'Rioting broke out after the government raised the fuel prices again.',
    'To whom were you talking?',
    'Sara is bringing up her children by herself.',
  ],
}
test_data_1070 = {

      # **Guideword:** VERB + ADVERB + PREPOSITION
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** prepositional
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use an adverb between the verb and the preposition.
        
  'positive': [
    'Jemma glanced uneasily at me.',
    'She arrived early for the meeting.',
    'I write regularly in my journal.',
    'Nina is dancing weirdly by the tree.',
    'The children love to play outside with the dogs.',
    'I drive occasionally for my sisters.',
    '“I don’t think you want to hear this story,” he said wickedly to Emma.',
    'We cheered loudly to support the team.',
    'We need to look carefully at the graphs.',
    'I went upstairs with my grandma.',
  ],
  'negative': [
    'Before I discovered this bar, I used to go home.',
    'I prefer to read in the library.',
    '“Stop singing in the shower!” my sister screamed loudly.',
    '“I need to buy new clothes,” my cousin said quietly.',
    'He displayed cruelty towards his dog.',
    'He swam across the pool.',
    'Mike traveled across America on his motorcycle.',
    'I don’t agree with your claim.',
    'I was born after the Great War ended.',
    'The police held an inquiry into the murder.',
    'Easter falls in spring every year.',
    'The train passes through the tunnel.',
    'I learned how to ski during the holidays.',
    'At the party, I had too much to drink.',
    'My wife curiously asked me what I was doing.',
    'We will meet at the airport.',
    'She went to the bowling alley every Friday last summer.',
    'He climbed up the ladder to get into the attic.',
    'Jasmine quietly walked out of the room.',
    'Florence finally announced his engagement.',
  ],
}
test_data_1071 = { 

      # **Guideword:** REPORTING VERBS + DIRECT OBJECT 'THAT'-CLAUSE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** patterns_that clauses
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of verbs, typically reporting, with a 'that'-clause as the direct object. 
        
  'positive': [
    'We hope that you will get better soon.',
    'She thinks that I am handsome.',
    'I saw that you and she walked together.',
    'I thought that you would come today.',
    'I heard that you are pretty famous among students.',
    'We wish that everything will be fine.',
    'She said that I couldn\'t work in her office.',
    'I saw that one of my friends brought a laptop in the class.',
    'You said that you could come to the party tonight.',
    'I heard that she stole your camera.',
  ],
  'negative': [
    'I would say it is crazy.',
    'I hope to see you again.',
    'It is obvious that John is honest.',
    'I could see what is going on.',
    'She thinks the same as you.',
    'I didn\'t say anything.',
    'The fact that it had a happy ending was immaterial to me.',
    'I should have said that before.',
    'This is the best hotel that I know.',
    'I think it will be fine.',
    'I don\'t want to say about this issue right now.',
    'I\'m not sure whether he hears it or not.',
    'I know nothing except that he was found dead.',
    'She is saying something about you.',
    'I saw you at the library.',
    'You can\'t think anything right now.',
    'I don\'t remember where I saw her.',
    'I haven\'t thought about it yet.',
    'She heard some strange sounds.',
    'She hopes to play baseball well someday.',
    'I do think about you.',
    'I hear the voice.',
    'I saw someone who just ran away.',
    'She saw me playing baseball at the stadium.',
  ],
}
test_data_1072 = { 

      # **Guideword:** VERBS + DIRECT OBJECT CLAUSE WITHOUT 'THAT'
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** patterns_that clauses
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use reporting verbs, especially mental process verbs, with a clause as the direct object, without 'that', especially in informal contexts. 
        
  'positive': [
    'I thought you would come today.',
    'She thinks I am handsome.',
    'I saw one of my friends brought a laptop in the class.',
    'We hope you will get better soon.',
    'We wish everything will be fine.',
    'She said I couldn\'t work in her office.',
    'I heard you are pretty famous among students.',
    'You said you could come to the party tonight.',
    'I heard she stole your camera.',
    'I think it will be fine.',
    'I would say it is crazy.',
  ],
  'negative': [
    'I would say that it is crazy.',
    'I saw that you and she walked together.',
    'I hope that I see you again.',
    'I don\'t want to speak about this issue right now.',
    'I haven\'t thought about it yet.',
    'She heard some strange sounds.',
    'I\'m not sure whether he hears it or not.',
    'The fact that it had a happy ending was immaterial to me.',
    'I should have said that before.',
    'I know that you could kill me anytime.',
    'I hear the voice.',
    'She said something about you.',
    'You can\'t think anything right now.',
    'I saw you at the library.',
    'She knew that I was the only one who could help me.',
    'She saw me playing baseball at the stadium.',
    'I saw someone who just ran away.',
    'You know that I like you more than anyone.',
    'I knew that these incidents would happen.',
    'I didn\'t say anything.',
  ],
}
test_data_1073 = { 

      # **Guideword:** VERBS + INDIRECT OBJECT CLAUSE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** patterns_that clauses
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use verbs, typically reporting verbs, followed by a noun or pronoun as the indirect object and a clause with or without 'that', as the direct object.
        
  'positive': [
    'I told my father that I got new bags for the next trip.',
    'I told her she could fly if she tries.',
    'She tells you she can come home.',
    'I could promise you that I can meet you someday.',
    'You told me that you would come to the party tonight.',
    'I promise you that I will give your cell phone back.',
    'She promises her friends she will go on a date with me.',
    'You promised me you would buy the birthday gift for me.',
    'She would like to promise me that she is going to eat dinner with me.',
    'She told me that I am famous among young people.',
  ],
  'negative': [
    'We hope that you will get better soon.',
    'She thinks that I am handsome.',
    'I would say it is crazy.',
    'I saw that you and she walked together.',
    'I thought that you would come today.',
    'I heard that you are pretty famous among students.',
    'I hope to see you again.',
    'She hopes to play baseball well someday.',
    'I don\'t want to say about this issue right now.',
    'I could see what is going on.',
    'I should have said that before.',
    'She said something about you.',
    'We wish that everything will be fine.',
    'She said that I couldn\'t work in her office.',
    'I saw that one of my friends brought a laptop into the classroom.',
    'You said that you could come to the party tonight.',
    'I don\'t remember where I saw her.',
    'I heard that she stole your camera.',
    'I think it will be fine.',
    'I didn\'t say anything.',
    'It is said that this theorem is independent from this axiom.',
  ],
}
test_data_1074 = { 

      # **Guideword:** REPORTING VERBS + DIRECT OBJECT 'THAT'-CLAUSE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** patterns_that clauses
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of verbs, typically reporting or mental process verbs, with a 'that'-clause as the direct object. 
        
  'positive': [
    'I realize that I like you every time we meet.',
    'I understand that there are various training times.',
    'I understand that it is a difficult request.',
    'I realize that I am falling in love.',
    'I realize that I am not alone.',
    'I understand that you need to pay for that.',
    'I understand that he used to support this bill.',
    'We realize that life is a competition for survival.',
    'I understand that you can\'t attend that meeting.',
    'I realize that you will pass.',
  ],
  'negative': [
    'I think I will try to realize that.',
    'I also hope strongly for that.',
    'I will think over what I have done.',
    'You realize that is funny.',
    'He doesn\'t realize I know that.',
    'We do not hope for that.',
    'Who do you think you are talking to?',
    'I understand that completely.',
    'I don\'t understand the difference that well yet.',
    'You don\'t realize that danger.',
    'I would rather think so.',
    'My hope is just that.',
    'I cannot understand that reasoning.',
    'I think it\'s good.',
    'They probably realize that too.',
    'What do you think of it?',
    'I hope you like that tea too.',
    'I\'ll think about it.',
    'I have come to understand that well.',
    'I think I\'ll draw something.',
  ],
}
test_data_1075 = { 

      # **Guideword:** VERBS + PREPOSITIONAL PHRASE + 'THAT'-CLAUSE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** patterns_that clauses
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use some reporting verbs with a prepositional phrase followed by a 'that'-clause as the direct object.
        
  'positive': [
    'You said to your parents that you would wait.',
    'I think to myself that she will come.',
    'I was told by my friend that I look like a bear.',
    'It is taught to students that they should always tell the truth to the teachers.',
    'I said to the students that we should try to understand and learn from our mistakes.',
    'He said to him that it was nine o\'clock.',
    'I said to you that I looked like my dad.',
    'He said to his wife that he was hungry.',
    'When I said to my friends that I had met with him, they didn\'t believe me.',
  ],
  'negative': [
    'They said that I was wise.',
    'I should have said.',
    'He said so at the lecture.',
    'He said to watch out.',
    'The same thing can be said of him.',
    'Just as you said it.',
    'I said it in jest.',
    'There\'s something to be said for both arguments.',
    'That\'s well said.',
    'I never said a word.',
    'You just said a mouthful',
    'I saw it just now.',
    'I saw her face in profile.',
    'I saw the email today.',
    'I never saw him after that.',
    'I saw him at the office.',
    'I saw a rainbow.',
    'The less said about it the better.',
    'I saw a blue bird.',
    'I saw stars.',
    'We saw something white.',
  ],
}
test_data_1076 = { 

      # **Guideword:** NO OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of phrasal verbs without an object.
        
  'positive': [
    'I will take off soon.',
    'The game will be called off.',
    'I already gave up a long time ago.',
    'You can probably find out by googling this phrasal verb.',
    'She normally wakes up late.',
    'The airplane my sister rode on took off.',
    'The solution will turn up soon.',
    'Did they make up yet?',
    'Many people came out on that day.',
    'I grew up in the forest.',
  ],
  'negative': [
    'She insists on women\'s rights.',
    'He agrees with her.',
    'We take part in the chorus contest.',
    'Change the lightbulb, please.',
    'Do you believe in fairies?',
    'I am looking forward to seeing you this autumn.',
    'I can pick you up at the airport.',
    'Pull into that gas station.',
    'I always look after my grandmother.',
    'I called on my aunt three days ago.',
    'You totally look like your mother.',
    'We did away with the old rules.',
    'Let\'s go out for dinner.',
    'I brought her to the store.',
    'I caught sight of Tom in a crowd.',
    # 'I have looked up to the teacher since I was a junior high school student.',
    # parser: look->teacher(nmod:to)
    'He doesn\'t come across as honest.',
    'I can\'t figure out this writing.',
    'Pay attention to the ceiling.',
    'I never got over you.',
  ],
}
test_data_1077 = { 

      # **Guideword:** VERB + PRONOUN + PARTICLE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 1.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use a limited range of phrasal verbs + object pronoun + particle. 
        
  'positive': [
    'I’ll pay you back as soon as I get the loan.',
    'I will figure it out by myself.',
    # 'I can’t get this out of my shirt.',
    # parser: out -> of (compound)
    'I brought her up at the meeting.',
    'I hope you’ll back me up on this.',
    'I can pick you up at the airport.',
    'I’ll check it out for you.',
    'You helped him out in a tough situation.',
    'You can throw this away if you don\'t need it.',
    'Could you take it out?',
  ],
  'negative': [
    'She normally wakes up late.',
    'Your parents used up all the coffee.',
    'Many people came out on that day.',
    'I think you should sit down.',
    'We did away with the old rules.',
    'I don’t think she’ll show up tonight.',
    'I’m so glad I ran into you.',
    'I was raised in the forest.',
    'You totally look like your mother.',
    'We’ve run out of milk.',
    'She insists on women\'s rights.',
    'I always look after my grandmother.',
    'He ran away from home and joined the circus.',
    'You can probably find out by googling this phrasal verb.',
    'The plane will take off as soon as the fog lifts.',
    'Pay attention to the ceiling.',
    'I already gave up a long time ago.',
    'He agrees with her.',
    'Do you believe in fairies?',
    'The airplane my sister rode on took off.',
  ],
}
test_data_1078 = { 

      # **Guideword:** NO OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of phrasal verbs without an object.
        
  'positive': [
    'Its battery had run out.',
    'The oil tank blew up.',
    'We decided to carry on.',
    'Because of the bad weather, the game was called off.',
    'Many things are going on.',
    'I have to wake up.',
    'He entered the room and sat down.',
    'I needed to hang out because my life was too jam-packed and hectic.',
    'I have never given up.',
    'The airplane my sister rode on took off.',
  ],
  'negative': [
    'I have looked up to the teacher since I was a junior high school student.',
    'We take part in the chorus contest.',
    'She insists on women\'s rights.',
    # 'I really look up to him.',
    # up -> him (nmod:to)
    'He won’t own up to his mistakes.',
    'You need to cut down on chocolate.',
    'We did away with the old rules.',
    'I want to get on well with him.',
    'Pay attention to the ceiling.',
    'I’m breaking up with him.',
    'I can’t make out what you say.',
    'He turned on the big radio.',
    'The car accident broke out at the crossing in winter.',
    'Turn on the room light, please.',
    'I caught sight of Tom in a crowd.',
    'He agrees with her.',
    'I called on my aunt three days ago.',
    'I am looking forward to seeing you this autumn.',
    'Do you believe in fairies?',
    'I always look after my grandmother.',
  ],
}
test_data_1079 = { 

      # **Guideword:** VERB + PARTICLE + OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 1.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use a limited range of phrasal verbs + particle + object.
        
  'positive': [
    'Were it not for my university, I would give up this class immediately.',
    'Do you believe in fairies?',
    'I ran into Steve at the store today.',
    'I switched on the television.',
    'I was walking to the office and ran into the bookshelf.',
    'It took me a long time to get over the flu.',
    'I called on my aunt three days ago.',
    'She turned off the phone and walked to the bathroom.',
    'I am looking for my keys.',
    'I always look after my grandmother.',
  ],
  'negative': [
    'We will have to stand up for our rights someday.',
    'He is the one who I ran into.',
    'He entered the room and sat down.',
    'He comes across as a bit rude.',
    'Could you hang on for a second?',
    'I have to wake up.',
    'We decided to carry on.',
    'This is what I was looking for.',
    'Many things are going on.',
    'I will call her back.',
    'She cheered up after hearing the good news.',
    'I think Mari is holding something back.',
    'She came to pick me up.',
    'The oil tank blew up.',
    'He is the one who I look up to the most.',
    'Because of the bad weather, the game was called off.',
    'The car accident broke out at the crossing in winter.',
    'The airplane my sister rode on took off.',
    'This new restaurant has not lived up to our expectations.',
    'I have never given up.',
    'You take a cooking class every month, and in today’s class you are going to learn how to prepare moules marinière.',
  ],
}
test_data_1080 = { 

      # **Guideword:** VERB + PRONOUN + PARTICLE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 2.0
      # **CEFR level:** B1
      # **CAN-DO:** Can use an increasing range of phrasal verbs + object pronoun + particle. 
        
  'positive': [
    'I will call her back.',
    'I think Mari is holding something back.',
    'He wanted to watch TV, so he turned it on.',
    # 'I have to give these back to Franz before his hockey game.',
    # back -> these (det)
    'I have to give them back to Franz before his hockey game.', # これなら通る
    'Please wake me up at 8.',
    'I figured it out.',
    'She always cheers me up.',
    'She came to pick me up at the airport.',
    'I\'m going to try them on, but I don\'t think they will fit.',
    # 'Please that off in the temple.',
    # Please -> that (dep)
  ],
  'negative': [
    'This new restaurant has not lived up to our expectations.',
    'He agrees with her.',
    'Because of the bad weather, the game was called off.',
    'It took me a long time to get over the flu.',
    'We decided to carry on.',
    'We will have to stand up for our rights someday.',
    'He comes across as a bit rude.',
    'Many things are going on.',
    'I was walking to the office and ran into the bookshelf.',
    'The oil tank blew up.',
    'I ran into Steve at the store today.',
    'I switched on the television.',
    'Do you believe in fairies?',
    'This is what I looked for.',
    'I have to wake up.',
    'The airplane my sister rode on took off.',
    'He entered the room and sat down.',
    'He is the one who I ran into.',
    'I have never given up.',
    'My sister got back at me for stealing her shoes.',
  ],
}
test_data_1081 = { 

      # **Guideword:** NO OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 3.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use a wide range of phrasal verbs without an object.
        
  'positive': [
    'He\'s about to go back.',
    'My car broke down and I had to take it to the mechanic.',
    'They broke up after she saw him with Lucia.',
    'I had a headache when I woke up.',
    'I think I am too young to settle down.',
    'He finally decided to settle down.',
    'If you want help, I can come over.',
    'Maria and Peter have broken up.',
    'My job doesn’t have a high salary, but it’s enough to get by.',
    'She should drop by.',
    'If anyone has any information, please come forward.',
  ],
  'negative': [
    'Soon he is going back to Russia.',
    'We\'re looking forward to the concert.',
    'I woke up with a headache.',
    'They plan to settle down as a family.',
    'Please come over to my house.',
    'I want to go soon.',
    'I would like to sleep in the near future.',
    'My mother brought up that little matter of my prison record again.',
    'She filled up the grocery cart with free food.',
    'The filling station was giving away free gas.',
    'You shouldn’t stand people up.',
    'In my country, women never ask men out.',
    'You need to fill out this form to register for the course.',
    'She found out that he had been cheating on her for three months.',
    'He felt nervous about asking Jo out.',
    'I waited for her for half an hour before I realized she had stood me up.',
    'Bob is not her usual type, but she fell for him after dating for a couple of months.',
    'I threw away the old pizza.',
    'They have been dating each other for five years when he asked her to marry him.',
    'They called off this afternoon’s meeting.',
    'He promised to spend more time with his son but he let him down.',
    'The terrorists tried to blow up the railroad station.',
    'He fell for Lucy on the first date.',
    'I am going to cut out fast food this year.',
    'If you ever let me down again I will leave you.',
    'Is she really dating him?',
    'They will pick John up from the airport.',
  ],
}
test_data_1082 = { 

      # **Guideword:** VERB + PARTICLE + OBJECT
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 3.0
      # **CEFR level:** B2
      # **CAN-DO:** Can use a wide range of phrasal verbs + particle + object. 
        
  'positive': [
    'I threw away the old pizza.',
    'The terrorists tried to blow up the railroad station.',
    'She hung up the phone before she hung up her clothes.',
    'The students handed in their papers and left the room.',
    'She filled up the grocery cart with free food.',
    'I hate to hold up the meeting.',
    'You need to fill out this form to register for the course.',
    'They called off this afternoon’s meeting.',
    'My mother brought up that little matter of my prison record again.',
    'Fill out this application form and mail it in.',
  ],
  'negative': [
    'He really liked Lucy from the first blind date.',
    'He settled down as a farmer with a family.',
    'You can come over to my house after school.',
    'You have misspelled this word again so you’d better look it up.',
    'In my country, women never ask men out.',
    'They broke up after she saw him with Lucia.',
    'Don’t just throw it away.',
    'He is going back to Russia next month.',
    'I waited for her for half an hour before I realized she had stood me up.',
    'Sarah dropped by to return the book I had lent her.',
    'My job doesn’t have a high salary, but it’s enough to get by.',
    'The filling station was giving free gas away.',
    'He was turned down both times.',
    'It isn’t easy to bring such topics up nowadays.',
    'My car broke down and I had to take it to the mechanic.',
    'The teacher called students in the back row.',
    'He promised to spend more time with his son but he let him down.',
    'Write them down before you forget.',
    'We put money away for our retirement.',
    'It seemed strange to see my old boss waiting tables.',
  ],
}
test_data_1083 = { 

      # **Guideword:** VERB + NOUN + PARTICLE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use phrasal verbs + nouns as object + particle.
        
  'positive': [
    'The students handed their papers in and left the room.',
    'You have misspelled this word again so you’d better look it up.',
    'You need to fill this form out to register for the course.',
    'She filled the grocery cart up with free food.',
    'The lawyers looked the papers over carefully.',
    'The filling station was giving free gas away.',
    'She made a story up about going to the movies with her friends.',
    'I have a feeling he’s not about to give it back.',
    'Write them down before you forget.',
    'You have to do this paint job over.',
  ],
  'negative': [
    'He was turned down both times.',
    'Don’t just throw away those photos.',
    'The teacher called on students in the back row.',
    'Grandpa couldn’t hear, so he turned up his hearing aid.',
    'They called off this afternoon’s meeting.',
    'I tried four cars before I could find the one that pleased me.',
    'We turned off the lights before anyone could see us.',
    'We put away money for our retirement.',
    'As we drove through Paris, Jean pointed out the major historical sites.',
    'My dad promised to look after my dog while I was gone.',
    'My mother brought up that little matter of my prison record again.',
    'Fill out this application form and mail in the rest of the documents.',
    'I was so hot and I had to took off my shirt.',
    'My second son seems to take after his mother.',
    'She hung up the phone before she hung up her clothes.',
    'The students went over the material together before the exam.',
    'My wife set up the living room exactly the way she wanted it.',
    'It seemed strange to see my old boss wait on tables.',
    'It isn’t easy to bring up children nowadays.',
    'The terrorists tried to blow up the railroad station.',
  ],
}
test_data_1084 = { 

      # **Guideword:** VERB + PRONOUN + PARTICLE
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** phrasal
      # **Lexical Range:** 3.0
      # **CEFR level:** C1
      # **CAN-DO:** Can use a wide range of phrasal verbs + object pronoun + particle. 
        
  'positive': [
    'He said he would turn us in if he catches us again.',
    'If there is something we don\'t know, we should look it up.',
    #'We should keep him away from Jasmine.',
    'Eat it up before you run out of time.',
    'Turn it on so that we can read.',
    'She brought it up in front of everyone.',
    'Let\'s tear it off before sunrise.',
    'She cut her off the team.',
    'I took them off because they were uncomfortable.',
    'Cassie and I need to work this out.',
  ],
  'negative': [
    'She brought up three kids all alone.',
    'He\'ll catch up with us in a minute.',
    'The plane took off an hour late.',
    'Let\'s work out together, if you\'re free.',
    'We\'d better set off before the rush-hour traffic starts.',
    'Choose which friends to hang out with.',
    'My father is someone I have to put up with.',
    'Let\'s turn around before its too late.',
    'Do you always look up every new word in a dictionary?',
    'We should hang up since its midnight now.',
    'Somebody broke into his car and stole his radio.',
    'Don\'t give away too much information.',
    'Tell me where you\'re going to set off to.',
    'The team only had an hour to put the stage up before the concert.',
    'I take back what I said earlier.',
    'Many couples do not want to take on the responsibility of bringing up a family.',
    'I\'ll tell you where to drop the children off at.',
    'The taxi broke down on the way to the airport and I thought I nearly missed my flight.',
    'It\'s difficult to make out what she is saying.',
    'That is the dorm which Sophie moved out of.',
  ],
}
test_data_1085 = { 

  # **Guideword:** MAIN VERBS
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** types
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use regular and irregular main verbs in simple verb phrases. ► present simple ► past simple
    
  'positive': [
    'She is from London.',
    'I went shopping the day before yesterday.',
    'He sent me a letter telling me how much effort he put on the project.',
    'They did not conduct research that afternoon at all.',
    'I see you there.',
    'Did you go to the hospital yesterday afternoon after that?',
    # parser error was -> like (aux)
    # 'How was the weather on that day like?',
    'We asked our professor to extend the deadline for the assignment.',
    'My colleague never argued with me about the issue.',
    'Charlie does not like talking to people in person.',
  ],
  'negative': [
    'Can you help me with that?',
    'I would never have tried to understand her.',
    'Will you go to the fancy restaurant this afternoon?',
    'May I ask you to go to the restaurant with me tomorrow around noon?',
    'Are you going to ask her to let them use her machine?',
    'He would always ask her that.',
    'You might want to choose this way to finish every task efficiently.',
    'They will not let me use that.',
    'I could get a silver ring from the store.',
    'Where can I find these dishes?',
    'What must I do to complete the assignment?',
    'You will end the war, won\'t you?',
    'I still cannot understand why she would not try to do new things.',
    'I could have said so at that moment.',
    'Will you plan to go to the basketball game?',
    'Would you be able to carry this water bottle to upstairs?',
    'They would have never expected that result.',
    'We can have a meeting on Tuesday instead of Monday.',
    'My brother must tell me what he could have done to them.',
    'My professors will go to Senegal for research.',
    'Charlie cannot talk to me like that.',
  ],
}
test_data_1086 = { 

  # **Guideword:** LINKING VERB, 'BE'
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** types
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use linking verb 'be'. 
    
  'positive': [
    # 'She was welcoming.',
    # 進行形判定が出てうまくいかない
    'I like the room because the smell of the room is oak.',
    'His wallet is golden because he heard something about how gold attracted money.',
    # 'Is it his house or similar house on the different street?',
    # parser error?
    'It\'s good to hear about his amazing accomplishment.',
    'She has never given up, which is her strength.',
    'Never open your wallet in front of strangers because it is dangerous.',
    'Her life was as beautiful as a story.',
    'Listening to the song is very helpful to get through the difficulties.',
    'What do you think is the best way to solve this problem.',
    'I am glad to see you.',
    'We are Exiles, and most of our kindred have long ago departed.',
    'They will not let you down, and there is nothing to feel worried about.',
    'Were I a little bird, I\'d fly to you.',
    'He was on Madison Street and having a photo shoot.',
  ],
  'negative': [
    'I found my way on my own, and you do not need to mind.',
    'I kept watching this funny video at least ten times continuously.',
    'The air conditioner in my room got broken yesterday, and I do not know how to survive.',
    'You might feel the pain, but you should not move yet.',
    'Have you taken any medication?',
    'She asked me where I was going since she just told me to sit still.',
    'Where do you think he found these resources?',
    'Did you have a weird dream that a hamburger told me what to do?',
    'Now I see a rainbow in the sky.',
    'Would you mind helping me learn how to let kids draw as they like?',
    'Didn\'t you expect him to show up at the station to welcome you?',
    'You might want to purchase a bus ticket to Pennsylvania  Station at this office.',
    'He seems like one of the most underestimated artists.',
    'I am going to travel to Toronto this summer with my siblings.',
    'Were you going to learn how to speak Hindi before you got to India?',
    'Learn how to dance so that you can communicate with everyone without learning a single word.',
    # 'They think we cannot be at the top of the building, but actually, we can.',
    # これ微妙ですね。課題文通り「beをlinking verbとして使う」を厳守すると、動作動詞の意味になるこの文は確かにアウトな気もします
    # ただパーサーだと普通にcopula文判定がでます。
    'I was calling the front desk to make sure that they would fix the issue I had with the room.',
    'He lifted his head to look at her.',
  ],
}
test_data_1087 = { 

  # **Guideword:** AUXILIARY VERB 'BE'
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** types
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use auxiliary verb 'be'. ►  present continuous
    
  'positive': [
    'I am speaking out on behalf of these people.',
    'They are calling you right now.',
    'We are not doing this anymore as a team.',
    'Are they talking to me or someone else?',
    # 'Who is Charlie seeing this time?',
    # 進行相判定
    'They are doing whatever they want to do.',
    'Are you trying to finish this task on time?',
    'Is she going on a picnic with her students?',
    'They are not going to the pool anymore.',
    'I will not be taking pictures of this board at that time.',
    # 'We are not satisfied with the result he just turned in.',
    # copula文判定でした。確かにどちらとも取れますね。 #detector should be working only on present continuous
    'I forget to see if they are going to work on the project.',
    'What he is going to do does not matter to me.',
  ],
  'negative': [
    'I would tell her the truth because she has a right to know what happened.',
    'I can organize this desk by the end of the day.',
    'They cannot stay at the house at this time of the day.',
    'Where will you go shopping this evening?',
    'Would you be open to closing the store?',
    'She is so intelligent that she can talk to anyone about almost any topic.',
    'Charlie cannot do that because he will not be at home on time.',
    'I planned to go to New York City this summer, which is not a thing anymore.',
    'He has a legitimate opinion to let them stay at the court.',
    'Are you always by yourself here?',
    'It was a silent night.',
    'You are free to go after finishing the laundry.',
    'If you come around to say hey, I would say hi back.',
    'Sometimes I rode on the train to see what happened.',
    # 'All they wanted to do was taking your money, so keep that in mind.', Incorrect grammar, should be "All they wanted to do was take your money..."
    # 動名詞が進行形判定されます。これなんか方法ないんですかね……
    'Charlie has never consulted me before doing it, and I am furious because of that.',
    'They would help me carry the box filled with books.',
    'I was not at the station and could not see what happened there.',
  ],
}
test_data_1088 = { 

  # **Guideword:** MODAL AUXILIARY VERBS
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** types
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of modal auxiliary verbs ('can', 'will', 'would'). 
    
  'positive': [
    'Can you give me some advice about counseling?',
    'You would not try to help her out because you are such a bad person.',
    'What would you do in the situation if you were me?',
    'I won\'t be able to help you because of that reason.',
    'Couldn\'t you ask me beforehand so that we can avoid the worst case?',
    'She would not mind even when someone asked her for help.',
    'I will tell them that they should not have done that.',
    'What do you think would be the best way to solve this problem?',
    'Who else can you think of who can be the person in charge of this event?',
    'I hope she will get what she deserves.',
  ],
  'negative': [
    'May I ask you the reason why he left school?',
    'Catch that mouse!',
    'The most motivational quote I got recently is this.',
    'He brought tons of sodas into this lodge.',
    'I have not been capable of this type of stuff.',
    'I believe that they are going to win the game.',
    'How about not getting this expensive wine?',
    'She did not expect this to happen.',
    'She is available right now.',
    'Do you want to have an appointment with her?',
    'Charlie does not believe in God, which was surprising to me at first.',
    'Where do you think my siblings went shopping last night?',
    'Whatever happened to him does not matter to me.',
    'What are they going to buy in the mall?',
    'I went on a picnic the other day, and it was fun.',
    'They see many vehicles lately.',
    'I think what happened to him affects her in some way.',
    'We did not agree with the new rule that does not allow me to have a dog in this building.',
    'My professor lets me use her books as much as I want for my project.',
    'How does this sound to you?',
  ],
}
test_data_1089 = { 

  # **Guideword:** AUXILIARY VERBS 'HAVE' AND 'DO'
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** types
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use auxiliary verbs 'have' and 'do'. 
    
  'positive': [
    'Have you gotten any call from her at all?',
    'I have never done that before in my life.',
    'Do you like having a dog in your house?',
    'I asked him how he has been doing since I have not seen him for more than two months.',
    'Where do you think we can find the right clue?',
    'Didn\'t you go to the festival yesterday?',
    'Everyone has been looking for you.',
    'You asked them where they have been during the summer, but they could not answer the question for some reason.',
    'We have been to the gym every single day during winter.',
    'I did attend the meeting yesterday but nobody noticed me somehow.',
  ],
  'negative': [
    'Can I ask you a question?',
    'How can it be possible that you are not sure about this fact till now?',
    'Where should Charlie go to find the best resource?',
    'Could you find the folder that we were talking about?',
    'Should I go to her office today to talk more about this topic?',
    'Who would be the best person who knows the most about this issue?',
    'How long will it take you to commute from home to school?',
    'We found it interesting to learn more about this method.',
    'Can your professor help you figure out the best way to get a satisfactory score on the exam?',
    'How would it be possible for them to climb this high mountain in just a day?',
    'She is wearing a black backpack today.',
    'I am guessing Charlie can see the blue sky from this window.',
    'Are you planning to go to Toronto this summer?',
    'Which beach is the best place to observe wild birds?',
    'They were very excited to hear the news.',
    'My advisor was surprised at the fact that I got the full score on the exam.',
    'He went for a walk the other day and never came back, which made us sad.',
    'Can you see her playing basketball?',
    'There are no animals here because there is no sunshine.',
    'Should they find the issue, they can contact the office in the main campus building.',
    'I have a pen.',
    'Do me a favor.',
  ],
}
test_data_1090 = { 

  # **Guideword:** LINKING VERBS + ADJECTIVE
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** types
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use linking verbs with adjective complements. 
    
  'positive': [
    'You seem happy.',
    'The skies grew dark and it began to rain.',
    'My father looks tired.',
    'It was proving extremely difficult to establish the truth.',
    'This fruit smells quite delicious.',
    # 'Your story sounds fun to me.',
    # funは基本的には名詞で、パーサーもそう判定たようです。
    # 辞書によると形容詞でも使えるらしいのでpositiveだとは思いますが……
    'Your story sounds funny to me.',
    'I feel dizzy these days.',
    'It appears unlikely that interest rates will fall further.',
    'This movie seems boring.',
    #Parser error - 'tiring': VBG
    #'This movie seems tiring.',
    # get bored
    # 'I got dressed since my friends don\'t understand me.',
    # dressed: VBP
    # 以下追加
    'I stayed happy all night.',  # stayの例
  ],
  'negative': [
    'I\'m staying late at the office tonight.'
    # stayはlinking verbだがこのlateは副詞
    'It seems like I have to go to school today.',
    'You seem like you don\'t like her at all.',
    'He seems like he will get up early tomorrow.',
    'This sounds like you will go back home soon.',
    'It sounds like you don\'t need me anymore.',
    'it sounds like your brother is fine.',
    'He feels like he will be attacked by people.',
    'I feel like you can get a new job soon.',
    'My friend feels that you can be a good friend to him.',
    'My mother feels that I don\'t study at all.',
    'My mother got me a new dress for the party.',
    'I usually get up early.',
    'You get along with any person.',
    'I will stay in my room tonight.',
    'You can stay with me if you want.',
    'I don\'t want to stay here because I\'m freezing in here.',
    'You look like you can\'t go to the party tonight.',
    'My mother looks like me.',
    'It looks you can teach me English better than a teacher.',
  ],
}
test_data_1091 = { 

      # **Guideword:** MODAL AUXILIARY VERBS
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** types
      # **Lexical Range:** 2.0
      # **CEFR level:** A2
      # **CAN-DO:** Can use an increasing range of modal auxiliary verbs. 
        
  'positive': [
    'He said it might rain tomorrow.',
    'It could get much colder in January.',
    'I can speak a little Italian.',
    'She could be at the station by now.',
    'I should be able to have two assistants, but now I only have one left.',
    'You shouldn’t smoke since it’s bad for your health.',
    'He shall pay for that.',
    'You mustn’t drive on the right in the United Kingdom.',
    'Alice could speak Chinese at the age of five.',
    'I think he will study harder this time.',
    'I mustn\'t ask my boss for a day off.',
    'You shouldn\'t go now.',
    'He really should stay the night.',
    'I would rather stay in tonight.',
    'I could lend you my dictionary.',
    'You may not speak during the test.',
    'They might tell the police about you.',
  ],
  'negative': [
    'I have a grudge against him.',
    'They have great service at that hotel.',
    'My mother loved my brother better than she loved me.',
    'This form has five windows.',
    'Good intentions sometimes do great harm.',
    'We enjoy playing with little children.',
    'I enjoy fighting with my big brothers.',
    'I have a letter to write tonight.',
    'I have enjoyed myself a lot this evening.',
    'I spend a lot of time drawing because I enjoy it.',
    'Jack had the kindness to give me a present.',
    'They enjoy listening to Jamie’s stories.',
    'I want to have that blue sweater.',
    'I don’t have a smartphone.',
    'He had a gun in his pocket.',
    'Have some consideration for others.',
    'You know I really enjoy skiing in the mountains.',
    'We have friends staying with us this week.',
    'I enjoy riding my bicycle in the park.',
    'I have finished my work for today.',
  ],
}
test_data_1092 = { 

      # **Guideword:** SEMI-MODAL AUXILIARY VERBS, 'HAVE (GOT) TO'
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** types
      # **Lexical Range:** None
      # **CEFR level:** A2
      # **CAN-DO:** Can use semi-modal auxiliary verb 'have (got) to'.
        
  'positive': [
    'We have to handle this problem privately.',
    'You don’t have to dress properly.',
    'We have got to climb Mount Everest.',
    'You should have got to get the point sooner.',
    'We have got to get him to take that project seriously.',
    'You will just have to make do with what you have.',
    'Although I’m sleepy, I have to go to work today.',
    'You have to make do with what you’ve got.',
    'I have got to leave here early tomorrow morning.',
    'We have got to go through some troublesome procedures.',
  ],
  'negative': [
    'I have gotten more and more sleepy.',
    'The police have found a clue.',
    'Larry got married to Anne, whom I haven’t met before.',
    'I go to the cinema at least once a week.',
    'Tom will have been studying English for three years next month.',
    'Without you, I would not have won the contest.',
    'I am glad to hear that you have gotten well.',
    'When we arrived, he was having a bath.',
    'It seems I have got a little tipsy.',
    'He wouldn\'t have got caught.',
    'They were to have got married in May.',
    'I have been walking out in the rain for the past few hours.',
    'I have never eaten caviar in my life.',
    'Larry will have been playing baseball for ten years next spring.',
    'This morning I got up too late to have breakfast.',
    'We have been good friends for about forty years.',
    'They were not having a good time at the party when they decided to go home.',
    'I’ve just been to the supermarket to get some eggs.',
    'She has been overdoing it with work recently.',
    'I have a male friend whom I get along with so well.',
    'I have no idea who stole my bag.',
    # おかしな例だが例外を起こさせるため
    'I have',
  ],
}
test_data_1093 = { 

      # **Guideword:** SEMI-MODAL AUXILIARY VERBS, 'USED TO', 'OUGHT TO'
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** types
      # **Lexical Range:** None
      # **CEFR level:** B1
      # **CAN-DO:** Can use semi-modal auxiliary verbs, 'used to' and 'ought to'. 
        
  'positive': [
    'You ought to keep your promise.',
    'He used to drink a lot.',
    'I used to live here.',
    'He is not what he used to be.',
    'That is what you ought to do.',
    'You ought to give up smoking.',
    'I think I ought to go.',
    'You ought to be ashamed of yourself.',
    'There used to be a bridge here.',
    'Dad used to play golf and Mother used to knit.',
  ],
  'negative': [
    'You\'ll get used to it soon.',
    'You should make notes.',
    'We should read more books.',
    'I want learn more useful English, even a little bit.',
    'What should I do?',
    'I should be getting up early every day.',
    'I still cannot get used to that.',
    'He got used by the manager to work for free.',
    'I will get used to it some day.',
    'He should buy it as well.',
    'You should take out your hat.',
    'Do you get used to work yet?',
    'You should watch it.',
    'You\'ll used it up in no time.',
    'You should take medicine.',
    'You should check it out.',
    'You should apologize.',
    'They got a used car.',
    'This will be hard if you don\'t get used to it.',
    'What should I talk about?',
  ],
}
test_data_1094 = { 

      # **Guideword:** SEMI-MODAL AUXILIARY VERBS, 'DARE', 'NEED'
      # **Guideword type:** FORM
      # **Super category:** VERBS
      # **Sub category:** types
      # **Lexical Range:** None
      # **CEFR level:** B2
      # **CAN-DO:** Can use semi-modal auxiliary verbs, 'dare' and 'need'. 
        
  'positive': [
    'I daren’t walk through the park at night.',
    'He needn’t have called; I told him I would be late.',
    'I dare not press the issue any further.',
    'You need not worry about the situation.',
    'We needn’t be concerned.',
    'We needn’t hurry since the movies starts in two hours.',
    'How dare she talk to me like that.',
    # parser mistakenly parsed need as NN
    #'No one need know about this.',
    'They daren’t give him a reason to be angry.',
    'You needn’t worry about my grades.',
  ],
  'negative': [
    'He needs that report by tomorrow.',
    'There is no need for you to wait.',
    'No one dares to question my authority.',
    'He didn\'t dare anybody to argue with the principal.',
    'Call me whenever you\'re in need.',
    'We need someone to look after the cat.',
    'I dare you to ask Suzan on a date.',
    'He didn’t used to be so mean.',
    'This job needs skill and experience.',
    'Does she need to know where the house is?',
    'Is there any need to explain further?',
    'You have plenty of time, so you don’t need to rush.',
    'We all feel a need for a good coach.',
    'We must meet the needs of the young.',
    'You don’t need to come if you don’ want to.',
    'I can’t believe he dared to stand up to the boss.',
    'I’ve never been dared to race someone before.',
    'I used to get up early when I lived in New York.',
    'He needed a place to stay, so I offered him one.',
    'We used to be in a band together.',
  ],
}
test_data_1095 = { 

  # **Guideword:** VERB + 'TO'-INFINITIVE
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** patterns_with to and -ing
  # **Lexical Range:** 1.0
  # **CEFR level:** A1
  # **CAN-DO:** Can use a limited range of verbs followed by a 'to'- infinitive. 
    
  'positive': [
    'What do you like to do in the evenings?',
    'My brother would like to invite you to the reception.',
    'I want to go to the movie theatre after dinner.',
    'I went to get a new table for our new room.',
    'Will Charlie need to wash dishes instead of you?',
    'We want to help more people in the world.',
    'When it happened, they wanted to make you hide under the bed.',
    'He must learn to face his fears.',
    'I hope to see you there tomorrow afternoon.',
    'Would you like to help me complete the task by the end of today?',
  ],
  'negative': [
    'She does not want you to regret any choices in your life.',
    'We were not ready to talk about the issue.',
    'I listened to the music, but I could not understand how good it was.',
    'You do not need it right now, but you will eventually.',
    'They went shopping and never returned.',
    'Is it possible for you to fix this laptop?',
    'I did not know what they expected from me.',
    'Did you hear her crying in the middle of the day?',
    'I have never seen her before.',
    'Only the genius can see the light.',
    'It is necessary for you to do what I told you.',
    'Charlie has not learned how to drive a car.',
    'I think the person who invented this is so intelligent.',
    'Can you help me clean this room thoroughly?',
    'She stopped smoking.',
    'I have never seen him getting annoyed this much.',
    'Do you know where I can look for good oranges?',
    'My professor has never given up on me.',
    'Her academic advisor was available that afternoon to help her figure out the best way.',
    'I stopped texting in the middle of the conversation.',
    'They listened to him very carefully, but they were unable to catch what he was saying to them.',
    # 以下追加
    'When it comes to fishing, he is the best',
    'Try',

  ],
}
test_data_1096 = { 

  # **Guideword:** 'LIKE' + 'TO'-INFINITIVE OR + '-ING'
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** patterns_with to and -ing
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'like' followed either by a 'to'-infinitive or an '-ing' form, with no change in meaning. 
    
  'positive': [
    'I would like to hang out with friends.',
    'Who doesn\'t like being with friends they like?',
    # 'You don\'t like being surrounded by strangers, do you?',
    # パーシングがぐちゃぐちゃだったので断念しました。
    'Do they like having office hours at the same time?',
    'It is interesting that they like to climb this mountain.',
    'Have you ever liked to be with that person?',
    'I don\'t normally like drinking much alcohol.',
    # 'I do not normally like drinking much alcohol.',
    # likeが前置詞判定がでます。
    'It is totally acceptable for them to like doing nothing.',
    'Do you remember they liked to have other people around all the time?',
    'I will be there to see if she likes reading.',
  ],
  'negative': [
    'Stop smoking in public.',
    'There must be something hidden,',
    'We are going to rise until we fall.',
    'It is likely that we will go to the farmer\'s market this Saturday.',
    'When we were at the bar, we saw a person who looked like Charlie.',
    'They do not speak our language, but we still like them.',
    'I like the taste of these new chips.',
    'They like freedom, and they are still looking for it.',
    'In order to finish the assignment, you need to start it now.',
    'I\'n not far away from finishing every homework.',
    'They do not see anyone crossing the street when the light is red.',
    'When I get older, I will not go back to where I come from.',
    'We listened to the song and thought it was a very good song to motivate ourselves.',
    'There can be something more than just a couple of chairs.',
    'He went to India before, and he liked the country a lot.',
    'I heard you really wanted to go to Toronto, so I booked a flight for you beforehand.',
    'It is doubtful that you need to do that right now before anything else.',
    'Tonight I am going to visit my brother\'s hospital.',
    'Turn on the light so that I can see how many people are in this room.',
    'Would you be able to let me stay at your house for a couple of days?',
  ],
}
test_data_1097 = { 

  # **Guideword:** 'WOULD LIKE TO'
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** patterns_with to and -ing
  # **Lexical Range:** None
  # **CEFR level:** A1
  # **CAN-DO:** Can use 'would like to' + infinitive. 
    
  'positive': [
    'I would like to invite you for lunch.',
    'They would like to go to the party with us.',
    'He wouldn\'t like to pay extra anymore.',
    'She would like to ask you for help.',
    'I think they would like to go on a picnic next Sunday.',
    'They never explained to me why their professor would not like to have office hours.',
    'After graduation, we would like to invite all our family to this ceremony.',
    'She thought the reason why I would like to pay her rent was different.',
    # parser error/ What I would like to .. を　主語句として識別できていない。
    # 元のparser orderならOK
    # 'What I would like to ask you is clearly indicated here.',
    'What would you like to do after lunch?',
  ],
  'negative': [
    'They would not want to invite you for lunch for no reason.',
    'I never expected her to be the one who said that she would try that.',
    'Would you be able to help me figure out what is going on here?',
    'What you would not want to do is turn on the switch.',
    'What would they do if they have not finished their assignments?',
    'They would like the new couch in their house.',
    'They did not listen to what I said in the first place.',
    'I do not think she would try to find the key she lost a while ago.',
    'They really wanted to get that book but they gave up because they did not have enough money.',
    'I have never explained to him why I would not want to go to the carnival on Madison Street.',
    'She would let me do what I have wanted to try for a long time.',
    'They would want to try the new ice cream sold in the store two blocks away from here.',
    'We would need to fix the problem first before we even try to see if it works.',
    'Would you need to move your car to another lot?',
    'What would you want to buy at the mall?',
    'Forget about what I told you before.',
    'I would like you to pay for whatever you have eaten at this dinner.',
    'Do not do whatever they would have told you to do.',
    'It would be much fun for us to go to New York City together next month.',
    'I am sorry but there would not be much stuff left for you.',
  ],
}
test_data_1098 = { 

  # **Guideword:** VERB + 'TO'- INFINITIVE
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** patterns_with to and -ing
  # **Lexical Range:** 2.0
  # **CEFR level:** A2
  # **CAN-DO:** Can use an increasing range of verbs followed by a 'to'-infinitive. 
    
  'positive': [
    'I want to buy this book.',
    'She went to set a record.',
    'They decided to start a business together.',
    'Remember to turn the lights out.',
    'Dogs need to go for a walk every day.',
    'You might want to make that as clear as possible.',
    'If you want to test a man’s character, give him power.',
    'I want to swim in the sea.',
    'They are to be married.',
    'My hobby is to collect stamps.',
    'I have tried to fry potatoes.',
    'We like to eat lunch at that restaurant.',
  ],
  'negative': [
    # 'It’s easy to play the piano, but it’s challenging to play well.',
    # 意味を無視すれば後半が進行形にもとれる
    'When I am traveling, I always take something to read.',
    'He encouraged his friends to vote for him.',
    'To study Spanish is very fun.',
    'I went to school yesterday for the first time in a while.',
    'They gave their dog to him.',
    'I have no desire to be rich.',
    'They gave him an opportunity to escape.',
    'I had no one to talk to.',
    'There is hardly anything to do in most of these small towns.',
    'It’s kind of you to help.',
    'It would be silly of him to spend all his money.',
    'It was difficult for us to hear what she was saying.',
    'It is easy for you to criticize other people.',
    'Unfortunately, I was unable to work for over a week.',
    'I am ready to go to bed.',
    'We were happy to come to the end of our journey.',
    'She reminded me to turn the lights off.',
    'We set off early in order to avoid the traffic.',
    'He knew two ways to get there.',
  ],
}
test_data_1099 = { 

  # **Guideword:** VERBS + 'TO'-INFINITIVE OR + '-ING'
  # **Guideword type:** FORM
  # **Super category:** VERBS
  # **Sub category:** patterns_with to and -ing
  # **Lexical Range:** None
  # **CEFR level:** A2
  # **CAN-DO:** Can use verbs expressing preference followed either by a 'to'-infinitive or an '-ing' form, with no change in meaning.
    
  'positive': [
    'I love to bake cookies.',
    'I love to play baseball.',
    'I hate to hurt your feelings.',
    # 'I would not say I like wearing uniforms.',
    # parser's problem.
    'I hate to play with my sister.',
    'I love to dance with my friends.',
    'I hate talking to older adults.',
    'I prefer watching comedy movies.',
    'I love listening to folk songs.',
    'I love eating chocolate.',
  ],
  'negative': [
    'I love my grandmother.',
    'I prefer mozzarella cheese over ricotta cheese.',
    'They gave him an opportunity to escape.',
    'I love video games more than I love board games.',
    'There is hardly anything to do in most of these small towns.',
    'It’s kind of you to help.',
    'It would be silly of him to spend all his money.',
    'It was difficult for us to hear what she was saying.',
    'It is easy for you to criticize other people.',
    'Unfortunately, I was unable to work for over a week.',
    'I am ready to go to bed.',
    'We were happy to come to the end of our journey.',
    'Lauren was surprised to see me.',
    'She reminded me to turn the lights off.',
    'We set off early to avoid the traffic.',
    'Dogs need to go for a walk every day.',
    'I went to school yesterday for the first time in a while.',
    'They are to be married.',
    'They decided to start a business together.',
    'Remember to turn the lights off.',
    # 以下追加
    'I would like you to come.',
  ],
}
