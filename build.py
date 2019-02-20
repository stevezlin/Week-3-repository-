print ('Using functions and loops to combine pages')

# Opening template HTML files
top_html = open ('templates/top.html').read()
bottom_html = open ('templates/bottom.html').read()

# Using function to make template from top and bottom html

def main():
    top_html = open ('templates/top.html').read()
    bottom_html = open ('templates/bottom.html').read()
    base_html = top_html + bottom_html
    open('templates/base.html', 'w+').write(base_html)
    print('Combined top and bottom html to create base.html')

main()
    

    




# Combine index HTML with top and bottom templates


index_html = top_html + index_html + bottom_html
open('docs/index.html', 'w+').write(index_html)


# Read project HTML file
projects_html = open ('content/projects.html').read()

# Combine project HTML with top and bottom html templates
projects_html = top_html + projects_html + bottom_html
open('docs/projects.html', 'w+').write(projects_html)

# Read contact HTML file 
contact_html = open ('content/contact.html').read()

# Combine contact_html with top and bottom
contact_html = top_html + contact_html + bottom_html
open('docs/contact.html', 'w+').write(contact_html)

print ('Finished combining HTML templates with conent')
