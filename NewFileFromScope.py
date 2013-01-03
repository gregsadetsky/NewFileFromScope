# created as an answer to http://stackoverflow.com/questions/13702405/

import re, os
from urlparse import urlparse
from posixpath import basename

import sublime, sublime_plugin

class NewFileFromScopeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        original_view = self.view
        original_window = self.view.window()

        for sel in self.view.sel():
            # in case we're dealing with multiple selections, go back to first view to extract scope
            original_window.focus_view(original_view)

            # get selection text
            sel_scope = self.view.extract_scope(sel.a)
            scope_str = self.view.substr(sel_scope)

            # scope will most probably include surrounding single and double quotes, get rid of them.
            scope_str = re.sub('[\'\"]', '', scope_str)

            # thanks to http://stackoverflow.com/questions/449775/
            parsed_path = urlparse(scope_str).path
            file_basename = basename(parsed_path)

            # bail
            if file_basename == "":
                return

            new_view = self.view.window().new_file()
            new_view.set_name(file_basename)
