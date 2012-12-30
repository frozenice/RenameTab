import sublime, sublime_plugin

class RenameTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().show_input_panel("Tab Name:", self.view.name(), self.on_done, None, None)
    
  def on_done(self, input):
    self.view.set_name(input)