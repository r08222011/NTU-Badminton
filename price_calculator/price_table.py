import os, csv
import math

court_price_student = 190
court_price_alumni  = 450

bucket_price   = 250 # total price of a bucket of shuttlecocks
shuttle_number = 12  # number of shuttlecocks per bucket
shuttle_used   = 1.5 # average number of shuttlecocks used per court per hour
shuttle_price  = shuttle_used * (bucket_price/shuttle_number)

def calculate_price_table(num_court, max_student, max_alumni):
    global court_price_student, court_price_alumni
    global bucket_price, shuttle_number, shuttle_price
    
    price_table = [[0 for j in range(max_alumni+1)] for i in range(max_student+1)]
    for num_student in range(max_student+1):
        for num_alumni in range(max_alumni+1):
            if num_student == 0 and num_alumni == 0:
                price_table[num_student][num_alumni] = 0
                continue
            elif num_student + num_alumni <= 4*(num_court-1):
                price_table[num_student][num_alumni] = 0
                continue
            elif num_student + num_alumni >= 4 * num_court:
                court_price = (max(0,(4*num_court-num_student))*court_price_alumni + min(num_student,4*num_court)*court_price_student) / 4
            else:
                full_alumni_court_price  = (num_alumni//4) * court_price_alumni
                if num_alumni % 4 == 0:
                    court_price = full_alumni_court_price + max(0,(num_court - (num_alumni//4))) * court_price_student
                else:
                    mix_court_price = ((num_alumni%4)*court_price_alumni + min(4-num_alumni%4,num_student)*court_price_student) / ((num_alumni%4)+min(4-num_alumni%4,num_student))
                    court_price = full_alumni_court_price + mix_court_price + max(0,(num_court - 1 - (num_alumni//4))) * court_price_student
            
            final_price_per_student = (court_price_student * num_court + shuttle_price * num_court) / (num_student + num_alumni)
            if num_alumni == 0:
                final_price_per_alumni = 0
            else:
                final_price_per_alumni  = final_price_per_student + (court_price - court_price_student * num_court) / num_alumni
                if num_student == 0:
                    final_price_per_student = 0
            price_table[num_student][num_alumni] = (int(round(final_price_per_student,-1)) , int(round(final_price_per_alumni,-1)))
    return price_table


if __name__ == '__main__':
    c1 = calculate_price_table(1,8,8)
    c2 = calculate_price_table(2,12,12)

    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dir_path, "price_table.csv"), "w") as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["court_s",190])
        csvwriter.writerow(["court_a",450])
        csvwriter.writerow(["shuttle",int(round(shuttle_price,-1))])

        csvwriter.writerow([])

        csvwriter.writerow(["1:s\\a"] + list(range(8+1)))
        for i in range(8+1):
            csvwriter.writerow([i]+c1[i])
        
        csvwriter.writerow([])

        csvwriter.writerow(["2:s\\a"] + list(range(12+1)))
        for i in range(12+1):
            csvwriter.writerow([i]+c2[i])