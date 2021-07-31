import sqlite3
import datetime
import random
import PIL
from PIL import Image, ImageDraw, ImageOps, ImageFont


def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im



def image_correction(image, name, tense, position):
    im1 = Image.open(image)
    im1 = ImageOps.expand(im1, border=55, fill='black')
    if position == 'reversed':
        im1 = im1.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    I1 = ImageDraw.Draw(im1)
    myfont = ImageFont.truetype('CormorantInfant-Bold.ttf', 18)
    I1.text((115, 410), name, font=myfont, fill=(255, 255, 255))
    I1.text((140, 20), tense, font=myfont, fill=(255, 255, 255))
    return im1



def tarot_card_creation():

    conn = sqlite3.connect("tarot.db")

    c = conn.cursor()

    # c.execute('''CREATE TABLE  Tarot_Cards (
    #             Name TEXT,
    #             Meaning_Upright TEXT,
    #             Meaning_Reversed  TEXT,
    #             Image_URL  TEXT)
    #             ''')

    Tarot_Deck        = {

        1                         : {
                       'name'     : 'The Fool',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\0.jpg',
                       'upright'  : 'beginnings possibilities, pleasure, thoughtlessness, adventure, opportunity',
                       'reversed' : 'indecision, hesitation, injustice, apathy, bad choice',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        2                         : {
                       'name'     : 'The Magician',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\1.jpg',
                       'upright'  : 'creativity, self-confidence, dexterity, sleight of hand,will-power, skill',
                       'reversed' : 'delay, unimaginative, insecurity, lack of self-confidence',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        3                         : {
                       'name'     : 'The High Priestess',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\2.jpg',
                       'upright'  : 'knowledge, wisdom, learning, intuition, impatience, virtue, purity',
                       'reversed' : 'selfishness, shallowness, misunderstanding, ignorance',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        4                         : {
                       'name'     : 'The Empress',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\3.jpg',
                       'upright'  : 'development, accomplishment action, evolution',
                       'reversed' : 'inaction, lack on concentration, vacillation, anxiety, infidelity',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        5                         : {
                       'name'     : 'The Emperor',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\4.jpg',
                       'upright'  : 'authority, father-figure, structure, solid foundation',
                       'reversed' : 'domination, excessive control, rigidity, inflexibility',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        6                         : {
                       'name'     : 'The Hierophant',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\5.jpg',
                       'upright'  : 'mercy, conformity, forgiveness, social approval, bonded, inspiration',
                       'reversed' : 'vulnerability, unconventionality, foolish generosity, impotence, frailty, unorthodoxy',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        7                         : {
                       'name'     : 'The Lovers',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\6.jpg',
                       'upright'  : 'harmony, trust,romance, optimism, honor, love, harmony',
                       'reversed' : 'separation, frustration, unreliability,fickleness, untrustworthy',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        8                         : {
                       'name'     : 'The Chariot',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\7.jpg',
                       'upright'  : 'perseverance, rushed decision, turmoil, vengeance, adversity',
                       'reversed' : 'vanquishment, defeat, failure, unsuccessful',
                       'dupright' : '''''',
                       'dreversed': ''''''
            },
        9                         : {
                       'name'     : 'Strength',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\8.jpg',
                       'upright'  : 'courage, conviction, strength, determination, action, heroism, virility',
                       'reversed' : 'pettiness, sickness, unfaithfulness, weakness',
                       'dupright' : '''''',
                       'dreversed': ''''''
             },
        10                         : {
                        'name'     : 'The Hermit',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\9.jpg',
                        'upright'  : 'inner strength, prudence, withdrawal, caution, vigilance',
                        'reversed' : 'hastiness, rashness,immaturity, imprudence, foolishness',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        11                         : {
                        'name'     : 'Wheel of Fortune',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\10.jpg',
                        'upright'  : 'unexpected events, advancement, destiny, fortune, progress',
                        'reversed' : 'interruption, outside influences, failure, bad luck',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        12                         : {
                        'name'     : 'Justice',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\11.jpg',
                        'upright'  : 'equality, righteousness, virtue, honor, harmony, balance',
                        'reversed' : 'alse accusation, unfairness, abuse, biased',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        13                         : {
                        'name'     : 'The Hanged Man',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\12.jpg',
                        'upright'  : 'change, reversal, boredom, improvement, rebirth, suspension, change',
                        'reversed' : 'alse prophecy, useless sacrifice, unwillingness',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        14                         : {
                        'name'     : 'Death',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\13.jpg',
                        'upright'  : 'unexpected change, loss, failure, transformation, death, bad luck',
                        'reversed' : 'immobility, slow changes, cheating, death, stagnation',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        15                        : {
                        'name'    : 'Temperance',
                        'image'   : 'D:\\antoa\\tarot_sql\\tarot_images\\14.jpg',
                        'upright' : 'balance, patience, purpose, good influence, confidence, moderation',
                        'reversed': 'conflict, disunion, re-alignment, impatience, self-healing',
                        'dupright': '''Upright Temperance
    Temperance is the card for bringing balance, patience and moderation into your life. You are being invited to stabilise your energy and to allow the life force to flow through you without force or resistance. It’s time to recover your flow and get your life back into order and balance.
    
    This card calls on you to remain calm, even when life feels stressful or frantic. Maintain an even temperament and manage your emotions. You have learned to keep composed in stressful situations. Little things don’t get to you, thanks to your seemingly abundant source of patience. Your respect for balance and tranquillity is what will help you achieve and experience fulfilment in your life.
    
    Temperance asks you to take the middle path and accommodate all perspectives. Now is not the time to be highly opinionated or controversial. Be the peacekeeper and take a balanced and moderate approach, avoiding any extremes. Include others and bring together diverse groups of people to create harmony and cooperation. By working together, you will collectively leverage the right mix of talents, experiences, abilities and skills.
    
    There is alchemy within Temperance. This Tarot card is about blending, mixing, and combining diverse elements in a way that creates something new and even more valuable than its separate parts. ‘Blending’ can take on many forms; for example, a blended family, an artist who blends different materials or techniques, a bartender who mixes new and exciting cocktails, or a chef who combines different cuisines and cooking styles.
    
    The Temperance card shows that you have a clear, long-term vision of what you want to achieve. You are not rushing things along; instead, you are taking your time to ensure that you do the best job you can. You know you need a moderate, guided approach to reach your goals.
    
    Finally, this card reflects higher learning. You are learning a great deal where you are now and are at peace with what you are doing – it is all coming together well. Your inner voice is guiding you to the right outcome, and you are patiently listening and following.''',
                        'dreversed':'''If you have recently experienced a period of excess, the reversed Temperance card is your invitation (or sometimes, your warning signal) to restore balance and moderation as soon as possible. You may have been over-eating, regularly drinking, buying things you can’t afford, arguing with loved ones, or engaging in negative thought patterns. These activities are taking you further away from who you are and what you are here to do. So, it is time to stop. As they say, “Everything in moderation!” Or, you may find you need 100% abstinence to break this negative cycle and bring your life back into balance again.
    
    The reversed Temperance card can also be a sign you sense that something is ‘off’ in your life, creating stress and tension. Life is not flowing as easily as you had hoped or there’s a niggling voice from within going, “Wait a second! This doesn’t feel right!” You can ignore it and carry on with life as usual. But, heed Temperance’s warning: If you stay in this state for too long, that voice will just get louder and louder until you pay attention. Or, you can listen to it now and make the necessary adjustments to find your flow once again. Focus on your long-term vision and higher purpose and seek to align your daily activities with this vision.
    
    Temperance reversed may reflect a period of self-evaluation in which you can re-examine your life priorities. Internally, you may feel called in one direction, but your daily life may not match up to what is emerging. See this as your opportunity to align your higher vibration with your outer world. You may need to change your living arrangements, relationships, career, and daily habits so you can cultivate more balance and purpose in line with your new priorities. Don’t be surprised if you run into tension or even conflict as you align your inner and outer worlds; it’s a natural part of the process of levelling up and creating positive change.
    
    Similarly, the reversed Temperance card can be a call for profound self-healing. By creating more balance and moderation in your life, you open the possibility for such healing to occur. Given the reversal of this card, you are doing it in a way that is personal and private to you, without the influence of others. You know you have what you need to heal yourself and create more ‘flow’ in your life.'''
             },
        16                         : {
                        'name'     : 'The Devil',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\15.jpg',
                        'upright'  : 'downfall, unexpected failure, controversy, ravage, disaster, ill tempered',
                        'reversed' : ' ravage, disaster, ill tempered	release, enlightenment, divorce, recovery',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        17                         : {
                        'name'     : 'The Tower',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\16.jpg',
                        'upright'  : 'disruption, abandonment, end of friendship, bankruptcy, downfall, unexpected events',
                        'reversed' : 'entrapment, imprisonment, old ways, rustic',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        18                         : {
                        'name'     : 'The Star',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\17.jpg',
                        'upright'  : 'balance, pleasure, optimism, insight, spiritual love, hope, faith',
                        'reversed' : 'disappointment, bad luck, imbalance, broken dreams',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        19                         : {
                        'name'     : 'The Moon',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\18.jpg',
                        'upright'  : 'Upright:double-dealing Deception, disillusionment, trickery, error, danger, disgrace',
                        'reversed' : 'trifling mistakes, deception discovered, negative advantage',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        20                         : {
                        'name'     : 'The Sun',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\19.jpg',
                        'upright'  : 'accomplishment, success, love, joy, happy marriage, satisfaction',
                        'reversed' : 'loneliness, canceled plans, unhappiness, break ups',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        21                         : {
                        'name'     : 'Judgment',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\20.jpg',
                        'upright'  : 'awakening, renewal, rejuvenation, rebirth, improvement, promotion, atonement, judgment',
                        'reversed' : 'disappointment, indecision, death, failure, ill-health, theft, worry',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        22                         : {
                        'name'     : 'The World',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\21.jpg',
                        'upright'  : 'perfection, recognition, success, fulfillment, eternal life',
                        'reversed' : 'ack of vision, disappointment, imperfection',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        23                         : {
                        'name'     : 'Ace of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\22.jpg',
                        'upright'  : 'profitable journey, new business, beginning, new career, birth, inheritance',
                        'reversed' : 'selfishness, lack of determination, setback',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        24                         : {
                        'name'     : 'Two of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\23.jpg',
                        'upright'  : 'generous person, courage, patience, courage',
                        'reversed' : 'impatience, domination',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        25                         : {
                        'name'     : 'Three of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\24.jpg',
                        'upright'  : 'cooperation, good partnership, success',
                        'reversed' : 'carelessness, arrogance, pride, mistakes',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        26                         : {
                        'name'     : 'Four of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\25.jpg',
                        'upright'  : 'dissatisfaction, kindness, reevaluation',
                        'reversed' : 'new relationship, new ambitions, action',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        27                         : {
                        'name'     : 'Five of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\26.jpg',
                        'upright'  : 'lawsuit or quarrel, courage, competition',
                        'reversed' : 'new opportunities, harmony, generosity',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        28                         : {
                        'name'     : 'Six of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\27.jpg',
                        'upright'  : 'leadership, good news, success',
                        'reversed' : 'postponement, bad news, pride in riches',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        29                         : {
                        'name'     : 'Seven of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\28.jpg',
                        'upright'  : 'stiff competition, victory, courage, energy',
                        'reversed' : 'advantage, patience, indecision',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        30                         : {
                        'name'     : 'Eight of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\29.jpg',
                        'upright'  : 'new ideas, love, journey',
                        'reversed' : 'violence, quarrels, courage',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        31                         : {
                        'name'     : 'Nine of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\30.jpg',
                        'upright'  : 'victory, good health, obstinacy',
                        'reversed' : 'weakness, ill-health, adversity',
                        'dupright' : '''Upright Nine Of Wands
    The Nine of Wands comes as a sign that even in the face of adversity, you stand tall and strong. You may be on the edge of exhaustion, but you are resilient, persistent, and ready to do what it takes to get to the finish line.
    
    This card may also come when you feel battered and bruised, having endured significant challenges and struggles along your path. Just when you think you are making progress, you suffer another setback. The Nine of Wands asks you to trust that this is merely a test of your ‘grit’ and resilience, and know that every time you overcome an obstacle, you are getting stronger. You have the inner resources necessary to overcome any difficulty you encounter, even though it may seem impossible at the time. See this Nine as an assurance that you will eventually prosper if you maintain your position. And, if you do not succeed at first, then try again.
    
    The Nine of Wands encourages you to keep pushing – you are so close to the finish line. Even if you want to give up, this is your final challenge before you reach your goal, so don’t let go of your hopes and dreams when you are so close to making them a reality. Stand firm in the face of your challenges, and you will achieve your goal.
    
    Others may try to oppose your plans, make things difficult for you, or even attack you for what you are putting out into the world. Often, they do it because they’re jealous of your success or are projecting their own insecurities and fears on you. Don’t let them get to you. You are a change-maker, and you have a vital message to share in this world. Don’t dim your light because of others’ insecurities.
    
    On a more positive note, you have people who support you. The Nine of Wands invites you to find your cheerleaders and personal bodyguards, those who will protect you from the ongoing challenges and cheer you on to the finish line. Even if others oppose you, you have many more people who support your cause. Let them help you.
    
    Finally, the advice of the Nine of Wands is to establish your boundaries and fiercely protect those lines. If you allowed others to stand in your way or deplete your energy, it is likely that you have not asserted yourself effectively with those people to protect yourself. Get clear on what you need in this situation to be successful and reach your goals, and then communicate those needs to others. On the same note, be aware that too many barriers will prevent others from getting close to you or helping you. Bring your conscious awareness to how you are proactively using boundaries to protect your energy.''',
                        'dreversed': '''Reversed Nine Of Wands
    The Nine of Wands reversed suggests that you are struggling to keep working towards your goal. The challenges on your path are relentless, pummelling you with setback after setback. You don’t know if you can cope with it anymore and may be ready to give up. Just know that you are oh-so-close to completing this challenge. Draw upon your internal resources – your resilience, inner courage, positive self-talk and mindset – to keep you going. You have it in you to turn this challenging situation into a fantastic success (and to help others facing similar hurdles). Keep fighting – you’ve got this!
    
    The Nine of Wands reversed can also appear when you feel overcome by your responsibilities or lack the support of those around you. It seems as if life is all work and no play. If you know this is a temporary setback, you may just need to push through it for now so you can get to the finish line. Also, make sure you do not take on any other commitments at this stage until you have more control over your circumstances. If you cannot see any end in sight, then get help – hire a personal assistant or a housecleaner, enlist the support of your loved ones, or work with a coach or therapist to help you manage.
    
    Sometimes, the reversed Nine of Wands can indicate paranoia, defensiveness and concern that everyone is out to get you. You may think you are always under attack by the same group of people or you are unfairly targeted. Often, this is a sign of fear from within you rather than an actual external threat. Focus on your own game and don’t worry about what other people are thinking or saying about you.'''
             },
        32                         : {
                        'name'     : 'Ten of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\31.jpg',
                        'upright'  : 'pain, ruined, failure. x',
                        'reversed': 'cleverness, energy, strength. x',
                        'dupright' : '''The Ten of Wands notes that you are taking on an extra burden, a heavier workload, or greater responsibility. Even though it is weighing you down and making things tougher for you, you understand it is only temporary, so you are willing to put in the hard work now to accomplish your goal and reap the rewards later. For example, you may work extra hours to save up for a family holiday. Or you may help out a friend with moving house, knowing they will return the favour when you move later in the year. Or you may care for a sick family member, adding to your responsibilities at home but knowing your loved one deeply appreciates it.
    
    Sometimes, the Ten of Wands appears when you are unconsciously taking on extra responsibility and finding yourself feeling weighed down, exhausted and burnt out. You may try to do everything at once, even though you know it is adding extra pressure to your daily life. The Ten of Wands asks you to stop and examine your current lifestyle or work. Assess which activities or tasks are urgent or important, particularly concerning your broader goals. You may need to use various time management or prioritisation methods to determine where best to spend your time and which tasks you can drop. Your goal needs to be higher efficiency while also freeing yourself up for rest and relaxation when you need it.
    
    The good news is that the Tens in Tarot represent the completion of a cycle, and with the Ten of Wands, the end is in sight! You have been pushing yourself to your limits and working very hard towards your goal. Now, you are taking those final steps on the path to realising your dreams. Sure, you might collapse in a heap of exhaustion when you get there, but you know it will be all worth it and well earned!
    
    The Ten of Wands can also show that even with the achievement of your goal, some significant responsibilities and commitments come with it. When you reach a point of completion, you become starkly aware that you must now carry on with the duties you have laid out for yourself, to ensure ongoing success. The trouble is, however, that these responsibilities may become too much to bear and you are struggling to let go. It is like the business owner who creates a flourishing business but is unprepared to delegate some of his or her responsibilities to the staff and ends up working seventy to eighty hours a week. The inspiration and creativity that came with the initial goal or vision disappear and everything becomes hard work all too quickly. Thus, it is essential to let go of or delegate some of your responsibilities to free you up to still enjoy life.''',
                        'dreversed':'''When the Ten of Wands reversed appears in a Tarot reading, it is often a sign that you are trying to do too much by yourself. In your effort to be everything to everyone, you have found yourself struggling under the weight of it all. Delegate and share the work – you don’t have to do it alone. And be firm in saying no to the things you know you can’t take on. It is imperative you put your self-care and personal well-being first; otherwise you’ll burn yourself out and be of no help to anyone. It’s just like they say, 'Put on your own oxygen mask first before helping others'.
    
    Similarly, the Ten of Wands reversed suggests that you are carrying a heavy weight on your shoulders, but you are keeping this private and are unwilling to share your burden with others. You may be grappling with emotional trauma, carrying a dark secret, or dealing with increased responsibilities. However, you do not feel comfortable sharing this with others, by talking about it or asking for help. In effect, you are pushing away the people who can help you. It may also be a huge relief to you when you do share some of this burden with others, as they are ready and willing to support you.
    
    Sometimes, the reversed Ten of Wands shows that you are holding on to this burden when you do not need to do so. If you are feeling weighed down by your present circumstances, look at ways you might lighten the load. Can you delegate certain tasks and responsibilities? Are you worrying about matters that do not concern you or cannot be changed? Do not become a martyr and take on more than you can realistically handle. On the positive side, if you are going through a challenging time, then the Ten of Wands reversed assures you that this time will soon pass and you will be able to set down this weight.
    
    You may also be actively identifying those activities that do not bring you any value in your life, and you are releasing yourself from these additional responsibilities. Consider going through a purging process, clearing out old clothes and selling old furniture, to declutter and simplify your life. You will benefit from better organisation and prioritisation and enjoy the lightness that comes with such release.'''
             },
        33                         : {
                        'name'     : 'Page of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\32.jpg',
                        'upright'  : 'enthusiasm, exploration, discovery, free spirit',
                        'reversed' : 'setbacks to new ideas, pessimism, lack of direction',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        34                         : {
                        'name'     : 'Knight of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\33.jpg',
                        'upright'  : 'generous, journey, impetuous',
                        'reversed' : 'suspicion, jealousy, narrow-mindedness',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        35                         : {
                        'name'     : 'Queen of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\34.jpg',
                        'upright'  : 'fondness, attraction, command',
                        'reversed' : 'jealous, revengeful, infidelity',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        36                         : {
                        'name'     : 'King of Wands',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\35.jpg',
                        'upright'  : 'passionate, good leader, noble',
                        'reversed' : 'unyielding, prejudice, quarrels',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        37                         : {
                        'name'     : 'Ace of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\36.jpg',
                        'upright'  : 'good health, love, joy, beauty',
                        'reversed' : 'egotism, selfishness, hesitancy',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        38                         : {
                        'name'     : 'Two of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\37.jpg',
                        'upright'  : 'romance, friendship, cooperation',
                        'reversed' : 'violent passion, misunderstanding',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        39                         : {
                        'name'     : 'Three of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\38.jpg',
                        'upright'  : 'fortune, hospitality, discovery',
                        'reversed' : 'hidden, overindulgence, pain, gossip',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        40                         : {
                        'name'     : 'Four of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\39.jpg',
                        'upright'  : 'dissatisfaction, kindness, reevaluation, redemption',
                        'reversed' : 'new goals, ambitions, beginning',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        41                         : {
                        'name'     : 'Five of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\40.jpg',
                        'upright'  : 'broken marriage,vain regret, sorrow, loss',
                        'reversed' : 'return, summon, hope',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        42                         : {
                        'name'     : 'Six of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\41.jpg',
                        'upright'  : 'acquaintance, good memories, happiness',
                        'reversed' : 'disappointment, past',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        43                         : {
                        'name'     : 'Seven of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\42.jpg',
                        'upright'  : 'imagination, illusion, directionless',
                        'reversed' : 'will-power, determination',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        44                         : {
                        'name'     : 'Eight of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\43.jpg',
                        'upright'  : 'disappointment, abandonment, misery',
                        'reversed' : 'pleasure, success, joy',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        45                         : {
                        'name'     : 'Nine of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\44.jpg',
                        'upright'  : 'physical well-being, hopes, security',
                        'reversed' : 'illness, failure, overindulgence',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        46                         : {
                        'name'     : 'Ten of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\45.jpg',
                        'upright'  : 'friendship, happiness, life',
                        'reversed' : 'waste, broken relationships, quarrel',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        47                         : {
                        'name'     : 'Page of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\46.jpg',
                        'upright'  : 'sweetness, interest in literature, gentleness',
                        'reversed' : 'poor imagination, selfishness, no desires',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        48                         : {
                        'name'     : 'Knight of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\47.jpg',
                        'upright'  : 'emotional, romantic dreamer, intelligence',
                        'reversed' : 'idleness, untruthful, fraud, sensuality',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        49                         : {
                        'name'     : 'Queen of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\48.jpg',
                        'upright'  : 'loving mother, gentle, happiness',
                        'reversed' : 'perverse, unhappy, gloom, over-active imagination',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        50                         : {
                        'name'     : 'King of Cups',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\49.jpg',
                        'upright'  : 'kindness, willingness, enjoyment',
                        'reversed' : 'double-dealer, scandal, crafty, violent',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        51                         : {
                        'name'     : 'Ace of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\50.jpg',
                        'upright'  : 'love, valiant, victory',
                        'reversed' : 'obstacles, tyranny, power',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        52                         : {
                        'name'     : 'Two of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\51.jpg',
                        'upright'  : 'indecision, trouble, balanced',
                        'reversed' : 'unscrupulous, release',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        53                         : {
                        'name'     : 'Three of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\52.jpg',
                        'upright'  : 'broken relationship, civil war',
                        'reversed' : 'sorrow, loss, confusion',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        54                         : {
                        'name'     : 'Four of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\53.jpg',
                        'upright'  : 'temporary exile, strife, retreat',
                        'reversed' : 'social unrest, labor strikes, renewed activity',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        55                         : {
                        'name'     : 'Five of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\54.jpg',
                        'upright'  : 'defeat, cowardliness, empty victory',
                        'reversed' : 'unfairness, defeat, loss',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        56                         : {
                        'name'     : 'Six of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\55.jpg',
                        'upright'  : 'harmony, sorrow, journey',
                        'reversed' : 'obstacles, difficulties, defeat',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        57                         : {
                        'name'     : 'Seven of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\56.jpg',
                        'upright'  : 'betrayal, insolence, unwise attempt',
                        'reversed' : 'counsel, helpful, advice',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        58                         : {
                        'name'     : 'Eight of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\57.jpg',
                        'upright'  : 'weakness, indecision, censure',
                        'reversed' : 'freedom, new beginnings, relaxation',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        59                         : {
                        'name'     : 'Nine of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\58.jpg',
                        'upright'  : 'desolation, illness, suspicion, cruelty',
                        'reversed' : 'unselfishness, good news, healing',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        60                         : {
                        'name'     : 'Ten of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\59.jpg',
                        'upright'  : 'defeat, failure, pain',
                        'reversed' : 'courage, positive energy, good health',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        61                         : {
                        'name'     : 'Page of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\60.jpg',
                        'upright'  : 'grace, diplomacy, dexterity, grace',
                        'reversed' : 'imposture, ill-health, cunningness',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        62                         : {
                        'name'     : 'Knight of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\61.jpg',
                        'upright'  : 'strong man, braver, clever person',
                        'reversed' : 'troublemaker, a crafty, tyranny',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        63                         : {
                        'name'     : 'Queen of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\62.jpg',
                        'upright'  : 'skillful, brave, clever, rush',
                        'reversed' : 'sly, keen, deceitful',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        64                         : {
                        'name'     : 'King of Swords',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\63.jpg',
                        'upright'  : 'powerful, friendship, counselor',
                        'reversed' : 'obstinate, evil intentions, judgments',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        65                         : {
                        'name'     : 'Ace of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\64.jpg',
                        'upright'  : 'prosperity, happiness, pleasure',
                        'reversed' : 'misery, greedy, money',
                        'dupright' : '''Upright Ace Of Pentacles
    The Ace of Pentacles, like the other Aces of the Tarot, represents new beginnings, opportunities, and potential – and as a Pentacles card, these new beginnings correlate to the material world: finances, wealth, career, physical health and manifestation of your goals. You may receive a new job offer, an unexpected sum of money, a new business or investment opportunity may come your way, or you’ll have the chance to bring an idea to fruition. No matter the occasion, the Ace of Pentacles heralds a sense of prosperity and abundance in the material or financial areas of your life. It undoubtedly comes as a welcome invitation – but it is not a free ride. As with all Aces in the Tarot deck, this card illustrates the possibility of a new endeavour but does not guarantee its manifestation or success. That piece is up to you.
    
    See the Ace of Pentacles as your ‘green light’. It marks the initial stages of manifesting your goals and assures you that you can truly achieve what you have set your mind to do. The world is your oyster and, through careful planning and determined effort, you can manifest your goals and desires. Your ideas are ready to turn into something tangible and real! This card encourages you to map out how you will achieve your ambitions, create targeted plans and get those actions underway. Keep your eyes open for chances to manifest your goals and realise your inner potential.
    
    The Ace of Pentacles also symbolises wealth, not just for your bank account but in a holistic sense as well. You may discover opportunities to generate a new source of income or receive a financial gift or windfall. Or you may have a chance to create wealth in a broader sense – happiness, fulfilment, potential, and love. This Ace signifies abundance in all areas of your life. Enjoy it! Feel blessed and deserving of everything that comes your way. If you wish to amplify this feeling of prosperity, live by the Law of Attraction and send your positive energy and intent into the Universe so you will receive more in return.''',
                        'dreversed': '''Reversed Ace Of Pentacles
    When the reversed Ace of Pentacles appears in a Tarot reading, you may feel hesitant about moving forward with an offer, invitation or opportunity, particularly one that relates to your career, finances or business. You may catch yourself second-guessing the timing or doubting whether you have what it takes to see it through. Don't move forward until you're ready. Assess the feasibility of your idea and its potential outcomes. Perform your due diligence and figure out if this opportunity is meant for you or not.
    
    The Ace of Pentacles reversed may also be a warning that a financial opportunity – a pay raise, a new job, a loan, or a business offer – could fall through unexpectedly or the other party might retract it without explanation. As the saying goes, “Don’t count your chickens before they hatch!” So, if you get an offer, wait until the money is in your bank account before spending it.
    
    Furthermore, the Ace of Pentacles reversed advises you to be very careful with your expenditures. When the card is inverted, the coin looks as though it's about to fall out of the magical hand. Now is not the time to get in over your head or take on any obligations with huge monthly repayments. Do not rely on the promise of a financial opportunity in the future (like a pay raise or a gift) either. Be pragmatic and allow a bit of ‘fat’ in your budgeting in case you are without employment or have a large and unexpected financial outlay.
    
    At times, the reversed Ace of Pentacles suggests that you are trying to manifest your goals but keep running into delays and other impediments. If you're having limited success, then you may need to revise your proposed approach. Do you need to realign your goals to something more realistic? Financial or other professional advice may be necessary to help you get back on track.
    
    If you are looking to start a new business or take up a new job offer, the reversed Ace of Pentacles warns of a significant risk due to lack of planning and foresight. Do not charge ahead without validating whether the market has a need for your services. Spend a bit more time in the planning stage and give ample consideration to the financial aspects of your new venture.'''
             },
        66                         : {
                        'name'     : 'Two of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\65.jpg',
                        'upright'  : 'harmony, new projects, helpful',
                        'reversed' : 'difficulty, discouragement',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        67                         : {
                        'name'     : 'Three of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\66.jpg',
                        'upright'  : 'abilities, approval,effort, abilities',
                        'reversed' : 'preoccupation, ambitions',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        68                         : {
                        'name'     : 'Four of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\67.jpg',
                        'upright'  : 'ungenerous, greed, miserly',
                        'reversed' : 'spendthrift, obstacles, earthy possessions',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        69                         : {
                        'name'     : 'Five of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\68.jpg',
                        'upright'  : 'destitution, poor health, despair, loneliness',
                        'reversed' : 'employment, courage, revival',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        70                         : {
                        'name'     : 'Six of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\69.jpg',
                        'upright'  : 'employment, courage, revival',
                        'reversed' : 'jealousy, miserliness, unfairness',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        71                         : {
                        'name'     : 'Seven of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\70.jpg',
                        'upright'  : 'development, re-evaluation, effort, hard work',
                        'reversed' : 'impatience, slow progress, investments',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        72                         : {
                        'name'     : 'Eight of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\71.jpg',
                        'upright'  : 'employment, money, learning, trade',
                        'reversed' : 'void, no ambition, dislike',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        73                         : {
                        'name'     : 'Nine of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\72.jpg',
                        'upright'  : 'solitude, well-being, green thumb',
                        'reversed' : 'caution, possible loss',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        74                         : {
                        'name'     : 'Ten of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\73.jpg',
                        'upright'  : 'wealth, property, stability',
                        'reversed' : 'dull, slothfulness, misfortune',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },
        75                         : {
                        'name'     : 'Page of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\74.jpg',
                        'upright'  : 'kindness,new ideas/opinions, scholar',
                        'reversed' : 'luxury, rebellious, bad news',
                        'dupright' : '''''',
                        'dreversed': ''''''

             },
        76                         : {
                        'name'     : 'Knight of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\75.jpg',
                        'upright'  : 'dull outlook, patience, animal lover, trustworthy',
                        'reversed' : 'carelessness, standstill, irresponsible',
                        'dupright' : '''''',
                        'dreversed': ''''''
             },

        77                         : {
                        'name'     : 'Queen of Pentacles',
                        'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\76.jpg',
                        'upright'  : 'thoughtfulness, intelligence, talents, melancholy',
                        'reversed' : 'mistrust, suspicion, neglect',
                        'dupright' : '''''',
                        'dreversed': ''''''

             },
        78                        : {
                       'name'     : 'King of Pentacles',
                       'image'    : 'D:\\antoa\\tarot_sql\\tarot_images\\77.jpg',
                       'upright'  : 'reliable person, steadiness. x',
                       'dupright' : '''Upright King Of Pentacles\n
    The King of Pentacles represents material wealth, financial abundance, and worldly success. This King is a faithful provider; he uses his ambition and confidence to create wealth for himself and others and generates his self-worth from what he has accumulated and can share with others. He is also a fatherly figure who provides others with advice, guidance and wisdom, especially in financial and work-related matters.
    \n
    When the King of Pentacles appears in a Tarot reading, you are confident and successful at attracting and managing wealth. Not only do you identify opportunities for growth and success, but you also draw upon your self-discipline and control to manage your wealth and invest it wisely for the long-term.
    \n
    The arrival of the King of Pentacles indicates that you can translate your vision into something tangible, practical, and often very lucrative. You are the ultimate business owner. You do not merely come up with ideas and hope for the best – you work hard to map out your plan of attack, gather your resources and manifest your goals, often with tremendous success. You are like King Midas: everything you touch turns to gold. When you apply yourself to your vision, you create huge success, particularly on a financial level. Money flows easily and abundantly to you, and as you sit at the pinnacle of your economic power and influence, you can rest assured of your continued prosperity. You no longer struggle to achieve what you desire, like the Page and the Knight, nor do you have any need to prove yourself.
    \n
    The King of Pentacles often indicates the final fulfilment of a creative task, a business venture or investment. Through diligence, responsibility and attention to detail, you have achieved great things and can finally say that you have completed your task or attained your goal. You can now enjoy all that you have accomplished and the successes you have created. You have created a rich life, not just financially but also spiritually, which will set you up well for the future.
    \n
    The King of Pentacles knows that a methodical, planned and well-thought-out approach will lead you to success. You have experimented in the past with what works best and have landed on your own methods and practices you know will continue to work for you in the future. Continue down this path rather than trying new ways of doing things. You do not need to take any more risks.\n''',
                       'reversed' : 'bribes, materialistic, calm. x',
                       'dreversed':'''Reversed King Of Pentacles\n
    The King of Pentacles reversed asks you to look at your relationship with money and wealth. On the one hand, you may not be managing your wealth well. You may attract large sums of money through your business enterprises or a high-flying career, but as soon as the cash hits your bank account, it’s on its way out again as you splurge on expensive items or invest in high-risk opportunities. You are not treating your money with respect, and instead, need to draw upon your self-discipline and control so you can save for your future while still enjoying the fruits of your labour.
    \n
    On the other hand, you may be putting money before anything else, negatively impacting your relationships and well-being. You may be a workaholic, over-investing in wealth creation and neglecting your loved ones. You may do anything for an extra buck, even if it means selling your soul and your integrity. You may be so impressed by other people’s status and social position that you kowtow to anyone ‘above’ you while dismissing anyone ‘below’ you. You might continuously name-drop and try to prove yourself by bragging about the people you know. If this resonates, step back for a moment and look at the greater impact of your obsession with money. Is it serving you in this state, or do you need to change?
    \n
    At times, the reversed King of Pentacles represents someone who is very stubborn and rigid in his approach. When this King shows up in a reading, look at your life. Are you feeling ‘stuck in a rut’? Has life become so predictable and routine that it is completely dull and lifeless? Being grounded is a good thing, but give yourself permission every now and then to break free and do something different. You don’t have to be so serious all of the time.'''

            },
    }

    # for card_number in range(1,79):
    #     c.execute("INSERT INTO Tarot_Cards VALUES('"
    #               + Tarot_Deck[card_number]['name'] + "', '"
    #               + Tarot_Deck[card_number]['upright'] + "', '"
    #               + Tarot_Deck[card_number]['reversed'] + "', '"
    #               + Tarot_Deck[card_number]['image'] + "')")


    c.execute("SELECT * FROM Tarot_Cards")

    # t = c.fetchone() #returns first item from Select statement
    # t = c.fetchmany(8) # returns first x from Select statement
    t = c.fetchall() # fetches all entries from Select statement
    for entry in t:
        print(entry)

    conn.commit()

    conn.close()

def user_daily_read_creation():

    conn = sqlite3.connect("tarot.db")

    c = conn.cursor()

    # c.execute('''CREATE TABLE  User_Daily_Read (
    #             User TEXT,
    #             date DATETIME,
    #             Past  TEXT,
    #             Present  TEXT,
    #             Future  TEXT)
    #             ''')

    c.execute("SELECT * FROM User_Daily_Read")

    conn.commit()

    conn.close()

def user_daily_read():

    conn = sqlite3.connect("tarot.db")

    c = conn.cursor()

    c.execute("SELECT Name FROM Tarot_Cards")

    card_names = c.fetchall()

    reading = {}

    co=0
    for card in sorted(card_names, key=lambda x: random.random())[0:3]:
        reading[card[0]] = {}
        reading[card[0]]['tense'] = ['past', 'present', 'future'][co]
        reading[card[0]]['position'] = random.choice(['upright', 'reversed'])
        reading[card[0]]['url'] = ''
        co+=1


    print(reading)
    for card in reading.keys():
        c.execute('SELECT Image_Url FROM Tarot_Cards WHERE name = "' + card + '"')
        i = c.fetchone()
        reading[card]['url'] = i[0]

    img_list = []

    for tcimage in reading.keys():
        img_list.append(image_correction(reading[tcimage]['url'], tcimage,  reading[tcimage]['tense'], reading[tcimage]['position']))

    get_concat_h_multi_blank(img_list).save('D:\\antoa\\tarot_sql\\reading.jpg')







# tarot_card_creation()
user_daily_read()