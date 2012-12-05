import sublime, sublime_plugin, re

class ComplineCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		def uniq(seq): 
			checked = []
			for e in seq:
				if e.strip() not in checked:
					checked.append(e)
			return checked

		
		def target():
			line = self.view.line(self.view.sel()[0].begin())
			return self.view.substr(line)

		def foo(index):
			if(index > -1):
				for i in range(len(self.view.sel())):
					line = self.view.line(self.view.sel()[i].begin())
					src = self.view.substr(line)
					match = re.search(r"$", src)
					if(match):
						end = match.end()
						match = re.search(r"\S", src)
						if(match):
							start = match.start()
						else:
							start = self.view.sel()[i].begin()
							end = line.end()
						length = end - start
						begin = self.view.sel()[i].begin()-length
						self.view.replace(edit, sublime.Region(begin, self.view.sel()[i].end()), matches[index])
		region = sublime.Region(0, self.view.size())
		lines = self.view.lines(region)
		target = target().strip()
		matches = uniq([self.view.substr(line).lstrip() for line in lines if self.view.substr(line).lstrip().startswith(target)])
		sublime.active_window().show_quick_panel(matches, foo)
