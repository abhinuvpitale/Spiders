import argparse
from goodreadsQuotes import GoodReadsQuotes
parser=argparse.ArgumentParser(description="Good Quotes Reader Cli")

parser.add_argument("--topic",
					help="Enter the topic to search"
					)
parser.add_argument("--limit",
					help="Limit of pages"
					)

args=parser.parse_args()


if __name__=="__main__":
	topic=args.topic
	limit=args.limit
	GoodReadsQuotes(topic,int(limit))

