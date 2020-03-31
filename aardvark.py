# Assignment #4
# Program 2 – The Itsy Bitsy Aardvark
# Design and develop a program that presents the user with a “Mad Libs” type game, 
# where a random choice of words are read from a file, then interjected into a story read 
# from another file.
# Name..: Cristina Ponay
# ID....: W0424195

__AUTHOR__ = "Cristina Ponay <w0424195@nscc.ca>"

# function that will get user choices from a series of multiple choice lists
# and will create a fun new story based on choices just like Mad Libs
def myMadLibs(in_choicesFile, in_story):
    # initialization
    letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    choices = [] # will hold lists of choices
    chosen = [] # will hold chosen answers

    # read the choices file per line
    for i, line in enumerate(in_choicesFile):
        line = line.replace("\n", "")
        # split the read values by each comma
        list_choices = line.split(",")

        # the first element in each line will be displayed as prompt
        title = list_choices[0]
        print(f"\nPlease choose {title}:")
        # the rest will be used as a multiple choice list
        values = list_choices[1:]
        # append to the list of choice (2d array)
        choices.append(values)

        # display the available choices        
        for j, keys in enumerate(letters):
            print(f"{keys}) {values[j]}")

        valid = 0   # flag
        while valid == 0:
            ans = input("Enter choice (a-e): ").lower()
            # valid answers are a-e or 1-5
            if ans in ["a", "b", "c", "d", "e", "1", "2", "3", "4", "5"]:
                if not ans.isnumeric():
                    chosen.append(choices[i][letters[ans]])
                else:
                    chosen.append(choices[i][int(ans)-1])
                valid = 1
    # replace numbered placeholders with chosen words
    for i in range(len(chosen)):
        temp = "_"
        temp += str(i+1)
        temp += "_"
        in_story = in_story.replace(temp, chosen[i].upper())

    return in_story

def main():
    try:
        # open files for reading
        story_file = open("the_story_file.txt", "r")
        choices_file = open("the_choices_file.csv", "r")
    except FileNotFoundError:
        print("The file does not exist.")   # if file does not exist
    else:
        story = story_file.read()

        # begin Mad Libs game
        print("The Itsy Bitsy Aadvark")
        new_story = myMadLibs(choices_file, story)  

        # display new story
        print("\nYour Completed Story:\n")
        print(new_story)
    finally:
        story_file.close()      # close the story file
        choices_file.close()    # close the choices file

if __name__ == "__main__":
    main()