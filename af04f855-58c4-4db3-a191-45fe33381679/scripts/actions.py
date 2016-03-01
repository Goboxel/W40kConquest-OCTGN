1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------
Resource = ("Resource", "906bc3a2-9315-4473-8671-7ece287de4a8")
Damage = ("Damage", "22adcef9-414c-4e96-8381-f155283e170e")
FstPlanet = ("FstPlanet", "9e9aceca-516f-43f4-8590-48068298af6f")
SixPlanet = ("SixPlanet", "8e41b199-b00c-4009-b94c-f10eb25cbaa2")
Infest = ("Infest", "5b35b6b8-aa47-4e70-934c-db3b7e64941a")
#---------------------------------------------------------------------------
# Table group actions
#---------------------------------------------------------------------------
 
def wilkommen():
    notify("Hi, i'm updating conquest to the new octgn API, if you get any error message, please copy and paste it on my blog : http://octgngames.com/wh40kc/ or my github : https://github.com/Kertanos/W40kConquest-OCTGN/    Enjoy your game, good luck and have fun !")
 
 
 
def setupPlanet(group):
    group.create("5e423620-6663-4198-8cdc-df0fabf876c8")
    group.create("12fea3b0-be4e-4142-89db-316c56956c8f")
    group.create("89b18d3e-431e-4889-94d1-0948f73a4b2a")
    group.create("9657b143-06c2-45fe-bd6e-4a3d131e1689")
    group.create("8ec7354b-eef5-4997-82ed-d7ed66a93c15")
    group.create("8fcab463-9c8c-4745-a49e-38f56bc49e6d")
    group.create("1a35a54a-0f21-44d0-ab40-b3ec7ac5cadc")
    group.create("e0c7e2e6-711d-4704-8e38-182d113c6282")
    group.create("3e58dd21-00fe-499e-87e9-7bb52bb66b95")
    group.create("36221c3a-591c-41e8-a4c9-fc71c89cac12")
    X =-682
    k=7
    notify("The planets for this game are :")
    for i in range(2):
        card =group.random()
        setGlobalVariable("Planet{}".format(k), card.name)
        card.moveToTable(X,-43,True)
        card.markers[SixPlanet] = k
        k-=1       
        X+=200
    for i in range(5):
        card =group.random()
        setGlobalVariable("Planet{}".format(k), card.name)
        notify("**{}**".format(card))
        card.moveToTable(X,-43)
        k-=1
        X+=200
    card.markers[FstPlanet] = 1
    for card in group: card.delete()
    fp=askChoice("Who'll be the first player ? ",['Me','My opponent'], customButtons =["Let the Chaos Gods decide"])
    if fp != 1 and fp!=2 : 
        fp = rnd(1,2)
        notify("The Chaos Gods choose")
    else: notify("{} decides to put".format(me))
    if len(getPlayers()) == 1 : fp =1
    if fp==1: 
        play=me
        if me.isInverted:Y2=-176
        else: Y2=88
    else : 
        play=players[1]
        if me.isInverted:Y2=88
        else: Y2=-176
    table.create("29133845-cfae-4d83-ba1b-8c7dc3dbbabe",668,Y2,persist=True)
    play.counters['Initiative'].value=1
    notify("{} as the first player.".format(play))
 
def setup(group, x = 0, y = 0):
    mute()
    var = me.getGlobalVariable("setupOk")
    if var == "1":
        notify("You already did your Setup")
        return
    if len(me.hand) == 0:
        notify("You need to load a deck first") 
        return
    var="1"
    me.setGlobalVariable("setupOk", var)
    notify("**{} has started setup, please wait**".format(me))
    set=(card for card in me.hand)
    if me.isInverted: 
        X1=-532
        X2=-432
        X3=694
        X4=632
        Y1=-288
        Y2=-88
    else:
        X1=468
        X2=368
        X3=632
        X4=694
        Y1=200
        Y2=0
    for card in set: 
        if card.Type == "Warlord":
            me.counters['Resources'].value = int(card.StartingResources)
            SHand=int(card.StartingHand)
            me.deck.shuffle()
            notify("**{}'s warlord is {}**".format(me,card))
            card.moveToTable(X1, Y1)
            if card.Faction == "Tyranid" : 
                table.create("124d3e0b-621a-4eb7-bb34-e4163794989f",X3,Y2,persist=True)
                table.create("a53b9f48-6ae2-4cd7-ba8a-6bfcf47bca3c",X4,Y2,persist=True)
            else : table.create("5c352ba9-9b70-4071-ae47-e2bed96d1e01",668,Y2,persist=True)
        if card.Type == "Synapse":
            notify("**{}'s Synapse is {}**".format(me,card))
            card.moveToTable(X2, Y1)
    for card in me.deck.top(SHand): card.moveTo(me.hand)
    notify("**{} is ready**".format(me))
    if not me.isInverted:setupPlanet(me.Planets)        
 
def flipCoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("**{} flips heads.**".format(me))
    else:
        notify("**{} flips tails.**".format(me))
 
     
def xSided(group, x = 0, y = 0):
    mute()
    sides = askInteger("Roll a how many sided die? (minimum 3)", 3)
    if sides == None: return
    elif sides < 3:
        whisper("Please choose a number greater than or equal to 3.")
        return
    else:
        n = rnd(1,sides)
        notify("**{} rolls a {} on a {}-sided die.**".format(me, n, sides))
 
 
def restoreAll(group,x = 0, y=0): 
    mute()
    myCards = (card for card in table if card.controller == me and card.Type!="Planet")
    for card in myCards:
        if card.isFaceUp:
            card.orientation &= ~Rot90
            card.highlight = None
    notify("{} readies all his or her cards.".format(me))
 
def holdOn(group, x = 0, y = 0):
    mute()
    notify("***PLEASE WAIT.  {} has an action/reaction.***".format(me))
 
def imDone(group, x = 0, y = 0):
    mute()
    notify("***{} is Done.***".format(me))
 
def createToken(group, x = 0, y = 0):
    mute()
    guid,quantity=askCard({'Type':'Token'})
    if guid == None: return
    if me.isInverted: 
        X1=-150
        for i in range(quantity):
            cards=table.create(guid, X1, -288)
            X1+=50 
    else:
        X1=150
        for i in range(quantity):
            cards=table.create(guid, X1, 200)
            X1-=50
    notify("{} creates {} {} Token(s)".format(me,quantity,cards))
 
def ServoSkull(group, x=0,y=0):
    mute()
    servo= (card for card in table if card.controller == me and card.Type == "Skull")
    notify("{} is choosing his or her Warlord destination.".format(me))
    choiceList = ['Planet 1', 'Planet 2', 'Planet 3', 'Planet 4', 'Planet 5']
    unit = "warlord"
    for card in servo:      
        choice = askChoice("To which planet do you want to commit your {} ? ".format(unit), choiceList)         
        if card.isFaceUp: card.isFaceUp = False
        card.peek()
        if choice == 0 : 
            notify("{} didn't change his or her Skull".format(me))
            return     
        elif choice == 1 : card.alternate=""
        elif choice == 2 : card.alternate="Skull2"
        elif choice == 3 : card.alternate="Skull3"
        elif choice == 4 : card.alternate="Skull4"
        else : card.alternate="Skull5"
        notify("{} has chosen where to commit his or her {}".format(me,unit))
        unit = "synapse"
         
     
def capture(group, x=0, y=0):
    mute()
    turn= getGlobalVariable("Turn")
    fstP= getGlobalVariable("Planet{}".format(turn))
    plan=(card for card in table if card.name == fstP)
    for card in plan:
        capt = confirm("Are you sure you want to capture {} ?".format(card.name))
        if capt == False : return
        if card.PlanetMaterial == "1" : me.counters['Material'].value += 1
        if card.PlanetStrongpoint == "1" : me.counters['Strongpoint'].value += 1
        if card.PlanetTech == "1" : me.counters['Tech'].value += 1
        card.moveTo(me.Planets)
        notify("**{} captures the first planet, {}**".format(me,card))
    if me.counters['Tech'].value >= 3 or me.counters['Strongpoint'].value >= 3 or me.counters['Material'].value >= 3 : notify ("**{} HAS WON THE GAME ! CONGRATULATIONS ! **".format(me))
 
def endTurn(group, x=0, y=0):
    mute()
    turn = int(getGlobalVariable("Turn"))
    if not confirm("Resolve the Turn {} HeadQuarter phase ? ".format(turn)) :return
    pturn= int(me.getGlobalVariable("Pturn"))
    if turn!=pturn : return
    notify("{} activates the resolution of Turn {} HeadQuarter phase.".format(me,turn))
    turn+=1
    setGlobalVariable("Turn",str(turn))
    HQRes(turn)
    if me.isInverted:Y= -176
    else:Y= 88
    if len(getPlayers()) != 1 :
        remoteCall(players[1],"HQRes",turn)
        if me.counters['Initiative'].value==0: 
            me.counters['Initiative'].value=1
            players[1].counters['Initiative'].value=0
            notify("{} has initiative for Turn {}.".format(me,turn))
        else: 
            me.counters['Initiative'].value=0
            players[1].counters['Initiative'].value=1
            notify("{} has initiative for Turn {}.".format(players[1],turn))
            if Y== -176: Y=88
            else: Y= -176
        init=(card for card in table if card.model == "29133845-cfae-4d83-ba1b-8c7dc3dbbabe")
        for card in init: card.moveToTable(668,Y)
    update()
    if turn==8: 
        Notify("End of the game ! The last players to have captured a planet win !")
        return
    fstP= getGlobalVariable("Planet{}".format(turn))
    plan=(card for card in table if card.name == fstP)
    for card in plan: card.markers[FstPlanet] = 1
    notify("** Turn {} HQ Phase Complete**".format(turn-1))
    if turn <= 3 :
        fstP=(card for card in table if card.markers[SixPlanet] == turn+4)
        for card in fstP: 
            card.isFaceUp=True
            card.markers[SixPlanet] = 0
            notify("The 5th planet is now {}.".format(card))
 
     
def HQRes(turn):
    mute()
    draw(me.deck)
    draw(me.deck)
    restoreAll(Table)
    me.counters['Resources'].value += 4
    notify("{} gains 4 resources.".format(me))
    me.setGlobalVariable("Pturn",str(turn))
 
 
def winC(group,x=0,y=0):
    mute()
    com=(card for card in table if card.targetedBy==me and (card.ResourceBonus!="" or card.CardBonus!=""))
    conf=0
    conf=askChoice("What do you want to do with targeted cards? ", ['Take all resources and draw bonuses.','Select for each.'])
    resB=0
    cardB=0
    if conf==0:return
    elif conf==1:
        for card in com: 
            if card.ResourceBonus!="": resB+=int(card.ResourceBonus)
            if card.CardBonus!="": cardB+=int(card.CardBonus)
        notify("{} chooses to take all bonuses".format(me))
    else:
        for card in com:
            bon=askChoice("For {} : {} Resources, {} Cards".format(card.name,card.ResourceBonus,card.CardBonus), ['Resources','Draw','Both','None'])
            if bon==1:
                if card.ResourceBonus!="":resB+=int(card.ResourceBonus)
                notify("{} chooses to only take resources from {}.".format(me,card))
            elif bon==2:
                if card.CardBonus!="":cardB+=int(card.CardBonus)
                notify("{} chooses to only take draw from {}.".format(me,card))
            elif bon==3:
                if card.ResourceBonus!="":resB+=int(card.ResourceBonus)
                if card.CardBonus!="":cardB+=int(card.CardBonus)
                notify("{} chooses to take both resources and draw from {}.".format(me,card))
            else: notify("{} chooses to take nothing from {}".format(me,card))
    notify("{} draws {} cards and take {} resources.".format(me, cardB,resB))
    if len(me.deck) <= cardB:
        notify("**{} was lost in the warp, he looses the game (last card drawn).**".format(me))
        return 
    for card in me.deck.top(cardB):
        card.moveTo(me.hand)
    me.counters['Resources'].value += resB
 
                 
 
#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------
 
def disc(card, x=0, y=0):
    mute()
    if card.Type != "Planet":
        if not confirm("Discard {} ?".format(card.name)): return
        group=card.group
        card.moveTo(me.piles['Discard pile'])
        notify("{} discards {} from his or her {}.".format(me, card,group.name))
    else:
        turn= getGlobalVariable("Turn")
        fstP= getGlobalVariable("Planet{}".format(turn))
        if card.name!=fstP: return
        if not confirm("Are you sure you want to destroy {} ? There is no going back !".format(card.name)): return
        notify("{} destroys {}.".format(me,card))
        card.delete()
 
def addMarker(card, x=0, y=0):
    mute()
    marker, qty = askMarker()
    if qty == 0 or marker== None: return
    card.markers[marker] += qty
    notify("{} adds {} {} marker on {}".format(me,qty,marker[0],card))
 
def subMarker(card, x=0, y=0):
    mute()
    marker, qty = askMarker()
    if qty == 0 or marker== None: return
    card.markers[marker] -= qty
    notify("{} removes {} {} marker on {}".format(me,qty,marker[0],card))
 
 
 
def displayErrata(card, x = 0, y = 0):
    mute()  
    notify('{} - Errata Text:'.format(card.name))
    notify('{}'.format(card.ErrataText))
     
     
def kneel(card, x = 0, y = 0):
    mute()
    card.orientation ^= Rot90
    if card.orientation & Rot90 == Rot90:
        notify('{} exhausts {}.'.format(me, card))
    else:
        notify('{} readies {}.'.format(me, card))
 
def flipcard(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} turns {} face down.".format(me, card))
        card.isFaceUp = False
    else:
        card.isFaceUp = True
        notify("{} turns {} face up.".format(me, card))
 
def addDamage(card, x = 0, y = 0):
    mute()
    notify("{} adds a Damage to {}.".format(me, card))
    card.markers[Damage] += 1
     
def addResource(card, x = 0, y = 0):
    mute()
    notify("{} adds a Resource to {}.".format(me, card))
    card.markers[Resource] += 1
     
     
def subDamage(card, x = 0, y = 0):
    mute()
    notify("{} removes a Damage from {}.".format(me, card))
    card.markers[Damage] -= 1
     
def subResource(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Resource to {}.".format(me, card))
    card.markers[Resource] -= 1
 
def infest(card, x = 0, y = 0):
    mute()
    if card.Type == "Planet": 
        notify("{} Infested {}.".format(me, card))
        card.markers[Infest] = 1
 
def uninfest(card, x = 0, y = 0):
    mute()
    if card.Type == "Planet": 
        notify("{} cleared the infestation on {}.".format(me, card))
        card.markers[Infest] = 0
 
def bloodied(card, x = 0, y = 0):
    mute()
    if card.Type != "Warlord" or card.alternate == "bloodied" : return
    notify("{} is now Bloodied.".format(card))
    card.alternate="bloodied"
    card.markers[Damage] = 0
    card.orientation = Rot90
 
 
def restore(card, x = 0, y = 0):
    mute()
    if card.Type != "Warlord" or card.alternate != "bloodied": return
    notify("{} is no longer Bloodied.".format(card))
    card.alternate=""
    card.markers[Damage] = 0
     
 
#---------------------------
#movement actions
#---------------------------
 
#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------
 
def randomDiscard(group):
    mute()
    card = group.random()
    if card == None: return
    card.moveTo(me.piles['Discard pile'])
    notify("{} randomly discards {}.".format(me, card))
  
def discardMany(group):
    count = 0
    discAmount = None
     
    mute()
    if len(group) == 0: return
    if discAmount == None: discAmount = askInteger("Randomly discard how many cards?", 2)
    if discAmount == None: return
     
    for index in range(0,discAmount):
        card = group.random()
        if card == None: break
        card.moveTo(me.piles['Discard pile'])
        count += 1
        notify("{} randomly discards {}.".format(me,card))
    notify("{} randomly discards {} cards.".format(me, count))
 
def mulligan(group):
    count = None
    draw = None
    mute()
     
    if not confirm("Are you sure you want to Mulligan?"): return
    if draw == None: draw = askInteger("How many cards would you like to draw for your Mulligan?", len(me.hand))
    if draw == None: return
     
    for card in group:
        card.moveToBottom(me.deck)
    update()
    me.deck.shuffle()
    update()
    for card in me.deck.top(draw):
        card.moveTo(me.hand)
    notify("{} mulligans and draws {} new cards.".format(me, draw))
 
 
def play(card, x=0, y=0):
    mute()
    if card.cost == "" : 
        whisper("You can't play this card")
        return
    if card.Cost == "X": cost=askInteger("How much do you want to pay to play {} ? ".format(card.name),0)
    else : cost=int(card.Cost)
    reduc=askInteger("Reduce Cost by ?",0)
    if reduc == None or cost == None: return
    if reduc>cost: reduc=cost
    cost-=reduc
    if me.counters['Resources'].value < cost :
        whisper("You don't have enough Resources to pay for {}.".format(card.name))
        return     
    if me.isInverted: card.moveToTable(0,-288)
    else :  card.moveToTable(0,200)
    notify("{} plays {} for {} resources (Cost reduced by {}).".format(me,card,cost,reduc))
    me.counters['Resources'].value -= cost
 
#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------
 
def shuffle(group):
    group.shuffle()
 
def draw(group):
    mute()
    if len(group) == 0: return
    group[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))
    if len(group) == 0: notify("**{} was lost in the warp, he looses the game (last card drawn).**".format(me))
     
def drawRandom(group):
    mute()
     
    card = group.random()
    if card == None: return
    card.moveTo(me.hand)
    notify("{} randomly draws a plot card.".format(me))
    if len(group) == 0: notify("**{} was lost in the warp, he looses the game (last card drawn).**".format(me))
 
def drawMany(group):
    drawAmount = None
     
    mute()
    if len(group) == 0: return
    if drawAmount == None: drawAmount = askInteger("Draw how many cards?", 7)
    if drawAmount == None: return
     
    if len(group) < drawAmount:
        drawAmount = len(group)
     
    for card in group.top(drawAmount):
        card.moveTo(me.hand)
    notify("{} draws {} cards.".format(me, drawAmount))
    if len(group) == 0: notify("**{} was lost in the warp, he looses the game (last card drawn).**".format(me))
  
def discardManyFromTop(group):
    count = 0
    discAmount = None
     
    mute()
    if len(group) == 0: return
    if discAmount == None: discAmount = askInteger("Discard how many from top?", 4)
    if discAmount == None: return
     
    for card in group.top(discAmount):
        card.moveTo(me.piles['Discard pile'])
        count += 1
        if len(group) == 0: break
    notify("{} discards {} cards from the top of their Deck.".format(me, count))
 
def searchTop(group):
    mute()
    searchAmount = askInteger("How many cards do you want to look ?",1)
    if searchAmount == None:return
    if len(group) < searchAmount: searchAmount = len(group)
    if searchAmount == 0 : return
    notify("{} is searching the top {} card(s) of his or her {}".format(me,searchAmount,group.name))
    list=[]
    group.addViewer(me)
    for card in group.top(searchAmount): list.append(card)
    dlg = cardDlg(list)
    dlg.title = "Select a card"
    cards = dlg.show()
    if cards != None:
        card = cards[0];
        if me.isInverted: card.moveToTable(0,-288,True)
        else: card.moveToTable(0,200,True)
        card.peek()
        notify("{} chose his or her card".format(me))
        searchAmount-=1
    else:notify("{} didn't find what he or she was looking for.".format(me))
    group.removeViewer(me)  
    for cards in group.top(searchAmount): cards.moveToBottom(group)
    notify("{} placed the {} remaining cards to the bottom of his or her deck.".format(me,searchAmount))
    if len(me.deck) == 0: notify("**{} was lost in the warp, he looses the game (last card drawn).**".format(me))
 
             
 
  
     
def reshuffle(group):
    count = None
     
    mute()
    if len(group) == 0: return
    if not confirm("Are you sure you want to reshuffle the {} back into your Deck?".format(group.name)): return
     
    myDeck = me.deck
    for card in group:
        card.moveTo(myDeck)
    myDeck.shuffle()
    notify("{} shuffles thier {} back into their deck.".format(me, group.name))
     
def moveOneRandom(group):
    mute()
    if len(group) == 0: return
    if not confirm("Are you sure you want to move one random card from your {} to your Hand?".format(group.name)): return
     
    card = group.random()
    if card == None: return
    card.moveTo(me.hand)
    notify("{} randomly moves {} from their discard to their hand.".format(me, card.name))
    
