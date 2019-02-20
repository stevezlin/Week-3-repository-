
# Lists of pages stored in dictionary

pages = [
	{ 
	"filename": "content/index.html",
	"output": "docs/index.html",
	"title": "Meet Steve",
	},
	{ 
	"filename": "content/projects.html",
	"output": "docs/projects.html",
	"title": "My future projects",
	},
	{ 
	"filename": "content/contact.html",
	"output": "docs/contact.html",
	"title": "Contact me",
	}
]


print ('Using functions and loops to combine pages')


# function used to combine html

def combine_template():
	template = open("templates/base.html").read()
	index_content = open("content/index.html").read()
	finished_index_page = template.replace("{{content}}", index_content)
	open("docs/index.html", "w+").write(finished_index_page)
	return results
	

combine_template()


	
	

	
  

    
# combines base html with index and creates output file in docs

#for page in pages:
	top_html = open ('templates/top.html').read()
	bottom_html = open ('templates/bottom.html').read()
	content = open ('content/index.html').read()
	index_html = top_html + content + bottom_html
	open('docs/index.html', 'w+').write(index_html)
	content = open(page['filename']).read()
	combined = top_html + content + bottom_html
	open(page['output'],'w+').write(combined) 
	




print ('Finished combining HTML templates with conent')


