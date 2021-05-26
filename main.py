import discord
from discord.ext import commands
from random import randint
from random import shuffle

bot = commands.Bot(command_prefix = "*")

@bot.event
async def on_ready():
  print("Prêt!")
  await bot.change_presence(status = discord.Status.online , activity= discord.Game("bot-lane.xyz"))

#Commande Pratiques

#Afficher le Site
@bot.command()
async def site(ctx):
  embedInfo = discord.Embed(title = "Notre Site", description = "Toutes nos commandes sont disponnible \n sur notre site internet", url = "http://www.bot-lane.xyz/", color = 0xF1A813)
  embedInfo.set_thumbnail(url = "https://icons.veryicon.com/png/o/business/1688-icon-library/go-to.png")
  await ctx.send(embed = embedInfo)

#Afficher les commandes
@bot.command()
async def command(ctx):
  embedInfo = discord.Embed(title = "Liste des commandes", description = "Toutes nos commandes sont disponnible \n sur notre site internet", url = "http://www.bot-lane.xyz/fonctionnalites.html", color = 0xF1A813)
  embedInfo.set_thumbnail(url = "https://img.icons8.com/metro/452/list.png")
  await ctx.send(embed = embedInfo)

#Nombre random
@bot.command()
async def random(ctx, nb_1, nb_2):
  await ctx.send("Le nombre est : " + str(randint(int(nb_1), int(nb_2))))

#Commandes des teams
@bot.command()
async def team(ctx,chaine):
  liste_joueurs= []
  equipe1 = []
  equipe2 = []
  index = 1
  for el in chaine.split(","):
    liste_joueurs.append(el)
    shuffle(liste_joueurs)
  for i in range (round(len(liste_joueurs)/2)): 
    equipe1.append(liste_joueurs[index])
    liste_joueurs.remove(liste_joueurs[index])
    index += 1
  equipe2 = liste_joueurs
  equipes = "**Equipe 1 :** " + (", ".join(equipe1)) + "\n" + "**Equipe 2 :** " + (", ".join(equipe2))
  emb = discord.Embed(title= "**Les équipes**", description = equipes, color= 0xF1A813)
  await ctx.send(embed=emb)
  await ctx.message.delete()

#Commande du sondage
@bot.command()
async def poll(ctx, question:str, reponse=""):
  question = "📊 " + question
  if reponse == "":
    emb=discord.Embed(title=" **SONDAGE** ", description = question, color = 0xF1A813)
    msg = await ctx.send(embed=emb)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
    await msg.add_reaction("🤷")
    await ctx.message.delete()
  
  else:
    liste_emo = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
    liste_rep = reponse.split(",")
    dict_rep = {}
    rep = ""
    for i in range(len(liste_rep)):
      dict_rep[liste_emo[i]] = liste_rep[i]
    for cle,values in dict_rep.items():
      rep += cle + " " + values + "\n"
    emb=discord.Embed(title= question, description = rep, color = 0xF1A813)
    msg = await ctx.send(embed=emb)
    for a in range(len(liste_rep)):
      await msg.add_reaction(liste_emo[a])
    await ctx.message.delete()


#Commandes Fun

#Jeu du pile ou face
@bot.command()
async def pileface(ctx, cote):
  random = randint(1,2)
  cote = cote.lower()
  dico = {"1" : "pile", "2" : "face"}
  rep = dico[str(random)]
  if rep == cote:
    embed = emb=discord.Embed(title="Pile ou Face ?", description = "Vous avez choisi le coté " + cote + "\n" + "Le bot a choisi le coté  " + rep + "\nVous avez gagné !", color = 0xF1A813)      
    await ctx.send(embed=emb)
  else:
    embed = emb=discord.Embed(title="Pile ou Face ?", description = "Vous avez choisi le coté " + cote + "\n" + "Le bot a choisi le coté " + rep + "\nVous avez perdu !", color = 0xF1A813)
    await ctx.send(embed=emb)


#Jeu du JustePrix
@bot.command()
async def justeprix(ctx):
  await ctx.message.delete()
  emb= discord.Embed(title = "Bienvenue dans le Jeu du JustePrix", description = "Choisis d'abord un nombre pour décider de l'intervalle dans laquelle tu vas chercher le nombre\nEnsuite tu donnera des nombres et le bot te dira si c'est plus ou moins bonne chance ?", color= 0xFF0000)
  emb.set_image(url = "https://i.skyrock.net/6393/78256393/pics/3245486596_1_3_cg8WiDDO.jpg")
  await ctx.send(embed=emb)

  def check(message):
    return message.author == ctx.message.author and ctx.message.channel == message.channel
  
  nb = await bot.wait_for("message", timeout = 40, check = check)
  nb = int(nb.content)
  random = randint(0, nb)
  print(random)
  essais = 0
  await ctx.channel.purge(limit = 2)
  await ctx.send("Ton nombre se trouve entre 0 et " + str(nb) + "\nMaintenant, essaye de trouver le nombre !")

  while nb != random:
    await ctx.send("Dit un nombre !")
    nb = await bot.wait_for("message", timeout = 60, check = check)
    nb = int(nb.content)
    if nb == random:
      essais += 1
      await ctx.channel.purge(limit = 4)
      await ctx.send("Bravo @" + str(ctx.message.author) + "\nTu as réussi à trouver le nombre en " + str(essais) + " essais")
      break
    if nb < random:
      await ctx.channel.purge(limit = 4)
      await ctx.send("C'est plus que " + str(nb) + " !")
      essais += 1
    elif nb > random:
      await ctx.channel.purge(limit = 4)
      await ctx.send("C'est moins que " + str(nb) + " !")
      essais += 1
    

#Gif aléatoire
@bot.command()
async def gif(ctx):
  await ctx.message.delete()
  liste_gif = liste_gif = ["https://tenor.com/view/lionking-throwing-offacliff-gif-5583349", 
"https://tenor.com/view/reverse-nozumi-uno-jojo-card-gif-15706915", 
"https://tenor.com/view/nadia-miyazaki-fushigi-no-umi-no-nadia-nadia-the-secret-of-blue-water-anime-gif-18119040",
"https://tenor.com/view/macron-gif-8664522",
"https://tenor.com/view/jean-lassalle-applaudir-applaudissement-applause-clap-gif-12992706",
"https://tenor.com/view/evangelion-eva-congratulations-neon-genesis-gif-4884859",
"https://tenor.com/view/oula-jamy-gourmand-cestpassorcier-oulah-gif-17071823",
"https://tenor.com/view/marie-mai-marie-mai-news-bon-beau-good-gif-17844632",
"https://tenor.com/view/one-piece-anime-manga-series-luffy-smiling-gif-17594271",
"https://tenor.com/view/dedikodu-gossip-shock-%c5%9fa%c5%9f%c4%b1rmak-shocking-gif-19902616",
"https://tenor.com/view/pedro-monkey-puppet-meme-awkward-gif-15268759",
"https://tenor.com/view/omg-shook-uncomfortable-help-me-dislike-gif-14273602",
"https://tenor.com/view/uan-konik-smiesne-funny-xddd-gif-19304296",
"https://tenor.com/view/juan-flip-gif-18577803",
"https://tenor.com/view/sao-cringe-gif-9515718",
"https://tenor.com/view/confused-white-persian-guardian-why-gif-11908780",
"https://tenor.com/view/lord-jesus-christ-sacred-heart-savior-gif-13610800",
"https://tenor.com/view/arya-actress-maisie-williams-dance-cheer-gif-5632606",
"https://tenor.com/view/winter-go-t-gameo-gif-5394725",
"https://tenor.com/view/thumbsup-game-of-thrones-khaleesi-yay-happy-gif-5501473",
"https://tenor.com/view/goat-goatlick-gif-5193394",
"https://tenor.com/view/danse-dancing-colossal-titan-snk-aot-gif-17422392",
"https://tenor.com/view/manga-com-sal-fruit-smelling-hungry-gif-17101904",
"https://tenor.com/view/manga-com-sal-fruit-smelling-hungry-gif-17101904",
"https://tenor.com/view/batman-dance-classic-batman-old-dancing-gif-4867455",
"https://tenor.com/view/rockfeller-street-gif-14820551",
"https://tenor.com/view/rockfeller-street-gif-14820551",
"https://tenor.com/view/eleven-elevensports-happy-celebration-goal-gif-19748516"]
  random = randint(0, int(len(liste_gif)))
  await ctx.send(liste_gif[random])


# Commandes de Modérations 

#Kick un membre
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
  reason = " ".join(reason)
  await ctx.message.delete()
  await member.kick(reason=reason)
  emb = discord.Embed(description = str(member) + " a été kick par @" + str(ctx.message.author) + "\n Raison : " + str(reason))
  await ctx.send(embed=emb)

#Ban un membre
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
  reason = " ".join(reason)
  await ctx.message.delete()
  await member.ban(reason=reason)
  emb = discord.Embed(description = str(member) + " a été banni par @" + str(ctx.message.author) + "\n Raison : " + str(reason))
  await ctx.send(embed=emb)

#Mute un membre
@bot.command()
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member, *, reason=None):
  reason = " ".join(reason)
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")

  for channel in guild.channels:
    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
  embed = discord.Embed(title="muted", description= str(member) + " a été mute. ")
  await ctx.send(embed=embed)
  await member.add_roles(mutedRole, reason=reason)
  await member.send("Tu as été mute par " + str(ctx.message.author) + "\nRaison : " + reason)

#Demute un membre
@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
  mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
  await member.remove_roles(mutedRole)
  await member.send("Tu as été démute par : " + str(ctx.message.author))
  embed = discord.Embed(title="unmute", description= str(member) + " a été démute.")
  await ctx.send(embed=embed)

#Clear des messages
@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, number:int):
  if number > 39:
    emb= discord.Embed(title = ":warning: Attention :warning:", description = "Tu es sur le point de supprimer un \n nombre important de messages (" + str(number) +" messages) \n Est tu sur de toi ? \n ✅ : Oui \n ❌ : Non", color= 0xFF0000)
    msg = await ctx.send(embed=emb)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")
    def chekEmoji(reaction, user):
      return ctx.message.author == user and msg.id == reaction.message.id and str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌" 
    reaction, user = await bot.wait_for("reaction_add", check= chekEmoji)
    if reaction.emoji == "✅":
      await ctx.channel.purge(limit = number + 2)
    else:
      await ctx.channel.purge(limit = 2)
  else:
    await ctx.channel.purge(limit = number + 1)
  



  


bot.run("ODE0NjE3ODI5Njk3NTE5NjU3.YDgd-Q.FKUuuBxexPQHWlqyO6GLHdxirLQ")

