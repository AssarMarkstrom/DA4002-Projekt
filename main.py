import file_handler
projectdata = {
  "1.": "25_years_of_salgskimmer",
  "2.": "helarsprestationer_from_2017"
}
def input_control(user_input):
    """ Check if user input is an integer
    :param user_input: value for key in data_dict
    :type user_input: UNKNOWN
    :return: Input value for data_dict or recursive call
    :rtype: int or functioncall
    """
    try:
        value_input = int(user_input)
        if value_input == 1 or value_input == 2:
            return value_input
        else: 
            print("Something went wrong! Try to choose a file again")
            user_input = input("FILE: ")
            return input_control(user_input)
    except:
        print("Something went wrong! Try to choose a file again")
        user_input = input("FILE: ")
        return input_control(user_input)

def main():
    print("Choose a file!")
    user_input = input(":")
    print(input_control(user_input))

if __name__ == '__main__':
    main()