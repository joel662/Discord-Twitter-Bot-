import discord
from discord.ext import commands, tasks
import tweepy

# Discord Bot Token
TOKEN = 'DISCORD_TOKEN'

# Twitter API Keys
TWITTER_API_KEY = 'TWITTER_API_KEY'
TWITTER_API_SECRET = 'TWITTER_API_SECRET'
TWITTER_ACCESS_TOKEN = 'TWITTER_ACCESS_TOKEN'
TWITTER_ACCESS_TOKEN_SECRET = 'TWITTER_ACCESS_TOKEN_SECRET'
TWITTER_BEARER_TOKEN = 'TWITTER_BEARER_TOKEN'


c = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN,consumer_key=TWITTER_API_KEY,
                  consumer_secret= TWITTER_API_SECRET,
                  access_token =TWITTER_ACCESS_TOKEN,
                  access_token_secret = TWITTER_ACCESS_TOKEN_SECRET)

# Define the intents you need (in this case, we need the default intents plus message content)
intents = discord.Intents.default()
intents.message_content = True


# Create an instance of the bot with the specified intents
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    send_message.start()

@tasks.loop(seconds=10)  # Send a message every 1 hour (adjust as needed)
async def send_message():
    # Replace 'YOUR_CHANNEL_ID' with the ID of the channel where you want to send the message
    channel = bot.get_channel(ChannelID)
    
    if channel:
        await channel.send(c.get_users_tweets(id=TwittterID).text)
@bot.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == bot.user:
        return

    # Check if the bot is mentioned in the message
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello!')


@bot.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == bot.user:
        return

    # Check if the message starts with the !tweet command
    if message.content.startswith('/tweet'):
        # Extract the tweet content from the message (remove the command prefix)
        tweet_content = message.content[7:]

        # Post the tweet using the Twitter API (you need to implement this part)
        # Example using Tweepy:
        try:
            c.create_tweet(text = tweet_content)
            await message.channel.send('Tweeted successfully!')
        except tweepy.TweepError as e:
            await message.channel.send(f'Error: {e}')

    
# Start the bot
bot.run(TOKEN)
