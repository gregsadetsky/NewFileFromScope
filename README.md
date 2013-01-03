NewFileFromScope
================

Microscopic Sublime Text 2 plugin created as an answer for http://stackoverflow.com/questions/13702405/

================

This plugin adds a "New File From Scope" to your Command Palette which will, upon invocation, 1) extract the scope of the current selection and 2) create a new file named after the scope's content (this will also work with multiple selections).

For instance, while editing the following line:

    <link href="app.css" rel="stylesheet">

place the cursor anywhere in the **"app.css"** text, open the Command Palette (Command + Shift + P under OS X), invoke "New File From Scope", and you'll get a new empty file pre-named app.css.
