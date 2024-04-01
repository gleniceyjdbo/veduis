if fields == 'timestamp':
    # Perform the necessary action if 'fields' is 'timestamp'
    # For example, convert the timestamp to a different format or print it
    handle_timestamp(fields)
else:
    # Handle the case where 'fields' is not 'timestamp'
    handle_other_fields(fields)

def handle_timestamp(field_value):
    # Assuming the timestamp is in UNIX format and needs to be converted to a human-readable format
    formatted_time = datetime.fromtimestamp(int(field_value)).strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_time)

def handle_other_fields(field_value):
    # Placeholder for handling other field values
    print(f"Field is not a timestamp: {field_value}")
