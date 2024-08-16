from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__, static_folder='static')

data = { "1": {
		"Id": "1",
"Title": "Murder on the Orient Express",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388267702i/16304.jpg",
"Plot": "Just after midnight, the famous Orient Express is stopped in its tracks by a snowdrift. By morning, the millionaire Samuel Edward Ratchett lies dead in his compartment, stabbed a dozen times, his door locked from the inside. One of his fellow passengers must be the murderer. Isolated by the storm, detective Hercule Poirot must find the killer among a dozen of the dead man’s enemies, before the murderer decides to strike again…",
"Year Published": "1934", 
"Similar Detective": ["2", "5", "6", "9", "12", "13", "15"],
"Detective": "Hercule Poirot", 
},
"2": {
		"Id": "2",
"Title": "Murder of Roger Ackroyd",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1389734015i/16328.jpg",
"Plot": "The peaceful English village of King\'s Abbot is stunned. The widow Ferrars dies from an overdose of Veronal. Not twenty-four hours later, Roger Ackroyd—the man she had planned to marry—is murdered. It is a baffling case involving blackmail and death that taxes Hercule Poirot\'s \"little gray cells\" before he reaches one of the most startling conclusions of his career.",
"Year Published": "1926", 
"Similar Detective": ["1", "5", "6", "9", "12", "13", "15"],
"Detective": "Hercule Poirot",
},
"3": {
		"Id": "3",
"Title": "And Then There Were None",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1638425885i/16299.jpg",
"Plot": "First, there were ten—a curious assortment of strangers summoned as weekend guests to a little private island off the coast of Devon. Their host, an eccentric millionaire unknown to all of them, is nowhere to be found. All that the guests have in common is a wicked past they\'re unwilling to reveal—and a secret that will seal their fate. For each has been marked for murder. A famous nursery rhyme is framed and hung in every room of the mansion: Ten little boys went out to dine; One choked his little self and then there were nine. Nine little boys sat up very late; One overslept himself and then there were eight. Eight little boys traveling in Devon; One said he\'d stay there then there were seven. Seven little boys chopping up sticks; One chopped himself in half and then there were six. Six little boys playing with a hive; A bumblebee stung one and then there were five. Five little boys going in for law; One got in Chancery and then there were four. Four little boys going out to sea; A red herring swallowed one and then there were three. Three little boys walking in the zoo; A big bear hugged one and then there were two. Two little boys sitting in the sun; One got frizzled up and then there was one. One little boy left all alone; He went out and hanged himself and then there were none. When they realize that murders are occurring as described in the rhyme, terror mounts. One by one they fall prey. Before the weekend is out, there will be none. Who has choreographed this dastardly scheme? And who will be left to tell the tale? Only the dead are above suspicion.",
"Year Published": "1939", 
"Similar Detective": ["11"],
"Detective": "No Detective",
},
"4": {
		"Id": "4",
"Title": "A Murder is Announced",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1348508635i/16298.jpg",
"Plot": "\"A Murder is Announced\" is a staple of crime fiction and often considered as the best Miss Marple novel. The villagers of Chipping Cleghorn, including Jane Marple who is staying nearby, are agog with curiosity over an advertisement in the local gazette which reads: \'A murder is announced and will take place on Friday October 29th, at Little Paddocks at 6.30 p.m.\' Is this a childish practical joke? Or a hoax intended to scare poor Letitia Blacklock? Unable to resist the mysterious invitation, a crowd gathers at Little Paddocks at the appointed time when, without warning, the lights go out…",
		"Year Published": "1950", 
"Similar Detective": ["7", "8", "10", "14"],
"Detective": "Miss Marple",
},
"5": {
		"Id": "5",
"Title": "Evil Under the Sun",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1386922974i/16305.jpg",
"Plot": "The beautiful bronzed body of Arlena Stuart lay face down on the beach. But strangely, there was no sun and she was not sunbathing... she had been strangled. Ever since Arlena\'s arrival the air had been thick with sexual tension. Each of the guests had a motive to kill her. But Hercule Poirot suspects that this apparent \'crime of passion\' conceals something much more evil.",
		"Year Published": "1941", 
"Similar Detective": ["1", "2", "6", "9", "12", "13", "15"],
"Detective": "Hercule Poirot",
},
"6": {
		"Id": "6",
"Title": "The Hollow",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1308815448i/16303.jpg",
"Plot": "Lady Angkatell, intrigued by the criminal mind, has invited Hercule Poirot to her estate for a weekend house party. The Belgian detective\'s arrival at the Hollow is met with an elaborate tableau staged for his amusement: a doctor lies in a puddle of red paint, his timid wife stands over his body with a gun while the other guests look suitably shocked. But this is no charade. The paint is blood and the corpse real!",
		"Year Published": "1946", 
"Similar Detective": ["1", "2", "5", "9", "12", "13", "15"],
"Detective": "Hercule Poirot",
},
"7": {
		"Id": "7",
"Title": "The Moving Finger",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1396227246i/16341.jpg",
"Plot": "The placid village of Lymstock seems the perfect place for Jerry Burton to recuperate from his accident under the care of his sister, Joanna. But soon a series of vicious poison-pen letters destroys the village's quiet charm, eventually causing one recipient to commit suicide. The vicar, the doctor, the servants—all are on the verge of accusing one another when help arrives from an unexpected quarter. The vicar's houseguest happens to be none other than Jane Marple.",
		"Year Published": "1942", 
"Similar Detective": ["4", "8", "10", "14"],
"Detective": "Miss Marple",
},
"8": {
		"Id": "8",
"Title": "The Body in the Library",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1389733809i/16319.jpg",
"Plot": "It\'s seven in the morning. The Bantrys wake to find the body of a young woman in their library. She is wearing an evening dress and heavy make-up, which is now smeared across her cheeks. But who is she? How did she get there? And what is the connection with another dead girl, whose charred remains are later discovered in an abandoned quarry? The respectable Bantrys invites Miss Marple to solve the mystery… before tongues start to wag.",
		"Year Published": "1942", 
"Similar Detective": ["4", "7", "10", "14"],
"Detective": "Miss Marple",
},
"9": {
		"Id": "9",
"Title": "The ABC Murders",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1389733983i/16322.jpg",
"Plot": "When Alice Asher is murdered in Andover, Hercule Poirot is already looking into the clues. Alphabetically speaking, it\'s one letter down, twenty-five to go. There\'s a serial killer on the loose. His macabre calling card is to leave the ABC Railway Guide beside each victim\'s body. But if A is for Alice Asher, bludgeoned to death in Andover, and B is for Betty Bernard, strangled with her belt on the beach at Bexhill, who will then be Victim C? More importantly, why is this happening?",
		"Year Published": "1936", 
"Similar Detective": ["1", "2", "5", "6", "12", "13", "15"],
"Detective": "Hercule Poirot",
},
"10": {
		"Id": "10",
"Title": "Pocket Full of Rye",		
"Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1389760577i/834378.jpg",
"Plot": "Let us explain. Rex Fortescue, king of a financial empire, was sipping tea in his \'counting house\' office when he suffered a sudden and agonizing death. On later inspection, the pockets of the deceased were found to contain rye grain. What is that all about? It was a second incident, this time in the parlor at his home, which confirmed Jane Marple\'s suspicion that here she was looking at a case of crime by rhyme!",
		"Year Published": "1953", 
"Similar Detective": ["4", "7", "8", "14"],
"Detective": "Miss Marple",
},
"11": {
    "Id": "11",
    "Title": "Why Didn\'t They Ask Evans",
    "Image":"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1311988642i/102303.jpg",
    "Plot": "Was it a misstep that sent a handsome stranger plummeting to his death from a cliff? Or something more sinister? Fun-loving adventurers Bobby Jones and Frances Derwent\'s suspicions are certainly roused--espeically since the man\'s dying words were so peculiar: Why didn\'t they ask Evans? Bobby and Frances would love to know. Unfortunately, asking the wrong people has sent the amateur sleuths running for their lives--on a wild and deadly pursuit to discover who Evans is, what it was he wasn\'t asked, and why the mysterious inquiry has put their own lives in mortal danger...",
    "Year Published": "1934",
    "Similar Detective": ["2"],
    "Detective": "No Detective",
},
"12": {
    "Id": 12,
    "Title": "Five Little Pigs",
    "Image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1429422068i/121648.jpg",
    "Plot": "It was an open and shut case. All the evidence said Caroline Crale poisoned her philandering husband, a brilliant painter. She was quickly and easily convicted and sentenced to life in prison.\n\nNow, sixteen years later, in a posthumous letter, Mrs. Crale has assured her grown daughter that she was innocent. But instead of setting the young woman\'s mind at ease, the letter only raises disquieting questions. Did Caroline indeed write the truth? And if she didn\'t kill her husband, who did?\n\nTo find out, the Crale\'s daughter asks Hercule Poirot to reopen the case. His investigation takes him deep into the conflicting memories and motivations of the five other people who were with the Crales on the fatal day. With his keen understanding of human psychology, he manages to discover the surprising truth behind the artist\'s death.",
    "Year Published": "1942",
    "Similar Detective": ["1", "2", "5", "6", "9", "13", "15"],
    "Detective": "Hercule Poirot",
},
"13":{
    "Id": 13,
    "Title": "The Mysterious Affair at Styles",
    "Image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1585632445i/52843028.jpg",
    "Plot": "A refugee of the Great War, Poirot has settled in England near Styles Court, the country estate of his wealthy benefactor, the elderly Emily Inglethorp. When Emily is poisoned and the authorities are baffled, Poirot puts his prodigious sleuthing skills to work. Suspects are plentiful, including the victim\'s much younger husband, her resentful stepsons, her longtime hired companion, a young family friend working as a nurse, and a London specialist on poisons who just happens to be visiting the nearby village. All of them have secrets they are desperate to keep, but none can outwit Poirot as he navigates the ingenious red herrings and plot twists that contribute to Agatha Christie\'s well-deserved reputation as the queen of mystery.",
    "Year Published": "1920",
    "Similar Detective": ["1", "2", "5", "6", "9", "12", "15"],
    "Detective": "Hercule Poirot",
},
"14": {
    "Id": 14,
    "Title": "Murder at the Vicarage",
    "Image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388386575i/16331.jpg",
    "Plot": "\'Anyone who murdered Colonel Protheroe,\' declared the parson, brandishing a carving knife above a joint of roast beef, \'would be doing the world at large a favour!\' It was a careless remark for a man of the cloth. And one which was to come back and haunt the clergyman just a few hours later -- when the colonel was found shot dead in the clergyman\'s study. But as Miss Marple soon discovers, the whole village seems to have had a motive to kill Colonel Protheroe.",
    "Year Published": "1930",
    "Similar Detective": ["4", "7", "8", "10"],
    "Detective": "Miss Marple",
},
"15": {
    "Id": 15,
    "Title": "Appointment with Death",
    "Image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1308808730i/16363.jpg",
    "Plot": "Among the towering red cliffs of Petra, like some monstrous swollen Buddha, sat the corpse of Mrs Boynton. A tiny puncture mark on her wrist was the only sign of the fatal injection that had killed her. With only 24 hours available to solve the mystery, Hercule Poirot recalled a chance remark he\'d overheard back in Jerusalem: \'You see, don\'t you, that she\'s got to be killed?\' Mrs Boynton was, indeed, the most detestable woman he\'d ever met.",
    "Year Published": "1938",
    "Similar Detective": ["1", "2", "5", "6", "9", "12", "13"],
    "Detective": "Hercule Poirot",
}
}

@app.template_filter('highlight_search')
def highlight_search(title, query):
    words = title.split()
    highlighted_title = []
    
    for word in words:
        if query.lower() in word.lower():
            index = word.lower().find(query.lower())
            highlighted_word = (word[:index] + f'<span class="highlight">{word[index:index+len(query)]}</span>' 
                                + word[index + len(query):])
            highlighted_title.append(highlighted_word)
        else:
            highlighted_title.append(word)
    
    return ' '.join(highlighted_title)

@app.route('/')
def welcome():
    popular_items = list(data.values())[:3]
    info = list(data.values())
    return render_template('welcome.html', data=info, popular_items=popular_items)

@app.route('/search', methods =["GET"])
def search_results():
    query = request.args.get('query', '').strip()
    if not query:
        return render_template('search_results.html', query=query, results=[])
    
    matching_results = []
    for item_id, item_data in data.items():
        if query.lower() in item_data['Title'].lower() or query.lower() in item_data['Detective'].lower() or query.lower() in item_data['Year Published'].lower():
            matching_results.append(item_data)

    return render_template('search_results.html', query=query, results=matching_results)

@app.route('/view/<string:item_id>')
def view_item(item_id):
    item = data.get(item_id)
    
    return render_template('view_data.html', data=data, item=item) 

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def adding():
    identification = len(data) + 1
    title = request.form.get('title')
    image = request.form.get('imgadr')
    plot = request.form.get('plot')
    detective = request.form.get('detective')
    year = request.form.get('year')

    new_book = {"Id": identification, "Title": title, "Image": image, "Plot": plot, "Similar Detective": [], "Year Published": year, "Detective": detective}
    count = len(data) + 1
    index = '' + str(count) + ''
    data[index]= (new_book)

    for items in list(data.values())[:-1]:
        if new_book["Detective"] == items["Detective"]:
            identification = str(items["Id"])
            new_book["Similar Detective"].append(identification)
            items["Similar Detective"].append(index)
 
    return jsonify(result=new_book) 

@app.route('/edit/<id>')
def edit(id):
    result = data.get(id)
    return render_template('edit.html', result=result)

@app.route('/edit/<id>', methods=['POST'])
def update_edit(id):
    item = data.get(id)
    identification = item["Id"]
    title = request.form.get('title')
    image = request.form.get('imgadr')
    plot = request.form.get('plot')
    detective = request.form.get('detective')
    year = request.form.get('year')

    updated_book = {"Id": identification, "Title": title, "Image": image, "Plot": plot, "Similar Detective": [], "Year Published": year, "Detective": detective}

    for items in data.values():
        index = items["Id"]
        if detective == items["Detective"]:
            if title == items["Title"]:
                continue
            updated_book["Similar Detective"].append(index)
            identification = str(identification)
            items["Similar Detective"].append(identification)
        if (detective != items["Detective"]) and (identification in items["Similar Detective"]):
            items["Similar Detective"].remove(identification)
    
    data[identification] = updated_book
    
    return render_template('view_data.html', item=updated_book, data=data)

if __name__ == '__main__':
   app.run(debug = True)