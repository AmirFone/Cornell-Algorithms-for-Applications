import unittest
import sys
sys.path.append("..")

from problem_2.p2_d import plan_city_d
from problem_2.p2_e import plan_city_e


def verify_result_b(input_name, result):
    truth_file_name = input_name.replace("_in.txt", "_out.txt")
    # Now, verify the result with truth file
    with open(truth_file_name, 'r') as file:
        valid_truth = file.readline().strip()
        compr_ = "Yes" if result else "No"
        if valid_truth == compr_:
            return True
        else:
            return False

def verify_result_c(input_name, result):
    truth_file_name = input_name.replace("_in.txt", "_out.txt")
    # Now, verify the result with truth file
    with open(truth_file_name, 'r') as file:
        valid_truth = file.readline().strip()
        if valid_truth == 'Yes':
            truth_values = list(map(int, file.readline().split()))
            if set(truth_values) == set(result):
                return True
            else:
                return False
        else:
            bot_recr_truth = list(map(int, file.readline().split()))
            if set(bot_recr_truth) == set(result):
                return True
            else:
                return False


def read_input(input_name, test_func, type='b'):
    with open(input_name, 'r') as file:
        n, k = map(int, file.readline().split())

        neighbours = {i: [] for i in range(n)}
        recruiterCapacities = [0] * (n + k)
        preliminaryAssignment = {}

        for i in range(n):
            parts = list(map(int, file.readline().split()))
            numRecruiters = parts[0]
            for j in range(1, numRecruiters + 1):
                recruiter = parts[j]
                neighbours[i].append(recruiter)

        recruiterCapacities = list(map(int, file.readline().split()))

        parts = list(map(int, file.readline().split()))
        for i in range(n - 1):
            preliminaryAssignment[i] = parts[i]

    result = test_func(num_data_hubs=n, num_service_providers=k, connections=neighbours, provider_capacities=[0]*n + recruiterCapacities, preliminaryAssignment=preliminaryAssignment)
    if type=='b':
        return verify_result_b(input_name, result)
    if type=='c':
        return verify_result_c(input_name, result)


class TestProblem2(unittest.TestCase):
    def test_correctness_public_d1(self):
        input_files = [
            "./test_files_p2/test_0_in.txt",
            "./test_files_p2/test_3_in.txt",
        ]
        for input_file in input_files:
            self.assertEqual(read_input(input_file, plan_city_d, type='b'), True)
    
    # def test_correctness_public_e1(self):
    #     input_files = [
    #         "./test_files_p2/test_0_in.txt",
    #         "./test_files_p2/test_3_in.txt",
    #     ]
    #     for input_file in input_files:
    #         self.assertEqual(read_input(input_file, plan_city_e, type='c'), True)
        
        

if __name__ == '__main__':
    unittest.main()
