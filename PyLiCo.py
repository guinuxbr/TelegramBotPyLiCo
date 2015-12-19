import telegram
import subprocess

bot = telegram.Bot(token='TOKEN')
print(bot.getMe())

try:
 LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
 LAST_UPDATE_ID = None

#LAST_UPDATE_ID = bot.getUpdates()[-1].update_id

while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id
            
            if text == '/start':
                #command_result = subprocess.getoutput("pwd")#.decode("utf-8")
                bot.sendMessage(chat_id, text="Ok, let's do something!")
            
            elif text == '/whereami':
                command_result = subprocess.getoutput("pwd")#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)
                
            elif text == '/whoami':
                command_result = subprocess.getoutput("whoami")#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result+" is the user logged in the box")
              
            elif text.startswith("/list"):
                args = (text.split()[1])
                command_result = subprocess.getoutput(["ls -sh %s" % args])#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)
            
            elif text.startswith("/removefile"):
                args = (text.split()[1])
                command_result = subprocess.getoutput(["rm -v %s" % args])#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)
                
            elif text.startswith("/removedir"):
                args = (text.split()[1])
                command_result = subprocess.getoutput(["rm -vr %s" % args])#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)
                
            elif text.startswith("/createdir"):
                args = (text.split()[1])
                command_result = subprocess.getoutput(["mkdir -v %s" % args])#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)
                
            elif text == "/screenoff":
                command_result = subprocess.getoutput("xset -display :0.0 dpms force off")#.decode("utf-8")
                bot.sendMessage(chat_id, text="A tela do dispositivo foi desligada.")
    
            elif text == "/screenon":
                command_result = subprocess.getoutput("xset -display :0.0 dpms force on")#.decode("utf-8")
                bot.sendMessage(chat_id, text="A tela do dispositivo foi ligada.")
                
            elif text == '/ifaces':
                command_result = subprocess.getoutput("ifconfig")#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)
                
            elif text == '/mountpoints':
                command_result = subprocess.getoutput("mount")#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)                
                
            elif text == '/screenshot':
                command_result = subprocess.getoutput("import -window root screenshot.jpg")#.decode("utf-8")
                screenshot = open('screenshot.jpg', 'rb')
                bot.sendPhoto(chat_id, photo=screenshot)
                screenshot.close()
                #bot.sendMessage(chat_id, text=command_result)
                        
            elif text.startswith('/installed'):
                args = (text.split()[1])
                command_result = subprocess.getoutput(["which %s" % args])#.decode("utf-8")
                bot.sendMessage(chat_id, text="Yes, "+args+" is installed in "+command_result)
                
            elif text.startswith("/download"):
                link = (text.split()[1])
                command_result = subprocess.Popen(["wget", "-q", link])
                bot.sendMessage(chat_id, text="Man, your download has begun!")
            
            elif text.startswith('/mountpoints'):
                args = (text.split()[1])
                command_result = subprocess.getoutput("mount")#.decode("utf-8")
                bot.sendMessage(chat_id, text=command_result)            
            
            elif text == '/help':
                #command_result = subprocess.getoutput("mount")#.decode("utf-8")
                bot.sendMessage(chat_id, text="""/start - Start the bot.:-)\n
                                /whereami - Print the current directory.\n
                                /list - List directories and files with human readable sizes. Should receive a path as an argument, for example: /list /home/user. Avoid directories like "/bin" and "/usr/bin"\n
                                /screenoff - Turn the host screen off.\n
                                /screenon - Turn the host screen on.\n
                                /ifaces - Print the interfaces information.\n
                                /mountpoints - Print the current mount points of partitions and filesystems.\n
                                /screenshot - Take a screenshot of the host actual screen.\n
                                /download - Download a file. Should receive an URL as an argument, for example: /download http://www.foo.com/bar.iso\n
                                /stop - Stop the bot.""")
                            
            elif text == '/stop':
                #command_result = subprocess.getoutput("mount")#.decode("utf-8")
                bot.sendMessage(chat_id, text="Ok, understood, I am out!")
                
            else:
                bot.sendMessage(chat_id, text="Unsupported command, try /help to show you some options!")
                
            
            LAST_UPDATE_ID = update_id + 1
