""" Script to load excuses in the database """

import sqlite3

excuses_data = [
    {"http_code": 701, "tag": "Inexcusable", "message": "Meh"},
    {"http_code": 702, "tag": "Inexcusable", "message": "Emacs"},
    {"http_code": 703, "tag": "Inexcusable", "message": " Explosion"},
    {"http_code": 704, "tag": "Inexcusable", "message": " Goto Fail"},
    {"http_code": 705, "tag": "Inexcusable", "message": " I wrote the code and missed the necessary validation by an oversight(see 795)"},
    {"http_code": 706, "tag": "Inexcusable", "message": " Delete Your Account"},
    {"http_code": 707, "tag": "Inexcusable", "message": " Can't quit vi"},
    {"http_code": 710, "tag": "Novelty Implementations", "message": " PHP"},
    {"http_code": 711, "tag": "Novelty Implementations", "message": " Convenience Store"},
    {"http_code": 712, "tag": "Novelty Implementations", "message": " NoSQL"},
    {"http_code": 718, "tag": "Novelty Implementations", "message": " I am not a teapot"},
    {"http_code": 719, "tag": "Novelty Implementations", "message": " Haskell"},
    {"http_code": 720, "tag": "Edge Cases", "message": " Unpossible"},
    {"http_code": 721, "tag": "Edge Cases", "message": " Known Unknowns"},
    {"http_code": 722, "tag": "Edge Cases", "message": " Unknown Unknowns"},
    {"http_code": 723, "tag": "Edge Cases", "message": " Tricky"},
    {"http_code": 724, "tag": "Edge Cases", "message": " This line should be unreachable"},
    {"http_code": 725, "tag": "Edge Cases", "message": " It works on my machine"},
    {"http_code": 726, "tag": "Edge Cases", "message": " It's a feature, not a bug"},
    {"http_code": 727, "tag": "Edge Cases", "message": " 32 bits is plenty"},
    {"http_code": 728, "tag": "Edge Cases", "message": " It works in my timezone"},
    {"http_code": 730, "tag": "Fucking", "message": " Fucking npm"},
    {"http_code": 731, "tag": "Fucking", "message": " Fucking Rubygems"},
    {"http_code": 732, "tag": "Fucking", "message": " Fucking Unic💩de"},
    {"http_code": 733, "tag": "Fucking", "message": " Fucking Deadlocks"},
    {"http_code": 734, "tag": "Fucking", "message": " Fucking Deferreds"},
    {"http_code": 736, "tag": "Fucking", "message": " Fucking Race Conditions"},
    {"http_code": 735, "tag": "Fucking", "message": " Fucking IE"},
    {"http_code": 737, "tag": "Fucking", "message": " FuckThreadsing"},
    {"http_code": 738, "tag": "Fucking", "message": " Fucking Exactly-once Delivery"},
    {"http_code": 739, "tag": "Fucking", "message": " Fucking Windows"},
    {"http_code": 738, "tag": "Fucking", "message": " Fucking Exactly"},
    {"http_code": 739, "tag": "Fucking", "message": " Fucking McAfee"},
    {"http_code": 750, "tag": "Syntax Errors", "message": " Didn't bother to compile it"},
    {"http_code": 753, "tag": "Syntax Errors", "message": " Syntax Error"},
    {"http_code": 754, "tag": "Syntax Errors", "message": " Too many semi-colons"},
    {"http_code": 755, "tag": "Syntax Errors", "message": " Not enough semi-colons"},
    {"http_code": 756, "tag": "Syntax Errors", "message": " Insufficiently polite"},
    {"http_code": 757, "tag": "Syntax Errors", "message": " Excessively polite"},
    {"http_code": 759, "tag": "Syntax Errors", "message": " Unexpected `T_PAAMAYIM_NEKUDOTAYIM`"},
    {"http_code": 761, "tag": "Substance", "message": " Hungover"},
    {"http_code": 762, "tag": "Substance", "message": " Stoned"},
    {"http_code": 763, "tag": "Substance", "message": " Under-Caffeinated"},
    {"http_code": 764, "tag": "Substance", "message": " Over-Caffeinated"},
    {"http_code": 765, "tag": "Substance", "message": " Railscamp"},
    {"http_code": 766, "tag": "Substance", "message": " Sober"},
    {"http_code": 767, "tag": "Substance", "message": " Drunk"},
    {"http_code": 768, "tag": "Substance", "message": " Accidentally Took Sleeping Pills Instead Of Migraine Pills During Crunch Week"},
    {"http_code": 771, "tag": "Predictable Problems", "message": " Cached for too long"},
    {"http_code": 772, "tag": "Predictable Problems", "message": " Not cached long enough"},
    {"http_code": 773, "tag": "Predictable Problems", "message": " Not cached at all"},
    {"http_code": 774, "tag": "Predictable Problems", "message": " Why was this cached?"},
    {"http_code": 775, "tag": "Predictable Problems", "message": " Out of cash"},
    {"http_code": 776, "tag": "Predictable Problems", "message": " Error on the Exception"},
    {"http_code": 777, "tag": "Predictable Problems", "message": " Coincidence"},
    {"http_code": 778, "tag": "Predictable Problems", "message": " Off By One Error"},
    {"http_code": 779, "tag": "Predictable Problems", "message": " Off By Too Many To Count Error"},
    {"http_code": 780, "tag": "Somebody Else's Problem", "message": " Project owner not responding"},
    {"http_code": 781, "tag": "Somebody Else's Problem", "message": " Operations"},
    {"http_code": 782, "tag": "Somebody Else's Problem", "message": " QA"},
    {"http_code": 783, "tag": "Somebody Else's Problem", "message": " It was a customer request, honestly"},
    {"http_code": 784, "tag": "Somebody Else's Problem", "message": " Management, obviously"},
    {"http_code": 785, "tag": "Somebody Else's Problem", "message": " TPS Cover Sheet not attached"},
    {"http_code": 786, "tag": "Somebody Else's Problem", "message": " Try it now"},
    {"http_code": 787, "tag": "Somebody Else's Problem", "message": " Further Funding Required"},
    {"http_code": 788, "tag": "Somebody Else's Problem", "message": " Designer's final designs weren't"},
    {"http_code": 789, "tag": "Somebody Else's Problem", "message": " Not my department"},
    {"http_code": 791, "tag": "Internet crashed", "message": " The Internet shut down due to copyright restrictions"},
    {"http_code": 792, "tag": "Internet crashed", "message": " Climate change driven catastrophic weather event"},
    {"http_code": 793, "tag": "Internet crashed", "message": " Zombie Apocalypse"},
    {"http_code": 794, "tag": "Internet crashed", "message": " Someone let PG near a REPL"},
    {"http_code": 795, "tag": "Internet crashed", "message": " #heartbleed (see 705)"},
    {"http_code": 796, "tag": "Internet crashed", "message": " Some DNS fuckery idno"},
    {"http_code": 797, "tag": "Internet crashed", "message": " This is the last page of the Internet. Go back"},
    {"http_code": 798, "tag": "Internet crashed", "message": " I checked the db backups cupboard and the cupboard was bare"},
    {"http_code": 799, "tag": "Internet crashed", "message": " End of the world"},
]
# Connect to db
connection = sqlite3.connect('excuses.db')
cursor = connection.cursor()

# Create DB if it's doesn't exist yet
cursor.execute('''CREATE TABLE IF NOT EXISTS excuses (
                    id INTEGER PRIMARY KEY,
                    http_code INTEGER,
                    tag TEXT,
                    message TEXT
                )''')

# Insert Data
for excuse in excuses_data:
    cursor.execute('''INSERT INTO excuses (http_code, tag, message) VALUES (?, ?, ?)''',
                   (excuse["http_code"], excuse["tag"], excuse["message"]))

connection.commit()
connection.close()

print("The excuses were loaded with success, GG !")
