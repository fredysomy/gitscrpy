<h1 align="center"> Gitscrpy </h1>

***



* `A python library to scrape github.`
* `Simple to use syntax`
* `Install using pip`

<h2 id="install">Install</h2>

```python
pip install gitscrpy


```

<h2 id="install">Run</h2>

```python
 from gitscrpy import getgit
 # Imports the package

 a=getgit.gitinit("fredysomy")
 # Initialize

# User repository functions

 a.getrepo(n)
 # return the first n repos in the users repository list.

 a.getrepo(2)

 # [{'name': 'MarkdownIt', 'description': 'Efficient Code Editor to live render Markdown and save as Markdown,Html and Pdf +⚡ Instant Hosting in The Web.⚡', 'url': 'https://github.com/fredysomy/MarkdownIt', 'stars': '13'}, {'name': 'fredysomy', 'url': 'https://github.com/fredysomy/fredysomy', 'stars': '4'}]
a.getrepo(1)
 # {'name': 'MarkdownIt', 'description': 'Efficient Code Editor to live render Markdown and save as Markdown,Html and Pdf +⚡ Instant Hosting in The Web.⚡', 'url': 'https://github.com/fredysomy/MarkdownIt', 'stars': '13'}

# User details functions

a.getuser("star")
# Retrun no of stars user have 
# 172

a.getuser("name")
# Returns the name of the User
# Fredy Somy

a.getuser("u_name")
# Returns the Username of the User
# fredysomy

a.getuser("follower")
# Returns no of followers the User
# 25

a.getuser("following")
# Returns the no of following the User
# 60

a.getuser("img")
# Returns the link to the User avatar
# https://hfsjdhfjshd.com

```