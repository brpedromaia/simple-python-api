import os
from . import devConfig 


def init():
  appEnv = os.getenv('APP_ENV')
  if appEnv == "dev":
    devConfig.init()
  
def getEngine():
  appEnv = os.getenv('APP_ENV')

  if appEnv == "dev":
    return devConfig.getEngine()
  return null
