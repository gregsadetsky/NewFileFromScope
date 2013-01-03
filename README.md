NewFileFromScope
================

Microscopic Sublime Text 2 plugin created as an answer to http://stackoverflow.com/questions/13702405/

================

This plugin adds a "New File From Scope" command to your Command Palette which will, upon invocation, 1) extract the scope of the current selection and 2) create a new file named after the scope's content (this will also work with multiple selections).

For instance, while editing the following line:

    <link href="app.css" rel="stylesheet">

place the cursor anywhere in the *app.css* text, open the Command Palette (Command + Shift + P under OS X) and invoke **New File From Scope**. This will get you a new, empty file pre-named app.css.

================

### How to install

I didn't want to pollute the list of packages available through the amazing Package Control. Because of this, installation of this plugin requires a bit more handling than usual:

1. Open the Command Palette and invoke the **Package Control: Add Repository** command
2. Paste "https://github.com/gregsadetsky/NewFileFromScope.git" (without the quotes) into the input panel, then press enter
3. Open the Command Palette and invoke the **Package Control: Install Package** command
4. Type **New File From Scope** -- the list of proposed plugins should filter down to this sole one
5. Select the plugin in the list, and press enter

You should now be able to invoke **New File From Scope** from the Command Palette.
