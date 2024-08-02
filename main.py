# These are the functions imported from 'functions.py' file
from functions import read_data, display_data, get_order_details, process_order, get_sale_details, process_sale, close_input_data


# This is the main function
def main():
  file_path = "furniture_data.txt"    # this is the path of the file
  input_data = read_data(file_path)   # 'read_data' function is called to read the data of the 'furniture_data.txt' file

  while True:
    display_data(input_data)        # 'display_data' function is called to show the data of 'furniture_data.txt' file
    option_type = input("\nEnter Transaction option type (order/sale/close): ").lower() # it asks for the transaction option type

    if option_type == "order":              # if option is 'order'
      order_details = get_order_details()   # it calls 'get_order_details' function
      process_order(input_data, order_details)  # it calls 'process_order' function where input data and order details are passed 

    elif option_type == "sale":             # if option is 'sale'
      sale_details = get_sale_details()     # it calls 'get_sale_details' function
      process_sale(input_data, sale_details)  # it calls 'process_sale' function where input data and sale details are passed 
    
    elif option_type == "close":            # if option is 'close'
      close_input_data(file_path, input_data) # it calls 'close_input_data' function where it saves updated data on 'furniture_data.txt' file and program is closed
      print("Data saved and now closing...")
      print("program closed!")
      break       # this command helps to terminate the program as it exits from the while loop
    else:
      print("Error: Invalid input. Please enter 'order', 'sale', or 'close'.")


if __name__ == "__main__":
  main()
