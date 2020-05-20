import lxml.etree as ET

# LELU file path
file_path = 'final_SPF_2.xml'

# Initializes the parser
parser = ET.XMLParser(recover=True)

# Parses the file
tree = ET.parse(file_path, parser=parser)
xroot = tree.getroot()

# Questions and answers
data_answers = {}
data_text = {}

# Process the file
for node in xroot:
    link_id = node.attrib.get('link_id')
    subreddit_id = node.attrib.get('subreddit_id')
    # Iterates over the posts into the conv
    for j in range(len(node.getchildren())):
        #uid = node.getchildren()[j].get('uid')
        comment_id = node.getchildren()[j].get('comment_id')
        #score = node.getchildren()[j].get('score')
        parent_id = node.getchildren()[j].get('parent_id')
        #create_utc = node.getchildren()[j].get('create_utc')
        text = node.getchildren()[j].text
        # Add it as a question
        data_answers[(link_id,subreddit_id,comment_id)] = []
        # Add it as an answer
        if (link_id,subreddit_id,parent_id) in data_answers:
        	data_answers[(link_id,subreddit_id,parent_id)].append((link_id,subreddit_id,comment_id))
       	# Add a reference to its text
       	data_text[(link_id,subreddit_id,comment_id)] = text.replace("\n"," ").lower()

# Make the list
for (link_id,subreddit_id,comment_id), answers in data_answers.items():
	question_text = data_text[(link_id,subreddit_id,comment_id)]
	for answer_link_id,answer_subreddit_id,answer_comment_id in answers:
		answer_text = data_text[(answer_link_id,answer_subreddit_id,answer_comment_id)]
		print("Question : " + question_text)
		print("Answer : " + answer_text)


