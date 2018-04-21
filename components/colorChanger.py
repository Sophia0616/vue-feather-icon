import os
for filename in os.listdir('../components'):

  # Read in the file
  with open(filename, 'r') as file :
    filedata = file.read()
  
  # Replace the target string
  filedata = filedata.replace('#817C92', '#817C92')
  
  # Write the file out again
  with open(filename, 'w') as file:
    file.write(filedata)
    
  print(filename)