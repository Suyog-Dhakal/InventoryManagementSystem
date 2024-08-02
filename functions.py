import datetime  # this module is used to format the date and time 


# This function is used to read the furniture data from a text file
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
  print("\nAvailable Furniture:")
  print(f"{'ID':<5} {'Manufacturer':<50} {'Product Name':<30} {'Quantity':<20} {'Price per unit':<20}")
  print("-" * 130)
  for fid, details in input_data.items(): # displaying data in form of table
    print(f"{fid:<5} {details['manufacturer']:<50} {details['product_name']:<30} {details['quantity']:<20} ${details['price']:<20}")




# This function is used to get order details from the user
def get_order_details():
  furniture_id = int(input("Enter furniture ID: "))
  quantity = int(input("Enter quantity: "))
  employee = input("Enter employee name: ")
  return {'furniture_id': furniture_id, 'quantity': quantity, 'employee': employee} # returns all the above entered data




#This function is used to process orders and update the furniture data in the text file
def process_order(input_data, order_details):
  fid = order_details['furniture_id']
  if fid in input_data:
    input_data[fid]['quantity'] += order_details['quantity']  # the ordered quantity is added in the total quantity
    generate_invoice(order_details, input_data[fid], 'order') # calls generate_invoice() function to generate invoice in separate file
  else:
    print("Error: Furniture ID not found.")    # if id is not matched, then this statement is printed




# This function is used to get sale details from the user
def get_sale_details():
  furniture_id = int(input("Enter furniture ID: "))
  quantity = int(input("Enter quantity: "))
  customer = input("Enter customer name: ")
  return {'furniture_id': furniture_id, 'quantity': quantity, 'customer': customer} # returns all the above entered data



#This function is used to process sales and update the furniture data in the text file
def process_sale(input_data, sale_details):
  fid = sale_details['furniture_id']
  if fid in input_data:
    if input_data[fid]['quantity'] >= sale_details['quantity']:  # checks if the available quantity is greater than or equals to sales quantity
      input_data[fid]['quantity'] -= sale_details['quantity']   # subtracts sales quantity from the available quantity
      generate_invoice(sale_details, input_data[fid], 'sale')   # calls generate_invoice() function to generate invoice in separate file
    else:
      print("Error: Not enough stock available.")   # if available quantity is less than sales quantity then this statement is printed
  else:
    print("Error: Furniture ID not found.")   # if id is not matched, then this statement is printed



# This function is used to save the updated furniture data to a text file and close the program
def close_input_data(file_path, input_data):
  with open(file_path, 'w') as file:      # opens file in 'write' mode
    for fid, details in input_data.items():   # writes the updated details on the file 
      file.write(f"{fid}, {details['manufacturer']}, {details['product_name']}, {details['quantity']}, ${details['price']}\n")



# This function is used to generate invoices(bill) for transactions
def generate_invoice(details, furniture, option_type):
    now = datetime.datetime.now()  # returns current date and time

    if option_type == 'order':      # when 'order' is selected
        total_amount = details['quantity'] * furniture['price']    # totalprice = number of quantity * price of furniture

        invoice = (f"***Order Invoice***\n"                 # this is the format of order bill
                   f"Employee: {details['employee']}\n"
                   f"Furniture ID: {details['furniture_id']}\n"
                   f"Product: {furniture['product_name']}\n"
                   f"Quantity: {details['quantity']}\n"
                   f"Total Amount: ${total_amount:.2f}\n"
                   f"Date and Time: {now}\n")
        
    else:                                                       # when 'sale' is selected
        total_amount = details['quantity'] * furniture['price']  # totalprice = number of quantity * price of furniture
        vat = total_amount * 0.13                               # n13% vat of total amount is calculated
        shipping_cost = 30                                      # $30 shipping cost is assumed
        total_amount_with_vat = total_amount + vat              # total amount including vat
        final_amount = total_amount_with_vat + shipping_cost    # final amount including vat and shipping cost

        invoice = (f"***Sale Invoice***\n"                      # This is the format of sales bill
                   f"Customer: {details['customer']}\n"
                   f"Furniture ID: {details['furniture_id']}\n"
                   f"Product: {furniture['product_name']}\n"
                   f"Quantity: {details['quantity']}\n"
                   f"Total Amount: ${total_amount:.2f}\n"
                   f"VAT (13%): ${vat:.2f}\n"
                   f"Shipping Cost: ${shipping_cost:.2f}\n"
                   f"Final Amount: ${final_amount:.2f}\n"
                   f"Date and Time: {now}\n")
    invoice_file = f"{option_type}_{now.strftime('%Y%m%d_%H%M%S')}.txt"   # invoice(bill) file name will include transaction option type with currentdate_currenttime
    with open(invoice_file, 'w') as file:       # invoice(bill) file will be created in 'write' mode
        file.write(invoice)                      # the data from above will be written in the bill
    print(f"Invoice generated in new file: {invoice_file}")   # after invoice(bill) file is created, this message is displayed


