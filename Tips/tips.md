This file should be viewed in GitHub, because forward slash is added here at the end of sentences as new line character.\
To make a folder in GitHub visible in the website, there must be an index.html file inside it\
If you want to open a link in the website open in the new tab, do this - `<p><a href="https://github.com/SuchitReddi/SuchitReddi.github.io" target="_blank" rel="noopener noreferrer">GitHub Repository</a></p>`.\
Add the folders you don't want to commit via GitHub desktop to .gitignore

**Mark Down and HTML**\
To add a line break in html, use `<br>`
To add a new line in markdown, use the forward slash \\
To mark something as a code, incorporate it within backticks"``".

**Issue 2**\
I faced an issue where nothing happened when I clicked on the back(.) link I added to index files of any folder.\
There are two fixes I came up for this issue.
1) Change the from `<a href=".">Back<br></a>` to `<a href="..">Back<br></a>`.
2) Don't use back link at all or provide absolute link instead of "..".
