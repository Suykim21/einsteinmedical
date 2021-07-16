'''
INSTRUCTIONS:
Create a parsing tool that takes the example config file (provided below) and turns it into a usable object in the language of your choice (hash, JSON object, associative array, class, etc). The instructions for this are below.

1. Do not use existing "complete" configuration parsing libraries/functions, we want to see how you would write the code to do this.
2. Use of core and stdlib functions/objects such as string manipulation, regular expressions, etc is ok.
3. We should be able to get the values of the config parameters in code, via their name. How this is done specifically is up to you.
4. Boolean-like config values (on/off, yes/no, true/false) should return real booleans: true/false.
5. Numeric config values should return real numerics: integers, doubles, etc
6. Ignore or error out on invalid config lines, your choice.
7. Please include a short example usage of your code so we can see how you call it/etc.
8. Push your work to a public git repository (github, bitbucket, etc) and send us the link.
'''

# Open config file
config = open("config.ini", "r")

# Reads all the lines and return them as each line a string element in a list.
lines = config.readlines()

# Close the file and free up memory space acquired by the config file
config.close()

def createObject(lines):
    '''
    Converts list of config lines into usable object consisting of config keys and its values.

    Parameters:
        lines (list<string>): list of strings
    Returns:
        obj (object): Object with keys<string> and values<object>
    '''
    try:
        obj = {}

        for line in lines:
            
            # Remove any leading and trailing newlines from the string
            line = line.strip()

            # Ignore line comments
            if "#" not in line and line != '':
                
                # Flags to determine whether value is integer or float
                is_int = False
                is_float = False

                # Split by '=' and remove whitespace
                line = line.split('=')
                key = line[0].strip()
                val = line[1].strip()

                # Converting certain values to boolean, integer, or float
                if val == 'on' or val == 'yes' or val == 'true':
                    val = True
                elif val == 'off' or val == 'no' or val == 'false':
                    val = False
                else:
                    # Defining value as integer, float, or string
                    is_int = checkForNumber(val, int)

                    if is_int == False:

                        is_float = checkForNumber(val, float)

                        if is_float: 
                            val = float(val)
                    else:
                        val = int(val)

                # Construct key value pair
                obj[key] = val

        return obj
    except:
        print('Error occurred at createObject function.')

# Helper function
def checkForNumber(val, datatype):
    '''
    Determines whether given value is integer or float value.

    Parameters:
        val (string): config value
        datatype (class): int or float class
    Returns:
           (boolean): Returns whether value is valid float or integer value.
    '''
    try:
        try:
            datatype(val)
            return True
        except:
            return False
    except:
        print('Error occurred at checkForNumber function.')


# Create config object
obj = createObject(lines)

# Printing results
print(obj)
print(obj['host'])
print(obj['server_id'])
print(obj['server_load_alarm'])
print(obj['debug_mode'])
