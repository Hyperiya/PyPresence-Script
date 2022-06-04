from pypresence import Presence
import psutil
import time

client_id = 'Placeholder'  
RPC = Presence(client_id,pipe=0)  
RPC.connect()  

app_pretty_name = {"r5apex.exe": "Apex Legends","TETR.IO.exe": "TETR.IO", "Roller.exe": "Roller Champions", "Warframe.x64.exe": "Warframe", "FactoryGame.exe": "Satisfactory",
"GRW.exe": "Tom Clancy's Ghost Recon Wildlands", "VRChat.exe": "VRChat", "VAIL.exe": "Vail VR", "ScrapMechanic.exe": "Scrap Mechanic", "Forts.exe": "Forts", "ModernWarfare.exe": "Call of Duty Warzone", "Crab Game.exe": "Crab Game", "VALORANT.exe": "Valorant", "RiotClientUx.exe": "Riot Client", "TslGame.exe": "PUBG", "starwarssquadrons.exe": "Star Wars Squadrons"}
app_nam = list(app_pretty_name.keys())

def ply_now(process):
    name = process.info["name"]
    exe = process.info["exe"]
    #print(name)
    if name in app_nam:
        return True
    else:
        return False 

while True:
    cpu_per = round(psutil.cpu_percent(),1) 
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)  
    iter = psutil.process_iter(["name", "exe"])    
    print(iter)
    
    playing = list(filter(ply_now, iter))
    open = "nothing"
    if len(playing)>0:
        p = playing[0]
        print(p)
        exe_name = p.info['name']
        open = app_pretty_name[exe_name]
        
    result = RPC.update( 
        large_image = "turts",
        small_image = "verify",
        small_text = "Verified",
        large_text = "Syrup",
        details = "bored...",
        state = "playing "+open,
        buttons = [{"label": "RAM: "+str(mem_per)+"%", "url": "https://warframe.market/profile/ViviPlaysX"}, {"label": "CPU "+str(cpu_per)+"%", "url": "https://steamcommunity.com/id/HyperionVCZ/home"}]
    )
    print(result)    
    time.sleep(10) 
    





