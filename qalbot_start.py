import discord
import argparse
import logging

logger = logging.getLogger('discord')
client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("!qb hello"):
		msg = 'hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

def main():
	parser = argparse.ArgumentParser(description="Qalbot, the friendly TF robot")
	parser.add_argument("token", help="Discord Token", type=str)
	parser.add_argument('-l', '--logfile', help="Log file for logger", default='qalbot.log')

	args = parser.parse_args()

	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(filename=args.logfile, encoding='utf-8', mode='w')
	handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)

	client.run(args.token)


if __name__ == "__main__":
	main()