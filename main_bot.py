from re import M
import cv2
import discord
import random

client = discord.Client()
a = False
f = 0
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = message.content.startswith

    def check(message):
        return message.author == message.author and bool(message.attachments)
    async def main_spung(f):
        
        try:
            global a

            
            img =  cv2.imread('profilepicture.png')
            if a ==  False:
                imgCanny =  cv2.Canny(img, 100, 100)
            else:
                print(f)

                imgCanny =  cv2.Canny(img, f, f)
                
            cv2.imwrite("profilepicture.png", imgCanny)
            await message.channel.send(file=discord.File('profilepicture.png'))
            a = False
            cv2.waitKey(0)
        except Exception as e:
            await message.channel.send(e)

    if message.author == client.user:
        return
    
    async def Intensity(f):  #bacisally so f is the number and then it checks if f exists and then if it does it 
        global a             #makes it an int and changes custom canny to on and then adds f as an argument to canny
        if f == '':
            return 0
        else:
            a = True
            print(f)
            print('okk')
            try:
                f = int(f)               
                return(f)
            except Exception as e:
                await message.channel.send(e)
    
    async def toesize():
        toesize = random.choice('1234566789')
        await message.channel.send('Your toesize is:')
        await message.channel.send(toesize)
    
    async def help():
                await message.channel.send( '\n-----------**COMMANDS**-----------'
                                   
                                    '\n| $spung <amount> - |Spung yourself'
                                    '\n| $$spung <amount> - |Spung an image'
                                    '\n| $spung- @user <amount> - |Spung any user'
                                    '\n| $credits - |Show credits'
                                    '\n| $other -|Show other commands'
                                    )
    async def credits():
        await message.channel.send('-----------------Made by **qebyyy#9954**----------------')
        await message.channel.send('With many thanks to **SpungMan#3864** for original code!')
    
    async def spung_image():
        global f
        try:
            f = message.content.replace('$$spung', '')
            f = await Intensity(f)
        except Exception as e:
            await message.channel.send(e)
            return 0
        await message.channel.send('**Waiting for an attachment...**')
        resp = await client.wait_for('message', check=check)
        image = resp.attachments[0]
        await image.save(fp="profilepicture.png")
        await main_spung(f)
    
    async def spung_avatar():
            try:
                f = message.content.replace('$spung', '')
                f = await Intensity(f)
                await message.channel.send('**spunging!**')
                await message.author.avatar_url_as(format="png").save(fp="profilepicture.png")
                await main_spung(f)
            except Exception as e:
                await message.channel.send(e)
    
    async def spung_other_avatar():
            global f
            try:
                j = message.content.replace('$spung-', '')
                split = j.split()
                length = len(split)
                print('length is', length)
                if length == 2:
                    f = split[1]
                    f = await Intensity(f)
                    print(f)                   
                j = split[0]
                print(split)
                print(j)
                j = j.replace('@', '')
                j = j.replace('<', '')
                j = j.replace('>', '')
                j = j.replace('!', '')
                print(j)
                user = await client.fetch_user(j)
                print(user)
                await user.avatar_url_as(format="png").save(fp="profilepicture.png")
                await main_spung(f)
            except Exception as e:
                await message.channel.send(e)
    async def penis_size():
        sizes = ['0.5 inches', '500meteres square', '53 seconds long', 'three footbool fields long', '85km', '53mm', '2mm', '8inches', '6foot five', '9 hours long','89cm squared']
        size = random.choice(sizes)
        print (size)
        await message.channel.send(size)
    async def other():
        await message.channel.send('$toesize')
        await message.channel.send('$penis size')

    
    
    
    if msg('$spung-'):
        await spung_other_avatar()
    elif msg('$spung'):
        await spung_avatar()
    elif msg('$$spung'):
        await spung_image()
    if msg('$credits'):
        await credits()
    elif msg('$help'):
        await help()
    elif msg('$toesize'):
        await toesize()
    elif msg('$penis size'):
        await penis_size()
    elif msg('$other'):
        await other()


client.run('TOKEN HERE')
