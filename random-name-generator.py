
import random
import requests
import json
import argparse


def download_wordlist(url_or_path):
    try:
        if url_or_path.startswith('http://') or url_or_path.startswith('https://'):
            response = requests.get(url_or_path)
            response.raise_for_status()
            word_list = [line.split("\t")[1].strip()
                         for line in response.text.split("\n") if line]
        else:
            with open(url_or_path, 'r') as file:
                word_list = json.load(file)
                if not isinstance(word_list, list):
                    raise ValueError(
                        "JSON file should contain a list of words")
        return word_list
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to download wordlist: {str(e)}")
    except FileNotFoundError:
        raise Exception(f"File not found: {url_or_path}")
    except json.JSONDecodeError:
        raise Exception(f"Invalid JSON file: {url_or_path}")


def generate_random_name(word_list, num_words, dividing_character):
    if num_words <= 0:
        return ""
    selected_words = random.sample(word_list, num_words)
    random_name = dividing_character.join(selected_words)
    return random_name


def main():
    num_words = 3
    dividing_character = "-"
    input_wordlist = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"

    parser = argparse.ArgumentParser(description="Generate random names.")
    parser.add_argument("--num-words", type=int,
                        help="Number of words to use (default: 3)")
    parser.add_argument("--dividing-character", type=str,
                        help="Dividing character (default: '-')")
    parser.add_argument("--wordlist", type=str,
                        help="Path or URL of the wordlist (default: EFF wordlist)")
    args = parser.parse_args()

    if args.num_words:
        num_words = args.num_words
    if args.dividing_character:
        dividing_character = args.dividing_character
    if args.wordlist:
        input_wordlist = args.wordlist

    try:
        word_list = download_wordlist(input_wordlist)
        if not word_list:
            raise ValueError("Wordlist is empty or unavailable")
        random_name = generate_random_name(
            word_list, num_words, dividing_character)
        print("Generated Random Name:", random_name)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
