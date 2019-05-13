

import os

input_dir  = './2014_2019/'

files      = os.listdir(input_dir)

files      = list(filter(lambda x: x[-4:] == '.txt', files))

output_dir = './2014_2019_txt/'

sep        = '   '

if_print   = False




for file in files[:]:

    #file        = 'fomcminutes20140618_page_21.txt'
   
    print('parse ' + file)

    output_file = './2014_2019_txt/' + file.split('/')[-1]
    
    try:
        f  = open(input_dir + file)
        
        lines = []
        
        for line in f:
        
            lines.append(line)
        
           # print(line)
                    
    except UnicodeDecodeError:
        
        #f.close()
        
        f  = open(input_dir + file, encoding = "utf8")

        lines = []
    
        for line in f:
        
            lines.append(line)
        
            #print(line)
    finally:
    
        f.close()
        
    
    left, right  = [], []
    
    deleted = []

    if file[-10:] ==  'page_1.txt':
    
     # delete the first line of page 1   
     
        line_length = len(lines[0])
        
        deleted.append(lines[0])
                        
        del lines[0]
        
        

        left.append(lines[0])
        
        left.append(lines[1])
        
        deleted.append(lines[0])
        del lines[0]
        deleted.append(lines[0])
        del lines[0]
        
    else:
        # for pages from no.2 to the last,  delete the first and second lines
        
        
        
        deleted.append(lines[0])
        del lines[0]
        deleted.append(lines[0])
        del lines[0]
        
        line_length = max(len(deleted[1]), len(lines[0]))
    
        #if set(lines[0]) <= {'_', '\n'}:
        
       #     del lines[0]
        
    
    
    
        
     
    
    
    

    
    for line in lines:
        
        left_part  = line[0: int(line_length/2) - 1]
        
        #print(left_part)

        right_part = line[int(line_length/2) - 1:]
        
            
            
        
        left_part  = left_part.rstrip(' ')    # try to  remove the beginning spaces
        
        if set(left_part) <= {'', '\n'} :
            
            left_part  = ' ' *  (int(line_length/2) - 1)  + '\n'    # keep an empty line
            

            
        if left_part[-1] !=  '\n':
        
            left_part  = left_part + '\n'     # and an end-of-line char in order to change lines
        
        
        left.append(left_part)
        
        right.append(right_part)
        
        
    new_page = left + right
    
    if if_print:
    
        for line in new_page:
        
            print(line)
        
    
    with open(output_file, 'w') as of:
        
        #of.writelines(new_page)
        
        try: 
           for line in new_page:
            
               of.write(line)
               
        except UnicodeEncodeError as e:
            
            #import pdb; pdb.set_trace()
            #print(dir(e))
            input_line = e.args[1]  # the line to write
            
            for pos in range(e.start, e.end):
                line       = input_line.replace(input_line[pos], ' ')
            of.write(line)