import os, json, re
class shellParser():
  def __init__(self):
    self.parserConf = open('parser.json', 'r').read()
    self.parseConf = json.loads(self.parserConf)

  def commandExecute(self, command, **params):
    try:
      Command = self.parseConf[command]["Command"]
      commandParams = re.findall(r'%[A-Za-z][A-Za-z0-9_]+%',Command)
      for commandParam in commandParams:
        Command = Command.replace(commandParam,params[commandParam.strip('%')])
      self.commandRead(Command)
      pattern = self.parseConf[command]["resultColumnPropertyPatterns"][0]["pattern"]
      groupIndex = self.parseConf[command]["resultColumnPropertyPatterns"][0]["groupIndex"]
      results = re.findall(pattern,self.commandResult)
      for index, result in enumerate(results):
        results[index] = result[groupIndex]
      return results
    except:
      print(command + " information not found in sisyShellParser Configuration")

  def commandRead(self, command):
    self.commandResult = os.popen(command).read();
    return self.commandResult