import re
import sys

### RUN_SCRIPT ###

# python generate_runs_of_Homozygosity.py <file_list.txt>
# here files_list.txt contains list of all individuals to be processed

file_list = open(sys.argv[1],"r")

chr_dic = {}
pos_dic = {}

out_file_list=[]

for filename in file_list:

    col1        = re.split("\.",filename)
    individual  = col1[0]
    #print individual  

    col2 =  re.split("\n",filename)
    #print col2[0]
    curr_file = open(col2[0],"r")

    chr_dic[individual]=[]
    pos_dic[individual]=[]

    fout_fname = individual + ".out"
    fout_regions = open(fout_fname,"w")
    prev_pos=-1
    prev_chr="NOT_APPLICABLE" 
    first_chrm=True

    str_print = "CHRM" + "\t" + "START" + "\t" + "END" + "\t" + "LEN" + "\t" + "STATE" 
    fout_regions.write(str_print)
    fout_regions.write("\n")                  

    for line in curr_file:
    
        if line[0]=="#":
            continue

        col = re.split("\t|\n",line)
        state = col[2]

        chrm = col[0]
        pos  = int(col[1])


        if chrm!=prev_chr:

            if first_chrm==True:   ## No need to process the previous chromosmes only start a new one

                if state=="0":    
                    flag=0
                    start_tr_pos = pos 
                    start_tr_chr = chrm

                else:  #state is 1
                    flag=1
                    start_tr_pos = pos 
                    start_tr_chr = chrm

                first_chrm==False

            else:                 ## Process previous chromsome out and start a new one

                end_tr_chr = prev_chr
                end_tr_pos = prev_pos

                if start_tr_chr == end_tr_chr:

                    temp_len = end_tr_pos - start_tr_pos
                    curr_state =flag 

                    str_print = start_tr_chr + "\t" + str(start_tr_pos) + "\t" + str(end_tr_pos) + "\t" + str(temp_len) + "\t" + str(curr_state)
                    fout_regions.write(str_print)
                    fout_regions.write("\n")                  

                    if state=="0":    
                        flag=0
                        start_tr_pos = pos 
                        start_tr_chr = chrm

                    else:  #state is 1
                        flag=1
                        start_tr_pos = pos 
                        start_tr_chr = chrm

                else:
                    print "Something went wrong 1 :",chrm," ",pos
                    sys.exit() 
 

        else:

            if state=="0":            

                if flag==1:    ## Process previous block  and start a new one            

                    end_tr_chr = prev_chr
                    end_tr_pos = prev_pos

                    if start_tr_chr == end_tr_chr:

                        temp_len = end_tr_pos - start_tr_pos
                        curr_state =flag 

                        str_print = start_tr_chr + "\t" + str(start_tr_pos) + "\t" + str(end_tr_pos) + "\t" + str(temp_len) + "\t" + str(curr_state)
                        fout_regions.write(str_print)
                        fout_regions.write("\n")                  

    
                        flag=0
                        start_tr_pos = pos 
                        start_tr_chr = chrm

                    else:
                        print "Something went wrong 2 :",chrm," ",pos
                        sys.exit() 

                else:          ## state is 0 and current state is also 0 so continue
                    pass 
                    
            else:    # state is 1

                if flag==0:    ## Process previous block and start a new one            

                    end_tr_chr = prev_chr
                    end_tr_pos = prev_pos

                    if start_tr_chr == end_tr_chr:

                        temp_len = end_tr_pos - start_tr_pos
                        curr_state =flag 

                        str_print = start_tr_chr + "\t" + str(start_tr_pos) + "\t" + str(end_tr_pos) + "\t" + str(temp_len) + "\t" + str(curr_state)
                        fout_regions.write(str_print)
                        fout_regions.write("\n")                  
    
                        flag=1
                        start_tr_pos = pos 
                        start_tr_chr = chrm

                    else:
                        print "Something went wrong 3 :",chrm," ",pos
                        sys.exit() 

                else:          ## state is 1 and current state is also 1 so continue
                    pass 
 

#        if state=="1": 

#            chr_dic[individual].append(chrm)
#            pos_dic[individual].append(pos)


        prev_pos = pos
        prev_chr = chrm
 


    # Process the last block in the last chromosome in a file

    end_tr_chr = prev_chr
    end_tr_pos = prev_pos

    if start_tr_chr == end_tr_chr:

        temp_len = end_tr_pos - start_tr_pos
        curr_state =flag 

        str_print = start_tr_chr + "\t" + str(start_tr_pos) + "\t" + str(end_tr_pos) + "\t" + str(temp_len) + "\t" + str(curr_state)
        fout_regions.write(str_print)
        fout_regions.write("\n")                  

    else:
        print "Something went wrong 4 :",chrm," ",pos
        sys.exit() 

    out_file_list.append(fout_fname)
    fout_regions.close()


####################################################################################################################

chr_all={}

for fname in out_file_list:

    curr_file = open(fname,"r")

    for line in curr_file:       # Skip the header line
        break   
        
    for line in curr_file:
        
        col = re.split("\t|\n",line)   

        curr_chr = col[0]
        start    = int(col[1])   
        end      = int(col[2])

        state = col[4]

        if state=="0":
            continue

        if curr_chr not in chr_all:

            chr_all[curr_chr]=[]
            chr_all[curr_chr].append(start)             
            chr_all[curr_chr].append(end) 

        else:

            if start not in chr_all[curr_chr]:
                chr_all[curr_chr].append(start)

            if end not in chr_all[curr_chr]:
                chr_all[curr_chr].append(end)
           
    curr_file.close()

#fout_final = open("ROH_all_sample.tmp","w")

# Define a 2D-array for column
# 0 - CHRM
# 1 - START
# 2 - END
# 3 - LEN
# 4 - SAM_1
# .
# n - 2 - TOTAL_1
# n - 1 - TOTAL_0
# n     - TOTAL_N

next_line_num=-1
col_print = []

col_print.append([])     ## This command you run when you are trying to add a new line
next_line_num = next_line_num + 1

## You start appending when you want to start filling the columns
col_print[next_line_num].append("CHRM")    
col_print[next_line_num].append("START")
col_print[next_line_num].append("END")
col_print[next_line_num].append("LEN")

#str_print_header = "CHRM" + "\t" + "START" + "\t" + "END" + "\t" + "LEN"
#fout_final.write(str_print_header)
#fout_final.write("\n")                  

keylist = chr_all.keys()
keylist.sort()

for every_chr in keylist:

    chr_all[every_chr].sort()

    curr_len = len(chr_all[every_chr])
    
    for i in xrange(0,(curr_len-1)):
         
        j=i+1           

        start = chr_all[every_chr][i]
        end   = chr_all[every_chr][j]

        curr_len_block = end - start

#        str_print = str(every_chr) + "\t" + str(start) + "\t" + str(end) + "\t" + str(curr_len_block)
#        fout_final.write(str_print)
#        fout_final.write("\n")

        col_print.append([])     ## This command you run when you are trying to add a new line
        next_line_num = next_line_num + 1
        col_print[next_line_num].append(every_chr)    
        col_print[next_line_num].append(str(start))
        col_print[next_line_num].append(str(end))
        col_print[next_line_num].append(str(curr_len_block))

#fout_final.close()

total_rows    =  next_line_num + 1
total_cols =  4

fout_final = open("ROH_all_sample.txt","w")


#for i in xrange(0,total_rows):

#    for j in xrange(0,total_cols):

#        fout_final.write(col_print[i][j])
        
#        if j!=(total_cols - 1):  ## if it is not the last column
#            fout_final.write("\t") 

#    fout_final.write("\n")

###########################################################################################



for fname in out_file_list:

    curr_file = open(fname,"r")

    col1        = re.split("\.|\n",fname)
    individual  = col1[0]

    #fname_write = individual + ".tmp"
    #curr_write  = open(fname_write,"w")
    #fout_final = open("ROH_all_sample.tmp","r")


    for curr_line_num in xrange(0,total_rows):

        if curr_line_num==0:
            col_print[curr_line_num].append(individual)
            total_cols = total_cols + 1
            continue 

        #coll=re.split("\t|\n",line)        
        #chr_all   = int(coll[0])
        #start_all = int(coll[1])
        #end_all   = int(coll[2]) 

        chr_all   = col_print[curr_line_num][0]
        start_all = int(col_print[curr_line_num][1])
        end_all   = int(col_print[curr_line_num][2]) 
        
        # go to begining of the current indivudual out file
        curr_file.seek(0, 0)

        for line_ind in curr_file:
            break

        for line_ind in curr_file:
            
            col11 = re.split("\t|\n",line_ind)

            chr_ind   = col11[0]
            start_ind = int(col11[1])   
            end_ind   = int(col11[2])
            state_ind = col11[4]

            fill="N"

            if chr_all==chr_ind:

                if end_all < start_ind:
                    break
 
                if start_all>=start_ind and end_all<=end_ind:
                    fill=state_ind
                    break

            else:
                continue              


        #curr_write.write(fill)
        #curr_write.write("\n") 
        col_print[curr_line_num].append(fill)


    curr_file.close()
    #curr_write.close()


for i in xrange(0,total_rows):

    total_0 = 0
    total_1 = 0 
    total_N = 0

    for j in xrange(0,total_cols):


        if i==0 or j==0 or j==1 or j==2 or j==3:
            fout_final.write(col_print[i][j])
            fout_final.write("\t")

        else:

            curr_state_value = col_print[i][j] 
            fout_final.write(curr_state_value)

            if curr_state_value == "0":
                total_0 = total_0 + 1

            elif curr_state_value == "1":
                total_1 = total_1 + 1

            elif curr_state_value == "N":
                total_N = total_N + 1

            else:
                print "Not a valid value of state"


            if j!=(total_cols - 1):  ## if it is not the last column
                fout_final.write("\t") 

            else:                    ## if it is the last column
                fout_final.write("\t")
                fout_final.write(str(total_0))
                fout_final.write("\t")
                fout_final.write(str(total_1)) 
                fout_final.write("\t") 
                fout_final.write(str(total_N)) 


    if i==0: # IF it is the first line

        fout_final.write("TOTAL_0")
        fout_final.write("\t") 
        fout_final.write("TOTAL_1")
        fout_final.write("\t") 
        fout_final.write("TOTAL_N")


    fout_final.write("\n")





