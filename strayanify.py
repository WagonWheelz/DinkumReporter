# strayanifier.py
import random
import re

def strayanify(text):
    endings = [
        "mate", "cobber", "sheila", "drongo", "legend", "bloke", "roo", "bushie", "battler",
        "galah", "bogan", "larrikin", "digger", "tradie", "ocker"
    ]
    
    interjections = [
        "Oi", "Crikey", "Strewth", "Blimey", "Fair dinkum", "Too right", "Nah yeah", "Reckon", 
        "Deadset", "Stone the crows", "Flamin’ hell", "How good's that", "Bloody oath"
    ]
    
    # Common Aussie replacements (word boundaries ensure full word matches)
    replacements = {
        r'\bhello\b': 'g’day',
        r'\bhi\b': 'g’day',
        r'\bhow are you\b': 'how ya goin’',
        r'\bare you\b': 'ya',
        r'\bmy\b': 'me',
        r'\bfriend\b': 'mate',
        r'\bfriends\b': 'mates',
        r'\bgood\b': 'bonza',
        r'\bgreat\b': 'ripper',
        r'\bman\b': 'bloke',
        r'\bwoman\b': 'sheila',
        r'\bboy\b': 'lad',
        r'\bgirl\b': 'lass',
        r'\bchildren\b': 'ankle biters',
        r'\bthank you\b': 'cheers',
        r'\bthanks\b': 'ta',
        r'\bvery\b': 'bloody',
        r'\bno\b': 'nah',
        r'\byes\b': 'yeah',
        r'\bmaybe\b': 'spose',
        r'\bnothing\b': 'nothin’ much',
        r'\bsomething\b': 'somethin’',
        r'\bnice\b': 'beaut',
        r'\bawesome\b': 'mad as',
        r'\blunch\b': 'sanga',
        r'\bbreakfast\b': 'brekkie',
        r'\bdinner\b': 'tea',
        r'\bbarbecue\b': 'barbie',
        r'\bmcdonald\'?s\b': 'Macca’s',
        r'\bflip flops\b': 'thongs',
        r'\btoilet\b': 'dunny',
        r'\bafternoon\b': 'arvo',
        r'\btruck\b': 'ute',
        r'\bMcDonald\'?s\b': 'Macca’s',
        r'\bsick\b': 'crook',
        r'\btired\b': 'knackered',
        r'\bdrunk\b': 'maggoted',
        r'\bpolice\b': 'coppers',
        r'\bcigarette\b': 'durry',
        r'\bshoes\b': 'boots',
        r'\bflip-flops\b': 'thongs',
        r'\bfood\b': 'tucker',
        r'\bdesert\b': 'outback',
        r'\bcrazy\b': 'mad as a cut snake',
        r'\bhot\b': 'scorchin’',
        r'\bcold\b': 'bloody chilly',
        r'\bwait a moment\b': 'hold ya horses',
    }

    # Replace words with Aussie slang
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Drop g's from -ing words
    text = re.sub(r'(\w+)ing\b', r"\1in’", text)

    # Aussie-ify punctuation and shortenings
    text = text.replace("you", "ya")
    text = text.replace("You", "Ya")

    # Add interjection and ending
    text = random.choice(interjections) + ", " + text
    text += f", ya {random.choice(endings)}!"

    print("[Strayanifier] Local Strayanified:", text)
    return text
