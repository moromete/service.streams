import xbmc, time, json
 
if __name__ == '__main__':
    monitor = xbmc.Monitor()
 
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
        xbmc.log("hello addon! %s" % time.time(), level=xbmc.LOGDEBUG)
        
        cmd = '{"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}'
        result = xbmc.executeJSONRPC(cmd)
        xbmc.log(result)
        result = json.loads(result)
        if(len(result['result'])):
          playerId = result['result'][0]['playerid'];
          xbmc.log(str(playerId))
          
          
          if(result['result'][0]['type']=='audio'):
            cmd = '{"jsonrpc": "2.0", "method": "Player.GetItem", \
                    "params": { "properties": ["title", "file", "artist"], "playerid": '+str(playerId)+' }, \
                    "id": "AudioGetItem"}'
          else:
            if(result['result'][0]['type']=='video'):
              cmd = '{"jsonrpc": "2.0", "method": "Player.GetItem", \
                      "params": { "properties": ["title", "file", "artist"], "playerid": '+str(playerId)+' }, \
                      "id": "VideoGetItem"}'
            
          result = xbmc.executeJSONRPC(cmd)
          xbmc.log(result)
          result = json.loads(result)
          
          
          
          
          
        
        #xbmc.log(result['result'])
        #xbmc.log(result['result'][0]['playerid'])
