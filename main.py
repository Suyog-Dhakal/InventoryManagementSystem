from functions import read_data, display_data, get_order_details, process_order, get_sale_details, process_sale, close_input_data

def main():
  file_path = "furniture_data.txt"
  input_data = read_data(file_path)

  while True:
    display_data(input_data)
    option_type = input("\nEnter Transaction option type (order/sale/close): ").lower()

    if option_type == "order":
      order_details = get_order_details()
      process_order(input_data, order_details)

    elif option_type == "sale":
      sale_details = get_sale_details()
      process_sale(input_data, sale_details)
    
    elif option_type == "close":
      close_input_data(file_path, input_data)
      print("Data saved and now closing...")
      print("program closed!")
      break
    else:
      print("Invalid input. Please enter 'order', 'sale', or 'close'.")


if __name__ == "__main__":
  main()
