import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

def print_intro():
    """ () -> ()

    Function to print what program does and what type of information parses.
    """
    print("\nThe program uses Twitter Standart Search API and\n"
          "returns the collection of relevant tweets matching a specified category.\n")



def get_relevant_tweets_data(search_query, number_of_tweets):
    """ (str) -> (dict)

    Function returns python dict with relevant tweets
    based user {search query} and {number_of_tweets},
    """

    TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    if len(search_query) < 1:
        print("Wrong input!")
    url = twurl.augment(TWITTER_URL,
                        {'q': search_query, 'count': number_of_tweets})

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    tweet_js = json.loads(data)


    return tweet_js


def get_possible_keys(twitter_dict):
    """ (dict) -> (str)

    Function to show all the dictionary keys user can get value of.
    """
    keys = [key for key in twitter_dict['statuses'][0].keys()]

    return "  |  ".join(keys)

def get_value_by_key(twitter_dict, key):
    """ (dict), (str) -> (str)

    Function to return a value by a dict returned by twitter.
    """
    for count, tweet in enumerate(twitter_dict['statuses'], 1):
        print("Tweet {}".format(str(count)))
        if key not in tweet :
            print('No {} found'.format(key))
            continue
        s = tweet[key]
        print('  ', s, end='\n\n')

if __name__ == "__main__":

    print_intro()

    while True:
        search_input = input("What are you going to search for?  ->  ")
        number_of_tweets = input("How many tweets do you want me to show ?  ->  ")
        if len(search_input) < 1 or len(number_of_tweets) < 1:
            print("Wrong input!")
            break

        twitter_data_dict = get_relevant_tweets_data(search_input, number_of_tweets)
        possible_dict_keys = get_possible_keys(twitter_data_dict)

        print("\nThese are the keys you can the value of:\n\n{}"
              "\n\nP.S  Use  'text'  key to get the actual tweet\n\n".format(possible_dict_keys))

        inp_key = input("Enter the key  ->  ")
        get_value_by_key(twitter_data_dict, inp_key)
