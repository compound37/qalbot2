import discord
import argparse
import logging
import random
import simple_tf

logger = logging.getLogger('discord')
client = discord.Client()

def weighted_select(weighted_list):
	totalItems = 0
	totalList = []
	for i in range(0, len(weighted_list)):
		totalItems += weighted_list[i][0]
		for j in range(0, weighted_list[i][0]): totalList.append(weighted_list[i][1])

	return random.choice(totalList)

def tf_parser(parse_msg):
	parse_words = parse_msg.split()
	if parse_words[0] == "simple":
		choice = weighted_select(simple_tf.simple_start)
		if choice == 'grow_limb': return weighted_select(simple_tf.grow_limb)
		elif choice == 'grow_genetalia': return weighted_select(simple_tf.grow_genetalia)
		elif choice == 'grow_tail': return weighted_select(simple_tf.grow_tail)
		elif choice == 'grow_mutation': return weighted_select(simple_tf.grow_mutation)


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("!qb hello"):
		msg = 'hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	elif message.content.startswith("!qb roll-tf"):
		result_tf = tf_parser('simple')
		msg = '{0.author.mention}'.format(message) + result_tf
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
