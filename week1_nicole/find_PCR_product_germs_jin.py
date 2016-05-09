#writing a program to find 500 bp fragments in blast file

#Adina created the blast file and put them in order
#in R I added a column that gave the difference between two adjacent rows

#need to find the ~500 bp fragments
#and output both that row and the one before it to get both primers

#originally run on hmp_with_diff file; then mock_imperfect file

#finally on usda mock file but changed to 400-600 (from 300-700)-still hundreds
# I think it is a good job to explain what is this code begining of the code

#Usage: python find_PCR_product_germs_jin.py inpufile > output
import sys

# setup parameter here then you don't need to dig where is the parameter if you want to change in the future, try not to use number in the middle of the code
lowcut = 100
hicut = 600
end_pos = 3

num_keep = 0 #initialize 
fread = open(sys.argv[1],'r')
for n, line in enumerate(fread):
    if n == 0: #skip the header
        continue
    #I think we don't need else then save one indent
    info=line.rstrip().split('\t')#I want to split after n==0 to save extra calculation
    difference = int(info[end_pos]) - num_keep # calculate diff here then you don't need another python code
    if (lowcut < difference < hicut):
        print info #using standard output, you can use ">" on the command line
    num_keep = int(info[end_pos]) #save number for next line
fread.close()


    
