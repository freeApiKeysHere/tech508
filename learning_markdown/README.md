# Markdown basics - "h1" tag
<h1> also a "h1" tag </h1>

## how to do headings - "h2" tag
<h2> also a "h1" tag </h2>

_italic_ \
*also italic*\

__bold__\
**also bold**

## lists

* Item 1
* Item 2
  * SubItem1
    * SubSubItem1
    * SubSubItem2
  * SubItem2
* Item 3

Note: Hyphens can be used instead of stars

## Numbered Lists

1. First Item
    * Bullet Point 1
    * Bullet Point 2
2. Second Item
3. Third Item

## Images

![woat](../images/Yelena%20face.png)

## Links

Website Link:
[Click Me!](https://youtu.be/dQw4w9WgXcQ?si=6Ha9QcCJA09N7EY2)

File/folder Link: 
[asdf.py](../asdf.py)

## Code

inline code example: 
To print a code block use  \`\`\` YOUR CODE HERE \`\`\` for inline text

```
function test() {
  console.log("notice the blank line before this function?");
}
```

with python formatting:
```python 
print("hello world!")
```

# 3 states of git


* Modified means that you have changed the file but have not committed it to your database yet.
* Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
* Committed means that the data is safely stored in your local database.

# git commands

we use . at the end to include all files in a folder
* git init - turn folder into git repo 
* git status - get the status of the repo
* git add - add changes to staging area
* git commit - record the changes to the repo 
