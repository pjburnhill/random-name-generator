import random
import json


def generate_random_name(word_list, num_words, dividing_character):
    if num_words <= 0:
        return ""

    selected_words = random.sample(word_list, num_words)
    random_name = dividing_character.join(selected_words)
    return random_name


def main():
    # Default values
    num_words = 3
    dividing_character = "-"
    input_json_file = "words.json"

    # Parse command-line arguments if provided
    import argparse
    parser = argparse.ArgumentParser(description="Generate random names.")
    parser.add_argument("--num-words", type=int,
                        help="Number of words to use (default: 3)")
    parser.add_argument("--dividing-character", type=str,
                        help="Dividing character (default: '-')")
    parser.add_argument("--json-file", type=str,
                        help="Input JSON file containing words (default: 'words.json')")
    args = parser.parse_args()

    if args.num_words:
        num_words = args.num_words
    if args.dividing_character:
        dividing_character = args.dividing_character
    if args.json_file:
        input_json_file = args.json_file

    try:
        with open(input_json_file, "r") as json_file:
            word_list = json.load(json_file)

        if not isinstance(word_list, list):
            raise ValueError("JSON file should contain a list of words")

        random_name = generate_random_name(
            word_list, num_words, dividing_character)
        print("Generated Random Name:", random_name)

    except FileNotFoundError:
        print(f"JSON file '{input_json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in '{input_json_file}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
