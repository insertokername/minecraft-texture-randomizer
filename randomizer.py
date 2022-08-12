import os
import random
import shutil
Older=["1"]
ResourcePath=r"C:\Users\{username}\AppData\Roaming\.minecraft\resourcepacks".format(username=os.getlogin())
ScriptLocation=os.getcwd().removesuffix("cringe test.py")+"\\RANDOMIZED_TEXTURE"
input("***IF THIS IS NOT THE FIRST SHUFFLE PLEASE MAKE SURE TO UNLOAD THE TEXTURE PACK BEFORE CONTINUING*** \n\nPress enter to begin")
if os.path.exists(ResourcePath+ "\\"+ "RANDOMIZED_TEXTURE")==False:
    print("Copying files this may take 1s~1min...\n")
    shutil.copytree(ScriptLocation, ResourcePath +'\\RANDOMIZED_TEXTURE' )
    print('Done')    
else:
    print('cleaning up last shuffle...')
    shutil.rmtree(ResourcePath +'\\RANDOMIZED_TEXTURE')
    print('Deleted...\nWaiting for copy...')
    shutil.copytree(ScriptLocation, ResourcePath +'\\RANDOMIZED_TEXTURE' )
    print('Copied.')    
DPath=r"C:\Users\{username}\AppData\Roaming\.minecraft\resourcepacks\RANDOMIZED_TEXTURE\assets\minecraft\textures".format(username=os.getlogin())
AvailableCategories=['block', 'entity', 'font', 'gui', 'item', 'mob_effect', 'models', 'painting', 'particle']
MODIFIEDpath=input("\n\nType in a number from 1~4 to choose your option:\n\n1-default shuffle----randomizes: blocks and items\n2-advanced shuffle----randomizes: blocks, items, particles, effect icons and particles\n3-cursed shuffle----randomises: blocks entity textures, fonts, the gui, items, effect icons, models, paintings and particles\n4-custom shuffle---u pick what to shuffle\n\n")
if MODIFIEDpath=="1":
    MODIFIEDpath="block,item".split(",")
elif MODIFIEDpath=="2":
    MODIFIEDpath="block,item,particle,mob_effect,particle".split(",")
elif MODIFIEDpath=="3":
    MODIFIEDpath="block,entity,font,gui,item,mob_effect,models,painting,particle".split(",")
elif MODIFIEDpath=="4":
    MODIFIEDpath=input('\n***TYPE CATEGORIES OUT AS THEY ARE SEEN IN THE LIST***\n(example:"block,gui,mob_effect")\n\navailable categories:\nblock\nentity\nfont\ngui\nitem\nmob_effect\nmodels\npainting\nparticle:\n\n').split(",")
else:
    input("\nInvallid number\n\nPress enter to close")
for i in range(0, len(MODIFIEDpath)):
    if MODIFIEDpath[i] not in AvailableCategories:
        input('\nInvalid category\n\n Press enter to close')
if MODIFIEDpath==['']:
    input("  Process cancelled... \n  (press enter to exit)")
    exit()
#print("Original search list is: ", MODIFIEDpath)
def Findit():#this def appends the list so that it includes subfolders
    for i in range(0,len(MODIFIEDpath)):
        folder_info=os.listdir(DPath +  "\\" + MODIFIEDpath[i])
        Folder_list=[]
        for l in range (0, len(folder_info)):
            if ".png" not in folder_info[l]:
                Folder_list.append(folder_info[l])
        if len(Folder_list)==0:
            if (MODIFIEDpath[i]) not in MODIFIEDpath:    
                MODIFIEDpath.append(MODIFIEDpath[i])
        else:
            for f in range(0, len(Folder_list)):
                if (MODIFIEDpath[i] + "\\" + Folder_list[f]) not in MODIFIEDpath:
                    MODIFIEDpath.append(MODIFIEDpath[i] + "\\" + Folder_list[f])
while True:#uses the def until the final list is complete 
    Findit() 
    if Older==MODIFIEDpath:
        break
    Older=MODIFIEDpath
#print("\n PATH LIST IS: ", MODIFIEDpath, "\n")
print('shuffle in progress...\n')
for a in range(0, len(MODIFIEDpath)):
    ShuffledList=[]
    CurItemList=os.listdir(DPath + "\\" + MODIFIEDpath[a])
    for b in range(0, len(CurItemList)):
        if ".png" in CurItemList[b] and ".mcmeta" not in CurItemList[b]:
            ShuffledList.append(CurItemList[b])
    random.shuffle(ShuffledList)
    saveditem=""
    for c in range(0, len(ShuffledList)):
        if c==0:
            os.rename(DPath + '\\' +  MODIFIEDpath[a] + '\\' + ShuffledList[c], DPath + '\\' +  MODIFIEDpath[a] + '\\' + "X.png")
            saveditem=ShuffledList[c]
        elif c==len(ShuffledList)-1:
            os.rename(DPath + '\\' +  MODIFIEDpath[a] + '\\' + ShuffledList[c], DPath + '\\' +  MODIFIEDpath[a] + '\\' + ShuffledList[c-1])
            os.rename(DPath + '\\' +  MODIFIEDpath[a] + '\\' + "X.png", DPath + '\\' +  MODIFIEDpath[a] + '\\' + ShuffledList[c])
        else:
            os.rename(DPath + '\\' +  MODIFIEDpath[a] + '\\' + ShuffledList[c], DPath + '\\' +  MODIFIEDpath[a] + '\\' + ShuffledList[c-1])
input('Done (press enter to exit)')