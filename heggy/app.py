from bs4 import BeautifulSoup

html_doc = '''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''

# soup = BeautifulSoup(html_doc, 'html.parser')  # output of soup html obj, and a parse tree
# BeautifulSoup transform the markup into a parse tree, which is set of linked objects representing the structure of the document.
# print(soup) # prints html out on the screen

# print(soup.prettify()[0:350]) # first 350 elements

soup = BeautifulSoup('<b body="description"">Product Description</b>', 'html')
tag=soup.b
type(tag)
print(tag)
print(f'########tag name:####### {tag.name}')
tag.name = 'bestbooks'
print(f'########reassign tag.name = bestbooks:####### {tag.name}')
print(f'########print out the whole prettify ####### {tag.name}')
print(soup.prettify()[0:350])

print('########reassign tag[body] is assigned description:#######')
print(tag['body'])

print('######## attribute of tag :#######')
print(tag.attrs)

tag['id']