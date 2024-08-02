import datetime

# This is a function to read the furniture data from a text file
def read_data(file_path):
  input_data = {}     # here dictionary data structure is used 
  with open(file_path,'r') as file:   # file is open in 'read' mode
    for line in file:
      parts = line.strip().split(', ')
      furniture_id = int(parts[0])
      manufacturer = parts[1]
      product_name = parts[2]
      quantity = int(parts[3])
      price = float(parts[4][1:])

      input_data[furniture_id] = {
        'manufacturer': manufacturer,
        'product_name': product_name,
        'quantity': quantity,
        'price': price

      }
  return input_data


# This function is used to display all the available furniture from the text file
def display_data(input_data):
  pass


# This function is used to get order details from the user
def get_order_details():
  pass


#This function is used to process orders and update the furniture data in the text file
def process_order(input_data, order_details):
  pass


# This function is used to get sale details from the user
def get_sale_details():
  pass

#This function is used to process sales and update the furniture data in the text file
def process_sale(input_data, sale_details):
  pass

# This function is used to save the updated furniture data to a text file and close the program
def close_input_data(file_path, input_data):
  pass




